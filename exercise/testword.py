


f_right = open("123a.txt", 'r').read()
f_check = open("123b.txt", 'r').read()

def removeSign(text, sign):
    cleanText = text
    for i in sign:
        cleanText = cleanText.replace(i, '')
    return cleanText.split(' ')

toRemove = [",", ".", "'", '"', ";", "--"]
words_right = removeSign(f_right, toRemove)
words_check = removeSign(f_check, toRemove)

misspellWords = []
for wd in words_check:
    if wd not in words_right:
        misspellWords.append(wd)

print misspellWords
