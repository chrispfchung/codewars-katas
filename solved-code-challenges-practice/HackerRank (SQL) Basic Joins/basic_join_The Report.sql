#https://www.hackerrank.com/challenges/the-report/problem

#Query using CASE and ORDER by hierarchy


SELECT (CASE G.GRADE >= 8 WHEN TRUE THEN S.NAME ELSE NULL END),G.GRADE, S.MARKS
FROM STUDENTS S JOIN GRADES G
ON (CASE WHEN S.MARKS BETWEEN G.MIN_MARK and G.MAX_MARK THEN G.GRADE ELSE NULL END)
ORDER BY G.GRADE DESC, S.name, S.marks desc
