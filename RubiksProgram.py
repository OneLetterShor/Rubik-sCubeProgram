#Rubik's Cube foundation program
#@author: Lux Wooten
autoDo = 0
pynDo = input('Do you have pynput installed? ')
doScramble = 0
if(pynDo == 'y' or pynDo == 'yes'):
    from pynput.keyboard import Key, Controller
    import time
    keyboard = Controller()
    auto = input('Perform auto? ')
    if(auto == 'y'):
        autoDo = 1
    autoScramble = input('Do you want the program to auto scramble it?')
    if(autoScramble == 'y'):
        import random
        doScramble = 1
def get_place():
    """
    Can be used in the manual gathering of input to find the place of the cube. Ex: (corner, side, or middle)
    """
    place1 = input('Enter the place ')
    return place1
def get_location():
    """Can be used to manually gather information about the place of the input. Ex:(tr(top right), bl(bottom left) etc"""
    location1 = input('Enter the location ')
    return location1
def get_color():
    """Can be used to manually gather the color of any place. Input Ex: r(red), y(yellow) """
    color = input('Enter the color: ')
    return color
def get_coords(place, location):
    """Uses the get_place() function and the get_location() function to find the coordinates on a side.
    Ex(The top left corner would have the coordinates of (-1, 1)"""
    xCoord = 0
    yCoord = 0
    if (place == 'corner'):
        if(location == 'tr'):
            xCoord = 1
            yCoord = 1
        elif(location == 'tl'):
            xCoord = -1
            yCoord = 1
        elif(location == 'br'):
            xCoord = 1
            yCoord = -1
        elif(location == 'bl'):
            xCoord = -1
            yCoord = -1
    elif(place == 'side'):
        if(location == 'l'):
            xCoord = -1
        elif(location == 'r'):
            xCoord = 1
        elif(location == 't'):
            yCoord = 1
        elif(location == 'b'):
            yCoord = -1
    elif(place == 'middle'):
        xCoord = 0
        yCoord = 0
    else:
        print('Not a valid input, try again')
    return [xCoord, yCoord ]
def get_side():
    """Shotcut function that uses get_color() to get the colors of a side, and stores it in a list"""
    c0 = get_color()
    c1 = get_color()
    c2 = get_color()
    c3 = get_color()
    c4 = get_color()
    c5 = get_color()
    c6 = get_color()
    c7 = get_color()
    c8 = get_color()
    return [c0, c1, c2, c3, c4, c5, c6, c7, c8]
def rot_r(x, y):
    """Uses rotation equation to rotate a side using the coordinates.
    Important: This function does NOT affect other sides of a cube. Use the rot_side_r/l functions for that"""
    if(x > 0 and y > 0):
        x *= -1
    elif(x > 0 and y < 0):
        x *= -1
    elif(x <0 and y < 0):
        x *= -1
    elif(x < 0 and y > 0):
        x*=-1
    if(x == 1 and y == 0):
        x*=-1
    elif(x == -1 and y == 0):
        x*= -1
    temp = y
    y = x
    x = temp
    return [x, y]
def print_side(side):    
   """Important funtion that will print out a side based on its coordinates.
   MAKE SURE TO INPUT THE SIDE VARIABLE NOT A NUMBER"""
   checker1 = 0
   while(checker1 <= 8):
       if(side[checker1][0] == 'b'):
           print("\033[48;5;21m   ", end = '')
       elif(side[checker1][0] == 'w'):
           print("\033[48;5;15m   ", end = '')
       elif(side[checker1][0] == 'g'):
           print("\033[48;5;40m   ", end = '')
       elif(side[checker1][0] == 'y'):
           print("\033[48;5;11m   ", end = '')
       elif(side[checker1][0] == 'r'):
           print("\033[48;5;160m   ", end = '')
       elif(side[checker1][0] == 'o'):
           print("\033[48;5;208m   ", end = '')
       if(checker1 == 2):
           print("\033[31;1;4m\033[0m")
       if(checker1 == 5):
           print("\033[31;1;4m\033[0m")
       if(checker1 == 8):
           print("\033[31;1;4m\033[0m")
       checker1 += 1
