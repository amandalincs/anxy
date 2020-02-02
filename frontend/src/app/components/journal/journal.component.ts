import { Component, ViewEncapsulation, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
    selector: 'app-journal',
    templateUrl: './journal.component.html',
    styleUrls: ['./journal.component.scss'],
    encapsulation: ViewEncapsulation.None
})

export class JournalComponent implements OnInit {

    readonly ROOT_URL = 'http://127.0.0.1:5000/api';
    newPost: any;
    constructor(private http : HttpClient) {}

    ngOnInit(){}

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

        // fetch('http://localhost:5000/api/posts/',{
        //     method: 'POST',
        //     body: JSON.stringify(userData)
        // }).then(response =>{

        // }).catch(error=>{console.log(error)});
        
    }

    addEntryRow()
    {
        var itm = document.getElementById("entry1");
        var cln = itm.cloneNode(true);
        document.getElementById('day1').appendChild(cln);
    }
}