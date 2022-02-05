from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from consumer.database.League import League


def get_connection_string(host: str = "localhost",
                          port: int = 5432,
                          db: str = "",
                          user: str = None,
                          password: str = None):
    db_type = "postgresql"
    if user and password:
        return f"{db_type}://{user}:{password}@{host}:{port}/{db}"
    else:
        return f"{db_type}://{host}:{port}/{db}"


def get_engine(connection_string):
    print(connection_string)
    engine = create_engine(connection_string)
    return engine


test = get_engine(get_connection_string(db="angstgegner"))

test_league = League(id=1,name='Foobar', country='DE')

Session = sessionmaker(bind=test)
session = Session()
session.add(test_league)

foobar = session.query(League)
print(foobar)