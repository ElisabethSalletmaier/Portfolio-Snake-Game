from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Snake:
    """this class creates the snake"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        """ this function gets rid of the old long snake -> brings it to a place outside the screen and creates again a new short one"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()   # all the segments of the snake will be deleted
        self.create_snake()     # creates new snake
        self.head = self.segments[0]

    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.segments[-1].position()) # starts at the end of the list(last element)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):  # start, stop, step
            """moving one segment of the snake after each other and taking the screen position of the former segment"""
            """ this means: only segment 1 changes directions and the other segments only follow"""
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto([new_x, new_y])
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


class Food(Turtle):
    """this class creates the food for the snake"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


class Scoreboard(Turtle):
    """this class creates the scoreboard for the game"""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        """this function saves the highest score in a text file"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increase_scores(self):
        self.score += 1
        self.update_scoreboard()
