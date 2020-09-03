import { Component, OnInit } from '@angular/core';
import { ListsService, List } from '../../services/lists.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-lists',
  templateUrl: './lists.component.html'
})
export class ListsComponent implements OnInit {

  lists:List[] = [];
  constructor(private _listsService: ListsService,
              private router: Router) {
  }

  ngOnInit(): void {
    this.lists = this._listsService.getLists();
  }

  showList(idx:number){
    this.router.navigate(['/list',idx]);
  }
}
