-- 10. Safe divide
DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
  DECLARE result FLOAT;
  SET result = a / b;
  IF result IS NULL THEN
    SET result = 0;
  END IF;
  RETURN result;
END;//
DELIMITER ;
