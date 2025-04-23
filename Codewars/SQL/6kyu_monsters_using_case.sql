SELECT
  th.id,
  th.heads as heads,
  bh.legs as legs,
  th.arms as arms,
  bh.tails as tails,
  CASE
    WHEN SUM(th.heads) > SUM(th.arms) OR SUM(bh.tails) > SUM(bh.legs) 
      THEN 'BEAST'
    ELSE 'WEIRDO'
  END AS species
FROM top_half th
  JOIN bottom_half AS bh ON th.id = bh.id
GROUP BY th.id
ORDER BY species 

SELECT
  th.id,
  th.heads,
  bh.legs,
  th.arms,
  bh.tails,
  CASE WHEN th.heads > th.arms or bh.tails > bh.legs
    THEN 'BEAST'
    ELSE 'WEIRDO'
  END as species
  
FROM top_half th

INNER JOIN bottom_half bh
  on bh.id = th.id

ORDER BY species