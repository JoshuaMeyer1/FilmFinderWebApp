def get_metadata_title(search_title, df):
    print(f"Query for {search_title} started!")
    result = df[df['title'].str.lower() == search_title.lower()]
    
    if not result.empty:
        print(f"Found {search_title}!")
        movie = result.iloc[0]
        print(f"Details:  {movie['title']}, {movie['genres']}, {movie['overview']}, {movie['keywords']}!")
        return {
            "title": movie["title"],
            "genres": movie["genres"],
            "summary": movie["overview"],
            "keywords": movie["keywords"],
        }

    else:
        print(f"Failed to find {search_title}!")
        return None
    

def get_metadata_index(indexes, df):
    movie_list = []
    for index in indexes:
        movie = df.iloc[index]
        dictionary = {
            "title": movie["title"],
            "genres": movie["genres"],
            "summary": movie["overview"],
            "keywords": movie["keywords"],
            
        }
        movie_list.append(dictionary)

    return movie_list


        
    
        
    

#print(get_metadata_title("INCEPTION"))