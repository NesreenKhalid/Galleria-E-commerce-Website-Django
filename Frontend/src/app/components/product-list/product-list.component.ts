import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductlistService } from '../services/productlist.service';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  products ;//= [{description: "MinaNagy",id:5,model:"",name:"test",price: 200,stock_items: 2}];
  // Pagination parameters.
  p: number = 1;
  count: number = 3;
  constructor(private api : ProductlistService,private route:ActivatedRoute){
    //let id = this.route.snapshot.params['id'];
    this.p=1;
    this.route.paramMap.subscribe(params => this.getProduct(params.get('id')))
    //console.log(id);

  }
    getProduct = (id) => {
      this.api.getProductById(id).subscribe(
        data => {
          this.products = data;
          console.log(this.products);          
        },
        error => {
          console.log(error);
        }
      );
    }
  /*productClicked=(product)=>{
	console.log(product.id);
  }*/
  ngOnInit(): void {
  }


}
