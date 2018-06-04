# Stackoverflow tag popularity
Comparison of popularity of Stackoverflow tags in 2009 and 2016 using Apache Hive™ Data Definition Language (DDL).

The goal is to see the popularity of top 10 tags in 2016 and see how popular they were in 2009.

The structure of *posts* table:

| Variable | Type |
| ------ | ------ |
| id | int | 
|post_type_id        |	tinyint         |    	                    
|date                	|string |             	                    
|owner_user_id       	|int|                 	                    
|parent_id           	|int|                 	                    
|score               	|int|                 	                    
|favorite_count      	|int                 	                    |
|tags                	|array<string>       	                    |
|year                	|string|              	                    
|month               	|string    |          	                    
	 	 
Partition Information

| col_name | data_type |
| ------ | ------ |
|year|string |             	                 
|month|               	string|              	                    
