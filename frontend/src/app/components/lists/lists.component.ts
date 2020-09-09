import { Component, OnInit } from '@angular/core';
import { ListsService, List } from '../../services/lists.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-lists',
  templateUrl: './lists.component.html'
})
export class ListsComponent implements OnInit {

  lists: any[] = [];
  constructor(private _listsService: ListsService,
              private router: Router) {
  }

  ngOnInit(): void {
    this._listsService.getLists().subscribe( (data) => {
      this.lists = data['results'];
    },
      (error) => {
        console.error(error);
      }
    );
    console.log(this.lists);
  };

  // showList(idx:number){
  //   this.router.navigate(['/list',idx]);
  // }
}
