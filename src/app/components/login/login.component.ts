import { UserAPIService } from './../services/user-api.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  user: string;
  token: string;
  login: boolean;
  constructor(private userServices: UserAPIService) {
    const first = this.userServices.login('admin', 'admin');
    const second = this.userServices.login('admin', 'admin2');
    console.log(first, second);
    console.log(second, first);
  }

  public getUser() {
    return this.user;
  }

  public setUser(){
    // this.user=data;
  }

  public getLogin() {
    return this.user;
  }

  public setLogin(){
    // this.user=data;
  }
  public getToken() {
    return this.user;
  }

  public setToken(){
    // this.user=data;
  }
}