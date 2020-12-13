import { Component, OnDestroy, OnInit, Inject } from '@angular/core';
import { Router } from '@angular/router';
import { Observable, Subscription } from 'rxjs';
import { ProfileService } from '../../core/services/profile.service';
import { CarsService } from '../../core/services/cars.service';
import { UserProfileModel } from '../../shared/models/user.profile.model';
import { Car, EditCar } from '../../shared/models/car.model';
import { FormBuilder, FormGroup, FormControl, Validators, FormArray } from '@angular/forms';
import { AuthorizationService } from 'src/app/core/services/authorization.service';
import { NameRegex } from 'src/app/shared/regexes/name.regex';
import { L10N_LOCALE, L10nLocale } from 'angular-l10n';
import {MatSnackBar} from '@angular/material/snack-bar';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit, OnDestroy {
  subscription: Subscription = new Subscription();
  user: UserProfileModel = new UserProfileModel();
  userProfileForm: FormGroup;

  carsFormGroup: FormGroup;
  carsFormArray: FormArray;

  cars: Car[];

  constructor(
    private profileService: ProfileService,
    private authorizationService: AuthorizationService,
    private router: Router,
    private carsService: CarsService,
    private fb: FormBuilder,
    private _snackBar: MatSnackBar,
    @Inject(L10N_LOCALE) public locale: L10nLocale
  ) {}

  ngOnInit(): void {
    this.GetUserProfile();
    this.CreateForm();

    this.subscription.add(
        this.carsService.GetMyCars().subscribe(data => {
          this.cars = data;
          this.createCarsForms(data);
        })
    );
  }

  CreateForm(): void {
    this.userProfileForm = this.fb.group({
      first_name: new FormControl(
        '', [Validators.required, Validators.maxLength(50), Validators.pattern(NameRegex.Regex)]),
      last_name: new FormControl(
        '', [Validators.required, Validators.maxLength(50), Validators.pattern(NameRegex.Regex)]),
    });
  }

  GetUserProfile(): void {
    this.subscription.add(this.profileService.GetUserProfile()
      .subscribe(data => {
        this.user = data;
      })
    );
  }

  EditUserProfile(): void {
    this.subscription.add(this.profileService.EditUserProfile(this.user)
      .subscribe(data => {
        this.user = data;
        this._snackBar.open('Success!', 'Close', {
          duration: 3000,
        });
      },
      error => {
        this._snackBar.open('Wrong data,', 'Close', {
          duration: 3000,
        });
      })
    );
  }

  onSubmitProfile(): void {
    this.EditUserProfile();
  }

  createCarsForms(cars_data: Car[]): void {
    this.carsFormGroup = this.fb.group({
      cars: this.fb.array([])
    });
    this.carsFormArray = this.carsFormGroup.get('cars') as FormArray;
    for (let i = 0; i < cars_data.length; i++) {
      let carFG = this.fb.group({
        name: new FormControl(
          cars_data[i].name, [Validators.required]),
        number: new FormControl(
          cars_data[i].number, [Validators.required, Validators.maxLength(10)]),
        is_special: new FormControl(
          cars_data[i].is_special, [Validators.required]),
      })
      this.carsFormArray.push(carFG);
    }
  }

  createCarForm() {
    return this.fb.group({
      name: new FormControl(
        '', [Validators.required]),
      number: new FormControl(
        '', [Validators.required, Validators.maxLength(10)]),
      is_special: new FormControl(
        false, [Validators.required])
    })
  }

  addCar() {
    this.carsFormArray.push( this.createCarForm() );
  }

  deleteCar(index) {
    if (index < this.cars.length) {
      this.subscription.add(this.carsService.DeleteCar(this.cars[index].id).subscribe(
        res => {
          this.cars.splice(index, 1);
          this.carsFormArray.removeAt(index);
        },
        errors => console.log(errors)
      ));
    }
    else {
      this.carsFormArray.removeAt(index);
    }
  }

  onSubmitCars(): void {
    for (let i = 0; i < this.carsFormArray.length; i++) {
      var carModel = <EditCar>(this.carsFormArray.controls[i].value);
      if (i < this.cars.length) {
        this.subscription = this.carsService.EditCar(this.cars[i].id, carModel).subscribe(
          res => this.cars[i] = res,
          errors => console.log(errors)
        );
      }
      else {
        this.subscription = this.carsService.CreateCar(carModel).subscribe(
          res => this.cars.push(res),
          errors => console.log(errors)
        );
      }
    }
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
