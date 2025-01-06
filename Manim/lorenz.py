import numpy as np
from manim import *
from scipy.integrate import solve_ivp


# Define the Lorenz system
def lorenz_system(t, state, sigma=10, rho=28, beta=8 / 3):  # rho=28
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


# Solve the Lorenz system
def generate_lorenz_points(starting_state, t_max=10, dt=0.01):
    t_values = np.arange(0, t_max, dt)
    solution = solve_ivp(
        lorenz_system,
        t_span=(0, t_max),
        y0=starting_state,
        t_eval=t_values,
        rtol=1e-8,
        atol=1e-10,
    )
    return np.array(solution.y).T  # Transpose to get (x, y, z) points


class LorenzAttractor(ThreeDScene):  # Use ThreeDScene for 3D rotations

    def construct(self):
        # Time for evolution
        evolution_time = 20

        # Set up axes
        axes = ThreeDAxes(
            x_range=[-50, 50, 5],
            y_range=[-50, 50, 5],
            z_range=[0, 50, 5],
            axis_config={"color": GRAY, "stroke_width": 2, "include_tip": False},
        )

        # Define parameters for the attractors
        num_curves = 6  # Change to add more curves
        epsilion = 1e-5  # Difference in set of curves
        starting_states = [[10, 10, 10 + n * epsilion] for n in range(num_curves)]
        running_colours = color_gradient([BLUE_E, BLUE_A], num_curves)
        final_colours = color_gradient([TEAL_E, TEAL_A], num_curves)

        # Generate points and create paths dynamically
        paths = []
        start_dots = []

        for i, state in enumerate(starting_states):
            points = generate_lorenz_points(state, t_max=evolution_time)
            path = VMobject(color=running_colours[i], stroke_width=2)
            path.set_points_smoothly([axes.c2p(*point) for point in points])
            paths.append(path)

            start_dot = Dot3D(
                axes.c2p(*points[0]), color=running_colours[i], radius=0.05
            )
            start_dot.add_updater(lambda dot, path=path: dot.move_to(path.get_end()))
            start_dots.append(start_dot)

        # Display Lorenz equations
        lorenz_title = MathTex(r"\text{The Lorenz System}", font_size=72)
        lorenz_equation = MathTex(
            R"""
            \begin{aligned}
            \frac{\mathrm{d} x}{\mathrm{~d} t} & =\sigma(y-x) \\
            \frac{\mathrm{d} y}{\mathrm{~d} t} & =x(\rho-z)-y \\
            \frac{\mathrm{d} z}{\mathrm{~d} t} & =x y-\beta z
            \end{aligned}
        """,
            font_size=48,
        )
        lorenz_latex = VGroup(lorenz_title, lorenz_equation).arrange(
            DOWN, aligned_edge=LEFT
        )
        lorenz_latex.move_to(UP * 1)

        self.add_fixed_in_frame_mobjects(lorenz_latex)
        self.wait(1)
        # self.play(FadeOut(lorenz_equations))

        # Add axes
        self.play(
            AnimationGroup(FadeOut(lorenz_latex), FadeIn(axes)),
            run_time=1.5,
            lag_ratio=0.75,
        )

        # Add rotation to the camera
        self.move_camera(
            phi=60 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.75,
            frame_center=(0, 0, 2),
        )
        self.begin_ambient_camera_rotation(rate=0.05)

        # Animate attractors
        self.add(*start_dots)
        self.play(
            *[Create(path) for path in paths],
            run_time=evolution_time,
            rate_func=linear,
        )

        # Stop updaters
        for dot in start_dots:
            dot.clear_updaters()

        # Change running_colours to final_colours to indicate completion
        self.play(
            *[path.animate.set_color(final_colours[i]) for i, path in enumerate(paths)],
            *[
                dot.animate.set_color(final_colours[i])
                for i, dot in enumerate(start_dots)
            ],
            run_time=2,
        )

        # Adjust camera speed
        self.stop_ambient_camera_rotation()
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(0.1)
        self.move_camera(zoom=1, frame_center=(0, 0, 3))
        self.wait(10)
