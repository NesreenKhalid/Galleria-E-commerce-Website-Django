import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { User } from 'src/app/models/user';
import { UserService } from '../services/user.service';
import { AuthenticationService } from '../services/authentication.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  errorMessage: string = ''

  constructor(private authServ: AuthenticationService, private us: UserService, private router: Router) { }

  ngOnInit(): void { }

  signup(form) {
    let data: User = form.value
    console.log(data.username + ' ' + data.email + ' ' + data.password);

    this.authServ.signup(data.username, data.email, data.password).subscribe(
      response => {
        alert('Welcome, ' + data.username);
        this.router.navigate(['login']);
      },
      err => {
        let errStr = "";
        console.log('oppppppppppp', err.error);
        
        errStr = (err.error.username) ? err.error.username : err.error.email;  
        alert('Error: ' + errStr);
      })
  }
}


