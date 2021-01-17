import pandas as pd
import numpy as np
import warnings

x="0"
name=None
warnings.filterwarnings('ignore')

columns_name=["user_id","item_id","rating","timestamp"]
df1=pd.read_csv("u.data",sep = "\t",names=columns_name)
df2=pd.read_csv("u.item",sep = "|",header=None,encoding='latin-1')    #Handles

movies_titles=df2[[0,1]]               #sliced the columns
movies_titles.columns=["item_id","Title"] #Named them
df=pd.merge(df1,movies_titles,on="item_id")  #stiched two datasets at item_id

ratings=pd.DataFrame(df.groupby("Title").mean()["rating"]) #rating and title only

ratings["num of ratings"]=pd.DataFrame(df.groupby("Title").count()["rating"])

moviemat=df.pivot_table(index="user_id",columns="Title",values="rating")

def predict_movies(movie_name):
        movie_user_ratings=moviemat[movie_name]
        similar_to_movie=moviemat.corrwith(movie_user_ratings)
        corr_movie=pd.DataFrame(similar_to_movie,columns=["correlation"])
        corr_movie.dropna(inplace=True)
        corr_movie=corr_movie.join(ratings["num of ratings"])

        predictions=corr_movie[corr_movie["num of ratings"]>100].sort_values("correlation",ascending=False)

        return predictions

def movie_name():

    name_of_movie=input("Enter name of the movie:....\n")
    print("\n\nTop 10 Movies similar to",name_of_movie)
    predict_my_movie=predict_movies(name_of_movie)
    chart=predict_my_movie.head(10)
    s = chart[chart.columns[0]]


    print(s)
    print("\n\n")
print('''
       ScrollWell Bootcamp on Machine Learning using Python
          Day 3 project: Movie Recommendation system
                                        -by Prajwal Ghogare''')
print("                            !!!!Movie predictor 10000!!!!\n\n")
while x!= "1":
    movie_name()
    x=input("Press 1 to stop ||| Press enter to continue ...\n")



print("Programme ended....")
