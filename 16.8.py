#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
sql = 'select title from book order by title asc'
rows = conn.execute(sql)
for row in rows:
    print(row)

('Perdido Street Station',)
('Small Gods',)
('The Spellman Files',)
('The Weirdstone of Brisingamen',)
('Thud!',)


# In[ ]:




