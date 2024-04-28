

# poemPractice.py
import random
from Poem import Poem

def getRandomPoem(poem_list):
    random_poem = random.choice(poem_list)
    title, dynasty, poet, content = random_poem.split('|')
    poem_obj = Poem(title, dynasty, poet)
    poem_obj.setContent(content)
    return poem_obj

def answerQuestion(poem_obj):
    content = poem_obj.content
    random_line = random.choice(content)
    blanked_line = random_line.replace(random.choice(random_line.split('，')), '___')

    print(f"{poem_obj.title.center(7)}")
    print(f"{poem_obj.dynasty.rjust(3)}", end=" ")
    print(f"{poem_obj.poet}")

    for line in content:
        if line == random_line:
            print(blanked_line.strip())
        else:
            print(line.strip())

    user_answer = input("请补充空缺的诗句：")
    user_answer2 = user_answer + "。"
    user_answer3 = user_answer + "，"

    if user_answer == random_line:
        return True
    elif user_answer2 == random_line:
        return True
    elif user_answer3 == random_line:
        return True

def main():
    # 示例用法
    poem_list = [
        "静夜思|唐代|李白|床前明月光，\n疑是地上霜。\n举头望明月，\n低头思故乡。",
        "江南春|唐代|杜牧|千里莺啼绿映红，\n水村山郭酒旗风。\n南朝四百八十寺，\n多少楼台烟雨中。",
        "望洞庭|唐代|刘禹锡|湖光秋月两相和，\n潭面无风镜未磨。",
        # 添加更多古诗词
    ]

    correct_answers = 0
    total_questions = 0
    count = 0

    while True:
        count += 1
        print(f'第{count}题')
        random_poem = getRandomPoem(poem_list)
        total_questions += 1
        if answerQuestion(random_poem):
            print("恭喜你，本题答对了!")
            correct_answers += 1
        else:
            print("很遗憾，本题答错了。")

        continue_answer = input("是否继续做下一题(N/Y)? ")
        if continue_answer.lower() != 'y':
            break

    print(f"本次答题结束，您一共答对{correct_answers}题，答错{total_questions - correct_answers}题！")
    print()

