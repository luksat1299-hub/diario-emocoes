/* Service worker do Diário das Emoções.
   Guarda os arquivos do app no aparelho para que ele abra sem internet.
   Ao alterar o app, troque o número da versão abaixo para forçar a atualização. */

const VERSAO = 'diario-v1';
const ARQUIVOS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icone-192.png',
  './icons/icone-512.png',
  './icons/icone-maskable-512.png'
];

// Instalação: baixa e guarda os arquivos do app
self.addEventListener('install', evento => {
  evento.waitUntil(
    caches.open(VERSAO)
      .then(cache => cache.addAll(ARQUIVOS))
      .then(() => self.skipWaiting())
  );
});

// Ativação: descarta versões antigas do cache
self.addEventListener('activate', evento => {
  evento.waitUntil(
    caches.keys()
      .then(chaves => Promise.all(
        chaves.filter(c => c !== VERSAO).map(c => caches.delete(c))
      ))
      .then(() => self.clients.claim())
  );
});

// Busca: responde do cache primeiro; se não houver, tenta a rede
self.addEventListener('fetch', evento => {
  if (evento.request.method !== 'GET') return;
  evento.respondWith(
    caches.match(evento.request).then(resposta => {
      if (resposta) return resposta;
      return fetch(evento.request).then(rede => {
        // Guarda o que for buscado com sucesso, para funcionar offline depois
        const copia = rede.clone();
        caches.open(VERSAO).then(cache => cache.put(evento.request, copia));
        return rede;
      }).catch(() => caches.match('./index.html'));
    })
  );
});
