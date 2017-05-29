
PLACE_VALUE = ['','thousand','million','billion','trillion']

NUMBER_WORD = ['zero', 'one','two','three','four','five','six','seven', 'eight','nine',
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
                main_place = PLACE_VALUE[counter]
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
    digit_len = len(str(value))
    dividen = int(value)
    COMMON_INDEX = 2
    step = 0
    while divisor > 0:
        quotent = dividen // divisor
        remainder = dividen % divisor
        step += 1
        if step == 1:
            if remainder == 0:
                if quotent > 0:
                    word += NUMBER_WORD[quotent] + ' hundred '
                return word
            else:
                if quotent > 0:
                    word +=  NUMBER_WORD[quotent] + ' hundred and '
                dividen  = remainder
        elif step == 2:
            if remainder == 0:
                if quotent > 0:
                    quotent = int('2' + str(quotent - 2) )
                    word += NUMBER_WORD[quotent]
                return word
            else:
                if quotent > 0:
                    quotent =  int('2' + str(quotent - 2))
                    word += NUMBER_WORD[quotent] + '-'
                    dividen = remainder
        elif step == 3:
            if remainder == 0:
                if quotent > 0:
                    word += NUMBER_WORD[quotent]
        else:
            pass
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
    value = '1003234'
    result = toword(value)
    print(result)



