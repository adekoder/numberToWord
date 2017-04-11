
place_value = ['','thousand','million','billion','trillion']

number_word = ['zero', 'one','two','three','four','five','six','seven', 'eight','nine',
				'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen',
				'eighteen','nineteen','twenty','thirty','fourty','fifty','sixty','seventy',
				'eighty','ninty'
			]

def toword(value):
	number = int(value)
	digit_len = len(value)
	word = ''
	word_format = []
	digit_group = []
	if digit_len > 3:
		# if digit is > 3 split them in schuncks of 3
		digit_group = groupNumber(number)
		digit_group_len = len(digit_group)
		counter = 0
		while digit_group_len > 0:
			#for each digit group perform hundred tens and units conversion
			number = digit_group[counter]
			number_word = hundredTensUnits(number)
			if number_word != '':
				main_place = place_value[counter]
				number_word += ' '+  main_place
			word_format.append( number_word)
			#word_format.append( main_place)
			counter += 1
			digit_group_len -= 1
		word = ' '.join(word_format[::-1])
		#print(word_format[::-1])
	else:
		word = hundredTensUnits(number)

	return word

def hundredTensUnits(value):
	""" hundred tens and units conversion """
	divisor = 100
	word = ""
	value = int(value)
	COMMON_INDEX = '2'
	while divisor > 0:
		digit = value % divisor
		# number is divisible by hundred
		if digit == 0:
			ans = value // divisor
			# means no remainder
			if ans != 0:
				word = number_word[ans] + "  hundred"
			return word
		else:
			# if there is remainder
			ans = value // divisor
			remainder = value % divisor
			if ans != 0:
				word = number_word[ans] + ' hundred and '
			# reduces the remainder by a factor of 10
			divisor /=10
			if remainder % divisor == 0:
				#if remainder is has no remainder 
				ans = remainder // divisor

				if ans > 1:
					# if ans is greater than 1 i.e ans == 2 ,3, upward
					# based on the structure of number word list 
					ans = ans - 2
					COMMON_INDEX += str(ans)
				else:
					#if  ans is 1 just add zero to the back and find in the list
					COMMON_INDEX = str(ans) + '0'
				word += number_word[int(COMMON_INDEX)]
				return word
			else:
				#if remainder has remainder
				ans = remainder // divisor
				remainder = remainder % divisor
				if ans == 0:
					word += number_word[remainder]
				elif ans > 1:
					ans = ans - 2
					COMMON_INDEX += str(ans)
					word += number_word[int(COMMON_INDEX)] +'-'+ number_word[remainder]
				else:
					ans = ans * 10
					word += number_word[ans + remainder]
					divisor /= 10
					return word

def groupNumber(number):
	""" this function group into chunck of threes from right to left"""
	number = int(number)
	digit_group = []
	while number > 0:
		remainder = number % 1000
		digit_group.append(remainder)
		number /= 1000
	return digit_group





if __name__ == '__main__':
	# file =  open('output1.txt' , 'w')
	# for value in range(1,999999):
	# 	result = toword(str(value))
	# 	file.write("%s => %s \n" %(value,result) )
	# file.close()
	value = '100100010000000'
	result = toword(value)
	print(result)
