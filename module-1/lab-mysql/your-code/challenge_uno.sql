SELECT titleauthor.au_id as AUTHOR_ID, 
       authors.au_lname AS LAST_NAME,
       authors.au_fname AS FIRST_NAME,
       titles.title AS TITLE,
       pub_name as PUBLISHER
FROM pubs.publishers
LEFT JOIN titles ON titles.pub_id = publishers.pub_id
LEFT JOIN titleauthor ON titleauthor.title_id = titles.title_id
INNER JOIN authors ON authors.au_id = titleauthor.au_id;
