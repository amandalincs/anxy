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
    dayPosts: Object;
    front_todaysDate: string;
    back_todaysDate: string;
    constructor(private http : HttpClient)
    {
        // this.todaysDate = this.datePipe.transform(this.todaysDate, 'yyyy-MM-dd');
    }
    // constructor(private http : HttpClient) {}

    ngOnInit(){
        this.front_todaysDate = formatDate(new Date(), 'M/d/yy', 'en');
        this.back_todaysDate = formatDate(new Date(), 'MM/dd/yyyy', 'en');
        this.getDayPosts(this.back_todaysDate);
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
    }

    getDayPosts(dateString)
    {
        // this.http.get(this.ROOT_URL+"/posts/2/2/2020")
        this.http.get(this.ROOT_URL+"/posts/"+dateString).subscribe(
            data => {this.dayPosts = data;}
        );
    }

    addEntryRow()
    {
        var itm = document.getElementById("entry1");
        var cln = itm.cloneNode(true);
        document.getElementById('day1').appendChild(cln);
    }
}