"""
Example of 
multiline comments
"""

import arcade

arcade.open_window(600, 600, "Drawing example")

arcade.set_background_color((230, 60, 120, 8))
arcade.start_render()
arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, arcade.csscolor.GREEN)
arcade.draw_rect_filled(arcade.XYWH(100, 320, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

arcade.finish_render()

arcade.run()
