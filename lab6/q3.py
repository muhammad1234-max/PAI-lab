import pandas as pd
import numpy as np

#sample dictionary from the question
exam_data = {
    'name':["Anastasia","Dima","Katherine","James","Emily","Michael","Mathhew","Laura","Kevin","Jonas"],
    'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
    'attempts':[1,3,2,3,2,3,1,1,2,1],
    'quality':['yes','no','yes','no','no','yes','yes','no','no','yes']
}

#equivalent of serial number in any datasheet
labels = ['a','b','c','d','e','f','g','h','i','j']

#creating the dataframe
df = pd.DataFrame(exam_data,index = labels)
print(df)
