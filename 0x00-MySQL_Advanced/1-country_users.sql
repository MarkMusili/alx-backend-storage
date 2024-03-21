-- A script that creates a table
-- Create users table with id, email, name and country attributes
-- Write a script that creates a table with specific requirements
-- Script that creates users table with id, email and name attributes
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

