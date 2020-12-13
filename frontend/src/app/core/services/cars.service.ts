import { Injectable } from '@angular/core';
import {environment} from '../../../environments/environment';
import {HttpClient, HttpParams} from '@angular/common/http';
import { Observable } from 'rxjs';
import { Car, EditCar } from '../../shared/models/car.model';


@Injectable({
  providedIn: 'root'
})
export class CarsService {


  controllerUrl: string = environment.apiURL + '/my-cars/';

  constructor(private http: HttpClient) {
  }


  GetMyCars(): Observable<Car[]> {
    return this.http.get<Car[]>(this.controllerUrl);
  }

  GetAllCars(): Observable<Car[]> {
    return this.http.get<Car[]>(environment.apiURL + '/all-cars/');
  }

  GetCar(carID: number): Observable<Car> {
    return this.http.get<Car>(this.controllerUrl + carID.toString() + '/');
  }

  CreateCar(car: EditCar): Observable<Car> {
    return this.http.post<Car>(this.controllerUrl, car);
  }

  EditCar(carID: number, car: EditCar): Observable<Car> {
    return this.http.put<Car>(this.controllerUrl + carID.toString() + '/', car);
  }

  DeleteCar(carID: number): Observable<any> {
    return this.http.delete<any>(this.controllerUrl + carID.toString() + '/');
  }
}
