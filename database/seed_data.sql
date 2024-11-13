-- Insert sample data into the change_records table
INSERT INTO change_records (change_id, description, status, created_at, updated_at) VALUES
('CHG001', 'Initial database setup', 'COMPLETED', '2024-01-10 10:00:00', '2024-01-11 14:00:00'),
('CHG002', 'Added data transformation scripts', 'IN_PROGRESS', '2024-01-12 09:30:00', NULL),
('CHG003', 'Data cleaning process', 'PENDING', '2024-01-13 11:15:00', NULL);