def fix_variables(sideNum, cube):
    """Essential to the rot_side_r/l functions, resets the variables in the list in their correct order"""
    onePlace = 0
    twoPlace = 1
    threePlace = 2
    fourPlace = 3
    fivePlace = 4
    sixPlace = 5
    sevenPlace = 6
    eightPlace = 7
    ninePlace = 8
    #locates the parts of the set based on their coordinates vVv
    for i in range(9):
        if(cube[sideNum][i][1] == -1 and cube[sideNum][i][2] == 1):
            onePlace = i
            break
    for j in range(9):
        if(cube[sideNum][j][1] == 0 and cube[sideNum][j][2] == 1):
            twoPlace = j
            break
    for e in range(9):
        if(cube[sideNum][e][1] == 1 and cube[sideNum][e][2] == 1):
            threePlace = e
            break
    for f in range(9):
        if(cube[sideNum][f][1] == -1 and cube[sideNum][f][2] == 0):
            fourPlace = f
            break
    for d in range(9):
        if(cube[sideNum][d][1] == 0 and cube[sideNum][d][2] == 0):
            fivePlace = d
            break
    for b in range(9):
        if(cube[sideNum][b][1] == 1 and cube[sideNum][b][2] == 0):
            sixPlace = b
            break
    for o in range(9):
        if(cube[sideNum][o][1] == -1 and cube[sideNum][o][2] == -1):
            sevenPlace = o
            break
    for k in range(9):
        if(cube[sideNum][k][1] == 0 and cube[sideNum][k][2] == -1):
            eightPlace = k
            break
    for y in range(9):
        if(cube[sideNum][y][1] == 1 and cube[sideNum][y][2] == -1):
            ninePlace = y
            break
    #rearanges them to the original order vVv
    temp1 = list(cube[sideNum][onePlace])
    temp2 = list(cube[sideNum][twoPlace])
    temp3 = list(cube[sideNum][threePlace])
    temp4 = list(cube[sideNum][fourPlace])
    temp5 = list(cube[sideNum][fivePlace])
    temp6 = list(cube[sideNum][sixPlace])
    temp7 = list(cube[sideNum][sevenPlace])
    temp8 = list(cube[sideNum][eightPlace])
    temp9 = list(cube[sideNum][ninePlace])
   
    cube[sideNum][0] = temp1
    cube[sideNum][1] = temp2
    cube[sideNum][2] = temp3
    cube[sideNum][3] = temp4
    cube[sideNum][4] = temp5
    cube[sideNum][5] = temp6
    cube[sideNum][6] = temp7
    cube[sideNum][7] = temp8
    cube[sideNum][8] = temp9
 
    return cube    
