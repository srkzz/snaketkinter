from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 40
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Comida:

    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="comida")


def create_button(self):
    button = tk.Button(self, text='New Game', command=lambda: self.new_game())
    button.place(relx=0.1, rely=0.10, anchor="center")

 # Function for game restart
 def new_game(self):
    self.make_GUI()
    self.start_game()

def jogar_again():
    Comida()
    Snake()


def prox_curva(snake, comida):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == comida.coordinates[0] and y == comida.coordinates[1]:

        global score

        score += 1

        label.config(text="Resultado:{}".format(score))

        canvas.delete("comida")

        comida = Comida()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if ver_col(snake):
        game_over()

    else:
        window.after(SPEED, prox_curva, snake, comida)


def mudar_dir(nova_dir):
    global direction

    if nova_dir == 'left':
        if direction != 'right':
            direction = nova_dir
    elif nova_dir == 'right':
        if direction != 'left':
            direction = nova_dir
    elif nova_dir == 'up':
        if direction != 'down':
            direction = nova_dir
    elif nova_dir == 'down':
        if direction != 'up':
            direction = nova_dir


def ver_col(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for pedaco in snake.coordinates[1:]:
        if x == pedaco[0] and y == pedaco[1]:
            return True

    return False

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2, font=('consolas', 70), text="GAME OVER",
                       fill="red", tags="GameOver")


window = Tk()
window.title("Snake Game")
window.resizable(False, False)
score = 0
direction = 'down'
label = Label(window, text="Resultado:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_height()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: mudar_dir('left'))
window.bind('<Right>', lambda event: mudar_dir('right'))
window.bind('<Up>', lambda event: mudar_dir('up'))
window.bind('<Down>', lambda event: mudar_dir('down'))

snake = Snake()
comida = Comida()

prox_curva(snake, comida)

window.mainloop()
