import { Injectable } from '@angular/core';

import { HttpClient }from '@angular/common/http';

export interface Wifi {
  ssid: string;
  bssid: string;
  auth_types: string;
  key_types: string;
  signal: string;
  frequency: string;

}


@Injectable({
  providedIn: 'root'
})
export class WifiService {

  constructor(
    public http: HttpClient
  ) { }
  getWifis() {
    return this.http.get<Wifi[]>('/api/wifi');
  }
}
