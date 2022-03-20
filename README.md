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