import { Injectable } from '@angular/core';
import { ListsComponent } from '../components/lists/lists.component';

@Injectable({
    providedIn: 'root'
})
export class ListsService {

    private lists: List[] = [
        {
          name: "Miralos Deprimirse",
          description: "Que mirar cuando te querés cortar las venas con una galletita de agua humeda?",
          img: "assets/img/ninioPijama.jpg",
          by: "Nico Annia",
          words: "corchazo, tiro en los huevos, suicidio, depre",
          movies: [{name: "The Boy in the Striped Pijamas", url: "https://letterboxd.com/film/the-boy-in-the-striped-pyjamas/"},
                    {name: "Her", url: "https://letterboxd.com/film/her/"},
                    {name: "Blue Valentine", url: "https://letterboxd.com/film/blue-valentine/"},
                    {name: "Amour", url: "https://letterboxd.com/film/amour/"}]
        }
      ];

    getLists(): List[]{
        return this.lists;
    }

    getList(idx: number){
        return this.lists[idx];
    }

    searchList( word: string){

      let listsArray:List[]=[];
      word = word.toLowerCase();
      for (let list of this.lists){
        let name = list.words.toLowerCase();
        if (name.indexOf(word) >= 0) {
          listsArray.push(list);
        }
      }
      return listsArray;
    }
}

export interface Movies{
  name: string;
  url: string;
}
export interface List{
    name: string;
    description: string;
    img: string;
    by: string;
    words: string;
    movies: Movies[];
}