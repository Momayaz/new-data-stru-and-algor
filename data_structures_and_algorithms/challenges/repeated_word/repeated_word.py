from data_structures_and_algorithms.challenges.linked_list.linked_list import Node, LinkedList

def length(string):
    star_len = 1
    while True:
        try:
            string[star_len]
        except IndexError:
            break
        else:
            star_len += 1
            continue
    return star_len

def repeated_word(paragraph):
    words = LinkedList()
    word = ''
    count = 0
    for i in paragraph:
        count +=1
        if count == length(paragraph): # for length it is a function i built it 
            words.append(word)
        elif i ==',' or i =='.':
            continue
        elif i == ' ' or i == ',':
            if words.includes(word):
                return word
            words.append(word)
            word=''
            continue
        else:
            word += i.lower()
        
    return 'there is no repeated word in this paragraph'




if __name__ == '__main__':
    test1 = "Once upon a time, there was a brave princess who..."
    assert repeated_word(test1) == 'a'
    print('all tests is passed !!!')


