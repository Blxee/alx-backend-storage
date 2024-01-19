-- 13. Average weighted score for all!
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN

  CREATE VIEW scores_view AS
    SELECT user_id AS id,
           SUM(weight) AS total_weights,
           SUM(score * weight) AS total_scores
    FROM corrections
    JOIN users
    ON corrections.user_id = users.id
    JOIN projects
    ON corrections.project_id = projects.id
    GROUP BY corrections.user_id;

  UPDATE users
    JOIN scores_view ON users.id = scores_view.id
    SET average_score = scores_view.total_scores / scores_view.total_weights;

END;//

DELIMITER ;
