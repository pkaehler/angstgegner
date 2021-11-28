from sqlalchemy import create_engine


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