def rot_side_r(sideNum, cube):
    """Main rotation function, first uses the rotation formula to rotate the specified side,
    then it makes sure all the adjacent sides are affected properly.
    Important: The input for the side must be either a number, or an integer from 1-6
    Also, the cube paramater will always be there. Ex: rot_side_r(3, cube)"""
    sideNum -= 1
    counter = 0
    #Rotates the entered side by switching the coordinates of the pieces on the side vVv
    for i in range(9):
        cube[sideNum][counter][1] *= -1
        temp = cube[sideNum][counter][1]
        cube[sideNum][counter][1] = cube[sideNum][counter][2]
        cube[sideNum][counter][2] = temp
        counter += 1
    counter = 0
    counter2 = 0
    #determines which side is being rotated with the center color, then changes the 4 adjacent sides correctly vVv
    if(cube[sideNum][4][0] == 'b'):
        counter2 = 6
        tempor = list(cube[5][0])
        tempora = list(cube[5][1])
        temporar = list(cube[5][2])
        for i in range(3):
           cube[5][counter][0] = cube[1][counter2][0]
           counter+=1
           counter2-=3
        counter = 0
        counter2 = 6
        for i in range(3):
            cube[1][counter][0] = cube[4][counter2][0]
            counter+=3
            counter2+=1
        counter = 8
        counter2 = 2
        for i in range(3):
            cube[4][counter][0] = cube[3][counter2][0]
            counter-=1
            counter2+=3
        counter = 2
        counter2 = 0
 
        cube[3][2][0] = tempor[0]
        cube[3][5][0] = tempora[0]
        cube[3][8][0] = temporar[0]
       
    elif(cube[sideNum][4][0] == 'w'):
        counter = 2
        counter2 = 6
        tempor = list(cube[5][2])
        tempora = list(cube[5][5])
        temporar = list(cube[5][8])
        for i in range(3):
            cube[5][counter][0] = cube[2][counter2][0]
            counter+=3
            counter2-=3
        counter = 0
        counter2 = 8
        for i in range(3):
            cube[2][counter][0] = cube[4][counter2][0]
            counter+=3
            counter2-=3
        counter = 2
        counter2 = 2
        for i in range(3):
            cube[4][counter][0] = cube[0][counter2][0]
            counter+=3
            counter2+=3
        cube[0][2][0] = tempor[0]
        cube[0][5][0] = tempora[0]
        cube[0][8][0] = temporar[0]
   
    elif(cube[sideNum][4][0] == 'g'):
        tempor = list(cube[5][8])
        tempora = list(cube[5][7])
        temporar = list(cube[5][6])
        counter = 8
        counter2 = 6
        for i in range(3):
            cube[5][counter][0] = cube[3][counter2][0]
            counter-=1
            counter2-=3
        counter = 0
        counter2 = 2
        for i in range(3):
            cube[3][counter][0] = cube[4][counter2][0]
            counter +=3
            counter2-=1
        counter= 0
        counter2 = 2
        for i in range(3):
            cube[4][counter][0] = cube[1][counter2][0]
            counter+=1
            counter2+=3
        cube[1][2][0] = tempor[0]
        cube[1][5][0] = tempora[0]
        cube[1][8][0] = temporar[0]
       
    elif(cube[sideNum][4][0] == 'y'):
        tempor = list(cube[5][0])
        tempora = list(cube[5][3])
        temporar = list(cube[5][6])
        counter = 0
        counter2 = 0
        for i in range(3):
            cube[5][counter][0] = cube[0][counter2][0]
            counter+=3
            counter2+=3
        counter = 0
        counter2 = 0
        for i in range(3):
            cube[0][counter][0] = cube[4][counter2][0]
            counter+=3
            counter2+=3
        counter = 0
        counter2 = 8
        for i in range(3):
            cube[4][counter][0] = cube[2][counter2][0]
            counter+=3
            counter2-=3
       
        cube[2][2][0] = temporar[0]
        cube[2][5][0] = tempora[0]
        cube[2][8][0] = tempor[0]
    elif(cube[sideNum][4][0] == 'r'):
        tempor = list(cube[0][0])
        tempora = list(cube[0][1])
        temporar = list(cube[0][2])
        counter = 0
        counter2 = 0
        for i in range(3):
            cube[0][counter][0] = cube[1][counter2][0]
            counter+=1
            counter2+=1
        counter = 0
        counter2 = 0
        for i in range(3):
            cube[1][counter][0] = cube[2][counter2][0]
            counter+=1
            counter2+=1
        counter = 0
        counter2 = 0
        for i in range(3):
            cube[2][counter][0] = cube[3][counter2][0]
            counter+=1
            counter2+=1
        cube[3][0][0] = tempor[0]
        cube[3][1][0] = tempora[0]
        cube[3][2][0] = temporar[0]
        counter = 0
    elif(cube[sideNum][4][0] == 'o'):
        tempor = list(cube[0][6])
        tempora = list(cube[0][7])
        temporar = list(cube[0][8])
        counter = 6
        counter2 = 6
        for i in range(3):
            cube[0][counter][0] = cube[3][counter2][0]
            counter+=1
            counter2+=1
        counter = 6
        counter2 = 6
        for i in range(3):
            cube[3][counter][0] = cube[2][counter2][0]
            counter+=1
            counter2+=1
        counter = 6
        counter2 = 6
        for i in range(3):
            cube[2][counter][0] = cube[1][counter2][0]
            counter+=1
            counter2+=1
        cube[1][6][0] = tempor[0]
        cube[1][7][0] = tempora[0]
        cube[1][8][0] = temporar[0]
    cube = fix_variables(sideNum, cube)
    print(sideNum+1, end = '')
    print('r')
    if(autoDo == 1):
        if(sideNum+1 == 1):
            keyboard.press(Key.shift)
            keyboard.press('r')
            keyboard.release(Key.shift)
            keyboard.release('r')
        elif(sideNum+1 == 2):
            keyboard.press(Key.shift)
            keyboard.press('f')
            keyboard.release(Key.shift)
            keyboard.release('f')
        elif(sideNum+1 == 3):
            keyboard.press(Key.shift)
            keyboard.press('l')
            keyboard.release(Key.shift)
            keyboard.release('l')
        elif(sideNum+1 == 4):
            keyboard.press(Key.shift)
            keyboard.press('b')
            keyboard.release(Key.shift)
            keyboard.release('b')
        elif(sideNum+1 == 5):
            keyboard.press(Key.shift)
            keyboard.press('d')
            keyboard.release(Key.shift)
            keyboard.release('d')
        elif(sideNum+1 == 6):
            keyboard.press(Key.shift)
            keyboard.press('u')
            keyboard.release(Key.shift)
            keyboard.release('u')
 
    return cube
