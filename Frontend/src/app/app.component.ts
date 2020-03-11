import { Component } from '@angular/core';
import { ProductlistService } from './components/services/productlist.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'testFront';
  /*category = [{title: 'test'}];
  constructor(private api : ProductlistService){
    this.getCategory();
  }
    getCategory = () => {
      this.api.getAllProducts().subscribe(
        data => {
          this.category = data;
          console.log(this.category);
        },
        error => {
          console.log(error);
        }
      );
    }*/
}
