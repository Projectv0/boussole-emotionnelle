/* Service worker — met le site en cache pour un usage hors connexion.
   Stratégie : réseau d'abord (pour recevoir les mises à jour), cache en secours. */
const CACHE = "boussole-v27";
const ESSENTIELS = ["./", "./index.html", "./merci.html", "./manifest.webmanifest",
                    "./logo-64.webp", "./icone-192.png", "./icone-512.png",
                    /* les polices sont désormais hébergées ici : sans elles en cache,
                       la page hors connexion retomberait sur les polices système —
                       polices.css seul ne suffit pas, il ne fait que les désigner */
                    "/polices/polices.css",
                    "/polices/plus-jakarta-sans-400-latin.woff2",
                    "/polices/fraunces-620-latin.woff2"];

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
