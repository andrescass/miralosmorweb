import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ListsService, List } from '../../services/lists.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html'
})
export class ListComponent {

  list: any = {};

  constructor(private activatedRoute: ActivatedRoute,
              private _listsService: ListsService) {
    this.activatedRoute.params.subscribe( params => {
      this.list = this._listsService.getList(params['id']);
    })
   }


}