def rot_side_l(sideNum, cube):
    """Main rotation function, first uses the rotation formula to rotate the specified side,
    then it makes sure all the adjacent sides are affected properly.
    Important: The input for the side must be either a number, or an integer from 1-6
    Also, the cube paramater will always be there. Ex: rot_side_l(2, cube)"""
    sideNum-=1
    counter = 0
    #Rotates the entered side by switching the coordinates of the pieces on the side vVv
    for i in range(9):
        cube[sideNum][counter][2] *= -1
        temp = cube[sideNum][counter][1]
        cube[sideNum][counter][1] = cube[sideNum][counter][2]
        cube[sideNum][counter][2] = temp
        counter += 1
    counter = 0
    counter2 = 0
    #determines which side is being rotated with the center color, then changes the 4 adjacent sides correctly vVv
    if(cube[sideNum][4][0] == 'b'):
        tempor = list(cube[5][0])
        tempora = list(cube[5][1])
        temporar = list(cube[5][2])
        counter = 0
        counter2 = 2
        for i in range(3):
            cube[5][counter][0] = cube[3][counter2][0]
            counter+=1
            counter2+=3
        counter = 2
        counter2 = 8
        for i in range(3):
            cube[3][counter][0] = cube[4][counter2][0]
            counter +=3
            counter2-=1
        counter = 6
        counter2 = 0
        for i in range(3):
            cube[4][counter][0] = cube[1][counter2][0]
            counter+=1
            counter2+=3
        cube[1][0][0] = temporar[0]
        cube[1][3][0] = tempora[0]
        cube[1][6][0] = tempor[0]
    elif(cube[sideNum][4][0] == 'w'):
        tempor = list(cube[5][2])
        tempora = list(cube[5][5])
        temporar = list(cube[5][8])
        counter = 2
        counter2 = 2
        for i in range(3):
            cube[5][counter][0] = cube[0][counter2][0]
            counter+=3
            counter2+=3
        counter = 2
        counter2 = 2
        for i in range(3):
            cube[0][counter][0] = cube[4][counter2][0]
            counter+=3
            counter2+=3
        counter = 8
        counter2 = 0
        for i in range(3):
            cube[4][counter][0] = cube[2][counter2][0]
            counter-=3
            counter2+=3
        cube[2][0][0] = temporar[0]
        cube[2][3][0] = tempora[0]
        cube[2][6][0] = tempor[0]
    elif(cube[sideNum][4][0] == 'g'):
        tempor = list(cube[5][6])
        tempora = list(cube[5][7])
        temporar = list(cube[5][8])
        counter = 8
        counter2 = 2
        for i in range(3):
            cube[5][counter][0] = cube[1][counter2][0]
            counter-=1
            counter2+=3
        counter = 0
        counter2 = 2
        for i in range(3):
            cube[1][counter2][0] = cube[4][counter][0]
            counter+=1
            counter2+=3
        counter = 2
        counter2 = 0
        for i in range(3):
            cube[4][counter][0] = cube[3][counter2][0]
            counter-=1
            counter2+=3
        cube[3][0][0] = tempor[0]
        cube[3][3][0] = tempora[0]
        cube[3][6][0] = temporar[0]
    elif(cube[sideNum][4][0] == 'y'):
        tempor = list(cube[5][0])
        tempora = list(cube[5][3])
        temporar = list(cube[5][6])
        counter = 6
        counter2 = 2
        for i in range(3):
            cube[5][counter][0] = cube[2][counter2][0]
            counter-=3
            counter2+=3
        counter = 2
        counter2 = 6
        for i in range(3):
            cube[2][counter][0] = cube[4][counter2][0]
            counter+=3
            counter2-=3
        counter = 0
        counter2 = 0
        for i in range(3):
            cube[4][counter][0] = cube[0][counter2][0]
            counter+=3
            counter2+=3
       
        cube[0][0][0] = tempor[0]
        cube[0][3][0] = tempora[0]
        cube[0][6][0] = temporar[0]
    elif(cube[sideNum][4][0] == 'r'):
        tempor = list(cube[0][0])
        tempora = list(cube[0][1])
        temporar = list(cube[0][2])
        counter = 0
        counter2 = 0
        for i in range(3):
            cube[0][counter][0] = cube[3][counter2][0]
            counter+=1
            counter2+=1
        counter = 0
        counter2 = 0
        for i in range(3):
            cube[3][counter][0] = cube[2][counter2][0]
            counter+=1
            counter2+=1
        counter = 0
        counter2 = 0
        for i in range(3):
            cube[2][counter][0] = cube[1][counter2][0]
            counter+=1
            counter2+=1
        cube[1][0][0] = tempor[0]
        cube[1][1][0] = tempora[0]
        cube[1][2][0] = temporar[0]
    elif(cube[sideNum][4][0] == 'o'):
        tempor = list(cube[3][6])
        tempora = list(cube[3][7])
        temporar = list(cube[3][8])
        counter = 6
        for i in range(3):
            cube[3][counter][0] = cube[0][counter][0]
            counter+=1
        counter=6
        for i in range(3):
            cube[0][counter][0] = cube[1][counter][0]
            counter+=1
        counter = 6
        for i in range(3):
            cube[1][counter][0] = cube[2][counter][0]
            counter+= 1
        cube[2][6][0] = tempor[0]
        cube[2][7][0] = tempora[0]
        cube[2][8][0] = temporar[0]
    fix_variables(sideNum, cube)
    print(sideNum+1, end = '')
    print('l')
    if(autoDo == 1):
        if(sideNum+1 == 1):
            keyboard.press('r')
            keyboard.release('r')
        elif(sideNum+1 == 2):
            keyboard.press('f')
            keyboard.release('f')
        elif(sideNum+1 == 3):
            keyboard.press('l')
            keyboard.release('l')
        elif(sideNum+1 == 4):
            keyboard.press('b')
            keyboard.release('b')
        elif(sideNum+1 == 5):
            keyboard.press('d')
            keyboard.release('d')
        elif(sideNum+1 == 6):
            keyboard.press('u')
            keyboard.release('u')
 
 
    return cube
