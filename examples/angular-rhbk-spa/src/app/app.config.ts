import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import {
  provideHttpClient,
  withInterceptors,
} from '@angular/common/http';
import { includeBearerTokenInterceptor } from 'keycloak-angular';

import { routes } from './app.routes';
import { provideKeycloakAngular } from './keycloak.config';

export const appConfig: ApplicationConfig = {
  providers: [
    // Keycloak must be provided before anything that injects it.
    provideKeycloakAngular(),
    provideRouter(routes),
    // The bearer interceptor attaches the access token to API calls that match
    // the condition declared in keycloak.config.ts (apiCondition).
    provideHttpClient(withInterceptors([includeBearerTokenInterceptor])),
  ],
};
