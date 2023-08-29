# LaunchPad
by NJ
She Codes crowdfunding project - DRF Backend.
## About
This website is called LaunchPad - a corwdfunding website for women in far remote towns of Australia to receive free sanitatory pads for their periods.
## Features
{{ The features your MVP will include. (Remember this is a working document, you can change these as you go!) }}
* [] feature
* [] feature
### Stretch Goals
{{ Outline three features that will be your stretch goals if you finish your MVP }}
* [] Stretch goal one
* [] Stretch goal two
* [] Stretch goal three
## API Specification
| HTTP Method | Url | Purpose | Request Body | Successful Response Code | Authentication <br /> Authorization
| --- | ------- | ------ | ---- | -----| ----|
| GET | projects/ | Return all projects | N/A | 200 | N/A |
| POST | projects/ | Create a new project | project object | 201 | User must be logged in. |
## Database Schema
{{ Insert your database schema }}
![image info goes here](./docs/image.png)
## Wireframes
{{ ![Alt text](<Screenshot 2023-08-12 at 11.42.43 am.png>)}}
![image info goes here](./docs/image.png)
## Colour Scheme
![image info goes here](./docs/image.png)
## Fonts
{{ outline your heading & body font(s) }}
## Submission Documentation
{{ Fill this section out for submission }}
Deployed Project: [Deployed website](http://linkhere.com/)
### How To Run
{{ What steps to take to run this code }}
### Updated Database Schema
![image info goes here](crowdfunding/img/schema.png)
### Updated Wireframes
![image info goes here](crowdfunding/img/wireframes.png)
### How To Register a New User
* set to "post" request
* use the address "http://localhost:8000/users/"
* In the JSON, input data for the new user (e.g -
{
    "username":"Test",
    "password":"Test",
    "email":"test@gmail.com"
})
* Send request, expected output should be a "200 OK" success message, and preview of new user details.
![image info goes here](crowdfunding/img/new_user.png)
### Screenshots
* A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
![image info goes here](crowdfunding/img/GETrequest.png)
* A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
![image info goes here](crowdfunding/img/POSTrequest.png)
* A screenshot of Insomnia, demonstrating a token being returned.
![image info goes here](crowdfunding/img/Usertoken.png)