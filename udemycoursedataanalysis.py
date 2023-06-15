# -*- coding: utf-8 -*-
"""UdemyCourseDataAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19D73Oa35TOc3N8V0qTAoLVtiqpRiHKYL
"""

import pandas as pd
data = pd.read_csv("/content/7. Udemy Courses.csv")
data

"""**WHAT ARE ALL DIFFERENT SUBJECTS FOR WHICH UDEMY IS OFFERING COURSES?**"""

data.subject.unique()

"""**WHICH SUBJECT HAS MAXIMUM NUMBER OF COURSES?**"""

data.head(2)

data.subject.value_counts()

"""**SHOW ALL THE COURSES WHICH ARE FREE OF COST**"""

data.head(2)

data[data.is_paid == False]

"""**SHOW ALL THE COURSES WHICH ARE PAID**"""

data[data.is_paid == True]

"""**WHICH ARE TOP SELLING COURSES?**"""

data.sort_values('num_subscribers',ascending = False)

"""**WHICH ARE LEAST SELLING COURSES?**"""

data.sort_values('num_subscribers')

"""**SHOW ALL THE COURSES OF GRAPHICS DESIGN WHERE PRICE IS BELOW 500**"""

data.head(1)

data.subject == 'Graphics Design'

data[(data.subject == 'Graphic Design') & (data.price < '100')]

"""**LIST OUT ALL THE COURSES THAT ARE RELATED WITH PYTHON**"""

data[data.course_title.str.contains('Python')]

len(data[data.course_title.str.contains('Python')])

"""**WHAT ARE THE COURSES THAT ARE PUBLISHED IN YEAR 2015?**"""

data.dtypes

data['published_timestamp'] = pd.to_datetime(data.published_timestamp)

data.dtypes

data['Year'] = data['published_timestamp'].dt.year
data

data[data.Year == 2015]

"""**WHAT ARE MAXIMUM NUMBERS OF SUBSCRIBERS FOR EACH LEVEL OF COURSES?**"""

data.level.unique()

data.groupby('level')['num_subscribers'].max()