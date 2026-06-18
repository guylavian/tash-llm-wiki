import { Component, inject } from '@angular/core';
import { AuthService } from '../auth/auth.service';

@Component({
  selector: 'app-home',
  standalone: true,
  template: `
    <h1>Angular + RHBK SPA</h1>
    @if (auth.authenticated()) {
      <p>You are signed in as <b>{{ auth.profile()?.username }}</b>.</p>
    } @else {
      <p>Public landing page. Use “Log in” to start the Authorization Code + PKCE flow.</p>
    }
  `,
})
export class HomeComponent {
  readonly auth = inject(AuthService);
}
