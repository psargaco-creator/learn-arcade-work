import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Drawing with Functions"

class GameView(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

    def setup(self):
        self.background_color = arcade.color.DARK_BLUE

        self.on_draw.snow_person1_x = 150
        # Call on_draw every 60th of a second.
        

    def draw_grass(self):
        """ Draw the ground """
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 3, arcade.color.AIR_SUPERIORITY_BLUE)


    def draw_snow_person(self, x, y):
        """ Draw a snow person """

        # Draw a point at x, y for reference
        arcade.draw_point(x, y, arcade.color.RED, 5)

        # Snow
        arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
        arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
        arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

        # Eyes
        arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


    def on_draw(self, delta_time):
        self.clear()

        """ Draw everything """
        self.draw_grass()
        self.draw_snow_person(self.on_draw.snow_person1_x, 140)
        self.draw_snow_person(450, 180)

        # Add one to the x value, making the snow person move right
        # Negative numbers move left. Larger numbers move faster.
        self.on_draw.snow_person1_x += 1

def main():
    window = GameView()
    window.setup()
    arcade.schedule(window.on_draw, 1/60)
    arcade.run()
    

# Call the main function to get the program started.
if __name__ == "__main__":
    main()