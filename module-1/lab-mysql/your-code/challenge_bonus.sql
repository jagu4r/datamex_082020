SELECT titleauthor.au_id AS AUTHOR_ID, 
       authors.au_lname AS LAST_NAME,
       authors.au_fname AS FIRST_NAME,
       IFNULL((price*ytd_sales*(royalty/100)*(titleauthor.royaltyper/100))+ (advance*royaltyper/100),0) AS PROFIT
FROM pubs.publishers
LEFT JOIN titles ON titles.pub_id = publishers.pub_id
LEFT JOIN titleauthor ON titleauthor.title_id = titles.title_id
RIGHT JOIN authors ON authors.au_id = titleauthor.au_id
GROUP BY authors.au_id
ORDER BY PROFIT DESC
LIMIT 3;