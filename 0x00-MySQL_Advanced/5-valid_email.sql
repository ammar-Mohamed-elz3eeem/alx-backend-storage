-- create triggers

DROP TRIGGER IF EXISTS change_email_status;

delimiter $$

CREATE TRIGGER change_email_status BEFORE UPDATE on users
	FOR EACH ROW
	BEGIN
		IF !(NEW.email <=> OLD.email) THEN
			SET NEW.valid_email = 0;
		END IF;
	END
$$

delimiter ;