def auto_get():
    """The intelligent input function, gets input from all of the little cubes on a side,
    assigns coordinates based on what order they were entered, and returns it. Also has a built in input checker.
    The input sequence is already set up."""
    gateChecker = 0
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    six = ''
    seven = ''
    eight = ''
    nine = ''
    side = [one, two, three, four, five, six, seven, eight, nine]
    #checks if input is acceptable vVv
    for i in range(9):
        side[gateChecker] = input('What is the color? ')
        if(side[gateChecker] != 'b' and side[gateChecker] != 'w' and side[gateChecker] != 'g' and side[gateChecker] != 'y' and side[gateChecker] != 'r' and side[gateChecker] != 'o'):
            while(True):
                side[gateChecker] = input('Error, not correct input, please try again: ')
                if(side[gateChecker] == 'b' or side[gateChecker] == 'w' or side[gateChecker] == 'g' or side[gateChecker] == 'y' or side[gateChecker] == 'r' or side[gateChecker] == 'o'):
                    gateChecker += 1
                    break
        else:
            gateChecker += 1
 
    side[0] = [side[0], -1, 1]
    side[1] = [side[1], 0, 1]
    side[2] = [side[2], 1, 1]
    side[3] = [side[3], -1, 0]
    side[4] = [side[4], 0, 0]
    side[5] = [side[5], 1, 0]
    side[6] = [side[6], -1, -1]
    side[7] = [side[7], 0, -1]
    side[8] = [side[8], 1, -1]
    return side
def scramble():
    numScrambles = input(int('How many rotations do you want to use when scrambling? '))
    for i in range(numScrambles):
        scrambleSide = random.randint(1, 6)
        scrambleRL = random.randint(1, 2)
        if(scrambleSide == 1):
            if(scrambleRL == 1):
                keyboard.press('r')
                keyboard.release('r')
            elif(scrambleRL == 2):
                keyboard.press(Key.shift)
                keyboard.press('r')
                keyboard.release('r')
                keyboard.release(Key.shift)
        elif(scrambleSide == 2):
            if(scrambleRL == 1):
                keyboard.press('f')
                keyboard.release('f')
            elif(scrambleRL == 2):
                keyboard.press(Key.shift)
                keyboard.press('f')
                keyboard.release('f')
                keyboard.release(Key.shift)
        elif(scrambleSide == 3):
            if(scrambleRL == 1):
                keyboard.press('l')
                keyboard.release('l')
            elif(scrambleRL == 2):
                keyboard.press(Key.shift)
                keyboard.press('l')
                keyboard.release('l')
                keyboard.release(Key.shift)
        elif(scrambleSide == 4):
            if(scrambleRL == 1):
                keyboard.press('b')
                keyboard.release('b')
            elif(scrambleRL == 2):
                keyboard.press(Key.shift)
                keyboard.press('b')
                keyboard.release('b')
                keyboard.release(Key.shift)
        elif(scrambleSide == 5):
            if(scrambleRL == 1):
                keyboard.press('d')
                keyboard.release('d')
            elif(scrambleRL == 2):
                keyboard.press(Key.shift)
                keyboard.press('d')
                keyboard.release('d')
                keyboard.release(Key.shift)
        elif(scrambleSide == 6):
            if(scrambleRL == 1):
                keyboard.press('u')
                keyboard.release('u')
            elif(scrambleRL == 2):
                keyboard.press(Key.shift)
                keyboard.press('u')
                keyboard.release('u')
                keyboard.release(Key.shift)

if(doScramble == 1):
    scramble()
