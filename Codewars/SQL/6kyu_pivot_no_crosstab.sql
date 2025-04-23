SELECT 
  p.name,
  COUNT(CASE WHEN d.detail = 'good' THEN 1 END) as good,
  COUNT(CASE WHEN d.detail = 'ok' THEN 1 END) as ok,
  COUNT(CASE WHEN d.detail = 'bad' THEN 1 END) as bad
FROM products p
JOIN details d ON p.id = d.product_id
GROUP BY p.name
ORDER BY p.name

/*
Lifted from top solution. Note p.id = d.product_id (First trick). And then move on to 
counting each instance of 'good', 'ok', and 'bad' by counting 
COUNT(CASE WHEN condition THEN 1 END)  cases when it occurs
*/