

import random
def guess():
    word = ['python', 'javaweb', 'html', 'sqlsever']

    while True:
        index = random.randint(0, len(word) - 1)
        chooseword = word[index]
        word.remove(word[index])

        answer = ''.join(random.sample(chooseword, len(chooseword)))
        real = chooseword

        getsth = input(f'根据{answer}，请猜出正确单词:')

        while getsth != '':
            if getsth == real:
                print(f'猜对了!,正确单词是:{real}')
                print()
                break
            getsth = input('猜错了，再猜:')

        response = input('要不要再玩一次?\n(Y/N):')

        if response.lower() != 'y':
            break
guess()
