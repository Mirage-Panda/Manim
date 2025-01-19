from manim import *


class KochSnowflake(Scene):
    def construct(self):
        def KochCurve(n, length=5):
            l = length / (3**n)
            LineGroup = Line().set_length(l)

            def NextLevel(LineGroup):
                return VGroup(
                    *[LineGroup.copy().rotate(i) for i in [0, -PI / 3, PI / 3, 0]]
                ).arrange(RIGHT, buff=0, aligned_edge=UP)

            for _ in range(n):
                LineGroup = NextLevel(LineGroup)
            KC1 = (
                VMobject(stroke_width=2)
                .set_points(LineGroup.get_all_points())
                .set_color(YELLOW)
            )
            KC2 = (
                KC1.copy()
                .rotate(2 * PI / 3, about_point=KC1.get_start())
                .shift(length * RIGHT)
            )
            KC3 = (
                KC1.copy()
                .rotate(-2 * PI / 3, about_point=KC1.get_end())
                .shift(length * LEFT)
            )
            return VGroup(KC1, KC2, KC3)

        kc = KochCurve(0).to_edge(UP).shift(DOWN)
        self.add(kc)
        for i in range(1, 4):
            self.play(kc.animate.become(KochCurve(i)).to_edge(UP).shift(DOWN))
        self.wait(3)
