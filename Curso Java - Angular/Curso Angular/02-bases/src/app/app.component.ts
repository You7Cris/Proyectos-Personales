import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  public title: string = 'Mi primera app de Angular';

  public counter: number = 10;

  reset():void{
    this.counter = 10;
  }

  increaseBy():void {
    this.counter++;
    // this.counter = this.counter + 1;
  }

  decreaseBy(): void {
    this.counter--;
  }
}
