import random

AMOUNT_OF_NUMS = 4

play_again = True

# NEW GAME
while(play_again):

	# init: setting "ans" (answer)
	ans = []

	for i in range(AMOUNT_OF_NUMS):

		new_rand = random.randint(0, 9 - i)

		sorted_ans = ans.copy()
		sorted_ans.sort()

		for j in range(i):

			if new_rand >= sorted_ans[j]:

				new_rand += 1

		ans.append(new_rand)

	# == "ans" setting complete ==

	gameover = False

	# GAME START
	print("=================")
	print("New Game Started!")

	while(not gameover):

		print("\nYour guess:", end = " ")
		user_input = input()

		try:

			input_int = int(user_input)

		except:

			print("Bad input! (Not numbers)")
			continue


		if input_int < 0:

			print("Bad input! (Negative sign not allowed)")
			continue


		input_nums = []

		while(input_int > 0):

			input_nums.append(input_int % 10)
			input_int //= 10

		# deal with 0-started numbers
		for num_char in user_input:

			if num_char == '0':
				input_nums.append(0)

			else:
				break


		if len(input_nums) < AMOUNT_OF_NUMS:

			print("Bad Input! (Less than " + str(AMOUNT_OF_NUMS) + " numbers)")
			continue

		elif len(input_nums) > AMOUNT_OF_NUMS:

			print("Bad Input! (More than " + str(AMOUNT_OF_NUMS) + " numbers)")
			continue


		input_nums.reverse()


		# check if it has duplicated numbers
		sorted_input_nums = input_nums.copy()
		sorted_input_nums.sort()

		is_duplicated = False

		for j in range( len(sorted_input_nums) - 1 ):

			if sorted_input_nums[j] == sorted_input_nums[j + 1]:

				is_duplicated = True


		if is_duplicated:

			print("Bad input! (same numbers appeared)")
			continue


		# Counting Bulls and Cows
		a_count = 0
		b_count = 0

		for i in range(AMOUNT_OF_NUMS):
			for j in range(AMOUNT_OF_NUMS):

				if input_nums[i] == ans[j]:

					if i == j:
						a_count += 1

					else:
						b_count += 1


		if (a_count < 4):

			print("You got " + str(a_count) + "A" + str(b_count) + "B")

		else:

			print("YOU WIN!")
			print("")

			gameover = True

			while(True):

				print("Play again? Y/N:", end = " ")
				y_n = input()

				if y_n == "y" or y_n == "Y":

					play_again = True
					break

				elif y_n == "n" or y_n == "N":

					play_again = False
					break
