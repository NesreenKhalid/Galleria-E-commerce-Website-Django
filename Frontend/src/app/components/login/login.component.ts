import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { AuthenticationService } from '../services/authentication.service';
import { Router } from '@angular/router';
import { User } from 'src/app/models/user';
import { SharedService } from '../services/shared.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [UserService]
})
export class LoginComponent {

  constructor(private authServ: AuthenticationService, public shServ: SharedService, private router: Router) { }

  login(form) {
    let data = form.value
    this.authServ.login(data.username, data.password).subscribe(
      response => {
        if (response.hasOwnProperty('user')) {
          console.log('response', response);
          alert('Welcome, ' + data.username);
          this.router.navigate([''])
          let currentUser = new User(response.user)

          localStorage.setItem('currentUser', JSON.stringify(currentUser));
          this.shServ.currentUserSubject.next(currentUser);

          console.log(currentUser);

          alert('Welcome, ' + data.username);
          this.router.navigate([''])
        } else {
          alert(response.error);
        }
      },
      err => {
        console.log(err);
        
        console.log(err.error);
        alert('Error: ' + err.error);
      })
  }
}