from manim import *


class QuadraticFormula(Scene):
    def construct(self):
        eq1 = MathTex("ax^2 + bx + c = 0", font_size=72)
        eq2 = MathTex("4a^2x^2 + 4abx + 4ac = 0", font_size=72)
        eq3 = MathTex("4a^2x^2 + bx + b^2 = b^2 - 4ac", font_size=72)
        eq4 = MathTex("(2ax + b)^2 = b^2 - 4ac", font_size=72)
        eq5 = MathTex("2ax + b = \\pm \\sqrt{b^2 - 4ac}", font_size=72)
        eq6 = MathTex("x =\\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}", font_size=72)
        self.play(Write(eq1))
        self.wait(1)
        self.play(TransformMatchingShapes(eq1, eq2))
        self.wait(0.5)
        self.play(TransformMatchingShapes(eq2, eq3))
        self.wait(0.5)
        self.play(TransformMatchingShapes(eq3, eq4))
        self.wait(0.5)
        self.play(TransformMatchingShapes(eq4, eq5))
        self.wait(0.5)
        self.play(TransformMatchingShapes(eq5, eq6))
        self.wait(2)
