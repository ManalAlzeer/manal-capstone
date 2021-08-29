# Capstone Project
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

- Roles:
  - Casting Assistant : Can view actors and movies
  - Casting Director :
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies
  - Executive Producer :
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database

## Getting Started

https://manal-capstone.herokuapp.com/


### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

### Running the server

To run the server, execute:

```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
python -m flask run
```

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```

The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 
- 500: Internal server error
- 405: Method not allowed


### Endpoints 
#### GET /movies
- General: Returns a list movies.

#### GET /Actors
- General: Returns a list Actors.

#### DELETE /movies/<int:id>
- General: Deletes the movie by using the passed id and returns the success value.

#### DELETE /actors/<int:id>
- General: Deletes the actor by using the passed id and returns the success value.

#### POST /movies

- General: Creates a new movie using the submitted id, title and release.

#### POST /actors

- General: Creates a new actor using the submitted id, name, age and gender.

#### PATCH /actors/<int:id>
- General: update values by using the passed id and returns a new values.

#### PATCH /movies/<int:id>
- General: update values by using the passed id and returns a new values.



## Authors
Manal Alzeer