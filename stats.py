def get_num_words(book_text):
    return len(book_text.split())

def get_num_chars(book_text):
    chars = {}
    for char in book_text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_by_num(item):
    return item["num"]

def get_sorted_num_chars(chars):
    items = []
    for char in chars:
        items.append({
            "char": char,
            "num": chars[char]
        })
    items.sort(reverse=True, key=sort_by_num)
    return items