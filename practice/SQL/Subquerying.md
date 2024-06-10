like querying but nested so we can query when [[Relating tables]]


queries within queries 

```
SELECT "title" FROM "books" WHERE "publisher_id" = (
	SELECT "id" FROM "publishers" WHERE "publisher" = 'MacLehose Press');
```

Subqueries one to many , many to many,,

Use IN (where multiple ids)

```
SELECT "title" FROM "books"

WHERE "id" IN (

    SELECT "book_id" FROM "authored" WHERE "author_id" = (

        SELECT "id" FROM "authors" WHERE "name" = 'Fernanda Melchor'));
```

Can take intersects,union of subqueries .