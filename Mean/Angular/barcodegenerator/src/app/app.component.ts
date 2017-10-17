import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  name = 'Eric';
  barcolor = [];
  colorArray(){
    for(let i = 0;i<10;i++){
      var barcolor = [];
      var colorpossibilities = 'abcdefABCDEF0123456789';
      this.barcolor[i]= '#';
      for(let y = 0;y<6;y++){
        this.barcolor[i] += colorpossibilities[Math.floor(Math.random() * colorpossibilities.length)];
      }
    }
  }
  // colors = this.colorArray;
  ngOnInit() {
    this.colorArray();
    }
}
