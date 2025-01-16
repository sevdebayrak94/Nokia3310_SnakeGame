from turtle import Turtle
Starting_positions = [(0,0), (-20,0), (-40,0)]
Move_distance = 20
Up = 90
Down = 270
Left = 180
Right = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for positions in Starting_positions:
           self.add_segment(positions)

    def add_segment(self, positions):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(positions)
        self.segments.append(snake)
    def extent(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(Move_distance)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(0)
