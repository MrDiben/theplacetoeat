/* eslint-disable */
workbox.setConfig({
  debug: false
});

workbox.routing.registerRoute(
  /\.(?:js|css|json|html)$/,
  new workbox.strategies.StaleWhileRevalidate()
);

workbox.routing.registerRoute(
  /\.(?:png|gif|jpg|jpeg|svg)$/,
  workbox.strategies.staleWhileRevalidate({
    cacheName: "images",
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 60,
        maxAgeSeconds: 30 * 24 * 60 * 60 // 30 days
      })
    ]
  })
);

workbox.routing.registerRoute(
  new RegExp(`${self.location.origin}`),
  workbox.strategies.networkFirst({
    cacheName: "front"
  })
);

workbox.routing.registerRoute(
  // Backend routes located on same host
  new RegExp(
    `${self.location.protocol}//(www\.)?${self.location.hostname}/api/`
  ),
  workbox.strategies.networkFirst({
    cacheName: "api"
  })
);

workbox.routing.registerRoute(
  new RegExp("https://fonts.(?:googleapis|gstatic).com/(.*)"),
  workbox.strategies.cacheFirst({
    cacheName: "googleapis",
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 30
      })
    ]
  })
);
