import { Component, OnInit } from '@angular/core';
import { ReviewComponent } from '../review/review.component'
import { ActivatedRoute } from '@angular/router';
import { ProductService } from '../services/product.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {

  product; pictures;
  constructor(private api : ProductService, private route:ActivatedRoute){
    this.route.paramMap.subscribe(params => this.getProduct(params.get('id')))
  }

  getProduct(id) : void {
    this.api.getProductById(id).subscribe(
      data => {
        this.product = data[0];
        console.log(this.product);          
      },
      error => {
        console.log(error);
      }
    );
    this.api.getPicturesByProductId(id).subscribe(
      data => {
        this.pictures = data[0];
        console.log(this.pictures);          
      },
      error => {
        console.log(error);
      }
    );
  }

  ngOnInit(): void {
  }

}
