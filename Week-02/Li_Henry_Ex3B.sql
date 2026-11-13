Drop Database if exists beanbrew_dev;
Create Database beanbrew_dev;
USe beanbrew_dev;
Select Database();
Create Table category(
category_id tinyint unsigned primary key Auto_increment,
category_name Varchar(30) Not Null
);

Create table customer (
customer_id int primary key auto_increment,
first_name varchar(30) not null,
last_name varchar(30) not null,
email varchar(100),
city varchar(40),
loyalty_points int unsigned not null default 0,
joined_at timestamp default current_timestamp
);

Create Table product (
product_id INT primary key auto_increment,
product_name varchar(60) not null,
category_id tinyint unsigned not null,
unit_price Decimal(6,2) not null,
stock_qty int unsigned,
active boolean not null default true,
constraint fk_product_category Foreign Key (category_id)
	References category(category_id)
    on delete restrict on update cascade
    );

Create table orders (
	order_id int primary key auto_increment,
    customer_id int not null,
    product_id int not null,
    order_date date not null,
    quantity smallint unsigned not null default 1,
    constraint fk_orders_customer Foreign Key (customer_id)
    references customer(customer_id)
    ON delete restrict on update cascade,
    constraint fk_order_product Foreign Key (product_id)
    references product(product_id)
    On delete restrict on update cascade
);
Create Table employee (
employee_id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
job_title VARCHAR(40) NOT NULL,
hire_date DATE NOT NULL,
reports_to INT,
CONSTRAINT fk_employee_manager FOREIGN KEY (reports_to)
REFERENCES employee(employee_id)
ON DELETE SET NULL
);
Alter TABLE employee AUTO_INCREMENT = 100;

INSERT INTO category (category_name) VALUES
('Coffee'), ('Tea'), ('Bakery'), ('Merchandise');
INSERT INTO product (product_name, category_id, unit_price, stock_qty) VALUES
('House Blend Drip', 1, 2.75, 120), ('Espresso Single', 1, 3.25, 80),
('Caramel Latte', 1, 4.95, 60), ('Cold Brew', 1, 4.50, 45),
('Earl Grey', 2, 2.95, 50), ('Chai Latte', 2, 4.75, 40),
('Blueberry Muffin', 3, 3.50, 24), ('Butter Croissant', 3, 3.25, 30),
('Cinnamon Roll', 3, 3.95, 18), ('Logo Travel Mug', 4, 14.99, 25),
('Pumpkin Spice Latte', 1, 5.45, 35), ('Ceramic Pour-Over Set', 4, 29.99, NULL);
INSERT INTO customer (first_name, last_name, email, city, loyalty_points) VALUES
('Maria', 'Lopez', 'maria.lopez@example.com', 'Boston', 340),
('James', 'Carter', 'james.carter@example.com', 'Cambridge', 120),
('Aisha', 'Khan', 'aisha.khan@example.com', 'Boston', 560),
('Tom', 'Nguyen', NULL, 'Somerville', 75),
('Priya', 'Shah', 'priya.shah@example.com', 'Boston', 0),
('Daniel', 'Brooks', 'daniel.brooks@example.com', 'Quincy', 210);
INSERT INTO orders (customer_id, product_id, order_date, quantity) VALUES
(1, 3, '2026-09-01', 1), (2, 1, '2026-09-02', 2), (3, 7, '2026-09-03', 1),
(1, 5, '2026-09-03', 1), (3, 11, '2026-09-04', 2), (4, 2, '2026-09-05', 1),
(6, 10, '2026-09-06', 1), (1, 11, '2026-09-08', 1), (2, 8, '2026-09-09', 3);
INSERT INTO employee (first_name, last_name, job_title, hire_date, reports_to) VALUES
('Dana', 'Reyes', 'Operations Manager', '2021-03-15', NULL);
SELECT LAST_INSERT_ID();
INSERT INTO employee (first_name, last_name, job_title, hire_date, reports_to) VALUES
('Marcus', 'Hill', 'Shift Lead', '2023-06-01', 100),
('Sofia', 'Alvarez', 'Barista', '2024-09-10', 101),
('Ken', 'Ito', 'Barista', '2025-01-20', 101);
-- Check the row counts
SELECT 'category' AS table_name, COUNT(*) AS row_count FROM category
UNION ALL SELECT 'product', COUNT(*) FROM product
UNION ALL SELECT 'customer', COUNT(*) FROM customer
UNION ALL SELECT 'orders', COUNT(*) FROM orders
UNION ALL SELECT 'employee', COUNT(*) FROM employee;
SELECT employee_id, first_name, job_title, reports_to FROM employee;

Alter table product
add product_description TEXT;
Describe product;

Alter table product modify column product_name varchar(100) NOT null;

Alter table customer add phone varchar(20);
Describe customer;

ALTER TABLE customer
ALTER COLUMN city SET DEFAULT 'Boston';
INSERT INTO customer (first_name, last_name) VALUES ('Lena', 'Park');
SELECT customer_id, first_name, last_name, email, city, loyalty_points
FROM customer
WHERE last_name = 'Park';
Alter table customer add constraint uq_customer_email unique(email);
