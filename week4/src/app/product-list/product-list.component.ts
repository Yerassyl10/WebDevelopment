import { Component, OnInit } from '@angular/core';

import { products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  public imagesUrl;
  products = products;



  share() {
    window.alert('The product has been shared!');
  }
  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
  ngOnInit() {
    this.imagesUrl = [
      'https://ae01.alicdn.com/kf/H6224fd045ff3411d84ba80bc39a3b3004/Men-s-PU-Leather-Jacket-Men-Motorcycle-Hood-Winter-Coat-Man-Warm-Casual-Leather-Jackets-Male.jpg',
      'https://ae01.alicdn.com/kf/HTB1jAeSPbrpK1RjSZTEq6AWAVXad/New-Wireless-Headphones-Bluetooth-Headset-Foldable-Stereo-Headphone-Gaming-Earphones-With-Microphone-For-PC-Mobile-phone.jpg',
      'https://ae01.alicdn.com/kf/HTB1a2kIabH1gK0jSZFwq6A7aXXaa/Mark-Ryden-Man-Backpack-Fit-17-inch-Laptop-USB-Recharging-Multi-layer-Space-Travel-Male-Bag.jpg',
      'https://ae01.alicdn.com/kf/H150e74a072b44439ab129f3a905a4ae1b/MOONBIFFY-Stylish-Women-Luxury-Laser-Mini-Wallet-Card-Holder-Clutch-Coin-Purse-Leather-Handbag-Purse-Bag.jpg'
      
    ];
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at http://angular.io/license
*/