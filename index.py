import madlibs

def printMadlib(madlibIndex):
    madlibs_string = ''
    tuple_length = len(madlibs.templates[madlibIndex]['paragraph'])
    
    for sentenceIndex in range(tuple_length):
        madlibs_string += madlibs.templates[madlibIndex]['paragraph'][sentenceIndex]
        
        if sentenceIndex != tuple_length - 1:
            fill_in_str = handleInput(madlibIndex, sentenceIndex)
            
            if madlibs_string[len(madlibs_string) - 2:] == ' a':
                if isVowel(fill_in_str[0]):
                    madlibs_string += 'n'
                madlibs_string += ' '
            
            madlibs_string += fill_in_str
        
    print(f'\n{madlibs_string}')
    
def handleInput(madlib_index, input_index):
    input_type = madlibs.templates[madlib_index]['fill_in'][input_index]
    suffix = getSuffix(input_type)
    
    if suffix != None:
        inv_message_prefix = f'invalid {input_type[5:]} : '
        message = f'Enter a/an {input_type[5:]} that ends in -{suffix} : '
    else:
        inv_message_prefix = f'invalid {input_type} : '
        message = f'Enter a/an {input_type}: '
    
    while True:
        user_input = input(message)

        if user_input == '':
            print(f'{inv_message_prefix}must not be empty\n')
            continue
            
        if input_type == 'number':
            if not isValidNum(user_input):
                print(f'{inv_message_prefix}must be a number\n')
                continue
        else:
            if isValidNum(user_input):
                print(f'{inv_message_prefix}must not be a number\n')
                continue
            elif suffix != None:
                if user_input[-3:] != suffix:
                    print(f'{inv_message_prefix}must end in -{suffix}\n')
                    continue
                
                if user_input == suffix:
                    print(f'{inv_message_prefix}must not be only -{suffix}\n')
                    continue
        
        return user_input

def getIndex():
    num_of_madlibs = len(madlibs.templates)
    inv_message_prefix = 'invalid index : '
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
            print(f'{inv_message_prefix}must not be empty\n')
            continue

        if not isValidNum(index):
            print(f'{inv_message_prefix}must be a number\n')
            continue
        
        if not 0 < int(index) <= num_of_madlibs:
            print(f'{inv_message_prefix}must be between 0 and {num_of_madlibs}\n')
            continue
        
        printMadlib(int(index) - 1)
        return
    
def isValidNum(string):
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
    
def isVowel(char):
    if char in ['a','e','i','o','u',]:
        return True
    else:
        return False

getIndex()
