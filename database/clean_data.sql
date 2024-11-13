-- Remove records with NULL change_id or description
DELETE FROM change_records WHERE change_id IS NULL OR description IS NULL;

-- Standardize status column to have consistent case
UPDATE change_records SET status = UPPER(status);

-- Remove duplicates based on change_id
DELETE FROM change_records
WHERE id NOT IN (
    SELECT MIN(id)
    FROM change_records
    GROUP BY change_id
);
