import time

def option1():
    code = 0
    for digit1 in range(0,10):
      for digit2 in range(0,10):
        if digit1 < digit2:
            for digit3 in range(0,10):
                if digit2<digit3:
                    code += 1
    return code

def option2():
    code = 0
    for x in range(0, 10):
      for y in range(0, 10):
          for z in range(0, 10):
                if x < y and y < z:
                    code += 1
    return code

def option3():
    code = 0
    for i in range(1000):
        x = i // 100
        y = (i % 100) // 10
        z = (i % 100) % 10
        if x < y and y < z:
            code += 1
    return code

start = time.time()
option1()
option1 = time.time()
option2()
option2 = time.time()
option3()
option3 = time.time()

print(format(option1 - start, '.20f'))
print(format(option2 - option1, '.20f'))
print(format(option3 - option2, '.20f'))

