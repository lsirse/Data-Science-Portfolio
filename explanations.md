```
%%writefile query.hql

USE stackoverflow_;
```



**Create views which select tags from respective year
by using explode function, counts tags and ranks them by
popularity.
**

```
DROP VIEW ranks_2009;

CREATE VIEW ranks_2009(
    rank, tag, amount
) AS SELECT rank() OVER (ORDER BY cnt.n DESC) as r, cnt.t, cnt.n FROM 
    (SELECT Count(e.T) as n, e.T as t FROM (
        SELECT explode(Tags) as T
    FROM posts
    WHERE Year=2009 AND post_type_id=1
    ) as e
    GROUP BY e.T) as cnt
ORDER by r ASC;

DROP VIEW ranks_2016;

CREATE VIEW ranks_2016(
    rank, tag, amount
) AS SELECT rank() OVER (ORDER BY cnt.n DESC) as r, cnt.t, cnt.n FROM 
    (SELECT Count(e.T) as n, e.T as t FROM (
        SELECT explode(Tags) as T
    FROM posts
    WHERE Year=2016 AND post_type_id=1
    ) as e
    GROUP BY e.T) as cnt
ORDER by r ASC;
```



**Finally, two views are joined on tag column and following row is made, for instance:**

| Tag | Rank of 2016 | Rank of 2009 | Count of 2016 | Count of 2009 |
| ------ | ------ | ------ | ------ | ------ |
| Php | 5 | 4 | 1233 | 3421 |




```
SELECT ranks_2016.tag, ranks_2016.rank, ranks_2009.rank, ranks_2016.amount, ranks_2009.amount
FROM ranks_2016
INNER JOIN ranks_2009 ON ranks_2016.tag=ranks_2009.tag
ORDER BY ranks_2016.rank ASC
LIMIT 10;
```
