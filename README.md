# Mapreduce_eCommerce

This is a Women’s Clothing E-Commerce dataset revolving around the reviews written by customers. Use WomenClothing.csv as the input. Data overview: The data is in a CSV file. The first column is Clothing ID number, the second column is product rating by reviewer, the third column is Recommended IND(Whether the product is recommended or not by the reviewer, where 1 is recommended, 0 is not recommended.) the last column is Positive Feedback Count(Positive Integer documenting the number of other customers who found this review positive.). However, the Clothing ID number are repeat, because individual cloth will receive different review by different customers. 
link to the data set: https://www.kaggle.com/nicapotato/womens-ecommerce-clothing-reviews


Business Problem: Which customer reviews is objective and which product is more popular
The total reviews received for each cloth
a.	Use sum(PositiveFeedbackCount)
b.	Use Sort to find the most popular product 
c.	The Positive Feedback Count is the number of other customers who found this review positive. By summing up the feedback count, I can find out which clothes are more popular and people would love to review those feedback. 

 
Summary: From the output below, the most popular clothing id is 1078, which have 2763positive feedback reviews. In this case, company should evaluate this review and produce more this clothing style
