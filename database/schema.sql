-- Create a table for storing change records
CREATE TABLE IF NOT EXISTS change_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    change_id VARCHAR(50) UNIQUE NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL
);
