from english_words import english_words_set

class wordle_solver(object):
    def __init__(self):
        pass

    def load_dictionary(self):
        # return [
        #     'banana', 'changeable', 'satiable', 'palazzo', 'cultivable', 'twa', 'tachinid', 'poincare', 'insensitive', 'driftwood'
        # ]
        words = []
        for word in english_words_set:
            words.append(word.lower())

        return words

    def words_correct_letters(self, letters, words=None):
        if words == None:
            words = self.load_dictionary()

        filtered_words = []
        dict = {}
        '''
        for list of words
        track if word contains all the required letters
        if yes, mark as true and return them
        '''
        for word in words:
            flags = []
            for letter in letters:
                if letter in word:
                    flags.append(True)
                else:
                    flags.append(False)

            if False in flags:
                dict[word] = False
            else:
                dict[word] = True

        for d in dict:
            if dict[d] == True:
                filtered_words.append(d)
        return filtered_words

    def words_wrong_letters(self, letters, words=None):
        if words == None:
            words = self.load_dictionary()

        filtered_words = []
        dict = {}
        '''
        for list of words
        track if word does not contain all the required letters
        if does not contain letters, return them
        '''
        for word in words:
            flags = []
            for letter in letters:
                if letter not in word:
                    flags.append(True)
                else:
                    flags.append(False)

            if False in flags:
                dict[word] = False
            else:
                dict[word] = True

        for d in dict:
            if dict[d] == True:
                filtered_words.append(d)
        return filtered_words

    def words_of_len(self, length = 5, words=None):
        if words == None:
            words = self.load_dictionary()

        filtered_words = []
        ''''
        filter to include only words x letters long
        '''
        for word in words:
            if len(word) == length:
                filtered_words.append(word)

        return filtered_words

    def specify_letter_pos(self, letter_pos, words=None):
        if words == None:
            words = self.load_dictionary()

        filtered_words = []
        '''
        use a list - flags to determine if a word contain all letters at specified position
        if letter at position, individual flag is true
        if all  the flag in flags are true, append to list
        '''
        for word in words:
            flags = []
            for l in letter_pos:
                '''
                if char at word is equal to the char at that dict position, set to true
                '''
                if word[l] == letter_pos[l]:
                    flags.append(True)
                else:
                    flags.append(False)
            
            if False in flags:
                pass
            else:
                filtered_words.append(word)

        return filtered_words

    def letters_not_in_pos(self, letter_pos, words=None):
        if words == None:
            words = self.load_dictionary()

        filtered_words = []

        for word in words:
            flags = []
            for l in letter_pos:
                '''
                if char at word is equal to the char at that dict position, set to false
                '''
                if word[l] == letter_pos[l]:
                    flags.append(False)
                else:
                    flags.append(True)
            
            if False in flags:
                pass
            else:
                filtered_words.append(word)

        return filtered_words

if __name__ == '__main__':
    x = wordle_solver()

    '''
    print full dictionary
    '''
    # print(x.load_dictionary())
    # print(len(x.load_dictionary()))
    # print('\n')

    '''
    print words after filtering for those with correct letters
    '''
    result = x.words_correct_letters(letters=['k'])
    print('After filtering for those with correct letters:', result)
    print('\n')

    '''
    print words after filtering away those with incorrect letters
    '''
    result = x.words_wrong_letters(letters=['w','o','u','n','d','h','a','r'], words = result)
    print('After filtering away those with incorrect letters:', result)
    print('\n')

    '''
    print words after filtering for those of length 5
    '''
    result = x.words_of_len(length = 5, words = result)
    print('After filtering for those with specified length:', result)
    print('\n')

    '''
    print words after specifying letters not in respective positions
    '''
    letter_pos = {4:'k'}
    result = x.letters_not_in_pos(letter_pos=letter_pos, words = result)
    print('After removing words with yellow characters:', result)
    print('\n')

    '''
    print words after specifying letters in their respective positions
    '''
    letter_pos = {0:'s'}
    result = x.specify_letter_pos(letter_pos=letter_pos, words = result)
    print('After specifying letters in their respective positions:', result)