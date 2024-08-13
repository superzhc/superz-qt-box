from abc import ABC, abstractmethod

from source.base_source import Source


class DBSource(Source, ABC):
    host: str
    port: int
    username: str
    password: str
    database: str

    _conn = None

    def __init__(self,
                 *,
                 host: str = None,
                 port: int = None,
                 username: str = None,
                 password: str = None,
                 database: str = None,
                 **kwargs,
                 ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.options = kwargs

        self._conn = None

    def get_connect(self):
        if not self._conn:
            self._conn = self.create_conn()

        return self._conn

    @abstractmethod
    def create_conn(self):
        pass

    def close_connect(self):
        if self._conn:
            self._conn.close()
            self._conn = None

    def handler(self, **kwargs):
        if not "sql" in kwargs:
            raise KeyError("sql 参数必须被设置")

        conn = self.get_connect()
        with conn.cursor() as cursor:
            cursor.execute(kwargs.get("sql"))

            results = cursor.fetchall()
            return results
