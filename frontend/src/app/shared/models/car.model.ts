import { Coordinates } from '../models/coordinates.model'

export class Car {
    id: number;
    name: string;
    number: string;
    owner: number;
    coordinates: Coordinates;
    is_special: boolean;
}

export class EditCar {
    name: string;
    number: string;
}
