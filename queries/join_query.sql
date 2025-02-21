SELECT books.title, authors.name
FROM books
JOIN authors ON books.author_id = authors.author_id;