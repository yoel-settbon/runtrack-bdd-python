SELECT * FROM etudiant ORDER BY age ASC LIMIT 1;

SELECT * FROM etudiant WHERE age = (SELECT MIN(age) FROM etudiant);