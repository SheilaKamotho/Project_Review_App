# Project_Review_App

## Description
This application allows a user to post a project he/she has created and have it reviewed by his/her colleagues. 
A user can:

###### View posted projects and their details
###### Post a project to be rated/reviewed
###### Rate/ review other users' projects
###### Search for projects 
###### View projects overall score
###### View my profile page

## Author
Sheila N.K.

## Set up instructions
### Requirements
##### 1. Clone the repository
Clone the the repository by running

###### git clone 
or download a zip file of the project from github

Navigate to the project directory

###### cd Awwards
##### 2. Create a virtual environment
Install Virtualenv

###### pip install virtualenv
To create a virtual environment named virtual, run

###### virtualenv virtual
To activate the virtual environment we just created, run

###### source virtual/bin/activate
##### 3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress

###### $ psql
Then run the following query to create a new database named Awwards

###### Create database Awwards
##### 4.Install dependencies
To install the requirements from requirements.txt file,

###### pip install -r requirements.txt
##### 5.Create Database migrations
Making migrations on postgres using django

###### python3 manage.py makemigrations myapp
then run the command below;

###### python3 manage.py migrate
##### 6.Run the app
To run the application on your development machine,

###### python3 manage.py runserver
##### 7. Running Tests
To run tests;

###### python3 manage.py test

## Technologies Used
Django\
Python\
Html\
Css\
Bootstrap

## Bugs
There are no know bugs at the moment

## License and Copyright information.
*{MIT License Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.}* Copyright (c) {2020} {Sheila Kamotho}

## Collaboration Information
Clone the repository\
Make changes and write tests\
Push changes to github\
Create a pull request

## Contact Details
kamothosheila@gmail.com\


