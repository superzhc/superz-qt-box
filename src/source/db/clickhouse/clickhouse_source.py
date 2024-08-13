import clickhouse_driver

from source.db.db_source import DBSource

DEFAULT_PORT = 9000
DEFAULT_USER = "default"
DEFAULT_PASSWORD = ""
DEFAULT_DATABASE = "default"


class ClickhouseSource(DBSource):

    def __init__(self,
                 port: int = DEFAULT_PORT,
                 username: str = DEFAULT_USER,
                 password: str = DEFAULT_PASSWORD,
                 database: str = DEFAULT_DATABASE,
                 **kwargs
                 ):
        super().__init__(port=port, username=username, password=password, database=database, **kwargs)

    def create_conn(self):
        return clickhouse_driver.connect(
            # f"clickhouse://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password if self.password else DEFAULT_PASSWORD,  # 注意：若clickhouse未设置密码，不能使用None，需要使用空字符串
            database=self.database,
            **self.options
        )


if __name__ == "__main__":
    source = ClickhouseSource(host="localhost", database="default")
    conn = source.get_connect()
    with conn.cursor() as cursor:
        cursor.execute("select * from simple")
        print(cursor.fetchall())
    conn.close()
