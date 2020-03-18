import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';


import { User } from 'src/app/models/user';
@Injectable({
  providedIn: 'root'
})
export class UserAPIService {
  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' })

  constructor(private http: HttpClient) { }

  getAllUsers(): Observable<any> {
    return this.http.get(this.baseurl + '/user/userslist/',
      { headers: this.httpHeaders });
  }

  getById(id: number) {
    return this.http.get(this.baseurl + `/user/userslist/${id}`);
  }

  login(user: User) {
    return this.http.post(this.baseurl+`/user/login/`, user);
  }

  register(user: User) {
    return this.http.post(this.baseurl+`/user/register/`, user);
  }

  update(user: User) {
    return this.http.put(this.baseurl+`/user/userslist/${user.id}`, user);
  }

  delete(id: number) {
    return this.http.delete(this.baseurl+`/user/userslist/${id}`);
  }

}


