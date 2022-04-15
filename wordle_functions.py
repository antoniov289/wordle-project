#wordle functions - antonio

#input validation
def valid_word(guess, word_list):
    #check if the word is not on the list and therefor invalid
    if guess not in word_list:
        print('Invalid word. Try again.')
        #if the word is invalid send them back to the beginning to try again
        main()

#compare letters to the secret word
def compare_words(guess, secret_word):
    results = ''

    #loop through the letters of guess
    for i in range(len(guess)):
        #if the letters are the same in the same spot, assign a '$'
        if guess[i] == secret_word[i]:
            results += '$'
        #if the letter is in the word anywhere, assign a '>'
        elif guess[i] in secret_word:
            results += '>'
        #otherwise, the letter is not in the word and assign an 'x'
        else:
            results += 'x'

    #print the results in the correct format
    for i in range(len(results)):
        print(results[i], end = ' ')

    #print a newline between the results and word
    print()

    #print the guess underneath in the correct format
    for i in range(len(guess)):
        print(guess[i].upper(), end = ' ')

#test jumps against jaunt, should return '$>xxx'
compare_words('jumps', 'jaunt')
