-- Script that creates a trigger that resets the attribute valid_email only when the email has been changed
-- Trigget to reset the value of valid_email implimentation
DELIMITER //

CREATE TRIGGER reset_value
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != Old.email THEN
        SET NEW.valid_email = 0;
    End IF;
END //

DELIMITER ;
