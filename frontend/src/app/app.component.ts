import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common'; 
import { MainMenuOverlayComponent } from './main-menu-overlay/main-menu-overlay.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, MainMenuOverlayComponent, CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less'],
})

export class AppComponent {
  selectedItem: string | null = null;

  openMenu(item: string) {
    this.selectedItem = item;
  }

  closeMenu() {
    this.selectedItem = null;
  }
}