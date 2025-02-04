from manim import *


class QuadraticFormula(Scene):
    def construct(self):
        equations = [
            MathTex(
                "ax^2 + bx + c = 0",
                font_size=72,
                substrings_to_isolate=["a", "b", "c", "x"],
            ).set_color_by_tex_to_color_map(
                {"x": GOLD, "a": RED, "b": BLUE, "c": GREEN}
            ),
            MathTex(
                "4a^2x^2 + 4abx + 4ac = 0",
                font_size=72,
                substrings_to_isolate=["a", "b", "c", "x"],
            ).set_color_by_tex_to_color_map(
                {"x": GOLD, "a": RED, "b": BLUE, "c": GREEN}
            ),
            MathTex(
                "4a^2x^2 + bx + b^2 = b^2 - 4ac",
                font_size=72,
                substrings_to_isolate=["a", "b", "c", "x"],
            ).set_color_by_tex_to_color_map(
                {"x": GOLD, "a": RED, "b": BLUE, "c": GREEN}
            ),
            MathTex(
                "(2ax + b)^2 = b^2 - 4ac",
                font_size=72,
                substrings_to_isolate=["a", "b", "c", "x"],
            ).set_color_by_tex_to_color_map(
                {"x": GOLD, "a": RED, "b": BLUE, "c": GREEN}
            ),
            MathTex(
                "2ax + b = \\pm \\sqrt{b^2 - 4ac}",
                font_size=72,
                substrings_to_isolate=["a", "b", "c", "x", "\\sqrt"],
            ).set_color_by_tex_to_color_map(
                {"x": GOLD, "a": RED, "b": BLUE, "c": GREEN, "\\sqrt": WHITE}
            ),
            MathTex("x =\\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}", font_size=72),
        ]

        def transform_equations(equations, wait_time=0.5):
            for i in range(len(equations) - 1):
                self.play(TransformMatchingShapes(equations[i], equations[i + 1]))
                self.wait(wait_time)

        self.play(Write(equations[0]))
        self.wait(1)
        transform_equations(equations)
        self.wait(2)
