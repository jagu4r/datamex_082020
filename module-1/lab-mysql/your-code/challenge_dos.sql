SELECT titleauthor.au_id AS AUTHOR_ID, 
       authors.au_lname AS LAST_NAME,
       authors.au_fname AS FIRST_NAME,
       count(titles.title) AS TITLE_COUNT,
       pub_name AS PUBLISHER
FROM pubs.publishers
LEFT JOIN titles ON titles.pub_id = publishers.pub_id
LEFT JOIN titleauthor ON titleauthor.title_id = titles.title_id
INNER JOIN authors ON authors.au_id = titleauthor.au_id
GROUP BY titles.title;