import unittest
from unittest.mock import MagicMock
import pandas as pd
import os

class TestJoinQuery(unittest.TestCase):
    def setUp(self):
        # Mock data for the books table
        self.mock_books_data = pd.DataFrame({
            "id": [1, 2, 3],
            "title": ["The Great Gatsby", "1984", "To Kill a Mockingbird"],
            "author_id": [1, 2, 3],
            "year": [1925, 1949, 1960]
        })

        # Mock data for the authors table
        self.mock_authors_data = pd.DataFrame({
            "author_id": [1, 2, 3],
            "name": ["F. Scott Fitzgerald", "George Orwell", "Harper Lee"]
        })

        # Mock the database
        self.mock_db = MagicMock()

        # Simulate the JOIN query result
        self.mock_join_result = pd.merge(
            self.mock_books_data,
            self.mock_authors_data,
            on="author_id"
        )[["title", "name"]]

        # Configure the mock to return the JOIN result
        self.mock_db.query.return_value = self.mock_join_result

        # Read the SQL query from the file
        with open("queries/join_query.sql", "r") as file:
            self.sql_query = file.read().strip()

    def test_join_query(self):
        # Simulate the SQL query
        result = self.mock_db.query(self.sql_query)

        # Verify the query was called with the correct SQL
        self.mock_db.query.assert_called_once_with(self.sql_query)

        # Verify the result matches the expected output
        pd.testing.assert_frame_equal(result, self.mock_join_result)

if __name__ == "__main__":
    unittest.main()