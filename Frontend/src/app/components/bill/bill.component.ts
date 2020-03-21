import { Component, OnInit } from '@angular/core';
import { CartService } from './../services/cart.service';
@Component({
  selector: 'app-bill',
  templateUrl: './bill.component.html',
  styleUrls: ['./bill.component.css'],
  providers: [CartService]
})
export class BillComponent implements OnInit {
  items;
  total_price = 0;
  value;
  constructor(private api: CartService) {
    this.getSummary();

  }

  getSummary = () => {
    // test cart with id
    this.api.getCart(2).subscribe(
      data => {
        this.items = data;
      },
      error => {
        console.log(error);
      }
    );
  }

  ngOnInit(): void {
    this.add(this.items);

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
}
