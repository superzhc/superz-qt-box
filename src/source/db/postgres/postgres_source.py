import psycopg2

from source.db.db_source import DBSource

DEFAULT_PORT = 5432
DEFAULT_USER = "postgres"


class PostgresSource(DBSource):
    def __init__(self,
                 port: int = DEFAULT_PORT,
                 username: str = DEFAULT_USER,
                 **kwargs
                 ):
        super().__init__(port=port, username=username, **kwargs)

    def create_conn(self):
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            database=self.database,
            **self.options
        )
