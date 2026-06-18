import { Component, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../auth/auth.service';

/**
 * Protected page. Calls a backend resource server; the bearer token is attached
 * automatically by includeBearerTokenInterceptor for URLs matching apiCondition
 * (see keycloak.config.ts). The resource server must validate that JWT via JWKS
 * (wiki: oidc-token-validation) — the SPA never validates its own access token.
 */
@Component({
  selector: 'app-profile',
  standalone: true,
  template: `
    <h2>Profile</h2>
    <pre>{{ profileJson() }}</pre>
    <button (click)="callApi()">Call protected API</button>
    @if (apiResult()) {
      <pre>{{ apiResult() }}</pre>
    }
  `,
})
export class ProfileComponent {
  private readonly http = inject(HttpClient);
  private readonly auth = inject(AuthService);

  readonly profileJson = signal(JSON.stringify(this.auth.profile(), null, 2));
  readonly apiResult = signal<string | null>(null);

  callApi(): void {
    // No manual Authorization header — the interceptor adds it for api.example.com.
    this.http.get('https://api.example.com/me').subscribe({
      next: (res) => this.apiResult.set(JSON.stringify(res, null, 2)),
      error: (err) => this.apiResult.set(`Error: ${err.status}`),
    });
  }
}
