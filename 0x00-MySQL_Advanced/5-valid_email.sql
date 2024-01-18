-- 5. Email validation to sent
DELIMITER //
CREATE TRIGGER reset_valid_email
AFTER UPDATE
ON users
FOR EACH ROW
BEGIN
  IF NEW.email != OLD.email THEN
    SET NEW.valid_email = DEFAULT;
  END IF;
END;//
DELIMITER ;
