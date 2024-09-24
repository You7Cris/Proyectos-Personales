import { Component } from '@angular/core';

@Component({
  selector: 'app-heroes-hero',
  templateUrl: './hero.component.html',
  styleUrl: './hero.component.css'
})
export class HeroComponent {

  public name: string = 'Ironman';
  public age: number = 45;

  //getters metodo de clase pero se usa como una propiedad

  get capitalizedName(): string{
    return this.name.toUpperCase();
  }


  getHeroDescription(): string{

    return `${this.name} - ${this.age}`;
  }

  chageHero(): void{
    this.name = 'Thor';
  }

  changeAge(): void{
    this.age = 40;
  }

  resetForm(): void{
    this.name = 'Ironman';
    this.age = 45;

    document.querySelectorAll('h1')!.forEach(element => {
      element.innerHTML = '<h1>Desde Angular</h1>';
    });
  }



}
