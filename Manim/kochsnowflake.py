from manim import *


class KochSnowflake(Scene):
    def construct(self):
        # Define the Koch curve function
        def koch_curve(iterations, length=5):
            # Calculate the initial segment length based on the number of iterations
            segment_length = length / (3**iterations)

            # Create the base line segment
            line_group = Line().set_length(segment_length)

            # Function to generate the next level of the Koch curve
            def next_level(line_group):
                return VGroup(
                    *[line_group.copy().rotate(i) for i in [0, -PI / 3, PI / 3, 0]]
                ).arrange(RIGHT, buff=0, aligned_edge=UP)

            # Recursively generate the Koch curve for the specified number of iterations
            for _ in range(iterations):
                line_group = next_level(line_group)

            # Create the three parts of the Koch snowflake
            part_1 = (
                VMobject(stroke_width=2)
                .set_points(line_group.get_all_points())
                .set_color(YELLOW)
            )
            part_2 = (
                part_1.copy()
                .rotate(2 * PI / 3, about_point=part_1.get_start())
                .shift(length * RIGHT)
            )
            part_3 = (
                part_1.copy()
                .rotate(-2 * PI / 3, about_point=part_1.get_end())
                .shift(length * LEFT)
            )
            return VGroup(part_1, part_2, part_3)

        # Initialize the Koch snowflake with 0 iterations (triangle)
        koch_snowflake = koch_curve(0).to_edge(UP).shift(DOWN)

        # Fade in the initial snowflake
        self.play(FadeIn(koch_snowflake))

        # Animate the snowflake through multiple iterations
        evolution_iterations = 4
        for i in range(1, evolution_iterations + 1):
            self.play(
                koch_snowflake.animate.become(koch_curve(i)).to_edge(UP).shift(DOWN)
            )

        # Wait before ending the animation
        self.wait(1)
