def single_root_words(root_word, *other_word):
    same_word = []
    for item in other_word:
        if root_word.lower() in item.lower() or item.lower() in root_word.lower():
            same_word.append(item)
    return same_word



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)