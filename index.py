import madlibs

def printMadlib(index):
    madlibs_string = ''
    tuple_length = len(madlibs.madlibsTuple[index][0])
    
    i = 0
    while i < tuple_length:
        madlibs_string += madlibs.madlibsTuple[index][0][i]
        
        if i != tuple_length - 1:
            madlibs_string += handleInput(index, i, madlibs.madlibsTuple[index][1][i])

        i += 1
        
    print(f'\n{madlibs_string}')
    
def handleInput(madlib_index, input_index, type):
    input_type = madlibs.madlibsTuple[madlib_index][1][input_index]
    suffix = getSuffix(input_type)
    
    if suffix != None:
        fail_prefix = f'invalid {input_type[5:]} : '
        message = f'Enter a/an {input_type[5:]} that ends in -{suffix} : '
    else:
        fail_prefix = f'invalid {input_type} : '
        message = f'Enter a/an {input_type}: '
    
    while True:
        user_input = input(message)

        if user_input == '':
            print(f'{fail_prefix}must not be empty\n')
            continue
            
        if type == 'number':
            if not validNum(user_input):
                print(f'{fail_prefix}must be a number\n')
                continue
        else:
            if validNum(user_input):
                print(f'{fail_prefix}must not be a number\n')
                continue
            elif suffix != None and user_input[-3:] != suffix:
                print(f'{fail_prefix}must end in -{suffix}\n')
                continue
        
        return user_input
    
def getIndex():
    num_of_madlibs = len(madlibs.madlibsTuple)
    selection = ''
    
    for i in range(num_of_madlibs):
        i += 1
        selection += str(i)
        if i != num_of_madlibs:
            selection += ', '
    
    message = f'Enter {selection} to choose a Mad Lib: '
        
    while True:
        index = input(message)
        
        if index == '':
            print('invalid index : must not be empty\n')
            continue

        if not validNum(index):
            print(f'invalid index : must be a number\n')
            continue
        
        if not 0 < int(index) <= num_of_madlibs:
            print(f'invalid index : must be between 0 and {num_of_madlibs}\n')
            continue
        
        printMadlib(int(index) - 1)
        return
    
def validNum(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def getSuffix(string):
    try:
        after_dash = string.index('-') + 1
        suffix = string[after_dash : after_dash + 3]

        return suffix
    except ValueError:
        return None

getIndex()