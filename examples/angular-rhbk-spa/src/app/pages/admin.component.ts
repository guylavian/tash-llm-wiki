import { Component } from '@angular/core';

/** Reached only by users holding the `app-admin` role (enforced in the guard). */
@Component({
  selector: 'app-admin',
  standalone: true,
  template: `<h2>Admin area</h2><p>Role-gated content.</p>`,
})
export class AdminComponent {}
