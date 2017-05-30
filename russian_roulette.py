import robot_helper
import turtle
import random
import math

PHI = 360 / 7	# Сектор от окружности. 306 градусов полная окружность, 7 секторов всего.
R = 50

def gotoxy(tortoise, x, y):
	tortoise.penup()
	tortoise.goto(x, y)
	tortoise.pendown()

def draw_circle(tortoise, r, color):
	tortoise.fillcolor(color)
	tortoise.begin_fill()
	tortoise.circle(r)
	tortoise.end_fill()

def draw_cylinder(tortoise, base_x, base_y):
	gotoxy(tortoise, base_x, base_y)	# Основной круг
	tortoise.circle(80)
	gotoxy(tortoise, base_x, base_y + 160)	# Рисуем мушку
	draw_circle(tortoise, 5, 'red')
	# Рисуем барабан
	for i in range(0, 7):
		phi_rad = PHI * i * math.pi / 180.0
		gotoxy(tortoise, base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 58)
		draw_circle(tortoise, 22, "white")

def draw_cylinder_spinning(tortoise, start, base_x, base_y):
	for i in range(start, random.randrange(7, 10)):
		phi_rad = PHI * i * math.pi / 180.0
		gotoxy(tortoise, base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 58)
		draw_circle(tortoise, 22, "brown")
		draw_circle(tortoise, 22, "white")

	gotoxy(tortoise, base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 58)
	draw_circle(tortoise, 22, "brown")

	return i

gun_turtle = turtle.Turtle()
gun_turtle.speed(0) # max speed - instant drawing

draw_cylinder(gun_turtle, 100, 100)

answer = ''
start = 0
text = turtle.Turtle()
while answer != 'N':
	answer = turtle.textinput("Wanna play?", "Y/N")
	if answer == 'Y':
		text.clear()
		pos = draw_cylinder_spinning(gun_turtle, start, 100, 100)

		start = pos % 7
		if start == 0:
			gotoxy(text, -150, 250)
			text.write("WASTED!", font=("Arial", 18, "bold"))
			random_punishment_number = random.randrange(0, 3)
			if random_punishment_number == 0:
				robot_helper.random_delete('test')
			elif random_punishment_number == 1:
				robot_helper.duplicate_files('test')
			else:
				gotoxy(text, -100, -50)
				print("YOU WERE LUCKY THIS TIME!")
	else:
		pass
