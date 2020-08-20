SELECT titleauthor.au_id AS AUTHOR_ID, 
       authors.au_lname AS LAST_NAME,
       authors.au_fname AS FIRST_NAME
FROM pubs.publishers
LEFT JOIN titles ON titles.pub_id = publishers.pub_id
LEFT JOIN titleauthor ON titleauthor.title_id = titles.title_id
RIGHT JOIN authors ON authors.au_id = titleauthor.au_id
LEFT JOIN roysched ON roysched.title_id = titles.title_id
WHERE authors.au_id IS NOT NULL
GROUP BY authors.au_id
ORDER BY sum(ytd_sales) DESC;