# Task details

Link: https://www.interviewquery.com/ (2020-03-06)

This question was asked by Facebook.

Given a users table and a user_comments table, write a SQL query to generate a histogam of number of comments per user in the month of January 2019. Assume bin buckets intervals of one.

`users` table:
| columns |   type   |
|---      |---       |
|id       |int       |
|name     |varchar   |
|joined_at|datetime  |
|city_id  |int       |
|device   |int       |

`user_comments` table:
| columns  |type    |
|---       |---     |
|user_id   |int     |
|body      |text    |
|created_at|datetime|