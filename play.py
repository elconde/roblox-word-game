FILE_NAME = 'words-alpha.txt'

with open(FILE_NAME) as file:
    words = file.read().splitlines()

while True:
    clue = input('> ')
    answers = []
    for word in words:
        if clue not in word:
            continue
        answers.append(word)
    answers.sort(key=len, reverse=True)
    for answer in answers:
        print(answer)
