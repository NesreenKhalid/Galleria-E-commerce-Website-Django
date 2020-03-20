import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';


import { User } from 'src/app/models/user';
@Injectable({
  providedIn: 'root'
})
export class UserService {
  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' })

  constructor(private http: HttpClient) { }

  getAllUsers(): Observable<any> {
    return this.http.get(this.baseurl + '/user/userslist/',
      { headers: this.httpHeaders });
  }

  getUserById(id: number) {
    return this.http.get(this.baseurl + `/user/userslist/${id}`);
  }

  updateUser(user: User) {
    return this.http.put(this.baseurl+`/user/userslist/${user.id}`, user);
  }

  deleteUser(id: number) {
    return this.http.delete(this.baseurl+`/user/userslist/${id}`);
  }

}


