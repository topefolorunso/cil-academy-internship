def padlock_code_challenge_1():
    '''
    code = 1 + 2 + 3 + 4 + … + 38 + 39 + 40

    Padlock Code Challenge - www.101computing.net/padlock-code-challenge-1/
    '''
    code = 0

    for i in range(1,41):
      code += i
      print(i)

    print("Code:")
    print(code)



def padlock_code_challenge_2():
    '''Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/
    '''

    code = 0
    #Update the code below to solve this challenge
    for digit1 in range(0,10):
      for digit2 in range(0,10):
        for digit3 in range(0,10):
          if digit1<digit2 and digit2<digit3:
            code += 1
      # print(str(digit1)+str(digit2)+str(digit3))


    print("Code:")
    print(code)



def padlock_code_challenge_3():
    '''Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/
    code = Total number of 3-digit combinations where digit1, digit2 and digit3 are all even numbers

    e.g. 024 and 886 count as valid combinations whereas 124 or 456 are invalid combinations.'''

    code = 0
    for digit1 in range(0,10):
        if digit1%2 == 0:
            for digit2 in range(0,10):
                if digit2%2 == 0:
                    for digit3 in range(0,10):
                        if digit3%2 == 0:
                            code += 1
                        # print(str(digit1)+str(digit2)+str(digit3))


    print("Code:")
    print(code)

def padlock_code_challenge_4():
    '''Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/

    code = Total number of 3-digit combinations where the sum of all three digits (digit1 + digit2 + digit3) is an odd number

    e.g. 034 and 555 count as valid combinations whereas 123 or 468 are invalid combinations.'''
    code = 0
    #Update the code below to solve this challenge
    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                if (digit1 + digit2 + digit3)%2 == 1:
                    code += 1
                # print(str(digit1)+str(digit2)+str(digit3))


    print("Code:")
    print(code)


def padlock_code_challenge_5():
    '''Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/
    code = Total number of 3-digit combinations where at least two digits are equal.

    e.g. 030 and 558 count as valid combinations whereas 123 or 468 are invalid combinations.'''
    code = 0
    #Update the code below to solve this challenge
    for digit1 in range(0,10):
        for digit2 in range(0,10):
            if digit1 == digit2:
                code += 10
                continue
            for digit3 in range(0,10):
                if digit1 == digit3 or digit2 == digit3:
                    code += 1
                # print(str(digit1)+str(digit2)+str(digit3))


    print("Code:")
    print(code)