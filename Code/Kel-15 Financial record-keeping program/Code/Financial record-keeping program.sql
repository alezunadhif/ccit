CREATE DATABASE ExpenseTracker;
USE ExpenseTracker;

-- 1. Buat tabel users
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'user') NOT NULL DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;


-- 2. Tabel Categories
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    type ENUM('INCOME', 'EXPENSE') NOT NULL
) ENGINE=InnoDB;

-- 3. Tabel Transactions
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    transaction_date DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_transactions_user 
        FOREIGN KEY (user_id) REFERENCES users(id) 
        ON DELETE CASCADE,
    CONSTRAINT fk_transactions_category 
        FOREIGN KEY (category_id) REFERENCES categories(id) 
        ON DELETE RESTRICT
) ENGINE=InnoDB;
ALTER TABLE users AUTO_INCREMENT = 1;
-- Data Awal Kategori (Opsional)
INSERT INTO categories (name, type) VALUES
('Gaji', 'INCOME'),
('Bonus', 'INCOME'),
('Makanan & Minuman', 'EXPENSE'),
('Transportasi', 'EXPENSE'),
('Tagihan & Utilitas', 'EXPENSE');

-- Data Awal users 
INSERT INTO users (username, password, role)
VALUES
('admin', SHA2('admin123', 256), 'admin'),
('bintang', SHA2('bintang123', 256), 'user');

-- Melihat Hasil
SHOW TABLES;
SELECT id, username, role FROM users;
SELECT * FROM categories;
SELECT * FROM transactions;
