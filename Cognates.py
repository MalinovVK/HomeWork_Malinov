def single_root_words(root_word, *other_words):
    root = root_word.lower()
    same_words = []
    for k in range(len(other_words)):
        s = other_words[k].lower()
        if root in s or s in root:
            same_words.append(other_words[k])
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))


