# App Demo Script

## Overview page

This is the landing page. It gives an owner a snapshot of every farm at once, as of October 31.

The four cards across the top each come from their own query. Clicking a card flips it over to show the SQL behind it.

- **Unpaid bills** totals what is still owed across all bills. A subquery groups the Payments table by bill and sums what has been paid, then a left join subtracts that from each bill's amount due. The same query counts how many unpaid bills are past their due date.
- **Orders to ship** counts orders that are still pending.
- **Fields to harvest** counts plantings that are not harvested yet and are expected to be ready within the next two weeks.
- **Animals needing care** counts animals whose health status is anything other than healthy.

Below the cards, **Upcoming harvests** lists those same plantings. It joins Plantings with Farms and Crops so each row shows the farm name, field, crop, acres, and harvest date.

On the right, **Sales by customer type** joins Orders, Customers, and the Contains table, which holds each order's line items. It keeps only delivered orders and groups by customer type to total the sales.

## Fields tab

The Fields tab lists every planting across all farms. The query joins Plantings with Farms and Crops.

Each dropdown adds a condition to the query's where clause. Picking a farm limits the results to that farm. Picking a crop also narrows the variety list to varieties of that crop. Growth status filters to planted, growing, or harvested.

Turning on the ER diagram switch at the bottom right shows the part of our ER diagram this page uses: Farms, the grows relationship, Plantings, the planting_of relationship, and Crops.

## Sales tab

The Sales tab covers delivered orders. It can be filtered by farm, date range, and product category.

This query joins five tables: Orders, Farms, Customers, Contains, and Products. It groups by farm and customer type, then counts the orders, computes the average order value, and totals the sales.

The table on the left shows each farm and customer type combination, sorted by total sales. The chart on the right adds those totals up by customer type, so we can see which kind of customer brings in the most revenue.
