How to run:
	1. First make sure the following packages are installed: wtforms, psycopg2, flask, flask-wtforms, postgresql
	2. create a database named ecrideshare_db on postgresql (check line 20 of flaskapp.py if there is a problem with db connection)
	3. Run create.sql file to create the tables.
	4. Now you should be able to run the app by typing "python flaskapp.py"
	5. Go to a browser and type localhost:5000/ and that should take you to the front page.

NOTE:
	1. We are assumming you enter valid values in all the fields in the form while posting for a ride.
	2. Right now, both links on the index page points to the same form
