import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Quote } from './quote';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  
  quote = new Quote();
  quotes = [];

  increaseRating(index) {
    this.quotes[index].totalvote ++;
  }

  decreaseRating(index) {
    this.quotes[index].totalvote --;
  }

  delete(index) {
    this.quotes.splice(index, 1)
  }

  
  onSubmit(){
    this.quotes.push(this.quote);
    this.quote = new Quote();
  }
}
