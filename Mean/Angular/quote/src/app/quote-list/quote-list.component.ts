import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';


@Component({
  selector: 'app-quote-list',
  templateUrl: './quote-list.component.html',
  styleUrls: ['./quote-list.component.css']
})
export class QuoteListComponent implements OnInit {

  constructor() { }

  @Input() text: string;
  @Input() author: string;
  @Input() totalvote: number;
  @Input() index: number;

  @Output() voteUp = new EventEmitter();
  @Output() voteDown = new EventEmitter();
  @Output() deleteQuote = new EventEmitter();


  ngOnInit() {
  }

  up(event,index){
    this.voteUp.emit(index);
  }
  down(event,index){
    this.voteDown.emit(index);
  }
  delete(event,index){
    this.deleteQuote.emit(index);
  }
}
