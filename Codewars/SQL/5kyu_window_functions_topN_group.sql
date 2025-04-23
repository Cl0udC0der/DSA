select
  c.id category_id,
  c.category,
  p.title,
  p.views,
  p.post_id
from categories c left join (
  select
    category_id,
    title,
    views,
    id post_id,
    row_number() over (partition by category_id order by views desc, id) rn
  from posts) p on p.category_id = c.id and p.rn < 3
order by category, views desc, post_id
