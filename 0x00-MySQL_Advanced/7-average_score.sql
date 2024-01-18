-- 7. Average score
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  DECLARE average INT;
  SELECT AVG(score) INTO average
    FROM users INNER JOIN corrections
    ON users.id = corrections.user_id
    GROUP BY user_id
    WHERE user.id = user_id;
  UPDATE users
    SET average_score = average
    WHERE id = user_id;
END;//
DELIMITER ;
