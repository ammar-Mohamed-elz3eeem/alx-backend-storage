-- create procedure that calculates weighted averge for students

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE weight_averge FLOAT;

	SET weight_averge = (SELECT (SUM(score * weight) / SUM(weight)) FROM projects
	INNER JOIN corrections ON projects.id = corrections.project_id
	WHERE corrections.user_id = user_id
	GROUP BY user_id);

	UPDATE users SET average_score = weight_averge WHERE users.id = user_id;
END$$

DELIMITER ;
