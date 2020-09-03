import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-list-card',
  templateUrl: './list-card.component.html'
})
export class ListCardComponent implements OnInit {

  @Input() list: any = {};
  @Input() index: number;

  @Output() selectedList: EventEmitter<number>;

  constructor(private router: Router) {
    this.selectedList = new EventEmitter();
  }

  ngOnInit(): void {
  }

  showList(){
    this.router.navigate(['/list', this.index]);
    //this.selectedList.emit(this.index);
  }

}
