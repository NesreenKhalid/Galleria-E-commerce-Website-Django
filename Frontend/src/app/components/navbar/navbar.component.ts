import { ActivatedRoute } from '@angular/router';
import { ProductlistService } from './../services/productlist.service';
import { Subscription } from 'rxjs';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

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
