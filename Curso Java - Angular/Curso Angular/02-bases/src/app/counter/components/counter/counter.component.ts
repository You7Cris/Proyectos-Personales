//.component significa que es un componente

import { Component } from "@angular/core";


@Component({
  selector: 'app-counter',
  template: `
    <h3>Counter: {{ counter }}</h3>
    <button (click)="increaseBy()">+1</button>
    <button (click)="reset()">Reset</button>
    <button (click)="decreaseBy()">-1</button>

  `
}) //Decorador que transforma en un componente
export class CounterComponent{

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

