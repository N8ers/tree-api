# tree-api

## Running Locally

- Create venv `python3 -m venv venv`

- Enter venv `. venv/bin/activate`
- Exit venv `deactivate`

- Run the app

  - enter venv
  - `flask --app tree --debug run`

- Initilize the db `flask --app tree db init`
- Create migration `flask --app tree db migrate -m "migrate name"`
- Migrate up `flask --app tree db upgrade`
- Migrate help menu `flask db --help`

- Run tests `pytest`
- Run tests with coverage `coverage run -m pytest` then `coverage report`
- Run tests with verbose failures `coverage run -m pytest -v`
