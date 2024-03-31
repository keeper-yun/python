
def vowel(s):
    wants = 'aeiouAEIOU'
    return s in wants
def vowelLetters():
    wordlist = []

    for i in range(10):
        word = input(f'请输入一个英文单词：')
        if(vowel(word[0])):
            wordlist.append(word)

    print()
    print("以元音字母开头的单词有：")
    for word in wordlist:
        print(word,end=' ')

vowelLetters()