from manim import *

class Swastika(Scene):
    def construct(self):
        rect = Rectangle(width=7, height=4.2, color=RED, fill_color="#dd0000", fill_opacity=1) 
        circle = Circle(color=WHITE, fill_color=WHITE, fill_opacity=1, radius=1.75)
        arm1 = Line(start=[1, 1, 0], end=[0, 1, 0], color=BLACK, stroke_width=40)
        arm2 = Line(start=[0, -1, 0], end=[-1, -1, 0], color=BLACK, stroke_width=40)
        arm3 = Line(start=[-1, 1, 0], end=[-1, 0, 0], color=BLACK, stroke_width=40)
        arm4 = Line(start=[1, 0, 0], end=[1, -1, 0], color=BLACK, stroke_width=40)
        bodyvert = Line(start=[0, 1.2, 0], end=[0, -1.2, 0], color=BLACK, stroke_width=40)
        bodyhoriz = Line(start=[-1.2, 0, 0], end=[1.2, 0, 0], color=BLACK, stroke_width=40)
        swastika = VGroup(arm1, bodyvert, arm2, arm3, bodyhoriz, arm4).rotate(PI / 4)
        self.play(DrawBorderThenFill(rect), DrawBorderThenFill(circle), FadeIn(swastika), run_time=2)
