# FastAPI Poll APP
an app created witha python web framework called fastAPI
mainly for building API's Asynchronously   

## Technologies used :
- python 3.9+
- FastAPI web framework
- postgresql
- python poetry -- it is a package package manager like NPM of javascript. it can manage mainly     installed files and help make use the are stored and can be ran with problems
- SQLAlchemy is a like an ORM for Flask(an extension of it) that can be used in FastAPI
- uvicorn 

### Schema 
User Table:
- username
- email
- created_at
- updated_at

### Functions
- people can vote like everyone
anyone can add an option to the poll during the poll(during the poll time)
can use a social login to Twitch

### how to run with poetry
- poetry run uvicorn poll:app --reload

### how to run with only uvicorn
- uvicorn poll:app --reload