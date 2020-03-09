import { BrowserModule } from '@angular/platform-browser';
import { NgModule, Component } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { ProductCardComponent } from './components/product-card/product-card.component';
import { CartComponent } from './components/cart/cart.component';
import { HomeComponent } from './components/home/home.component';
import { CheckoutComponent } from './components/checkout/checkout.component';
import { BillComponent } from './components/bill/bill.component';
import { OrderDoneComponent } from './components/order-done/order-done.component';
import { LoginComponent } from './components/login/login.component';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { WishlistComponent } from './components/wishlist/wishlist.component';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    ProductCardComponent,
    CartComponent,
    HomeComponent,
    CheckoutComponent,
    BillComponent,
    OrderDoneComponent,
    LoginComponent,
    UserProfileComponent,
    WishlistComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
