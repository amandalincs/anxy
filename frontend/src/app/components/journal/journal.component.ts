import { Component, ViewEncapsulation, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { formatDate } from '@angular/common';

@Component({
    selector: 'app-journal',
    templateUrl: './journal.component.html',
    styleUrls: ['./journal.component.scss'],
    encapsulation: ViewEncapsulation.None
})

export class JournalComponent implements OnInit {

    readonly ROOT_URL = 'http://127.0.0.1:5000/api';
    todaysPosts: any[] = new Array();
    pastPosts: any[] = new Array();
    categories: any[] = new Array();
    todaysDate: string;
    start = 1;
    constructor(private http : HttpClient)
    {
        
    }

    ngOnInit(){
        this.todaysDate = formatDate(new Date(), 'M/d/yy', 'en');
        this.getTodaysPosts();
        this.getMorePosts(6);
    }

    submitEntry()
    {
        let userFeelings = (<HTMLInputElement>document.getElementById('input1')).value;
        let userCategory = (<HTMLInputElement>document.getElementById('category1')).value;
        let userFix = (<HTMLInputElement>document.getElementById('fix1')).value;
        let userData = {
            bothering: userFeelings,
            c_id: userCategory,
            goal: userFix
        };

        console.log(JSON.stringify(userData));
        
        this.http.post(this.ROOT_URL+'/posts/', userData).subscribe();
        location.reload();
    }

    getTodaysPosts()
    {
        this.http.get(this.ROOT_URL+"/posts/today").subscribe(
            data => {this.todaysPosts = data['posts'];}
        );
    }

    getMorePosts(numPosts)
    {
        for (let i = this.start; i < this.start+numPosts; i++)
        {
            // this.http.get(this.ROOT_URL+"/posts/days_before/"+String(i)).subscribe(
            //     data => {console.log(data);}
            this.http.get(this.ROOT_URL+"/posts/days_before/"+String(i)).subscribe(
                data => {this.pastPosts.push(data);}
            );
        }
        console.log(this.pastPosts);
        this.start += numPosts;
        // console.log(this.pastPosts);
    }

    addEntryRow()
    {
        var itm = document.getElementById("entry1");
        var cln = itm.cloneNode(true);
        document.getElementById('day1').appendChild(cln);
    }
}