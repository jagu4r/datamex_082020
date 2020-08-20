SELECT titleauthor.au_id AS AUTHOR_ID, 
       authors.au_lname AS LAST_NAME,
       authors.au_fname AS FIRST_NAME,
       titles.title AS TITLE,
       SUM(ytd_sales) AS SUM_SALES,
       pub_name AS PUBLISHER
FROM pubs.publishers
LEFT JOIN titles ON titles.pub_id = publishers.pub_id
LEFT JOIN titleauthor ON titleauthor.title_id = titles.title_id
INNER JOIN authors ON authors.au_id = titleauthor.au_id
GROUP BY authors.au_id
ORDER BY sum(ytd_sales) DESC
LIMIT 3;