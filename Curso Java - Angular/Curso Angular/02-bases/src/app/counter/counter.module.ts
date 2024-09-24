//Definicion de mis componentes

import { NgModule } from "@angular/core";
import { CounterComponent } from "./components/counter/counter.component";
import { CommonModule } from "@angular/common";

@NgModule({
  declarations: [
    //Aquí van todos los componentes que se encuentran en este módulo
    CounterComponent,
  ],
  exports: [
    //Aquí van todos los componentes que se exportan para que puedan ser usados en otros módulos
    CounterComponent,
  ]

})
export class CounterModule {}
