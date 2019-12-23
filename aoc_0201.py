#aoc_0201.py

#WIP not working
def intcode(opcode_list): #, noun, verb):
    counter = 0
    #opcode_list[1] = noun
    #opcode_list[2] = verb
    while counter <= len(opcode_list):
    
        if opcode_list[counter] == 1:
            opcode_list[opcode_list[counter+3]] = opcode_list[opcode_list[counter+1]] + opcode_list[opcode_list[counter+2]]
            #print('1')
            counter += 4
            
            
        elif opcode_list[counter] == 2:
            opcode_list[opcode_list[counter+3]] = opcode_list[opcode_list[counter+1]] * opcode_list[opcode_list[counter+2]]
            #print('2')
            counter += 4
            
        elif opcode_list[counter] == 99:
            print('code 99 %d' % opcode_list[0])
            return opcode_list
        
        else:
            print('something is very very wrong')
            print('unknown code %d' % opcode_list[0])
            return opcode_list
            break


def checker(values, noun, verb):
    
    values[1] = noun
    values[2] = verb
    return intcode(values)
    #print(intcode(values))

        
def baseValue():
    baseValues = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,
    1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,
    1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0]
    return baseValues
    
    
if __name__ == '__main__':
    #values = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,
    #1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,
    #1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0]
    
    stopVal = 19690720
    # noun = 0
    # verb = 0
    checkVal = [0]
# ##    for num in range(99):
# ##        for val in range (99):
# ##            checkVal = intcode(values, num, val)
# ##            print(checkVal[0])
# ##            #if checkVal[0] == stopVal:
# ##                #print(num,val)
# ##                #break
# ##
    # #for i in range(99):
    # #while noun < 99:
    # print(checker(values, noun, verb))
    # for item in values:
        # print(item)
    while checkVal[0] != stopVal:
        tempVals = baseValue()
        for i in range(99):
            for j in range(99):
                checkVal = checker(tempVals, i, j)
