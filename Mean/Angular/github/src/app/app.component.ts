import { Component } from '@angular/core';
import { GithubService } from './github.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';

  username = "";
  name = null;
  userExists = null;
  score = null;
  promise;


  constructor(private _githubService : GithubService) { }

  onSubmit() {
    console.log("hit on submit")
    // Grab breed from form (this.breed)
    // Make the call to the service to get image from API
    // Set my image to this.imageUrl to see in html
    this.promise = this._githubService.getGithubScore(this.username)
    if (this.promise) {
      this.promise.then((user) => {
        if (user.id) {
          this.userExists = true;
          this.score = user.public_repos + user.followers;
        } else {
          this.userExists = false;
          this.score = null;
        }
        this.username = null;
        console.log(this.username)
      })
        .catch((err) => {
          this.userExists = false;
        });
    } else {
      this.userExists = false;
    }
  }
}