#Input sequence v
print('Enter the color of each cube on a side starting with the top left, and moving right, then going down a row, like reading a book. When entering the color, only enter in the character the color starts with. Ex: "r"\n')
print('Start with the face that has a blue cube in the middle, and make sure the face on the top has a red middle cube.')
side1 = auto_get()
print_side(side1)
print('\nTurn your cube to the face with a white center, keeping the red center on top.\n')
side2 = auto_get()
print_side(side2)
print('\nTurn your cube to the face with a green center, keeping the red on top.\n')
side3 = auto_get()
print_side(side3)
print('\nTurn your cube to the face with a yellow center, once again keeping the red on the top.\n')
side4 = auto_get()
print_side(side4)
print('\nTurn your cube back to the blue side. Then turn it to the side with the red center, keeping the blue on the bottom.\n')
side5 = auto_get()
print_side(side5)
print('\nLastly, turn your cube to the side with an orange center, and position the blue on the top.\n')
side6 = auto_get()
print_side(side6)
print()
#cube var v
cube = [side1, side2, side3, side4, side5, side6]
 
print('The program will instruct you how to solve your cube with two pieces of information: The side to rotated, and the direction. Ex: 1r for rotating side 1 right. Here is a list of what number the sides are based on the middle color: \nside1 = b')
print('side2 = w')
print('side3 = g')
print('side4 = y')
print('side5 = r')
print('side6 = o')
print('Hit enter to continue')
input('')
if(autoDo == 1):
    time.sleep(5)
"""
      side5
side4 side1 side2 side3  
      side6
side1 = b
side2 = w
side3 = g
side4 = y
side5 = r
side6 = o
 
0 1 2
3 4 5
6 7 8
"""
#Solving! vvv
    #red cross v
crossCurrentSide = 0
crossGoalSide = 2
sideToLeft = 1
sideToRight = 1
checkey = 1
numTillBottom = 0
crossBottomPlace = 1
numBottomRotates = 0
unRotate = 0
#The loop vVv
for i in range(4):
    for i in range(64):
 
        unRotate = 0
        if(cube[crossCurrentSide][checkey][0] == 'r'):
            print(f'running on side {crossCurrentSide + 1}')
            #find number of times needed to rotate the side
            if(checkey == 1):
                numTillBottom = 2
            elif(checkey == 3):
                numTillBottom = 1
            elif(checkey == 5):
                numTillBottom = 3
            elif(checkey  == 7):
                numTillBottom = 0
               
            #rotates the sides based on ^^^
            for k in range(numTillBottom):
                cube = rot_side_l(crossCurrentSide+1, cube)
                unRotate += 1
             
            #finds the place the cube will be rotated to v
            if(crossCurrentSide == 0):
                crossBottomPlace = 1
            elif(crossCurrentSide == 1):
                crossBottomPlace = 5
            elif(crossCurrentSide == 2):
                crossBottomPlace = 7
            elif(crossCurrentSide == 3):
                crossBottomPlace= 3
           
            #finds the side needed to rotate to vVv
            if(cube[5][crossBottomPlace][0] == 'b'):
                crossGoalSide = 1
            elif(cube[5][crossBottomPlace][0] == 'w'):
                crossGoalSide = 2
            elif(cube[5][crossBottomPlace][0] == 'g'):
                crossGoalSide = 3
            elif(cube[5][crossBottomPlace][0] == 'y'):
                crossGoalSide = 4
           
            #finds the side that will be to the left of the goal
            if(crossGoalSide == 1):
                sideToLeft = 4
            else:
                sideToLeft = crossGoalSide - 1
           
            #finds the amount of times that you need to rotate side6
            numBottomRotates = crossGoalSide - (crossCurrentSide+1)
           
            #rotates side 6 based on above
            if(numBottomRotates > 0):
                for g in range(numBottomRotates):
                    cube = rot_side_r(6, cube)
            elif(numBottomRotates < 0):
                for g in range(numBottomRotates * -1):
                    cube = rot_side_l(6, cube)
           
            #Resets original side just in case
            if(crossGoalSide != crossCurrentSide+1):
                for m in range(unRotate):
                    cube = rot_side_r(crossCurrentSide+1, cube)
           
            #The final positioning algorithm vVv
            cube = rot_side_r(crossGoalSide, cube)
            cube = rot_side_r(5, cube)
            cube = rot_side_l(sideToLeft, cube)
            cube = rot_side_l(5, cube)
           
            #part of the checker loop vVv
        elif(checkey >= 7 and crossCurrentSide < 3):
            checkey = 1
            crossCurrentSide += 1
        elif(checkey >= 7 and crossCurrentSide >= 3):
            crossCurrentSide = 0
        else:
            checkey+=2
    #Getting pieces from side 6 to the cross vVv
    for i in range(4):
        bottomCheckey = 1
        bottomCorrespondingSide = 0
        for y in range(4):
            if(cube[5][bottomCheckey][0] == 'r'):
                   
                #finds the side that goes with where the checker is vVv
                if(bottomCheckey == 1):
                    bottomCorrespondingSide = 0
                elif(bottomCheckey == 3):
                    bottomCorrespondingSide = 3
                elif(bottomCheckey == 5):
                    bottomCorrespondingSide = 1
                elif(bottomCheckey == 7):
                    bottomCorrespondingSide = 2
 
                #finds the side that the piece has to go to vvv
                if(cube[bottomCorrespondingSide][7][0] == 'b'):
                    bottomCrossGoal = 1
                elif(cube[bottomCorrespondingSide][7][0] == 'w'):
                    bottomCrossGoal = 2
                elif(cube[bottomCorrespondingSide][7][0] == 'g'):
                    bottomCrossGoal = 3
                elif(cube[bottomCorrespondingSide][7][0] == 'y'):
                    bottomCrossGoal = 4
                   
                #roughly finds bottom rotates.
                numBottomRotates2 = bottomCrossGoal - (bottomCorrespondingSide+1)
 
                #rotates based on ^
                if(numBottomRotates2 > 0):
                    for g in range(numBottomRotates2):
                        cube = rot_side_r(6, cube)
                elif(numBottomRotates2 < 0):
                    for g in range(numBottomRotates2 * -1):
                        cube = rot_side_l(6, cube)
 
                #rotates the goal side to get the red piece on the top vVv
               
                for t in range(2):
                    cube = rot_side_r(bottomCrossGoal, cube)
 
            else:
                bottomCheckey += 2
 
