// Synthétise un texte avec une voix de macOS et note le moment où chaque mot est dit.
//
//   swift voix.swift <voix> <texte.txt> <sortie.caf> <sortie.json>
//
// Le synthétiseur prévient, pendant qu'il écrit l'audio, du mot qu'il s'apprête à
// dire ; on relève à cet instant la quantité d'audio déjà produite. C'est ce qui
// permet d'afficher chaque mot à l'écran exactement quand la voix le prononce —
// sans ça, il faudrait découper le texte en morceaux synthétisés séparément, et la
// voix perdrait son souffle à chaque coupure.
import Foundation
import AVFoundation

let args = CommandLine.arguments
guard args.count == 5 else { print("usage : swift voix.swift <voix> <texte.txt> <sortie.caf> <sortie.json>"); exit(1) }
let nomVoix = args[1]
let texte = try! String(contentsOfFile: args[2], encoding: .utf8).trimmingCharacters(in: .whitespacesAndNewlines)
let urlAudio = URL(fileURLWithPath: args[3])
let urlJSON = URL(fileURLWithPath: args[4])

guard let voix = AVSpeechSynthesisVoice.speechVoices().first(where: { $0.name == nomVoix && $0.language.hasPrefix("fr") }) else {
  print("voix « \(nomVoix) » introuvable"); exit(2)
}

final class Suivi: NSObject, AVSpeechSynthesizerDelegate {
  var mots: [[String: Any]] = []
  var trames: Int64 = 0
  var debit: Double = 0
  var fini = false
  func speechSynthesizer(_ s: AVSpeechSynthesizer, willSpeakRangeOfSpeechString r: NSRange, utterance u: AVSpeechUtterance) {
    let ns = u.speechString as NSString
    let mot = ns.substring(with: r)
    let t = debit > 0 ? Double(trames) / debit : 0
    mots.append(["mot": mot, "debut": r.location, "longueur": r.length, "t": t])
  }
  func speechSynthesizer(_ s: AVSpeechSynthesizer, didFinish u: AVSpeechUtterance) { fini = true }
  func speechSynthesizer(_ s: AVSpeechSynthesizer, didCancel u: AVSpeechUtterance) { fini = true }
}

let suivi = Suivi()
let synth = AVSpeechSynthesizer()
synth.delegate = suivi
let u = AVSpeechUtterance(string: texte)
u.voice = voix
u.rate = 0.40          // posé : les références parlent lentement, ~150 mots par minute
u.pitchMultiplier = 0.92
u.preUtteranceDelay = 0.15
u.postUtteranceDelay = 0.3

var fichier: AVAudioFile? = nil
synth.write(u) { buffer in
  guard let pcm = buffer as? AVAudioPCMBuffer, pcm.frameLength > 0 else { return }
  if fichier == nil {
    suivi.debit = pcm.format.sampleRate
    fichier = try? AVAudioFile(forWriting: urlAudio, settings: pcm.format.settings,
                               commonFormat: pcm.format.commonFormat, interleaved: pcm.format.isInterleaved)
  }
  try? fichier?.write(from: pcm)
  suivi.trames += Int64(pcm.frameLength)
}

let debut = Date()
while !suivi.fini && Date().timeIntervalSince(debut) < 180 { RunLoop.current.run(until: Date().addingTimeInterval(0.05)) }
fichier = nil
let duree = suivi.debit > 0 ? Double(suivi.trames) / suivi.debit : 0
let sortie: [String: Any] = ["voix": nomVoix, "duree": duree, "texte": texte, "mots": suivi.mots]
let data = try! JSONSerialization.data(withJSONObject: sortie, options: [.prettyPrinted])
try! data.write(to: urlJSON)
print(String(format: "%.2f s · %d mots datés", duree, suivi.mots.count))
