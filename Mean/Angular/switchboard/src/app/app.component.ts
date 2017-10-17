import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  // listofdivs = [];
  // builddivs(){
  //   for(let i = 0; i<10;i++){
  //     if(i%2==0){
  //       this.listofdivs.push('On');
  //     } else {
  //       this.listofdivs.push('Off');
  //     }
  //   }
  // }
  // changediv(){
    
  // }

  switches = [true, true, true, true, true, true, true, true, true, true];
  flipSwitch(idx) {
    this.switches[idx] = !this.switches[idx];
  }
}
