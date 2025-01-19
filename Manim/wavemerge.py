from manim import *


class WaveMerge(Scene):
    def construct(self):
        # define axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": WHITE, "stroke_width": 2, "include_tip": False},
        )

        # Define sine waves with different frequencies
        wave1 = axes.plot(lambda x: np.sin(2 * PI * x), color=RED, stroke_width=3)
        wave2 = axes.plot(
            lambda x: 0.5 * np.sin(4 * PI * x), color=GREEN, stroke_width=3
        )
        wave3 = axes.plot(
            lambda x: 0.25 * np.sin(8 * PI * x) + 1, color=YELLOW_D, stroke_width=3
        )
        waves = VGroup(wave1, wave2, wave3)

        # Merge the waves into one
        merged_wave = axes.plot(
            lambda x: np.sin(2 * PI * x)
            + 0.5 * np.sin(4 * PI * x)
            + 0.25 * np.sin(8 * PI * x),
            color=TEAL,
            stroke_width=3,
        )

        # Display the axes and waves
        self.play(Create(axes), run_time=1)
        self.wait(0.5)
        self.play(
            Create(merged_wave),
            run_time=8,
            lag_ratio=0,
            rate_func=linear,
        )

        # Animate the merging process
        self.play(
            Transform(merged_wave, waves),
            run_time=3,
        )
        self.wait(2)
