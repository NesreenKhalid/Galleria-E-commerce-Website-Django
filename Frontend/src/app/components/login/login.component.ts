import { UserAPIService } from './../services/user-api.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [UserAPIService]
})
export class LoginComponent {
  products ;
  p: number = 1;
  count: number = 1;
  constructor(private api: UserAPIService) {
    this.getProduct();
   }


    getProduct = () => {
      this.api.getAllUsers().subscribe(
        data => {
          this.products = data;
          console.log(this.products);          
        },
        error => {
          console.log(error);
        }
      );
    }
  productClicked=(product)=>{
	console.log(product.id);
  
  }

  public getUser() {
    // return this.user;
  }

  public setUser(){
    // this.user=data;
  }

  public getLogin() {
    // return this.user;
  }

  public setLogin(){
    // this.user=data;
  }
  public getToken() {
    // return this.user;
  }

  public setToken(){
    // this.user=data;
  }
}