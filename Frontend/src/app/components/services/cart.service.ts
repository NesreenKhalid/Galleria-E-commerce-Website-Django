import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  baseurl="http://127.0.0.1:8000";
  httpHeaders=new HttpHeaders({'Content-Type':'application/json'})
  constructor(private http :HttpClient) { }

  getCart(id: number){
    return this.http.get(
              this.baseurl+'/user/cart/' ,
            {headers :this.httpHeaders }
            );
  }
}
