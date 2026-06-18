import { Routes } from '@angular/router';
import { canActivateAuth } from './guards/auth.guard';
import { HomeComponent } from './pages/home.component';
import { ProfileComponent } from './pages/profile.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  // Protected route: requires an authenticated session.
  {
    path: 'profile',
    component: ProfileComponent,
    canActivate: [canActivateAuth],
  },
  // Role-gated example: only users with the `app-admin` role (realm or this
  // client) may enter. The guard reads route.data.roles.
  {
    path: 'admin',
    loadComponent: () =>
      import('./pages/admin.component').then((m) => m.AdminComponent),
    canActivate: [canActivateAuth],
    data: { roles: ['app-admin'] },
  },
  { path: '**', redirectTo: '' },
];
