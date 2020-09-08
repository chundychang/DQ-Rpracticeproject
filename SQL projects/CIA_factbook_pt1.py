#!/usr/bin/env python
# coding: utf-8

# 1. Connect Jupyter Notebook to database file

# In[ ]:


get_ipython().run_cell_magic('capture', '', '%load_ext sql\n%sql sqlite:///factbook.db')


# 2. Obtain information on database

# In[5]:


get_ipython().run_cell_magic('sql', '', "SELECT *\n  FROM sqlite_master\n WHERE type='table';")


# 3. Return the first 5 rows of the `facts` table in database

# In[6]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM facts\nLIMIT 5')


# 4. Summary statistics for: min & max population, min & max population growth

# In[7]:


get_ipython().run_cell_magic('sql', '', 'SELECT MIN(population), MAX(population), MIN(population_growth), MAX(population_growth)\nFROM facts')


# 5. Determine which country has min & max population

# In[8]:


get_ipython().run_cell_magic('sql', '', 'SELECT name, population\nFROM facts\nWHERE population = (SELECT MIN(population)\n                   FROM facts);')


# In[9]:


get_ipython().run_cell_magic('sql', '', 'SELECT name, population\nFROM facts\nWHERE population = (SELECT MAX(population)\n                   FROM facts);')


# 6. Recalculate summary statistics for min/max population & population growth excluding World population

# In[10]:


get_ipython().run_cell_magic('sql', '', 'SELECT MIN(population), MAX(population), MIN(population_growth), MAX(population_growth)\nFROM facts\nWHERE population < (SELECT MAX(population)\n                   FROM facts)')


# 7. Calculate average value for `population` and `area`

# In[13]:


get_ipython().run_cell_magic('sql', '', "SELECT AVG(population) 'avg_population', AVG(area) 'avg_area'\nFROM facts")


# 8. Return list of countries that have above average `population` and below average `area`

# In[14]:


get_ipython().run_cell_magic('sql', '', 'SELECT name, population, area\nFROM facts\nWHERE population > (SELECT AVG(population)\n                   FROM facts)\nAND area < (SELECT AVG(area)\n           FROM facts);')


# 9. Which country has the most people?

# In[17]:


get_ipython().run_cell_magic('sql', '', 'SELECT name, population\nFROM facts\nWHERE population < (SELECT MAX(population)\n                   FROM facts)\nORDER BY population DESC\nLIMIT 1')


# 10. Which country has the highest growth rate? 

# In[18]:


get_ipython().run_cell_magic('sql', '', 'SELECT name, population_growth\nFROM facts\nORDER BY population_growth DESC\nLIMIT 1')


# 11. Which countries have the highest ratio of water to land? (Top 10)

# In[30]:


get_ipython().run_cell_magic('sql', '', "SELECT name, ROUND(CAST(area_water AS float)/CAST(area_land AS float), 4) 'water_land_ratio'\nFROM facts\nORDER BY water_land_ratio DESC\nLIMIT 10")


# 12. Which countries have more water than land?

# In[32]:


get_ipython().run_cell_magic('sql', '', 'SELECT name, area_water, area_land\nFROM facts\nWHERE area_water > area_land\nORDER BY area_water\nLIMIT 10')


# 13. Which countries will add the most people to their population next year? (Top 10)

# In[35]:


get_ipython().run_cell_magic('sql', '', "SELECT name, (birth_rate*population)/1000 'births_number'\nFROM facts\nWHERE population < (SELECT MAX(population)\n                   FROM facts)\nORDER BY births_number DESC\nLIMIT 10")


# 14. Which countries havea  higher death rate than birth rate?

# In[43]:


get_ipython().run_cell_magic('sql', '', "SELECT name, death_rate, birth_rate, ROUND(death_rate-birth_rate, 2) 'death_birth_dif'\nFROM facts\nWHERE death_rate > birth_rate\nORDER BY death_birth_dif DESC")


# 15. What countries have the highest population/area ratio?

# In[44]:


get_ipython().run_cell_magic('sql', '', "SELECT name, population/area 'pop_area_ratio'\nFROM facts\nORDER BY pop_area_ratio DESC\nLIMIT 10")

