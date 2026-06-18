import { Injectable, effect, inject, signal } from '@angular/core';
import Keycloak, { KeycloakProfile } from 'keycloak-js';
import {
  KEYCLOAK_EVENT_SIGNAL,
  KeycloakEventType,
  typeEventArgs,
  ReadyArgs,
} from 'keycloak-angular';
import { environment } from '../../environments/environment';

/**
 * Thin facade over the injected Keycloak instance.
 *
 * Exposes auth state as signals and wraps login/logout per the wiki rules:
 *  - login()  -> Authorization Code + PKCE redirect.
 *  - logout() -> redirect to the OIDC end_session_endpoint with a registered
 *                post_logout_redirect_uri (keycloak-js builds the id_token_hint).
 *  - getValidToken() -> returns a token guaranteed fresh for `minValidity`
 *                seconds; this is the single-flight, proactive refresh the wiki
 *                requires. Call it right before an API request when you need the
 *                raw token (the HTTP interceptor already does this for you).
 */
@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly keycloak = inject(Keycloak);
  private readonly keycloakSignal = inject(KEYCLOAK_EVENT_SIGNAL);

  readonly authenticated = signal(false);
  readonly profile = signal<KeycloakProfile | undefined>(undefined);

  constructor() {
    // React to keycloak-angular lifecycle events.
    effect(() => {
      const event = this.keycloakSignal();
      switch (event.type) {
        case KeycloakEventType.Ready:
          this.authenticated.set(typeEventArgs<ReadyArgs>(event.args));
          if (this.authenticated()) {
            void this.loadProfile();
          }
          break;
        case KeycloakEventType.AuthLogout:
          this.authenticated.set(false);
          this.profile.set(undefined);
          break;
      }
    });
  }

  login(): Promise<void> {
    return this.keycloak.login({
      redirectUri: window.location.origin,
    });
  }

  logout(): Promise<void> {
    // Redirect logout -> end_session_endpoint. The post-logout URI MUST be
    // registered under the client's "Valid post logout redirect URIs".
    return this.keycloak.logout({
      redirectUri: window.location.origin,
    });
  }

  /** Account-management console for the current user (RHBK Account Console v2). */
  manageAccount(): Promise<void> {
    return this.keycloak.accountManagement();
  }

  /**
   * Returns a token valid for at least `minValidity` seconds, refreshing it
   * (single-flight, handled by keycloak-js) if needed. Treat a thrown error as
   * "session is gone — re-authenticate", not a retryable bug.
   */
  async getValidToken(minValidity = 30): Promise<string | undefined> {
    try {
      await this.keycloak.updateToken(minValidity);
      return this.keycloak.token;
    } catch {
      // Session expired / invalid_grant -> force a clean re-login.
      await this.login();
      return undefined;
    }
  }

  hasRole(role: string, clientId = environment.keycloak.clientId): boolean {
    return (
      this.keycloak.hasRealmRole(role) ||
      this.keycloak.hasResourceRole(role, clientId)
    );
  }

  private async loadProfile(): Promise<void> {
    this.profile.set(await this.keycloak.loadUserProfile());
  }
}
