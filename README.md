# Search-Engine-Comparator
Comparing search results from DuckDuckGo vs search results from Google
Here 100 search queries from queries.txt file are read and searched for in the DuckDuckGo search engine. The top 10 results are stored in sample.json file.
Similarly the top 10 results for Google browser are stored in googlequeries.json file.
The overlaop and Spearmans correlation are stored and calculated in the task5.csv file.
Negative value indicating very less correlation.
Summary of results obtained is as follows:




This assignment was run on DuckDuckGo and compared with Google
The average overlap obtained is 2.01
The average percent overlap is 20.1%
The average spearman correlation obtained is -8.279714285714286
The average percent overlap is very low.
This is indicates a strong negative relationship between the google results and the results obtained from DuckDuckGo.
It means that the higher the rank of a result is obtained from google, the lower it is obtained from DuckDuckGo due to differences in the algorithms used by each of them.
The variances in how DuckDuckGo works when compared to Google often produce markedly different search results.
When you click on a search result link on Google, the platform sends your specific search term directly to the website you’re visiting.
If you take a look at the HTTP referrer header, you might even spot your original search words spelled out right in front of you.
Your IP address is also shared so that the website can identify it. 
But at DuckDuckGo, they’ve labeled this practice “search leakage,” and they do not engage in it. 
This protects your search history – and any possible control of results – from both the websites you visit and the search engine itself.
