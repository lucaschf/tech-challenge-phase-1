from typing import Any, List, Optional, Tuple

import psycopg2
from config.settings import settings
from psycopg2.extensions import connection as _connection


class PostgresAdapter:
    """Adapter for connecting to a PostgreSQL database."""

    def __init__(self) -> None:
        """Initializes the connection to the PostgreSQL database."""
        self.connection: _connection = psycopg2.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            dbname=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
        )

    def fetch_all(
        self,
        query: str,
        params: Optional[Tuple[Any, ...]] = None,
    ) -> List[Tuple[Any, ...]]:
        """Executes a query and fetches all results.

        Args:
            query (str): The SQL query to be executed.
            params (Optional[Tuple[Any, ...]]): The parameters to be used with the query.

        Returns:
            List[Tuple[Any, ...]]: The results of the query.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def execute(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> None:
        """Executes a query without returning any results.

        Args:
            query (str): The SQL query to be executed.
            params (Optional[Tuple[Any, ...]]): The parameters to be used with the query.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()

    def close(self) -> None:
        """Closes the connection to the PostgreSQL database."""
        self.connection.close()
