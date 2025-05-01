import { Component, inject } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common'; 
import { MainMenuOverlayComponent } from './main-menu-overlay/main-menu-overlay.component';
import { UserService, User } from './services/user.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, MainMenuOverlayComponent, CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less'],
})
export class AppComponent {
  selectedItem: string | null = null;

  private userService = inject(UserService);
  users: User[] = [];

  constructor() {
    this.loadUsers();
  }

  openMenu(item: string) {
    this.selectedItem = item;
  }

  closeMenu() {
    this.selectedItem = null;
  }

  loadUsers() {
    this.userService.getUsers().subscribe(data => {
      this.users = data;
      console.log('Usuários carregados:', data);
    });
  }

  deleteUser(id: number) {
    this.userService.deleteUser(id).subscribe(() => {
      this.users = this.users.filter(u => u.id !== id);
    });
  }
}
