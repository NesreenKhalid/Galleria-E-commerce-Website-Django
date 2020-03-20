import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductService } from '../services/product.service';

@Component({
  selector: 'app-review',
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.css']
})
export class ReviewComponent implements OnInit {

  comments;
  constructor(private api : ProductService, private route:ActivatedRoute){
    this.route.paramMap.subscribe(params => this.getComments(params.get('id')))
  }

  getComments(id) : void {
    this.api.getCommentsByProductId(id).subscribe(
      data => {
        this.comments = data;
        console.log(this.comments);          
      },
      error => {
        console.log(error);
      }
    );
  }

  ngOnInit(): void {
  }

}