import turtle

turtle.reset()

turtle.speed(10000)


def TriangleRec(pos_X, pos_Y, pos_X2, pos_Y2, pos_X3, pos_Y3, count):
    if count > 0:
        new_pos_X1 = (pos_X + pos_X2) // 2

        new_pos_Y1 = (pos_Y + pos_Y2) // 2

        new_pos_X2 = (pos_X2 + pos_X3) // 2

        new_pos_Y2 = (pos_Y2 + pos_Y3) // 2

        new_pos_X3 = (pos_X3 + pos_X) // 2

        new_pos_Y3 = (pos_Y3 + pos_Y) // 2

        turtle.pu()

        turtle.goto(new_pos_X3, new_pos_Y3)

        turtle.pd()

        turtle.goto(new_pos_X1, new_pos_Y1)

        turtle.goto(new_pos_X2, new_pos_Y2)

        turtle.goto(new_pos_X3, new_pos_Y3)

        TriangleRec(pos_X, pos_Y, new_pos_X1, new_pos_Y1, new_pos_X3, new_pos_Y3, count - 1)

        TriangleRec(pos_X2, pos_Y2, new_pos_X1, new_pos_Y1, new_pos_X2, new_pos_Y2, count - 1)

        TriangleRec(pos_X3, pos_Y3, new_pos_X3, new_pos_Y3, new_pos_X2, new_pos_Y2, count - 1)


pos_x = 20

pos_y = -200

pos_x2 = 339

pos_y2 = 279

pos_x3 = -300

pos_y3 = 279

count = 4

turtle.pu()

turtle.speed(1)

turtle.goto(pos_x, pos_y)

turtle.pd()

turtle.goto(pos_x2, pos_y2)

turtle.goto(pos_x3, pos_y3)

turtle.goto(pos_x, pos_y)

TriangleRec(pos_x, pos_y, pos_x2, pos_y2, pos_x3, pos_y3, count);

turtle.exitonclick()