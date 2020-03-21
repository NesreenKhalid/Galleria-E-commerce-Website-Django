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
  total_price = 0;
  value;
  updated_id;
  new_quantity;

  constructor(private api: CartService) {
    this.getCart();

  }

  getCart = () => {
    // test cart with id
    this.api.getCart(2).subscribe(
      data => {
        this.products = data;
      },
      error => {
        console.log(error);
      }
    );
  }

  ngOnInit(): void {
    this.add(this.products);

  }

  add(data) {
    this.value = data
    for (let j = 0; j < data.length; j++) {
      this.total_price += this.value[j].product_price * this.value[j].quantity;
    }
  }

  // calcTotalPrice(){
  //   if (this.products) {  
  //     this.products.forEach(item => {
  //       this.total_price += item.product_price * item.quantity;
  //     });
  //   }
  // }


  onChange($event){

    var index = $event.path[2].rowIndex ;

    this.new_quantity = $event.target.value;
    this.updated_id = this.products[index-1].id;

    this.products[index-1].quantity = this.new_quantity;

    this.updateQTY(this.updated_id, this.new_quantity);
  }

  updateQTY = (updated_id, new_quantity) => {
    // test cart with id
    this.api.updateQTY(updated_id , new_quantity).subscribe(
      data => {
        console.log(data);         
      },
      error => {
        console.log(error);
      }
    );
  }

}
