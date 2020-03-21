import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { User } from 'src/app/models/user';
import { SharedService } from './shared.service';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
    baseurl = "http://127.0.0.1:8000";

    constructor(private http: HttpClient, public shServ: SharedService) { }


    signup(username: string, email: string, password: string ) {
        return this.http.post(this.baseurl+`/user/register/`, { username, email, password });
    }

    
    login(username: string, password: string) {
        return this.http.post<any>(this.baseurl+`/user/login/`, { username, password })
    }

    logout() {
        localStorage.removeItem('currentUser');
        this.shServ.currentUserSubject.next(null);
    }
}


