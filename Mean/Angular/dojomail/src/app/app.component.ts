import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  emails = [{
    address:"bill@gates.com",
    important: true,
    subject: "New Windows",
    content: "Windows XI will launch in year 2100"
  },{
    address:"ada@lovelace.com",
    important: true,
    subject: "Programming",
    content: "Enchantress of Numbers"
  },{
    address:"John@carmac.com",
    important: false,
    subject: "Update Algo",
    content: "New Algorithm for shadow volumes"
  },{
    address:"gabe@newel.com",
    important: false,
    subject: "HL3!",
    content: "Just kidding..."}]
}
