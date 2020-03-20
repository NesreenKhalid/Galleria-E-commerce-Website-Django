import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { ProductlistService } from '../services/productlist.service';
@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit, OnDestroy {

  products ;//= [{description: "MinaNagy",id:5,model:"",name:"test",price: 200,stock_items: 2}];
  // Pagination parameters.
  p: number = 1;
  count: number = 3;
  searchText;
  productsObservable: Subscription;
  constructor(private api : ProductlistService,private route:ActivatedRoute){
    //let id = this.route.snapshot.params['id'];
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

  ngOnDestroy() {
    this.productsObservable.unsubscribe()
  }

}

/*{
  id:number;
  name:string;
  description:string;
  model: string;
  price: string;
  stock_items: number;
  base_view:string;
  BID: number;
  CategoryID: number;
}*/

