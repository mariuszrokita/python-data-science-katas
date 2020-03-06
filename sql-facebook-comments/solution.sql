DECLARE @user TABLE
(
    id int,
    name varchar,
    joined_at datetime,
    city_id int,
    device int
)

DECLARE @user_comments TABLE
(
    user_id int,
    body text,
    created_at datetime
)


SELECT
    u.name,
    COUNT(uc.user_id) AS 'comment_count'
FROM @user AS u
LEFT JOIN @user_comments AS uc ON u.id = uc.user_id
WHERE uc.created_at >= '2019-01-01' and uc.created_at < '2019-02-01'
GROUP BY u.name


;WITH hist AS
(
    -- comment count per user
    SELECT
        u.name,
        COUNT(uc.user_id) AS 'comment_count'
    FROM @user AS u
    LEFT JOIN @user_comments AS uc ON u.id = uc.user_id
    WHERE uc.created_at >= '2019-01-01' and uc.created_at < '2019-02-01'
    GROUP BY u.name
)
SELECT
    hist.comment_count,
    COUNT(*) AS 'number of occurrences'
FROM hist
GROUP BY hist.comment_count
