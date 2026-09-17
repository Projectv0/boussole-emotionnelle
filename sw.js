/* Service worker — met le site en cache pour un usage hors connexion.
   Stratégie : réseau d'abord (pour recevoir les mises à jour), cache en secours. */
const CACHE = "boussole-v19";
const ESSENTIELS = ["./", "./index.html", "./merci.html", "./manifest.webmanifest",
                    "./icone-192.png", "./icone-512.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ESSENTIELS)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys()
      .then(noms => Promise.all(noms.filter(n => n !== CACHE).map(n => caches.delete(n))))
      .then(() => self.clients.claim())
  );
});
self.addEventListener("fetch", e => {
  if(e.request.method !== "GET") return;
  e.respondWith(
    fetch(e.request)
      .then(rep => {
        if(rep && rep.status === 200 && rep.type === "basic"){
          const copie = rep.clone();
          caches.open(CACHE).then(c => c.put(e.request, copie));
        }
        return rep;
      })
      /* Le repli sur index.html ne vaut que pour une navigation. Appliqué à toute
         requête échouée, il servait la page du test en réponse à une image ou à un
         script manquant — et à merci.html, qui revenait alors du cache en page de
         test au lieu de confirmer le paiement. */
      .catch(() => caches.match(e.request).then(r =>
        r || (e.request.mode === "navigate" ? caches.match("./index.html") : Response.error())))
  );
});
