import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; // <-- Import FormsModule
import { HttpModule } from '@angular/http'; // <-- Import HttpModule
import { AppComponent } from './app.component';
import { MyComponentComponent } from './my-component/my-component.component';
import { HumanComponent } from './human/human.component';

@NgModule({
  declarations: [
    AppComponent,
    MyComponentComponent,
    HumanComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
