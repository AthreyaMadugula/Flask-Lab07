
# Login Register Form with Flask + SQLAlchemy


I have just started learning Flask and I am developing a project. I plan to share some special things I do occasionally. This form I share with, in the light of new beginners. You can use this simple and useful form as you like.

### Requirements

    pip install flask
    pip install SQLAlchemy
    pip install Flask-SQLAlchemy
    pip install flask-login



### In This Project

With SQLAlchemy, data logging and data retrieval to the database and user registration and logging were performed. That is all :)


before you run it you will need to change this part of the code  in the app.py file 

	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://////{home/vurudi100/Downloads/Flask Exercise 2- Sign up}/database.db'
	
	replace the part in the {} braces with actual path to the database.db file  {home/vurudi100/Downloads/Flask Exercise 2- Sign up}
