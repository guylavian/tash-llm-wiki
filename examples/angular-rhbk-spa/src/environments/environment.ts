/**
 * RHBK / Keycloak connection settings.
 *
 * These three values must match a PUBLIC client in your realm:
 *   - Client authentication = OFF   (public client — no secret in the browser)
 *   - Standard flow = ON            (Authorization Code)
 *   - Implicit / Direct access grants = OFF
 *   - PKCE Code Challenge Method = S256 (set below + on the client Advanced tab)
 *   - Valid redirect URIs:            https://app.example.com/*       (exact-ish)
 *   - Valid post logout redirect URIs: https://app.example.com/*
 *   - Web origins (CORS):             https://app.example.com
 *
 * See ../README.md and wiki/questions/angular-spa-oidc-best-practice.md.
 */
export const environment = {
  production: false,
  keycloak: {
    // Base URL of the RHBK server (no trailing /auth on RHBK 26 — that prefix was dropped).
    url: 'https://sso.example.com',
    realm: 'my-realm',
    clientId: 'angular-spa',
  },
};
