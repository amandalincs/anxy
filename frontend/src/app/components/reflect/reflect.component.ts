import { Component, ViewEncapsulation, OnInit } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { HttpErrorResponse } from '@angular/common/http';
import * as Chart from 'chart.js';
import { Observable } from 'rxjs';

@Component({
    selector: 'app-reflect',
    templateUrl: './reflect.component.html',
    styleUrls: ['./reflect.component.scss'],
    encapsulation: ViewEncapsulation.None
})

export class ReflectComponent implements OnInit {
    chart: any;
    readonly ROOT_URL = 'http://127.0.0.1:5000/api';

    constructor(private httpService: HttpClient){}

    chartLabels = ['school', 'love', 'money', 'work', 'home', 'world'];

    chartData = [];

    countData = [0, 0, 0, 0, 0, 0];

    posts = [];

    ngOnInit(){
      
        this.httpService.get(this.ROOT_URL+'/posts/').subscribe(
            data => {
                for (var key in data) {
                    this.posts = data[key];
                
                for (var post in this.posts)
                {
                    var val = this.posts[post];
                    // console.log(val['category_id']);
                    this.chartData.push(val['category_id']);
                    // console.log(val['category_id']);
                }
            } 
                for (var i = 0; i < this.chartData.length; i++)
                {
                    var item = this.chartData[i];
                    if (item == 1)
                    {
                      console.log("BING");
                      this.countData[0]++;
                    }
                    else if (item == 3)
                    {
                      this.countData[1]++;
                    }
                    else if (item == 4)
                    {
                      this.countData[2]++;
                    }
                    else if (item == 5)
                    {
                      this.countData[3]++;
                    }
                    else if (item == 6)
                    {
                      this.countData[4]++;
                    }
                    else if (item == 7)
                    {
                      this.countData[5]++;
                    }
                }

            console.log(this.countData);

            },
            (err: HttpErrorResponse) => {
                console.log (err.message);
            }
        );

        this.showChart();
    }


    showChart() {
        this.chart = new Chart('lineCharts', {
          type: 'bar',
          data: {
          labels: this.chartLabels, // your labels array
          datasets: [
            {
              label: '# of anxious moments',
              data: this.countData, // your data array
              backgroundColor: [
               'rgba(54, 162, 235, 1)',
               'rgba(255, 99, 132, 1)',
               'rgba(255, 206, 86, 1)',
               'rgba(75, 192, 192, 1)',
               'rgba(153, 102, 255, 1)',
               'rgba(230, 25, 75, 1)',
               'rgba(60, 180, 75, 1)',
               'rgba(245, 130, 48, 1)',
               'rgba(145, 30, 180, 1)',
               'rgba(210, 245, 60, 1)',
               'rgba(0, 128, 128, 1)',
               'rgba(128, 0, 0, 1)'
    
              ],
              fill:true,
              lineTension:0.2,
              borderWidth: 1
            }
          ]
          },
          options: {
            responsive: true,
            title: {
            text:"your anxiety trends this week",
            display:true
            },
            scales: {
              yAxes:[{
                ticks:{
                  beginAtZero:true
                }
              }]
            }
          }
        });
      }
}

