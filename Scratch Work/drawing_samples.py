# Import the "arcade" library
import arcade
arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.PINK)
arcade.draw_rectangle_filled(100, 320, 30, 120, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 350, 45, arcade.csscolor.DARK_RED)
arcade.draw_text("Саня, ты где?", 150, 230,
                 arcade.color.BLACK, 24)
arcade.finish_render()
arcade.run()