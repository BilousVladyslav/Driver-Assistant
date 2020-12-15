import { Component, OnInit, Inject, OnDestroy } from '@angular/core';
import { Subscription, timer } from 'rxjs';
import { CarsService } from '../../core/services/cars.service';
import { L10N_LOCALE, L10nLocale } from 'angular-l10n';
import { Car } from '../../shared/models/car.model';


@Component({
  selector: 'app-cars-map',
  templateUrl: './cars-map.component.html',
  styleUrls: ['./cars-map.component.css']
})
export class CarsMapComponent implements OnInit, OnDestroy {
  subscription: Subscription = new Subscription();

  cars: Car[];

  lat = 50.005942;
  lng = 36.229618;
  
  constructor(
    private carsService: CarsService,
    @Inject(L10N_LOCALE) public locale: L10nLocale
  ) {
    this.cars = [];
  }

  ngOnInit(): void {
    this.subscription.add(timer(0, 2000).subscribe(ellapsedCycles => {
      this.subscription.add(
        this.carsService.GetAllCars().subscribe(data => this.cars = data)
      )
    }));
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
