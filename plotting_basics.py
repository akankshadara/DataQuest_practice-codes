
# coding: utf-8

# In[1]:
import seaborn
import pandas
forest_fires = pandas.read_csv("forest_fires.csv")
forest_fires.head(5)


# In[2]:

print forest_fires.head(5)


# In[4]:


weight = [600,150,200,300,200,100,125,180]
height = [60,65,73,70,65,58,66,67]

import matplotlib.pyplot as plt
plt.scatter(height, weight)
plt.show()


# In[7]:

wind = forest_fires["wind"]
area = forest_fires["area"]
temp = forest_fires["temp"]
plt.scatter(wind, area)
plt.show()


# In[11]:

plt.scatter(temp, area)
plt.show()


# <b>Line chart</b>

# In[8]:

age = [5, 10, 15, 20, 25]
height = [25, 45, 65, 75, 75]
plt.plot(age, height)
plt.show()


# <b>bar graph</b>

# In[15]:

names = ["McDonalds", "Burger King", "Wendys", "Subway"]
patrons = [10000, 5000, 5000, 7500]
x = [0, 1, 2, 3]

plt.bar(x, patrons)
plt.show()


# In[17]:

# with titles/labels
import numpy
area_by_y = forest_fires.pivot_table(index="Y", values="area", aggfunc=numpy.mean)
area_by_x = forest_fires.pivot_table(index="X", values="area", aggfunc=numpy.mean)
print area_by_x


# In[18]:

# 5
area_by_y = forest_fires.pivot_table(index="Y", values="area", aggfunc=numpy.mean)
area_by_x = forest_fires.pivot_table(index="X", values="area", aggfunc=numpy.mean)
plt.bar(area_by_y.index, area_by_y)
plt.show()
plt.bar(area_by_x.index, area_by_x)
plt.show()


# <b>Horizontal bar graph</b>

# In[19]:

plt.barh(area_by_y.index, area_by_y)
plt.show()


# In[ ]:




# In[32]:

area_by_month = forest_fires.pivot_table(index="month", values="area", aggfunc=numpy.mean)
area_by_day = forest_fires.pivot_table(index="day", values="area", aggfunc=numpy.mean)

plt.barh(area_by_month,range(len(area_by_month)) )
plt.show()
plt.style.use("bmh")
plt.barh(area_by_day ,range(len(area_by_day)))
plt.show()


# In[23]:

area_by_day


# In[28]:

# 8 Plotting along with labels!

wind = forest_fires["wind"]
area = forest_fires["area"]
plt.scatter(wind, area)
plt.title("Wind speed vs fire area")
plt.xlabel("Wind speed when fire started")
plt.ylabel("Area consumed by fire")
plt.show()


# In[ ]:



