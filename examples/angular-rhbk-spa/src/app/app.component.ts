import { Component, inject } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { AuthService } from './auth/auth.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  template: `
    <nav>
      <a routerLink="/">Home</a>
      <a routerLink="/profile">Profile</a>
      <a routerLink="/admin">Admin</a>
      <span class="spacer"></span>
      @if (auth.authenticated()) {
        <span>{{ auth.profile()?.username }}</span>
        <button (click)="auth.manageAccount()">Account</button>
        <button (click)="auth.logout()">Log out</button>
      } @else {
        <button (click)="auth.login()">Log in</button>
      }
    </nav>
    <main>
      <router-outlet />
    </main>
  `,
  styles: [
    `nav { display: flex; gap: 1rem; align-items: center; padding: 0.75rem 1rem; border-bottom: 1px solid #ddd; }
     .spacer { flex: 1; }
     main { padding: 1rem; }`,
  ],
})
export class AppComponent {
  readonly auth = inject(AuthService);
}
