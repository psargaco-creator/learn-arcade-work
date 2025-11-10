"""
Example of
multiline comments
"""

import arcade

# background
arcade.open_window(600, 600, "Drawing example")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()

# grass
arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, arcade.csscolor.GREEN)

# Tree 1
arcade.draw_rect_filled(arcade.XYWH(100, 320, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# Tree 2
arcade.draw_rect_filled(arcade.XYWH(200, 300, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(170, 300, 230, 300, 200, 400, arcade.csscolor.DARK_GREEN)
arcade.draw_rect_outline(arcade.XYWH(300, 300, 350, 200), arcade.csscolor.BLACK,3)

r = 0
g = 0
b = 0
g_true = False
b_true = False
for angle in range(360):
    arcade.draw_ellipse_outline(300, 300, 350, 200, (r, g, b), 3, angle*10)
    if not(g_true and b_true):
        r = angle*10        
    if r >= 255:
        r = 255
        g_true = True
        if not(b_true and g < 255):
            g = angle*10
            if g > 255:
                g = 255
        else:
            g = 255
            b_true = True
    if g == 255:
        b = angle*10
        if b >= 255:
            b = 255

text_ob = arcade.text.Text("Plant a tree", 250, 50, arcade.csscolor.GOLD,font_size=24)
text_ob.draw()
arcade.finish_render()
arcade.run()




