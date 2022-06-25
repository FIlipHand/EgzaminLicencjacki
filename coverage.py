import json
import re

with open('kurwa_juz_git.tex', 'r') as file:
    data = file.read().splitlines()

SECTION_START = '\\section'
TODO_FLAG = '\\color{red} TODO:'

data = [x for x in data if SECTION_START in x]
all_questions = len(data)

data = [x for x in data if TODO_FLAG not in x]
done_questions = len(data)

output = {
    "done": done_questions,
    "all": all_questions
}


with open('coverage.json', 'w+') as file:
    json.dump(output, file)
