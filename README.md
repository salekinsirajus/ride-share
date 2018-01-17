# EC RideShare
This is a web app intended for the Earlham College community members
to share rides.

## Tools
We are using Flask, which is a lightweight web framework, ideal for our
purposes. The backend is powered by PostgreSQL (as of now), but we plan
on moving to a lighter, more convenient database.


## Setup
1. Clone this repo:
```
git clone https://github.com/salekinsirajus/ride-share.git
```   
2. Install the dependencies:
    * wtforms 
    * psycopg2
    * flask 
    * flask-wtforms
    You can use pip to install all these:
    ```
    pip -r install requirements.txt
    ```
3. Make sure PostgreSQL is installed and ready to be used
2. create a database named ecrideshare_db on postgresql 
(check line 20 of flaskapp.py if there is a problem with db connection)
3. Run create.sql file to create the tables.
4. Now you should be able to run the app by typing "python flaskapp.py"
5. Go to a browser and type localhost:5000/ and that should take you to the front page.

## Comments
1. We are assumming you enter valid values in all the fields in the form 
    while posting for a ride.
2. Right now, both links on the index page points to the same form
