## Analyze Pubmed Records  

* ### Download Data from Pubmed
download publication records from 2017-01-01 to 2017-12-31 (publication date) as csv file.   

* ### Raw Data (2017.csv)
Raw csv file has 1292498 rows.  

* ### Clean the Data  
 1. Remove multiple headers;
 2. Strip 'Title';
 3. Remove null in 'Description';
 4. Remove duplicates.

* ### Count Total Publications per Journal
![Journal Rank with Publication number](paper_per_j_total.png)  

* ### Total Publications with Tissue Keywords in Title  
![](Tissue_Rank.png)

* ### Top Journal Publications with Tissue Keywords in Title  
![](Tissue_Rank_Top.png)

* ### Total Publications with Disease Keywords in Title  
![](Disease_Rank.png)

* ### Top Journal Publications with Disease Keywords in Title  
![](Disease_Rank_Top.png)

* ### Chinese PI Publication Ratio  
![](Chinese_PI_Ratio.png)

* ### Chinese PI Publication Ratio in Top Journals (IF>20)  
![](Chinese_PI_Ratio_Top.png)

* ### Journals Published Most Studies from Chinese PI  
![](Chinese_paper_per_j_total.png)

* ### Journals Published Most Studies from Chinese PI (Normalized, and Ratio<85%)  
![](Norm_Chinese_Pub.png)

* ### Most Frequent words in Publication Titles (use 1000 records, and filtered with words blacklist)  
![](Word_Fre.png)
