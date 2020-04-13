import { Component, OnInit } from '@angular/core';

import { WifiService, Wifi  } from '../wifi.service';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {
 
 
  wifis: Wifi[];
  
  
  constructor(
    public wifiService: WifiService
  ) { 
    this.getWifis();
  }

  ngOnInit()  {
    
  }
  getWifis() {
    this.wifiService.getWifis().subscribe(
      data => {
        this.wifis = data;
      },
      error => {
        alert('Could not retrieve a list of wifis');
      }
    );
    }

}
