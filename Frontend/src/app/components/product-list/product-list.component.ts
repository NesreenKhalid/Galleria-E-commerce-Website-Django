import { Component, OnInit, OnDestroy } from '@angular/core';import { ProductlistService } from '../services/productlist.service';
import { Subscription } from 'rxjs';
@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit, OnDestroy{

  products;//= [{description: "MinaNagy",id:5,model:"",name:"test",price: 200,stock_items: 2}];
  // Pagination parameters.
  p: number = 1;
  count: number = 3;
  productsObservable: Subscription;

  constructor(private api: ProductlistService) {
    this.getProduct();
  }
  getProduct = () => {
    this.api.getAllProducts().subscribe(
      data => {
        this.products = data;
        console.log(this.products);
      },
      error => {
        console.log(error);
      }
    );
  }
  productClicked = (product) => {
    console.log(product.id);
  }
  ngOnInit(): void {
  }

  ngOnDestroy() {
    this.productsObservable.unsubscribe()
  }

}