if(autoDo != 1):    
    input('Hit enter when you are done')
   
           
    #Red corners vVv
cornerSideCheck = 0
cornerChecker = 0
cornerGoalSide = 1
numBottomRotates3 = 0
cornerSideToRight = 2
for i in range(4):
    for p in range(48):
        #checking system vVv
        if(cube[cornerSideCheck][cornerChecker][0] == 'r'):
            print(f'running on side {cornerSideCheck+1}')
            if(cornerChecker == 0):
               
                #calculates the side to the left vVv
                if((cornerSideCheck+1) == 1):
                    cornerSideToLeft = 4
                else:
                    cornerSideToLeft = cornerSideCheck
               
                #puts the red on the bottom to be taken care of by the other functions
                cube = rot_side_r(cornerSideToLeft, cube)
                cube = rot_side_l(6, cube)
                cube = rot_side_l(cornerSideToLeft, cube)
                   
            elif(cornerChecker == 2):
                #calculates the side to the right vVv
                if(cornerSideCheck+1 == 4):
                    cornerSideToRight = 1
                else:
                    cornerSideToRight = cornerSideCheck + 2
               
                #positions the cube similarly to above
                cube = rot_side_l(cornerSideToRight, cube)
                cube = rot_side_r(6, cube)
                cube = rot_side_r(cornerSideToRight, cube)
               
               
            elif(cornerChecker == 6):
                #sets the place to look at on the bottom vVv
                if(cornerSideCheck == 0):
                    cornerBottomCheck = 0
                elif(cornerSideCheck == 1):
                    cornerBottomCheck = 2
                elif(cornerSideCheck == 2):
                    cornerBottomCheck = 8
                elif(cornerSideCheck == 3):
                    cornerBottomCheck = 6
                   
                #Looks at that piece^ and sets the goal side vVv
                if(cube[5][cornerBottomCheck][0] == 'b'):
                    cornerGoalSide = 1
                elif(cube[5][cornerBottomCheck][0] == 'w'):
                    cornerGoalSide = 2
                elif(cube[5][cornerBottomCheck][0] == 'g'):
                    cornerGoalSide = 3
                elif(cube[5][cornerBottomCheck][0] == 'y'):
                    cornerGoalSide = 4
               
                #finds the side that will be to right of the goal side vVv
                if(cornerGoalSide == 1):
                    cornerSideToLeft = 4
                else:
                    cornerSideToLeft = cornerGoalSide - 1
                   
                #calculates how many times the bottom side has to be rotated vVv
                cornerBottomRot = (cornerGoalSide - (cornerSideCheck))
                   
                #rotates based on^ vVv
                if(cornerBottomRot > 0):
                    for g in range(cornerBottomRot):
                        cube = rot_side_r(6, cube)
                elif(cornerBottomRot < 0):
                    for g in range(cornerBottomRot * -1):
                        cube = rot_side_l(6, cube)
               
                #puts the red on top vVv
                cube = rot_side_r(cornerSideToLeft, cube)
                cube = rot_side_l(6, cube)
                cube = rot_side_l(cornerSideToLeft, cube)
               
                   
            elif(cornerChecker == 8):
                #sets the place to look at on the bottom
                if(cornerSideCheck == 0):
                    cornerBottomCheck = 2
                elif(cornerSideCheck == 1):
                    cornerBottomCheck = 8
                elif(cornerSideCheck == 2):
                    cornerBottomCheck = 6
                elif(cornerSideCheck == 3):
                    cornerBottomCheck = 0
               
                #Looks at that piece^ and sets the goal side vVv
                if(cube[5][cornerBottomCheck][0] == 'b'):
                    cornerGoalSide = 1
                elif(cube[5][cornerBottomCheck][0] == 'w'):
                    cornerGoalSide = 2
                elif(cube[5][cornerBottomCheck][0] == 'g'):
                    cornerGoalSide = 3
                elif(cube[5][cornerBottomCheck][0] == 'y'):
                    cornerGoalSide = 4
               
                #finds the side that will be to right of the goal side vVv
                if(cornerGoalSide == 4):
                    cornerSideToRight = 1
                else:
                    cornerSideToRight = cornerGoalSide + 1
               
               
                #calculates how many times the bottom side has to be rotated vVv
                cornerBottomRot = cornerGoalSide - (cornerSideCheck + 1)
               
                #rotates based on^ vVv
                if(cornerBottomRot > 0):
                    for g in range(cornerBottomRot):
                        cube = rot_side_r(6, cube)
                elif(cornerBottomRot < 0):
                    for g in range(cornerBottomRot * -1):
                        cube = rot_side_l(6, cube)
               
                #places the red side on the top vVv
                cube = rot_side_l(6, cube)
                cube = rot_side_l(cornerSideToRight, cube)
                cube = rot_side_r(6, cube)
                cube = rot_side_r(cornerSideToRight, cube)
               
        elif(cornerSideCheck >= 3 and cornerChecker >= 8):
            cornerSideCheck = 0
            cornerChecker = 0
        elif(cornerChecker >= 8):
            cornerChecker = 0
            cornerSideCheck +=1
        elif(cornerChecker == 2):
            cornerChecker = 6            
        else:
            cornerChecker +=2
   
    cornerBottomGoal = 1
    cornerBottomChecker = 0
    cornerBottomSide= 0
    numBottomRotates3 = 0
    cornerBottomRight = 0
    #Getting corner pieces from the bottom vVv
    for j in range(8):
        cornerBottomGoal = 0
        cornerBottomSide= 0
        numBottomRotates3 = 0
        cornerBottomRight = 0
        if(cube[5][cornerBottomChecker][0] == 'r'):
            print('Running on side 6')
            #senses what spot to sense to find the goal
            if(cornerBottomChecker == 0):
                cornerBottomSide = 0
            elif(cornerBottomChecker == 2):
                cornerBottomSide = 1
            elif(cornerBottomChecker == 6):
                cornerBottomSide = 3
            elif(cornerBottomChecker == 8):
                cornerBottomChecker = 2
           
            #finds the goal side vVv
            if(cube[cornerBottomSide][6][0] == 'b'):
                cornerBottomGoal = 1
            elif(cube[cornerBottomSide][6][0] == 'w'):
                cornerBottomGoal = 2
            elif(cube[cornerBottomSide][6][0] == 'g'):
                cornerBottomGoal = 3
            elif(cube[cornerBottomSide][6][0] == 'y'):
                cornerBottomGoal = 4
 
            #finds how much side 6 has to be roated vVv
            numBottomRotates3 = (cornerBottomGoal - cornerBottomSide)
           
            #rotates 6 vvv
           
            if(numBottomRotates3 > 0):
                for i in range(numBottomRotates3):
                    cube = rot_side_r(6, cube)
            elif(numBottomRotates3 < 0):
                for i in range(numBottomRotates3):
                    cube = rot_side_l(6, cube)
           
            #finds the side that will be to the right vvv
           
            if(cornerBottomGoal == 4):
                cornerBottomRight = 1
            else:
                cornerBottomRight = cornerBottomGoal+1
           
            #puts it on side 5 vvv
           
            cube = rot_side_l(cornerBottomRight, cube)
            cube = rot_side_l(6, cube)
            cube = rot_side_l(6, cube)
            cube = rot_side_r(cornerBottomRight, cube)
            cube = rot_side_r(6, cube)
            cube = rot_side_l(cornerBottomRight, cube)
            cube = rot_side_l(6, cube)
            cube = rot_side_r(cornerBottomRight, cube)
           
            #adds to checker
            if(cornerBottomChecker == 2):
                cornerBottomChecker = 6
            else:
                cornerBottomChecker += 2
 
 
 
 
 
 


