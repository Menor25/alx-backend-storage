-- Create a table called users
-- Attributes:
--      id: integer, never null, auto increament, primary key
--      email: string(255 characters), never null, unique
--      name: string(255 characters)
--      country: enumweration of countries (US, CO, TN), never null, defaultis US
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN' ) DEFAULT 'US'
);
