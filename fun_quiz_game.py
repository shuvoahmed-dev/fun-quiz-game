name = input("What is your name?\n")

print("\nGood to have you,", name + ", it's time to test your knowledge about Germany!\n")

print("Here is your first question:\n")

questions = ["What is the capital city of Germany? ",
             "Which German city is famous for its annual Oktoberfest beer festival? ",
             "How many FIFA World Cups has Germany won (men's team)? ",
             "Which is the biggest football club in Germany? ",
             "Who scored the winning goal in the 2014 World Cup final for Germany? "]

answers = ["berlin", "munich", "4", "bayern munich", "mario gotze"]

a = 1000
b = 2000
c = 3000
d = 4000
e = 5000

answer1 = input(questions[0])
if answer1.lower() == answers[0]:
    print("Easy huh? You have won", a, "euros.\n")

    answer2 = input(questions[1])
    if answer2.lower() == answers[1]:
        print("Two in a row? You have won", b, "euros.\n")

        answer3 = input(questions[2])
        if answer3.lower() == answers[2]:
            print("Hat-trick! You have won", c, "euros.\n")

            answer4 = input(questions[3])
            if answer4.lower() == answers[3]:
                print("Four? You're on fire! Bayern Munich wants you on the team! You have won", d, "euros.\n")

                answer5 = input(questions[4])
                if answer5.lower() == answers[4]:
                    print("Five outta five! This quiz needs harder questions. You have won", e, "euros!\n")
                else:
                    print("Wrong answer. Your take-home amount is", d, "euros.\n")
            else:
                print("Wrong answer. Your take-home amount is", c, "euros.\n")
        else:
            print("Wrong answer. Your take-home amount is", b, "euros.\n")
    else:
        print("Wrong answer. Your take-home amount is", a, "euros.\n")
else:
    print("Yeah... this game isn't for everyone. You won 0 euros.\n")

print("It was great playing with you,", name + "!")