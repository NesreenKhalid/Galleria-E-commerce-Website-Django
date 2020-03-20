import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ProductService {
  baseurl="http://127.0.0.1:8000";
  httpHeaders=new HttpHeaders({'Content-Type':'application/json'})
  constructor(private http :HttpClient) { }
  getProductById(id: number):Observable<any>{
    return this.http.get(this.baseurl+'/product/id/'+id+'/',
    {headers :this.httpHeaders });
  }
  getPicturesByProductId(product_id: number){
    return this.http.get(this.baseurl+'/product/'+product_id+'/pictures/',
    {headers :this.httpHeaders });
  }
  getCommentsByProductId(product_id: number){
    return this.http.get(this.baseurl+'/product/'+product_id+'/comments/',
    {headers :this.httpHeaders });
  }
}
