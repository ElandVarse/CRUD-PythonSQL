import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MainMenuOverlayComponent } from './main-menu-overlay/main-menu-overlay.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, MainMenuOverlayComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less']
})

export class AppComponent {
  title = 'frontend';
}