import pandas as pd

class MovieRecommender:

    def __init__(self, filename):
        moviesDF = pd.read_csv(filename, encoding='utf-8')
        sortedDF = moviesDF.sort_values('Title').reset_index(drop=True)
        self.__allMovies = sortedDF
        self.__myFavorites = set()
  
    def movieAsString(self, idx):
        movieString = str(idx) + ': ' + '[' + str(self.__allMovies['IMDB ID'][idx]) +\
                '] ' + '(' +str(self.__allMovies['Rating'][idx]) + '/10) ' + \
                str(self.__allMovies['Year'][idx]) + ' - ' + str(self.__allMovies['Title'][idx])
        return movieString + '\n'
    
    def addToFavorites(self, idx):
        self.__myFavorites.add(idx)

    def favorites(self):
        string = ''
        for idx in self.__myFavorites:
            string += self.movieAsString(idx)
        return string

    def recommendations(self, keyword, column):
        string = ''
        movies = self.__allMovies[self.__allMovies[str(column)].str.contains(str(keyword), case=False)]
        movies = movies.sort_values(['Rating'], ascending=False).head(5)
        for movie in movies.index:
            string += self.movieAsString(movie)
        return string 

    def __len__(self):
        return len(self.__allMovies)