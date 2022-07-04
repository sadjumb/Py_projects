def open_file(path=str('')):
    try:
        file = open(path, 'r')
    except IOError:
        print("Can't open file")
    else:
        return file


def next_line(the_file):
    line = the_file.readline()
    line = line.replace('/', '\n')
    return line


def next_block(the_file):
    episode = next_line(the_file)
    question = next_line(the_file)
    answer = []
    for i in range(4):
        answer.append(next_line(the_file))
    correct_answer = next_line(the_file)
    return episode, question, answer, correct_answer


def run_victorina():
    f = open_file("trivia.txt")
    episode, question, answers, correct_answer = next_block(f)
    score = 0
    while episode:
        print(episode, '\n', question)
        for i, value in enumerate(answers):
            print(i + 1, value)
        try:
            answer = int(input("Enter you answer: "))
        except ValueError as ve:
            print("ValueError ", ve)
        else:
            if answers[answer - 1] == correct_answer:
                print('Right')
                score += 1
            else:
                print('Mistake, Correct answer is: ', correct_answer)
            print('Your score: ', score)
        episode, question, answers, correct_answer = next_block(f)
    f.close()
