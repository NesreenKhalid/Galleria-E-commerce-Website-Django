import { Component, OnInit } from '@angular/core';
import { ProductlistService } from '../services/productlist.service';
@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  products = [{description: "MinaNagy",id:5,model:"",name:"test",price: "",stock_items: 2}];
  constructor(private api : ProductlistService){
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

  ngOnInit(): void {
  }

}
