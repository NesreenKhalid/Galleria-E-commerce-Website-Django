import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserAPIService {

  constructor() {
  }

  // login service logic
  login(user, password) {
    if (user == 'admin' && password == 'admin') {
      return true;
    } else {
      return false;
    }
  }

}
