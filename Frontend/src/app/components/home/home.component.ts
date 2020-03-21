import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { Component, OnInit } from '@angular/core';

import { ProductlistService } from '../services/productlist.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  products ;
  p: number = 1;
  count: number = 3;
  searchText;
  productsObservable: Subscription;
  constructor(private api : ProductlistService,private route:ActivatedRoute){
    this.route.paramMap.subscribe(params => this.getAllProducts())

  }
  getAllProducts = () => {
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
