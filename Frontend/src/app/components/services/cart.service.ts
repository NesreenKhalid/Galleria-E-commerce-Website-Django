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
    // return this.http.get(
    //           this.baseurl+'/user/cart/' ,
    //         {headers :this.httpHeaders }
    //         );

    // # test cart with id

    return this.http.get(
              this.baseurl+'/user/'+id+'/cart/' ,
            {headers :this.httpHeaders }
            );
  }

  
  updateQTY(id: number, new_quantity: number){
    const body = {quantity: new_quantity}
    return this.http.put(
              this.baseurl+'/user/cart/'+id , body,
            {headers :this.httpHeaders }
            );
  }

}
