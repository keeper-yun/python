import ast

def calculate_average(salary):
    total = sum(salary)
    return total / len(salary)

def main():
    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    salary = {}
    for line in lines:
        try:
            data = ast.literal_eval(line.strip())
            sid = data.pop('sid')
            values = list(data.values())
            avg = calculate_average(values)
            salary[sid] = values + [avg]
        except (SyntaxError, ValueError) as e:
            print(f"", end="")


    print("{", end="")
    for key in sorted(salary.keys()):
        print(f"‘{key}’:{salary[key]}",end="\n")
    print('}')

if __name__ == "__main__":
    main()
