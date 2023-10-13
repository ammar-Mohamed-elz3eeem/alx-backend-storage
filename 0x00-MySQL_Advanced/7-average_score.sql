-- procedure that calculates averge score for users

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

delimiter //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
UPDATE users SET average_score = (SELECT AVG(score) FROM corrections GROUP BY corrections.user_id HAVING corrections.user_id = user_id) WHERE id = user_id;
END //

delimiter ;
