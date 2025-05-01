import { Component, Input, Output, EventEmitter, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserService, User } from '../services/user.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-main-menu-overlay',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './main-menu-overlay.component.html',
  styleUrl: './main-menu-overlay.component.less'
})
export class MainMenuOverlayComponent {
  @Input() item: string | null = null;
  @Output() close = new EventEmitter<void>();

  private userService = inject(UserService);
  users: User[] = [];

  // Modelos para formulário
  newUser: User = { name: '', email: '', password: '' };
  updateId: number | null = null;
  updateEmailValue: string = '';

  constructor() {
    this.loadUsers();
  }

  loadUsers() {
    this.userService.getUsers().subscribe(data => {
      this.users = data;
    });
  }

  addUser() {
    if (!this.newUser.name || !this.newUser.email || !this.newUser.password) return;

    this.userService.addUser(this.newUser).subscribe(() => {
      this.newUser = { name: '', email: '', password: '' };
      this.loadUsers();
      this.closeMenu();
    });
  }

  updateUserEmail() {
    if (this.updateId === null || !this.updateEmailValue) return;

    this.userService.updateUserEmail(this.updateId, this.updateEmailValue).subscribe(() => {
      this.updateId = null;
      this.updateEmailValue = '';
      this.loadUsers();
      this.closeMenu();
    });
  }

  deleteUser(id: number) {
    this.userService.deleteUser(id).subscribe(() => {
      this.users = this.users.filter(u => u.id !== id);
    });
  }

  closeMenu() {
    this.close.emit();
  }
}
