# microblog

## Virtual Envinroments

VEs is the way that python enables multiple projects to have different dependency (packages) versions between them.

If the packages were installed globally different projects would be forced to use the same version. Imagine that when you were working on project A the current flask version was 1.2. Then when you started project B flask version 2 had been released. A global installation wouldn't allow you to have both projects running in the same environment.

To create a custom environment just type `python3 -m venv venv` in the root path of the project (the first venv parameter is the VE package and the second the VE name that I'm creating and it could be anything but by convention it takes this name).

To activate the virtual environment you have to run the command `source venv/bin/activate` - you are basically telling the system that you want to use it.

Once the VE is activates you are good to start installing packages `pip install flask`. To test installations open python interpreter and try to import the new package eg `import flask`.

By default the latest version is installed. To force an older one use the command `pip install "flask<2". It will pick up the latest version before version 2.


## Running a flask application

Flask need to know what the entry point is. In order to define that, export the environment variable `FLASK_APP={file name}` (example `FLASK_APP=microblog.py`). Then simply run the command `flask run`. 

Alternatively `FLASK_APP=app/test.py flask run`.

### Removing the need to provide FLASK_APP environment variable every time

Providing FLASK_APP env variable every time a new terminal session is open can be quite tedious. Since Flask 1.0 it is possible to automate this process using the package `python-dotenv`.

1. `pip install python-dotenv`
2. create a file `.flaskenv` in the root directory and add the following entry `FLASK_APP=microblog.py` (or entry file name).

### Working with Web Forms

Flask-WTF extension is a thin wrapper around the WTForms package that integrates nicely with Flask. `pip install flask-wtf`.

Configuration options:

1. providing keys in app.config. Example: `app.config['SECRET_KEY']='my-strong-secret-key'`
2. isolate the configs in a separated (and isolated) in a class module:
```
# config.py
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-default-strong-secret-key'

```

The secret key is used by flask and extensions as a cryptographic key to generate signatures and tokens. Flask-WTF uses it to protect the website against Cross Site Request Forgery (CSRF). The keys are supposed to be secret and only know by trusted maintainers and as few people as possible.

## Databases

Databases is one of the many areas that Flask is intentionally not opinionated. Through extensions it supports relational and non-relational databases and it is down to you to choose the one that suits your needs the best.


### ORMS

Flask-SQLAlchemy is an extension that provides ORMs (object relational mapper) functionalities and supports an array of databases out of the box, including popular choices like Postgres, MySQL, SQLite, etc.
ORMs translate high-level object mappings into database commands.

To install this extension run `pip install flask-sqlalchemy`.

#### Configuring SQLite

SQLite is a lightweight DB that stores each DB in a single file on the disk and there is no need to run a formal DB server like MySQL and Postgres. It is a convenient choice for development and small applications.

To begin the configuration add two extra entries in the configuration class.

```
basedir = os.path.abspath(os.path.dirname(__file__))
...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```


### DB Migrations

Data migration is a critical part of relational databases are they are centered around structured data. Once the structure change, the data which is already in the DB has to be migrated.

Database migrations can be done using the extension Flask-Migrate that is a wrapper for Alembic - `pip install flask-migrate`. 

Flask-migrate extension exposes its commands via the flask command under the subcommand db. To initiate the migration repository run the subcommand `flask db init`.

There are two ways of creating db migration scripts: manually and automatically. When creating migration scripts automatically Alembic will perform a diff between the current db schema defined by the `database models` and the `actual database`. To run the automatic creation run the command `flask db migrate` (provide the parameter `-m "users table"` to add a brief description to the created migration file name).
 
The `migrate` command does not make any changes to the DB, only creates the migration scripts. To apply the changes run `flask db upgrade` (and `flask db downgrade` to revert the latest change).  