from colorama import Back

class tile():
    def __init__(self) -> None:
        self.type = "blank"

    def __repr__(self) -> str:
        #this is to shorten it down to 1 char
        if self.type == "blank":
            return "/"
        else:
            return self.type[0]
    
    def __str__(self) -> str:
        #this is to shorten it down to 1 char
        if self.type == "blank":
            return "/"
        else:
            return self.type[0]
        
    def changetype(self, color):
        self.type = color

def setup():
    toadd = []
    tilearray = []
    for i in range(20):
        for j in range(20):
            toadd.append(tile())
        tilearray.append(toadd)
        toadd = []

    return tilearray

def go(color):
    x = input("whats your x: ")
    y = input("whats your y: ")
    tilearray[int(y)-1][int(x)-1].changetype(color)

def switchgo(ccolor):
    if ccolor == "red":
        color = "green"
    if ccolor == "green":
        color = "yellow"
    if ccolor == "yellow":
        color = "blue"
    if ccolor == "blue":
        color = "red"
    return color

def niceprint(array):
    for i in array:
        toprint = ""
        for j in i:
            #find color to print with
            if j.type == "red":
                color = Back.RED
            if j.type == "green":
                color = Back.GREEN
            if j.type == "yellow":
                color = Back.YELLOW
            if j.type == "blue":
                color = Back.BLUE
            if j.type == "blank":
                color = Back.RESET
                

            #add to str
            toprint = toprint+(color + str(j) + Back.RESET ) #reset to handle printing over lines over the board
        print(toprint)

currentcolor = "red"
tilearray = setup()
go(currentcolor)
currentcolor = switchgo(currentcolor)
niceprint(tilearray)


print(Back.RESET)        