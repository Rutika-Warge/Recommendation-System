import numpy as np #mathematical operations
import pandas as pd #file and mathematical
import matplotlib.pyplot as plt # graph

Elect_data = pd.read_excel(r"C:\ProjectData.xlsx")
print(Elect_data.head())

print(Elect_data.shape)

print(Elect_data.info())

print(Elect_data.describe()['Rating'])

#Find the minimum and maximum ratings
print('Minimum rating is: %d' %(Elect_data.Rating.min()))
print('Maximum rating is: %d' %(Elect_data.Rating.max()))

rating_mean=Elect_data.groupby('Brand_Name')['Rating'].mean()
print(rating_mean.head())

rating_mean=Elect_data.groupby('Brand_Name')['Rating'].mean().sort_values(ascending=False)
print(rating_mean.head())

rating_count=Elect_data.groupby('Brand_Name')['Rating'].count().sort_values(ascending=False)
print(rating_count.head())

print("Total data ")
print("\nTotal No of ratings :",Elect_data.shape[0])
print("Total No of Users   :", len(pd.unique(Elect_data.User_Id)))
print("Total No of products  :", len(pd.unique(Elect_data.Brand_Name)))

ratings_mean_count = pd.DataFrame(Elect_data.groupby('Brand_Name')['Rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(Elect_data.groupby('Brand_Name')['Rating'].count())
print(ratings_mean_count.head())

ratings_counts=ratings_mean_count.iloc[:,1].values
print(ratings_counts)

Ratings=ratings_mean_count.iloc[:,0].values
print(Ratings)

plt.xlabel('Rating')
plt.ylabel('Rating counts')
plt.scatter(Ratings,ratings_counts)
plt.show()

popular_products = pd.DataFrame(Elect_data.groupby('Brand_Name')['Rating'].count())
most_popular = popular_products.sort_values('Rating', ascending=False)
print(most_popular.head(30).plot(kind = "bar"))
plt.show()

user_Brand_rating =Elect_data.pivot_table(index='User_Id', columns='Brand_Name', values='Rating',fill_value=0)
print(user_Brand_rating.head())

Jethro_ratings = user_Brand_rating['Jethro']
print(Jethro_ratings.head())

Brand_like_Jethro = user_Brand_rating.corrwith(Jethro_ratings,axis=0,drop=False, method='pearson')
print(Brand_like_Jethro.head())

corr_Jethro = pd.DataFrame(Brand_like_Jethro , columns=['Correlation'])
corr_Jethro.dropna(inplace=True)
print(corr_Jethro.head())

print(corr_Jethro.sort_values('Correlation', ascending=False).head())

corr_Jethro = corr_Jethro.join(ratings_mean_count['rating_counts'])
print(corr_Jethro.head())

print(corr_Jethro[corr_Jethro['rating_counts']>50].sort_values('Correlation', ascending=False).head())

Lenovo_ratings = user_Brand_rating['Lenovo']
print(Lenovo_ratings)

Brand_like_Lenovo = user_Brand_rating.corrwith(Lenovo_ratings,axis=0,drop=False, method='pearson')
print(Brand_like_Lenovo.head())

corr_Lenovo = pd.DataFrame(Brand_like_Lenovo , columns=['Correlation'])
corr_Lenovo.dropna(inplace=True)
print(corr_Lenovo.head())

print(corr_Lenovo.sort_values('Correlation', ascending=False).head())

corr_Lenovo = corr_Lenovo.join(ratings_mean_count['rating_counts'])
print(corr_Lenovo.head())

print(corr_Lenovo[corr_Lenovo['rating_counts']>50].sort_values('Correlation', ascending=False).head())
