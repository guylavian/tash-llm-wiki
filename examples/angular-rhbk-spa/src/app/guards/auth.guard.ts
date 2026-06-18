import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import Keycloak from 'keycloak-js';
import {
  AuthGuardData,
  createAuthGuard,
} from 'keycloak-angular';

/**
 * Route guard built on keycloak-angular's functional helper.
 *
 * - If the user is not authenticated, kick off the Authorization Code + PKCE
 *   redirect (keycloak.login), returning them to the URL they asked for.
 * - If authenticated, optionally enforce a required realm/client role declared
 *   on the route's `data.roles`.
 *
 * See wiki: oidc-grant-types / client-authentication-methods.
 */
const isAccessAllowed = async (
  route: any,
  _state: any,
  authData: AuthGuardData,
): Promise<boolean> => {
  const { authenticated, grantedRoles } = authData;
  const keycloak = inject(Keycloak);
  const router = inject(Router);

  if (!authenticated) {
    // Trigger the redirect login; bring the user back where they wanted to go.
    await keycloak.login({
      redirectUri: window.location.origin + router.url,
    });
    return false;
  }

  const requiredRoles: string[] = route.data?.['roles'] ?? [];
  if (requiredRoles.length === 0) {
    return true;
  }

  // grantedRoles exposes realm roles and per-client (resource) roles.
  const hasRole = requiredRoles.some(
    (role) =>
      grantedRoles.realmRoles.includes(role) ||
      Object.values(grantedRoles.resourceRoles).some((roles) =>
        roles.includes(role),
      ),
  );

  if (!hasRole) {
    router.navigate(['/forbidden']);
    return false;
  }
  return true;
};

export const canActivateAuth: CanActivateFn = createAuthGuard(isAccessAllowed);
