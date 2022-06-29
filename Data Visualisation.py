import pandas as pd
import matplotlib.pyplot as mt
import tensorflow as tf
import numpy as np
import seaborn as sns

autism = pd.read_csv(r"C:/Users/Abhay Bhat/Desktop/BrainSightAI/Autism.csv")



#Removing the values with '?' by first replacing it with a string since the symbol is not being recognised.
#autism=autism.replace(to_replace = "?", value = "Question")
#autism.dropQuestion() 

#question = autism['ethnicity'] == '?'
#autism.drop(index = autism[question].index)

missing_value = ['NaN',np.nan]
autism = pd.read_csv(r"C:/Users/Abhay Bhat/Desktop/BrainSightAI/Autism.csv",na_values=missing_value)

autism = autism.dropna()


#To remove the first 10 columns as they don't have any function
autism.drop(autism.columns[[1,2,3,4,5,6,7,8,9,10]],axis = 1,inplace = True)

#To change the string into binary for later convinience 
autism=autism.replace(to_replace = "no", value = 0)
autism=autism.replace(to_replace = "yes", value = 1)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.BOLD + 'Male = 0, Female = 1' + color.END)

autism=autism.replace(to_replace = "m", value = 0)
autism=autism.replace(to_replace = "f", value = 1)


#Rounding the values for convinience

autism.round(2)

print(autism)


#To check if the data has any null values:
# File.isnull tells us if the value true or false i.e. if its null or not and the same information is used to plot this heatmap 

mt.figure(figsize = (10,10))
sns.heatmap(autism.isnull(),yticklabels = False, cbar = False)
mt.show()

print(autism.isnull().sum())


#IN order to see how many Autism cases exist in the data set ie. Frequency distribution of Autism

mt.figure(figsize = (10,10))
sns.countplot(x=autism["austim"],palette='Blues', linewidth = 2)
mt.title("Frequency of Autism")
mt.show()

#Regression, KDE and Hexagon Plot between Jaundice and Autism
sns.jointplot(x='austim',y='jaundice',data=autism, kind='reg')
sns.jointplot(x='austim',y='jaundice',data=autism, kind='kde')
sns.jointplot(x='austim',y='jaundice',data=autism, kind='hex')
mt.show(block=True)

#Pair Plot for all the values  
sns.pairplot(autism)
mt.title("Pair plot")
mt.show(block=True)


#Relation with the Country of Residence: Plotting String
autism.set_index('contry_of_res').plot()
mt.title("Relation with the Country of Residence")
mt.show(block=True)


#Ethnicity pair plot 
sns.pairplot(autism, hue = 'ethnicity',palette = 'tab10')
mt.title("Relation with the Ethnicity")
mt.show(block=True)

























