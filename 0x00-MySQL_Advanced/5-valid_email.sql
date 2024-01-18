-- 5. Email validation to sent
DELIMITER //
CREATE TRIGGER reset_valid_email
AFTER UPDATE
ON users
FOR EACH ROW
BEGIN
  IF NEW.email != OLD.email THEN
    UPDATE users
    SET valid_email = DEFAULT
    WHERE id = NEW.id;
  END IF;
END;//
DELIMITER ;
