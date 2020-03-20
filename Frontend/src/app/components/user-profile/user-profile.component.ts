import { Component, OnInit, OnDestroy } from '@angular/core';
import { SharedService } from '../services/shared.service';
import { User } from 'src/app/models/user';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit, OnDestroy {
  currentUser: User;
  currentUserSubscription: Subscription;

  constructor(public shServ: SharedService) {
    this.currentUserSubscription = this.shServ.currentUser.subscribe(user => {
      this.currentUser = user;
      console.log(this.currentUser);

    })
  }


  ngOnInit() { }

  ngOnDestroy() {
    // unsubscribe to ensure no memory leaks
    this.currentUserSubscription.unsubscribe();
  }


}
// this.authenticationService.currentUserValue;