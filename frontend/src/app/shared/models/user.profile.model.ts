export class UserProfileModel {
    username: string;
    email: string;
    first_name: string;
    last_name: string;
    is_staff: boolean;
}

export class ChangePassword{
    old_password: string;
    new_password: string;
    confirm_password: string;
}

export class ChangeEmail{
    email: string;
}