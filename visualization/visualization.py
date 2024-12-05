import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read the excel file
df = pd.read_excel('data/decisionTree.xlsx')


# Visualizing the relationship between age and disease
plt.figure(figsize=(10,6))            
sns.histplot(data = df, x ='Age', hue='Disease', multiple='stack', kde=False)
plt.title('Age and Disease Status')
plt.xlabel('Age')
plt.ylabel('Number of Person')
plt.show()



# Cholesterol and Disease Status
plt.figure(figsize=(10,6))            
sns.histplot(data = df, x ='Cholesterol', hue='Disease', multiple='stack', kde=False)
plt.title('Cholesterol and Disease Status')
plt.xlabel('Cholesterol')
plt.ylabel('Number of Person')
plt.show()


# Blood Pressure and Disease Status
plt.figure(figsize=(10,6))           
sns.histplot(data = df, x ='Blood_Pressure', hue='Disease', multiple='stack', kde=False)
plt.title('Blood Pressure and Disease Status')
plt.xlabel('Blood Pressure')
plt.ylabel('Number of Person')
plt.show()