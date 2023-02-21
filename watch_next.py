# import spacy and specify model
import spacy
nlp = spacy.load('en_core_web_md')


# function to return the most similar movie to 'desciption'
def watch_next(description):
    # create empty dict
    similarity_dict = {}

    # run 'description' through the model
    watched = nlp(description)

    # split the title and description of each movie in data
    # run the description of each movie through the model
    # compare the similarity of each movie description to watched
    # add each movie title and the similarity result to dictionary 
    for movie in data:
        split_movie = movie.split(':')
        next_title = split_movie[0]
        next_description = nlp(split_movie[1])
        movie_similarity = watched.similarity(next_description)
        similarity_dict[next_title] = movie_similarity
    
    # find the movie title with the highest similarity
    most_similar = max(similarity_dict, key=similarity_dict.get)

    # return the title of most similar movie
    return f'The most similar movie is {most_similar}'
    

# open, read and store entries from movies.txt
with open('movies.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

# description of Hulk movie
Hulk = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'

# run watch_next function with Hulk, print the result
print(watch_next(Hulk))