import {
  AutoRefreshTokenService,
  UserActivityService,
  provideKeycloak,
  withAutoRefreshToken,
  createInterceptorCondition,
  IncludeBearerTokenCondition,
  INCLUDE_BEARER_TOKEN_INTERCEPTOR_CONFIG,
} from 'keycloak-angular';
import { environment } from '../environments/environment';

/**
 * Central Keycloak wiring for the SPA.
 *
 * Why these options (see wiki/questions/angular-spa-oidc-best-practice.md):
 *  - PUBLIC client + Authorization Code + PKCE(S256): the only supported SPA flow.
 *    `pkceMethod: 'S256'` forces PKCE on the browser side; the realm client should
 *    also require it. We never carry a client secret in the browser.
 *  - `onLoad: 'check-sso'` does a silent SSO check (no forced login on every load);
 *    route-level protection is handled by the auth guard instead. Use
 *    'login-required' instead if the whole app must be authenticated.
 *  - `silentCheckSsoRedirectUri` points at a tiny static page (see
 *    src/assets/silent-check-sso.html) so the check happens in a hidden iframe.
 *  - Tokens live in JS memory only — NEVER localStorage (XSS exfiltration risk).
 *  - Auto token refresh: keycloak-angular refreshes proactively and single-flight,
 *    which is exactly the refresh discipline the wiki calls for. If the session is
 *    idle past SSO Session Idle/Max, the user is sent back to re-authenticate.
 */

// Attach the bearer token only to calls hitting our resource-server API origin —
// never leak the access token to third-party hosts.
const apiCondition: IncludeBearerTokenCondition = createInterceptorCondition({
  // Adjust to your API base URL(s).
  urlPattern: /^https:\/\/api\.example\.com(\/.*)?$/i,
  // Only attach for the bearer scheme.
  bearerPrefix: 'Bearer',
});

export const provideKeycloakAngular = () =>
  provideKeycloak({
    config: {
      url: environment.keycloak.url,
      realm: environment.keycloak.realm,
      clientId: environment.keycloak.clientId,
    },
    initOptions: {
      onLoad: 'check-sso',
      silentCheckSsoRedirectUri:
        window.location.origin + '/assets/silent-check-sso.html',
      // PKCE is mandatory for public clients (RFC 9700 / OAuth 2.1).
      pkceMethod: 'S256',
      // Do not store tokens in any persistent browser storage.
      // (keycloak-js keeps them in memory by default; we leave it that way.)
    },
    features: [
      // Proactive, single-flight refresh; logs the user out if the session dies.
      withAutoRefreshToken({
        onInactivityTimeout: 'logout',
        sessionTimeout: 60000,
      }),
    ],
    providers: [
      AutoRefreshTokenService,
      UserActivityService,
      {
        provide: INCLUDE_BEARER_TOKEN_INTERCEPTOR_CONFIG,
        useValue: [apiCondition],
      },
    ],
  });
