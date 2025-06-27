
CREATE TABLE Books(
    book_id PRIMARY KEY,
    title VARCHAR(130),
    author_id FOREIGN KEY Authors,
    price DOUBLE,
    publication_date DATE
);

CREATE TABLE Authors(
    author_id PRIMARY KEY,
    author_name VARCHAR(215)
);

CREATE TABLE Customers(
    customer_id PRIMARY KEY,
    customer_name VARCHAR(215),
    address TEXT
);

CREATE TABLE Orders(
    order_id PRIMARY KEY,
    customer_id FOREIGN KEY Customers
);