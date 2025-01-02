# Write your MySQL query statement below
SELECT c.candidate_id from Candidates c
JOIN Rounds r on r.interview_id = c.interview_id
where c.years_of_exp >= 2
group by c.candidate_id
having sum(r.score) > 15;