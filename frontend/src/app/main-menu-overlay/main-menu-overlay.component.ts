import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common'; // <-- IMPORTAR ISSO

@Component({
  selector: 'app-main-menu-overlay',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './main-menu-overlay.component.html',
  styleUrl: './main-menu-overlay.component.less'
})

export class MainMenuOverlayComponent {
  @Input() item: string | null = null;
  @Output() close = new EventEmitter<void>();

  closeMenu() {
    this.close.emit();
  }
}