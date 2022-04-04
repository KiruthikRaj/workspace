import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/kirut/Downloads/Train.csv")
data.head()
data.info()
data.Item_Type.value_counts()
data.describe()
data.dtypes
data.boxplot()
data.drop('Item_Identifier')#if you want to delete on column
data.drop(['Item_Identifier','Outlet_Identifier'],axis=1,inplace=True)#if you want to delete to more than one line

data.Item_Weight.hist()
data.isnull().sum()
data.dropna(inplace=True)
plt.boxplot(data.Item_Weight)
data.shape
data.Item_Weight.describe()
data.Item_Weight.fillna(data.Item_Weight.mean(),inplace=True)
data.isnull().sum()
data.Item_Visibility.max()
data.Item_Visibility.min()
data.Item_Visibility.describe()
plt.boxplot(data.Item_Visibility)
data.Item_Visibility=data.Item_Visibility.replace(0,data.Item_Visibility.median())
data.Item_Fat_Content.value_counts()
data.Item_Fat_Content.describe()
data.Item_Fat_Content=data.Item_Fat_Content.replace('LF','Low Fat').replace('low fat','Low Fat')
data.Item_Fat_Content=data.Item_Fat_Content.replace('reg','Regular')
data.Item_Fat_Content.value_counts()

data.Item_Type.value_counts()
data.Item_Type.describe()
data.Item_MRP.describe()
data.Outlet_Establishment_Year.describe()
data.columns
data.Outlet_Size.describe()
data.Outlet_Size.isnull().sum()
data.Outlet_Size.value_counts()
data.Outlet_Location_Type.describe()
data.Item_Outlet_Sales.describe()
plt.boxplot(data.Item_Outlet_Sales)
data.Outlet_Size.fillna('Others',inplace=True)
data.Outlet_Size.unique()
data.Item_Outlet_sales[]
lf=data.Item_Outlet_Sales[data.Item_Fat_Content=="Low Fat"]
reg=data.Item_Outlet_Sales[data.Item_Fat_Content=="Regular"]
from scipy import stats
stats.ttest_ind(lf,reg)
