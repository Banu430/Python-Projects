import tkinter as tk
# creating a GUI
import random
# importing random posistions for snake food

# Game settings
GAME_WIDTH = 400
GAME_HEIGHT = 400
SPACE_SIZE = 20
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
#constraints of the game


class SnakeGame:
    def __init__(self):
        #game window
        self.window = tk.Tk()
        self.window.title("Simple Snake Game")
        self.window.resizable(False, False)

        self.score = 0
        #score label
        self.direction = 'down'
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food_position = self.place_food()

        self.canvas = tk.Canvas(self.window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.canvas.pack()
        #creating a game canvas

        self.label = tk.Label(self.window, text=f"Score: {self.score}", font=('Arial', 20))
        self.label.pack()
        
        #game controls
        self.window.bind('<Left>', lambda event: self.change_direction('left'))
        self.window.bind('<Right>', lambda event: self.change_direction('right'))
        self.window.bind('<Up>', lambda event: self.change_direction('up'))
        self.window.bind('<Down>', lambda event: self.change_direction('down'))
        #creating Directions

        self.update_game()
        self.window.mainloop()
        

    def place_food(self):
        #generating random positions
        
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        return (x, y)
        

    def update_game(self):
        #update game according to snake position
        
        head_x, head_y = self.snake[0]

        if self.direction == 'up':
            head_y -= SPACE_SIZE
        elif self.direction == 'down':
            head_y += SPACE_SIZE
        elif self.direction == 'left':
            head_x -= SPACE_SIZE
        elif self.direction == 'right':
            head_x += SPACE_SIZE

        # Insert new head position
        new_head = (head_x, head_y)
        
        # Check for collisions with food
        if new_head == self.food_position:
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            self.food_position = self.place_food()
        else:
            # Remove last segment of the snake if not eating food
            self.snake.pop()

        # Check for collisions with walls or itself
        if (head_x < 0 or head_x >= GAME_WIDTH or 
                head_y < 0 or head_y >= GAME_HEIGHT or 
                new_head in self.snake):
            self.game_over()
            return

        # Update snake position
        self.snake.insert(0, new_head)
        
        # Redraw the game elements
        self.draw_elements()
        
        # Call this method again after a delay
        self.canvas.after(100, self.update_game)
        

    def draw_elements(self):
        # Clear canvas
        self.canvas.delete(tk.ALL)
        
        # Draw snake segments
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

        # Draw food
        food_x, food_y = self.food_position
        self.canvas.create_oval(food_x, food_y, food_x + SPACE_SIZE, food_y + SPACE_SIZE, fill=FOOD_COLOR)
        

    def change_direction(self, new_direction):
        opposite_directions = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction
            

    def game_over(self):
        self.canvas.delete(tk.ALL)
        
        self.canvas.create_text(GAME_WIDTH//2, GAME_HEIGHT//2,
                                text="GAME OVER", fill="red", font=('Arial', 30))


if __name__ == "__main__":
    SnakeGame()
