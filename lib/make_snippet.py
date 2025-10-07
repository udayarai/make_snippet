def make_snippet(string):

    words_list = string.strip().split()
    #new_words_list = []

    if len(words_list) <= 5:
        return string
    else:
        """
        for word in words_list:
            if words_list.index(word) <= 4:  #finds the index
                new_words_list.append(word)
        """
        filtered_words_list = [word for word in words_list if words_list.index(word) <= 4]

        new_string = " ".join(filtered_words_list)
        
        return f"{new_string}..."