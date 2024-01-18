-- 5. Email validation to sent
DELIMITER //
CREATE TRIGGER reset_valid_email
AFTER UPDATE
ON users
FOR EACH ROW
BEGIN
  UPDATE users
  SET valid_email = 0
  WHERE id = NEW.id;
END;//
DELIMITER ;
