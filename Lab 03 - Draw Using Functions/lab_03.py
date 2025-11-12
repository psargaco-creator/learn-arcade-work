import math
import arcade

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

def main():
    initialise()

    arcade.schedule(on_draw, 1/60)
    arcade.run()


def finish():
    arcade.finish_render()
    arcade.run()

def initialise():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    
def draw_snowman(x: int, y: int):
    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snowman
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

def draw_grass():
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 3, arcade.color.WHITE_SMOKE)

def draw_sky():
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, SCREEN_HEIGHT, arcade.color.DARK_BLUE)

def on_draw(delta_time):
    # Draw the ground
    #self.clear()
    arcade.set_background_color(arcade.color.DARK_BLUE)
    draw_sky()
    draw_grass()

    # Draw a snow person

    draw_snowman(140, 50)
    draw_snowman(200+on_draw.snow_person1_x, 100)

    on_draw.snow_person1_x += 1

# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 150

main()