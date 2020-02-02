import { Component, ViewEncapsulation, OnInit } from '@angular/core';

@Component({
    selector: 'app-journal',
    templateUrl: './journal.component.html',
    styleUrls: ['./journal.component.scss'],
    encapsulation: ViewEncapsulation.None
})

export class JournalComponent implements OnInit {
    constructor(){}

    ngOnInit(){}

    submitEntry()
    {
        let userFeelings = (<HTMLInputElement>document.getElementById('input1')).value;
        let userCategory = (<HTMLInputElement>document.getElementById('category1')).value;
        let userFix = (<HTMLInputElement>document.getElementById('fix1')).value;
        let userData = {
            bothering: userFeelings,
            category: userCategory,
            goal: userFix
        };

        console.log(userData);

        // fetch('http://localhost:5000/api/categories/dfxer45tft/',{
        //     method: 'POST',
        //     body: JSON.stringify(userData)
        // }).then(response =>{

        // });
        
    }

    addEntryRow()
    {
        var itm = document.getElementById("entry1");
        var cln = itm.cloneNode(true);
        document.getElementById('day1').appendChild(cln);
    }
}