# Kingfisher

Assume all the following commands are executed in the root context.

### Requirements

- Python 3.6
- Docker

### Configuration

#### Sandbox

- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip3 install -r ./requirements.txt`

#### Environment

- `source env.sh`

#### DB

- `docker run --name kingfisher_db -d -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:9.6.2`

##### Migrations

- `cd kingfisher`
- `python3 -m kingfisher.manage db upgrade`
- `cd -`

### Running

- `flask run` OR `python3 kingfisher`

