import json

with open('Odpowiedzi.tex', 'r') as file:
    data = file.read().splitlines()

QUESTION_START = '\\subsection'
TODO_FLAG = '\\color{red}'

data = [x for x in data if QUESTION_START in x]
all_questions = len(data)

data = [x for x in data if TODO_FLAG not in x]
done_questions = len(data)

output = {
    "done": done_questions,
    "all": all_questions
}

print(output)


with open('coverage.json', 'w+') as file:
    json.dump(output, file)
