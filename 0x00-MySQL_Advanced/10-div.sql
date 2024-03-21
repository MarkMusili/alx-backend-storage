-- A script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
-- SafeDIV implimentation
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS INT
BEGIN
    IF b == 0 THEN
        RETURN 0
    ELSE 
        RETURN a / b
    END IF
END //