#You are assigned a Customer Churn Analysis Project as part of your Data Analytics practical work.

#Project Title
#Customer Churn Analysis Using Python

#Project Objective
#A company wants to understand why customers are leaving and identify customer groups
#that have a higher risk of churn.

#Your task is to analyze the customer dataset, identify important churn patterns,
# and provide business recommendations based on your findings.
#Dataset :Use the provided Customer Churn Dataset (customer_churn.csv).
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#1st step always readexcel file/csv file
df=pd.read_excel(r"C:\Users\Srikant Nair\Downloads\customer_churn_sample_dataset.xlsx")
#2nd step uderstand dataset loaded
print(df.head()) #head to get first 5 for understanding excel file
print(df.shape) #shape to know how many rows nd columns this excel file contains
print(df.info()) #info to know datatype(integer,float) non null values name of columns
print("Duplicates:",df.isnull().sum())
#3rd step (as there is no duplicates no need to clean data by drop duplicates)
#but churn data
totalcustomers=len(df)
churnedcustomers=(df["Churn"]==1).sum() #from churn column we are counting 1 as lost customer from prev year
retainedcustomers=(df["Churn"]==0).sum()#from churn col we are counting 0 as retained customer from prev year
if totalcustomers>0: #totalcustomer value cant be 0 so for safer side
    churnrate=churnedcustomers/totalcustomers*100 #chuurn% means % of customers you lost is lostcustomer/totalcustomer*100
else:
    churnrate=0
print("Total customers:",totalcustomers)
print("Churned customers:",churnedcustomers)
print("Retained customers:",retainedcustomers)
print("Churn percentage:",round(churnrate,2),"%") #round means roundfigure for decimal nd 2 for .2
#4.visualize churned vs retianed customers you can use boxplot/scatterplot
#but you will use countplot so it can count retained nd lost customer
plt.figure(figsize=(7,5))
sns.countplot(data=df,x="Churn") #churn is a column in excel file
plt.xticks([0,1],["Retained","Churned"]) #xticks are used to rename 0,1 as retained,churned
plt.title("Customer churned Distribution")
plt.tight_layout()
plt.show()
#5. now churn as per column contracttype given in excel file annual,month,quarter,etc
contractchurn=df.groupby("Contract_Type")["Churn"].mean().mul(100).sort_values(ascending=False)
#mean() is used so we can get avg so we can bring both columns together 
#mul(100) conversion multiply by 100 so it can be converted removing decimal
print("Churn by contracttype",round(contractchurn,2))
contractchurn.plot(kind="bar",figsize=(7,5))
plt.title("Churn rate by contract type")
plt.xlabel("contract type")
plt.ylabel("churn %")
#plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
#6. now churn as per column payment method
paymentmethodchurn=df.groupby("Payment_Method")["Churn"].mean().mul(100).sort_values(ascending=False)
print("Churn by payment method",round(paymentmethodchurn,2))
paymentmethodchurn.plot(kind="bar",figsize=(7,5)) #figsize 7 inches wide nd 5 inches height
plt.title("Churn by Payment method")
plt.xlabel("Payment type")
plt.ylabel("Churn %")
plt.tight_layout()
plt.show()