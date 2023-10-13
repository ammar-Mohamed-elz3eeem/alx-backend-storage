-- create procedure that calculates weighted averge for students

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users, (SELECT users.id as uid, (SUM(score * weight) / SUM(weight)) AS weighted_averge FROM users
	INNER JOIN corrections ON users.id = corrections.user_id
	INNER JOIN projects ON corrections.project_id = projects.id
	GROUP BY users.id) AS weight_all SET users.average_score = weight_all.weighted_averge WHERE users.id = weight_all.uid;
END$$

DELIMITER ;
