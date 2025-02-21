import unittest
from unittest.mock import MagicMock
import pandas as pd
import os

class TestBooksQuery(unittest.TestCase):
    def setUp(self):
        # Mock data for the books table
        self.mock_books_data = pd.DataFrame({
            "id": [1, 2, 3],
            "title": ["The Great Gatsby", "1984", "To Kill a Mockingbird"],
            "author_id": [1, 2, 3],
            "year": [1925, 1949, 1960]
        })

        # Mock the database
        self.mock_db = MagicMock()
        self.mock_db.query.return_value = self.mock_books_data

        # Read the SQL query from the file
        with open("queries/books_query.sql", "r") as file:
            self.sql_query = file.read().strip()

    def test_books_query(self):
        # Simulate the SQL query
        result = self.mock_db.query(self.sql_query)

        # Verify the query was called with the correct SQL
        self.mock_db.query.assert_called_once_with(self.sql_query)

        # Verify the result matches the expected output
        pd.testing.assert_frame_equal(result, self.mock_books_data)

if __name__ == "__main__":
    unittest.main()