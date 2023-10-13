-- create procedure that adds bounes

DROP PROCEDURE IF EXISTS AddBonus;

delimiter //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE project_id INT;
	IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0 THEN
		INSERT INTO projects VALUES (NULL, project_name);
	END IF;
	SET project_id = (SELECT id FROM projects WHERE projects.name = project_name LIMIT 1);
	INSERT INTO corrections VALUES (user_id, project_id, score);
END //

delimiter ;
