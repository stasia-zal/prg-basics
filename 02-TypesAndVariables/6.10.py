###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('title in caps: ', movie.upper() )

# print title in small letters
print('title in small letters: ', movie.lower())

# print how many times the vowel "e" appears in the title
print('how many times the vowel "e" appears in the title: ', movie.count('e'))


# print where in the text is the word "Lord"
print('the word "Lord" is: ', movie.find('Lord'))

# print where in the text is the word "dragon"
print('the word "dragon" is: ', movie.find('dragon'))