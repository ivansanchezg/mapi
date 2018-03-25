# Mapi

Mapi is a Movie API made with [python](https://www.python.org/), [flask](http://flask.pocoo.org/) and [marshmallow](https://marshmallow.readthedocs.io/en/latest/index.html).

This project was done with sole purpose of learning this technologies.

## How to Run locally

### Unix (Linux & MacOs)

1. Install python

2. Execute: `pip install -r requirements/common.txt`

3. In your terminal run:
```
$ export FLASK_APP="mapi/app.py"
$ export FLASK_DEBUG=1
$ flask run
```

> `export FLASK_DEBUG=1` is optional. It will set the debugger, which will log errors into the terminal and reset the application anytime there is a change in the code.

The application will be run in your [localhost](http://localhost:5000) on port `5000`.
To exit press `Ctrl + C` on your terminal.

### Windows

1. Install python

2. Execute: `pip install -r .\requirements\common.txt`

3. In PowerShell run:
```
> $env:FLASK_APP = "mapi/app.py"
> $env:FLASK_DEBUG = 1
> flask run
```

`$env:FLASK_DEBUG = 1` is optional. It will set the debugger, which will log errors into the terminal and reset the application anytime there is a change in the code.

The application will be run in your [localhost](http://localhost:5000) on port `5000`.
To exit press `Ctrl + C` on your terminal.

## API

### Get the list of movies

GET to `http://localhost:5000/movies`

`$ curl http://localhost:5000/movies`

### Get a movie

GET to `http://localhost:5000/movies/<movie_id>`

`$ curl http://localhost:5000/movies/<movie_id>`

### Add a movie

POST to `http://localhost:5000/movies`

Headers
```
Content-Type = application/json
```

Request example:
```json
{
	"name": "WALL-E",
	"director": "Andrew Stanton",
	"year": 2008,
	"genres": ["Animation", "Comedy"]
}
```

`curl -X POST http://localhost:5000/movies -H "Content-Type: application/json" -d '{\"name\": \"WALL-E\", \"director\": \"Andrew Stanton\", \"year\": 2008, \"genres\": [\"Animation\", \"Comedy\"]}'`

### Update a movie

PATCH to `http://localhost:5000/movies/<movie_id>`

Headers
```
Content-Type = application/json
```

Request example:
```json
{
	"name": "WALL-E 2: The Attack of the Robots",
	"year": 2012
}
```

`curl --request PATCH http://localhost:5000/movies/<movie_id> -H "Content-Type: application/json" -d '{\"name\": \"WALL-E 2: The Attack of the Robots\"}'`

### Delete a movie:

DELETE to `http://localhost:5000/movies/<movie_id>`

`curl -X DELETE http://localhost:5000/movies/<movie_id>`
