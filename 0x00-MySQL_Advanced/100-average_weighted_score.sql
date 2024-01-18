-- 12. Average weighted score
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
  DECLARE average FLOAT;
  SELECT AVG(score * weight) INTO average
    FROM corrections
    JOIN users
    ON corrections.user_id = users.id
    JOIN projects
    ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id
    GROUP BY corrections.user_id;
  UPDATE users
    SET average_score = average
    WHERE id = user_id;
END;//
DELIMITER ;
