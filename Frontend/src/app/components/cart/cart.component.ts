import { CartService } from './../services/cart.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css'],
  providers: [CartService]
})
export class CartComponent implements OnInit {
  products;
  constructor(private api: CartService) { 
    this.getCart();
  }

  getCart =()=>{
    // test cart with id
    this.api.getCart(2).subscribe(
      data => {
        this.products = data;
      },
      error=>{
        console.log(error);
        
      }
    );
  }
  ngOnInit(): void {
  }

}
