﻿export class User {
    id?: number;
    username?: string;
    email?: string;
    password?: string;
    photoUrl?: string;

    isLoggedIn: boolean = false;

    constructor (userResponse: any ){
        this.id = userResponse.id;
        this.username = userResponse.username;
        this.email = userResponse.email;
        this.photoUrl = userResponse.photoUrl;
        
        this.isLoggedIn = true;
    }
}