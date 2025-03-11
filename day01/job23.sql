SELECT * FROM etudiant ORDER BY age DESC LIMIT 1;

SELECT * FROM etudiant WHERE age = (SELECT MAX(age) FROM etudiant);