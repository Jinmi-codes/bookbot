def get_book_text(path):
    with open(path,'r') as file:
        content = file.read()
        return content
    
def count_words(path):
    words = get_book_text(path).split()
    return len(words)

def count_chars(path):
    chars,count = [],{}
    text = get_book_text(path)
    for char in text:
        if char.lower() not in chars:
            chars.append(char.lower())
        
    for value in chars:
        counter=0
        for char in text:
            if char.lower() == value.lower():
                counter+=1
        count.update({value:counter})

    return count


