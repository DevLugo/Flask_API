# Flask_API-TEST

Simple Rest API to download users form github API and store it on sqlite database.

Implemented Unittest/integration test and mock the api requests

### Tech

We uses a number of open source projects to work properly:

* [Flask] - Flask
* [SQLAlchemy] - Flask-SQLAlchemy
* [Flask-Testing] - Flask-Testing
* [dotenv] - python-dotenv
* [Python] Python 3.6

### Installation

This project requires [Python](https://nodejs.org/) v3.6+ to run.

You can create a venv enviroment with the following command.

Linux/Mac 
```sh
$ cd flask_api
$ python -m venv ./venv 
$ source venv/bin/activate 
$ pip install -r requirements.txt 
```

Windows 
```sh
$ cd flask_api
$ python -m venv ./venv 
$ source venv/Scripts/activate 
$ pip install -r requirements.txt 
```


Rename the .env.exmaple to .env
### Run the following to start the project

```sh
$ python flask_api/run.py
```

### Seed the project
I implemented a urls to seed/clean/create the db direct from browser. Only for testint propurses. In productions this is a bad practice but for development is usefull

Create db
```sh
$ http://localhost:5000/api/v1/create_db
```

seed db
```sh
$ http://localhost:5000/api/v1/seed_db
$ http://localhost:5000/api/v1/seed_db?total=250
```
You cand pass as parameter the amount of data that you want to download. The Insertions code is a batch process to optimize the queries

clean db
```sh
$ http://localhost:5000/api/v1/clean_db
```
You can clean the db and seed again with different parameters

### Retrive Users and paginate it
```sh
$ http://localhost:5000/api/v1/users
$ http://localhost:5000/api/v1/users?page=2&per_page=2
```

### Testing
For testing purpose we use a diferente database.This databas will be empty because for every test the tables will'be create and delete.
```sh
$ cd flask_api
$ nosetests --verbosity=2 test_github_process.py
$ nosetests --verbosity=2 test_github_repository.py
```

  [Python]: <https://www.python.org/>
  [Flask]: <https://flask.palletsprojects.com/>
  [SQLAlchemy]: <https://www.sqlalchemy.org/>
  [Flask-Testing]: <https://pythonhosted.org/Flask-Testing/>
  [dotenv]: <https://pypi.org/project/python-dotenv/>

 



