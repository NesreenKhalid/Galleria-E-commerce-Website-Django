import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { CheckoutComponent } from './components/checkout/checkout.component';
import { CartComponent } from './components/cart/cart.component';
import { HomeComponent } from './components/home/home.component';
import { NgModule } from '@angular/core';
import { ProductComponent } from './components/product/product.component';
//import { ProductListComponent } from './components/product-list/product-list.component';
import { SignupComponent } from './components/signup/signup.component';
import { LoginComponent } from './components/login/login.component';
import { Routes, RouterModule } from '@angular/router';
import { ProductListComponent } from './components/product-list/product-list.component';

const routes: Routes = [
  { path: '', component: HomeComponent},
  { path: 'cart', component: CartComponent},
  { path: 'checkout/:id', component: CheckoutComponent},
  { path: 'profile/:id', component: UserProfileComponent},
  { path: 'products/:id', component: ProductComponent},
  { path: 'product/:id', component: ProductListComponent},
  { path: 'signup', component: SignupComponent},
  { path: 'login', component: LoginComponent},
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
