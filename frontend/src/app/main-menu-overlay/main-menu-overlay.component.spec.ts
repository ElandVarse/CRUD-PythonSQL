import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MainMenuOverlayComponent } from './main-menu-overlay.component';

describe('MainMenuOverlayComponent', () => {
  let component: MainMenuOverlayComponent;
  let fixture: ComponentFixture<MainMenuOverlayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MainMenuOverlayComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MainMenuOverlayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
