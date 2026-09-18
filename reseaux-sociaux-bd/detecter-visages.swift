// Repère les têtes sur les illustrations, pour que l'assembleur sache vers qui
// pointer les queues de bulles. Écrit du JSON sur la sortie standard.
//
//     swift detecter-visages.swift illustrations/*.jpg > file/visages.json
//
// Deux passes : le détecteur de visages, précis mais aveugle dès qu'un personnage
// est de dos ou la tête levée ; puis le détecteur de posture, qui situe la tête à
// partir du cou et des oreilles même sans visage lisible. Les têtes trouvées par la
// posture ne sont retenues que là où le premier n'a rien vu.
//
// Coordonnées normalisées, origine en haut à gauche : x et y au centre de la tête,
// l et h sa largeur et sa hauteur, c la confiance.
import Foundation
import Vision
import AppKit

func tetesDeLaPosture(_ cg: CGImage) -> [[String: Double]] {
    let req = VNDetectHumanBodyPoseRequest()
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    var out: [[String: Double]] = []
    for obs in (req.results ?? []) {
        guard let pts = try? obs.recognizedPoints(.all) else { continue }
        let hauts: [VNHumanBodyPoseObservation.JointName] =
            [.nose, .leftEye, .rightEye, .leftEar, .rightEar]
        let vus = hauts.compactMap { pts[$0] }.filter { $0.confidence > 0.25 }
        guard !vus.isEmpty else { continue }
        let x = vus.map { $0.location.x }.reduce(0, +) / Double(vus.count)
        let y = vus.map { $0.location.y }.reduce(0, +) / Double(vus.count)
        // Taille de la tête : deux fois la distance au cou, ou une valeur par défaut.
        var h = 0.11
        if let cou = pts[.neck], cou.confidence > 0.25 {
            h = min(max(abs(y - cou.location.y) * 2.0, 0.06), 0.30)
        }
        let conf = vus.map { Double($0.confidence) }.reduce(0, +) / Double(vus.count)
        out.append(["x": x, "y": 1 - y, "l": h * 0.82, "h": h, "c": conf, "posture": 1])
    }
    return out
}

var sortie: [String: [[String: Double]]] = [:]
for chemin in CommandLine.arguments.dropFirst() {
    guard let img = NSImage(contentsOfFile: chemin),
          let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { continue }

    let req = VNDetectFaceRectanglesRequest()
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    var tetes: [[String: Double]] = (req.results ?? [])
        .filter { $0.confidence >= 0.35 }
        .map { o in
            let b = o.boundingBox   // origine en bas à gauche
            return ["x": b.midX, "y": 1 - b.midY, "l": b.width, "h": b.height,
                    "c": Double(o.confidence), "posture": 0]
        }

    for t in tetesDeLaPosture(cg) {
        // on ne double pas une tête déjà trouvée par le détecteur de visages
        let proche = tetes.contains { hypot($0["x"]! - t["x"]!, $0["y"]! - t["y"]!) < 0.12 }
        if !proche { tetes.append(t) }
    }

    let nom = ((chemin as NSString).lastPathComponent as NSString).deletingPathExtension
    sortie[nom] = tetes
}
let d = try! JSONSerialization.data(withJSONObject: sortie,
                                    options: [.sortedKeys, .prettyPrinted])
FileHandle.standardOutput.write(d)
