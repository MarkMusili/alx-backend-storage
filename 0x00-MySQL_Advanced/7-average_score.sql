-- A script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
-- ComputeAvarageScoreForSure implimentation that takes in user_id as input

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    UPDATE users
    SET users.average_score = (
        SELECT AVG(score) 
        FROM corrections
        WHERE corrections.user_id = user_id
    )
    WHERE user.user_id = user_id;

END //

DELIMITER ;

