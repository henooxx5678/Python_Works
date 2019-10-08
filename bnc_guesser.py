import random

DIGIT_RNAGE      = 10  # 0 - 9
AMOUNT_OF_DIGITS = 4

amount_of_possibilities = 1

for i in range(AMOUNT_OF_DIGITS):

    amount_of_possibilities *= DIGIT_RNAGE - i


guessed_list = []
a_count_list = []
b_count_list = []


def run():

    global guessed_list, a_count_list, b_count_list

    play_again = True

    while(play_again):

        guessed_list = []
        a_count_list = []
        b_count_list = []

        gameover = False

        # GAME START
        print("=================")
        print("New Game Started!")

        while(not gameover):

            guess_result = guess()

            if guess_result == -1:

                print("\nIt's totally no answer!", end = "\n\n")

                play_again = ask_to_play_again()
                gameover = True

            elif guess_result == 1:

                print("BINGO!")
                print("Congratulate myself :D", end = "\n\n")

                play_again = ask_to_play_again()
                gameover = True


def guess ():

    first_guessed_index = random.randint(0, amount_of_possibilities)

    guessed_index = first_guessed_index
    guessed_nums  = get_nums(guessed_index)

    while( not is_possible(guessed_nums) ):

        guessed_index = (guessed_index + 1) % amount_of_possibilities
        guessed_nums = get_nums(guessed_index)

        if guessed_index == first_guessed_index:
            return -1


    print("\nGuess: " + nums_to_str(guessed_nums))

    while(True):

        print("A:", end = " ")

        input_a_str = input()

        print("B:", end = " ")

        input_b_str = input()

        try:
            input_a = int(input_a_str)
            input_b = int(input_b_str)

        except:
            print("Bad input!")
            continue

        if (input_a + input_b > 4):
            print("Wrong input!")
            continue

        break;

    if (input_a == 4):
        return 1

    else:
        guessed_list.append(guessed_nums)
        a_count_list.append(input_a)
        b_count_list.append(input_b)
        return 0


def get_nums (index):

    indices = []
    result  = []

    for n in range(AMOUNT_OF_DIGITS)[::-1]:

        indices.append( index % (DIGIT_RNAGE - n) )
        index //= DIGIT_RNAGE - n

    indices.reverse()

    for ind in indices:

        thisNum = ind

        sorted_result = result.copy()
        sorted_result.sort()

        for num in sorted_result:

            if (num == thisNum):
                thisNum += 1

        result.append(thisNum)

    return result


def is_possible (nums):

    is_possible = True

    for i in range( len(guessed_list) ):

        a_counter = 0
        b_counter = 0

        for j in range(AMOUNT_OF_DIGITS):
            for k in range(AMOUNT_OF_DIGITS):

                if (nums[j] == guessed_list[i][k]):

                    if j == k:
                        a_counter += 1

                    else:
                        b_counter += 1

        if (a_counter != a_count_list[i] or b_counter != b_count_list[i]):
            is_possible = False

    return is_possible


def nums_to_str (nums):

    result = ""

    for num in nums:
        result += str(num)

    return result


def ask_to_play_again ():

    while(True):

        print("Play again? Y/N:", end = " ")
        y_n = input()

        if y_n == "y" or y_n == "Y":
            return True

        elif y_n == "n" or y_n == "N":
            return False


run()
