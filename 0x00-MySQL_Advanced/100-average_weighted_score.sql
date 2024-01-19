-- 12. Average weighted score
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN

  DECLARE total_scores FLOAT;
  DECLARE total_weights FLOAT;

  SELECT SUM(weight) into total_weights, SUM(score * weight) INTO total_scores
    FROM corrections
    JOIN users
    ON corrections.user_id = users.id
    JOIN projects
    ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id
    GROUP BY corrections.user_id;

  UPDATE users
    SET average_score = total_scores / total_weights
    WHERE id = user_id;

END;//

DELIMITER ;
