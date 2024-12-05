import pandas as pd


def get_metadata_title(search_title, df):
    result = df[df['title'].str.lower() == search_title.lower()]
    
    if not result.empty:
        movie = result.iloc[0]
        return {
            "title": movie["title"],
            "genres": movie["genres"],
            "summary": movie["overview"],
            "keywords": movie["keywords"],
        }
    else:
        return None
    

def get_metadata_index(indexes, df):
    movie_list = []
    for index in indexes:
        movie = df.iloc[index]
        dict = {
            "title": movie["title"],
            "genres": movie["genres"],
            "summary": movie["overview"],
            "keywords": movie["keywords"],
            
        }
        movie_list.append(dict)

    return movie_list


        
    
        
    

#print(get_metadata_title("INCEPTION"))