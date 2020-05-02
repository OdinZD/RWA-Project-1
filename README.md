# About the project

**This is the back-end part of Bug/Issue tracker web application.**

## Installation

For setting virtualenv find the location of project folder in command prompt, powershell or terminal:

Then install Python in the folder and create Virtual enviroment:

On Windows:
 
 > python -m venv venv

Before you work on your project, activate the corresponding environment:

On linux:

> $venv/bin/activate


On Windows Command prompt:

> venv\Scripts\activate.bat

On Windows powershell:
> venv\Scripts\Activate.ps1

Once enviroment is activated, install from requirements.txt

> pip install -r requirements.txt

Open the project folder in VSCode and use

> python manage.py run 

to run the application.


## Contents
- [Project structure](#project_structure)
- [Management script](#management_script)
- []

### [Project structure](#project_structure)
- **app** - the main app container
    - **__init__** - all available (application) API endpoint registration
    - **main** - package where all user related functional resides (for easy integration & modularization)
- **migrations** - database migrations

#### **main**
    - controller (API endpoint definitions)
        - auth - user sign in handler
        - user
            - user list handler
            - user detail handler
            - user create handler
            - ticket list handlers 
    - model - database related object definitions
        - user - user model definition (for db)
        - ticket - ticket model definition (for db)
    - service - business logic related definitions
        - auth - user signin & database retrieval logic
        - ticket - for creating and getting all or specific ticket from database
        - user - user manager methods (creation, list & single item retrieval)
    - util
        - decorators - permission decorators, differentiate user from admin
        - dto (Data Transfer Objects)

