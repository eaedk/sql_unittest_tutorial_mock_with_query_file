# SQL Unit Testing with Python and `unittest.mock`

This repository demonstrates how to unit test SQL queries in Python using `unittest.mock` to simulate a database. The SQL queries are read from `.sql` files, and the tests are designed to be isolated, maintainable, and reproducible.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Setup Instructions](#setup-instructions)
4. [Running the Tests](#running-the-tests)
5. [How It Works](#how-it-works)
6. [Contributing](#contributing)
7. [License](#license)

---

## Project Overview

This project provides a framework for unit testing SQL queries in Python without requiring a real database. Instead, it uses `unittest.mock` to simulate database behavior and reads SQL queries from `.sql` files. This approach ensures that the tests are:

- **Isolated**: No external dependencies like a real database or CSV files.
- **Maintainable**: SQL queries are stored separately in `.sql` files.
- **Reproducible**: Tests can be run consistently across different environments.

Two examples are included:
1. A simple SQL query to fetch all books from a `books` table.
2. A SQL query that joins the `books` and `authors` tables.

---

## Project Structure

```
sql_unittest_tutorial_mock_with_query_file/
│
├── queries/                  # Contains SQL query files
│   ├── books_query.sql       # Query to fetch all books
│   └── join_query.sql       # Query to join books and authors
│
├── tests/                   # Contains unit test files
│   ├── test_books_query.py  # Tests for books_query.sql
│   └── test_join_query.py   # Tests for join_query.sql
│
└── README.md                # Project documentation
```

---

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- `pandas` library (for DataFrame comparisons)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sql_unittest_tutorial_mock.git
   cd sql_unittest_tutorial_mock
   ```

2. Install the required dependencies:
   ```bash
   pip install pandas
   ```

---

## Running the Tests

To run the unit tests, use the following commands:

1. Test the `books_query.sql`:
   ```bash
   python -m unittest tests/test_books_query.py
   ```

2. Test the `join_query.sql`:
   ```bash
   python -m unittest tests/test_join_query.py
   ```

### Expected Output

If the tests pass, you will see an output like:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```

If the tests fail, the output will indicate which part of the query or data did not match.

---

## How It Works

### Simulating the Database

The `unittest.mock` library is used to simulate a database. A `MagicMock` object is created to mock the `query` method of the database. The mock is configured to return predefined data when specific SQL queries are executed.

### Reading SQL Queries

SQL queries are stored in `.sql` files inside the `queries/` directory. The tests read these queries dynamically using Python's `open()` function. This ensures that the queries are not hardcoded in the test files, making the tests more maintainable.

### Testing Logic

1. **Mock Data**: Mock data is created using `pandas.DataFrame` to simulate database tables.
2. **Query Execution**: The SQL query is executed using the mocked database.
3. **Assertions**:
   - Verify that the query was called with the correct SQL statement.
   - Compare the result of the query with the expected output using `pd.testing.assert_frame_equal`.

---

## Example Queries

### `books_query.sql`

```sql
SELECT * FROM books;
```

### `join_query.sql`

```sql
SELECT books.title, authors.name
FROM books
JOIN authors ON books.author_id = authors.author_id;
```

---

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Python's `unittest.mock` library for simulating database behavior.
- `pandas` for DataFrame comparisons.
