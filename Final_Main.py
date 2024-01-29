from Final_Classes import *

movieRecommender = MovieRecommender('Hydra-Movie-Scrape.csv')

FIRST_MOVIE_IDX = 0
FIRST_PAGE = 0
MOVIES_PER_PAGE = 10
LAST_PAGE = 3876

startingIndex = FIRST_MOVIE_IDX
totalMovies = range(movieRecommender.__len__())

print('Current Page of Movies in alphabetical order:')
for i in range(MOVIES_PER_PAGE):
    page = movieRecommender.movieAsString(i)
    print(page, end='')

done = False
while not done:
    print('A - add movie to favorites' + '\n' + 'R - get recommendations' + '\n' + 
          'N - show next page of movies' + '\n' + 'P - show previous page of movies' + '\n' + 
          'J - jump to movie with index' + '\n' + 'F - print my favorites'+ '\n' + 
          'X - exit program')
    choice = input('Enter Command (A/R/N/P/J/F/X): ').upper()
    for selection in choice:

        if selection == 'A':
            movieIndex = int(input('Enter index of movie to add: '))
            movieRecommender.addToFavorites(movieIndex)

        elif selection == 'R':
            keyword = str(input('Enter a name or search term: '))
            column = input('Search Title, Summary, or Cast (S/T/C): ').upper()
            if column == 'S':
                column = 'Summary'
            elif column == 'T':
                column = 'Title'
            elif column == 'C':
                column = 'Cast'
            print('The top rated movies with ' + '"' + keyword + '"' + ' in ' 
                  + '"' + column + '" are:' + '\n'
                  + movieRecommender.recommendations(keyword, column))

        elif selection == 'N':
            print('Current Page of Movies in alphabetical order:')
            startingIndex = startingIndex + MOVIES_PER_PAGE
            endingIndex = startingIndex + MOVIES_PER_PAGE
            if startingIndex > LAST_PAGE:
                for page in totalMovies[LAST_PAGE:MOVIES_PER_PAGE]:
                    print(movieRecommender.movieAsString(page), end='')
            else: 
                for page in totalMovies[startingIndex:endingIndex]:
                    print(movieRecommender.movieAsString(page), end='')
            
        elif selection == 'P':
            print('Current Page of Movies in alphabetical order:')
            startingIndex = startingIndex - MOVIES_PER_PAGE
            endingIndex = startingIndex + MOVIES_PER_PAGE
            if startingIndex < FIRST_PAGE:
                for page in totalMovies[FIRST_PAGE:MOVIES_PER_PAGE]:
                    print(movieRecommender.movieAsString(page), end='')
            else:
                for page in totalMovies[startingIndex:endingIndex]:
                    print(movieRecommender.movieAsString(page), end='')

        elif selection == 'J':
            index = int(input('Enter index: '))
            startingIndex = index
            endingIndex = startingIndex + MOVIES_PER_PAGE
            print('Current Page of Movies in alphabetical order:')
            for page in totalMovies[startingIndex:endingIndex]:
                print(movieRecommender.movieAsString(page), end='')

        elif selection == 'F':
            print('My Current Favorite Movies:' + '\n' + movieRecommender.favorites())

        elif selection == 'X':
            done = True