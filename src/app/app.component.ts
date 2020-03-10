import { Component } from '@angular/core';
import { ProductlistService } from './components/services/productlist.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'testFront';
  movies = [{title: 'test'}];
  constructor(private api : ProductlistService){
    this.getMovies();
  }
    getMovies = () => {
      this.api.getAllProducts().subscribe(
        data => {
          this.movies = data;
          console.log(this.movies);
        },
        error => {
          console.log(error);
        }
      );
    }
}
