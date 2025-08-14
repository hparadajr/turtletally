import turtle
screen = turtle.Screen()
turtle.speed(0)
tallyturtle = turtle.Turtle()

def validnum():
    while True:
        try:
            num = int(input("Please enter a number of tally marks between 1-100: "))
            if 1 <= num <= 100:
                return num
            else:
                print("Enter a number between 1 and 100.")
        except ValueError:
            print("INVALID INPUT")


def tallymark(num):
    xstart = -300
    ystart = 200
    x = xstart
    y = ystart

    group_count = 0
    while group_count < num:
        for i in range(5): 
            if group_count < num:
                if i < 4:
                    tallyturtle.penup()
                    tallyturtle.goto(x + i * 10, y)
                    tallyturtle.pendown()
                    tallyturtle.setheading(90)
                    tallyturtle.forward(50)
                else:
                    tallyturtle.penup()
                    tallyturtle.goto(x, y)
                    tallyturtle.pendown()
                    tallyturtle.setheading(45)
                    tallyturtle.forward(70)
    
                group_count += 1
        x += 60  
    
        if group_count % 20 == 0:
            x = xstart
            y -= 70  

num = validnum()
tallymark(num)
print("ALL DONE!")
