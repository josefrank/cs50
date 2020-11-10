text = input("Text: ")
letter_count = 0
word_count = 1
sentence_count = 0

for i in text:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        letter_count += 1
    elif i == ' ':
        word_count += 1
    elif i == '.' or i == '!' or i == '?':
        sentence_count += 1

print(f"letters: {letter_count}, words: {word_count}, sentences: {sentence_count}.")

grade = 0.0588 * (100 * float(letter_count) / float(word_count)) \
        - 0.296 * (100 * float(sentence_count) / float(word_count)) - 15.8

if grade < 16 and grade >= 0:
    print(f"Grade {int(round(grade))}")
elif grade >= 16:
    print("Grade 16+")
else:
    print("Before Grade 1")
