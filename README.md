# Flask-Boilerplate

![GitHub last commit](https://img.shields.io/github/last-commit/saapooch/Flask-Boilerplate.svg?style=flat-square)
![Github All Releases](https://img.shields.io/github/downloads/saapooch/Flask-Boilerplate/total.svg?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/saapooch/Flask-Boilerplate.svg?style=flat-square)
![license](https://img.shields.io/github/license/saapooch/Flask-Boilerplate.svg?style=flat-square)



![GitHub forks](https://img.shields.io/github/forks/saapooch/Flask-Boilerplate.svg?style=social&label=Fork)
![GitHub stars](https://img.shields.io/github/stars/saapooch/Flask-Boilerplate.svg?style=social&label=Stars)
![GitHub watchers](https://img.shields.io/github/watchers/saapooch/Flask-Boilerplate.svg?style=social&label=Watch)

A skeleton repository for developing web applications with Flask.

## Contents
* [Features](#features)
* [Get Started](#get-started)
* [Tests](#tests)
* [License](#license)
* [Questions and comments](#questions-and-comments)

## Features
This repository includes:
  * SQLAlchemy Backend Support
  * Migrations
  * User Authentication
  * Password Encryption
  * WTForms
  * REST API 
  
## Get Started
  ### Using a virtual environment
  You'll need the following installed:
  * python3
  * pip3
  * virtualenv
    
  To start the virtual environment:
  ```
  python3 -m virtualenv .venv 
  source .venv/bin/activate
  ```
  
  Install the required dependencies:
  ```
  pip3 install -r requirements.txt
  ```
  
  Create the database and establish and administrator:
  ```
  python3 manage.py create_db
  python3 manage.py create_admin
  ```
  
  Run the application on a local server:
  ```
  python3 manage.py runserver
  ```
  
  Go to the [application](http://127.0.0.1:5000/)
 
## Tests
We recommend using `pytest` to run these tests as follows:

```
python3 -m pytest tests
```

## License 
This software is released open-source under the [MIT license](LICENSE).

## Questions and comments
Please contact [Saahith Pochiraju](mailto:saahith116@gmail.com) with any questions or comments.
