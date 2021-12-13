import sys
file1 = sys.argv[1]
file2 = sys.argv[2]
health = int(sys.argv[3])
file3 = sys.argv[4]
maze = []
f2 = open(file3, "a")
def mazeopen():
    f = open(file1, 'r')
    lines = f.readlines()
    global maze
    maze = [list(i.strip()) for i in lines]
mazeopen()

def start_point():
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S":
                return i,j
a = []
a.append(start_point())


def move(row,col):

    if maze[row][col] == "F":

        return True
    elif maze[row][col] == "W":

        return False
    elif maze[row][col] == "0":

        return False

    maze[row][col] = "0"

    if ((row < len(maze)-1 and move(row+1, col))
        or (col > 0 and move(row, col-1))
        or (row > 0 and move(row-1, col))
        or (col < len(maze[0])-1 and move(row, col+1))):
        maze[row][col] = "1"

        return True

    return False
move(a[0][0],a[0][1])

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "W":
            maze[i][j] = "0"
        if maze[i][j] == "P":
            maze[i][j] = "0"
maze[a[0][0]][a[0][1]] = "S"

for i in maze:
    f2.write(', '.join(i))
    f2.write("\n")
f2.write("\n")
maze2 = []
k = 0
l = 0
def mazeopen2():
    f = open(file2, 'r')
    lines = f.readlines()
    global maze2
    maze2 = [list(i.strip()) for i in lines]
mazeopen2()

def start_point():
    for i in range(len(maze2)):
        for j in range(len(maze2[0])):
            if maze2[i][j] == "S":
                return i,j
a2 = []
a2.append(start_point())


def move2(row,col):
    global health
    global k
    global l

    if maze2[row][col] == "F":
        return True
    elif maze2[row][col] == "W":
        return False
    elif maze2[row][col] == "0":
        return False

    if maze2[row][col] == "H" and health >= -1:
        health = int(sys.argv[3])

    health -= 1
    k += 1

    maze2[row][col] = "0"

    if ((row < len(maze2)-1 and move2(row+1, col))
        or (col > 0 and move2(row, col-1))
        or (row > 0 and move2(row-1, col))
        or (col < len(maze2[0])-1 and move2(row, col+1))):

        maze2[row][col] = "1"
        l +=1
        return True

    return False

move2(a2[0][0],a2[0][1])

for i in range(len(maze2)):
    for j in range(len(maze2[0])):
        if maze2[i][j] == "W":
            maze2[i][j] = "0"
        if maze2[i][j] == "P":
            maze2[i][j] = "0"
maze2[a2[0][0]][a2[0][1]] = "S"

if k-l+health <= -1:
    f2.write("No health")
else:
    for i in maze2:
        f2.write(', '.join(i))
        f2.write("\n")


