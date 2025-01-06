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

        # Generate points for two attractors with slightly different starting states
        starting_state_1 = [10, 10, 10]
        starting_state_2 = [10, 10, 10.001]  # Slight variation in the z-coordinate
        starting_state_3 = [10, 10.001, 10]  # Slight variation in the z-coordinate
        starting_state_4 = [10.001, 10, 10]  # Slight variation in the z-coordinate

        points_1 = generate_lorenz_points(starting_state_1, t_max=evolution_time)
        points_2 = generate_lorenz_points(starting_state_2, t_max=evolution_time)
        points_3 = generate_lorenz_points(starting_state_3, t_max=evolution_time)
        points_4 = generate_lorenz_points(starting_state_4, t_max=evolution_time)

        # Set up axes
        axes = ThreeDAxes(
            x_range=[-50, 50, 5],
            y_range=[-50, 50, 5],
            z_range=[0, 50, 5],
            axis_config={"color": GRAY, "stroke_width": 2, "include_tip": False},
        )

        # Create paths for both attractors
        attractor_path_1 = VMobject(color=BLUE, stroke_width=2)
        attractor_path_1.set_points_smoothly([axes.c2p(*point) for point in points_1])

        attractor_path_2 = VMobject(color=RED, stroke_width=2)
        attractor_path_2.set_points_smoothly([axes.c2p(*point) for point in points_2])

        attractor_path_3 = VMobject(color=RED, stroke_width=2)
        attractor_path_3.set_points_smoothly([axes.c2p(*point) for point in points_3])

        attractor_path_4 = VMobject(color=RED, stroke_width=2)
        attractor_path_4.set_points_smoothly([axes.c2p(*point) for point in points_4])

        # Add starting points (dots) for both attractors
        start_dot_1 = Dot3D(axes.c2p(*points_1[0]), color=BLUE, radius=0.05)
        start_dot_2 = Dot3D(axes.c2p(*points_2[0]), color=RED, radius=0.05)
        start_dot_3 = Dot3D(axes.c2p(*points_3[0]), color=RED, radius=0.05)
        start_dot_4 = Dot3D(axes.c2p(*points_4[0]), color=RED, radius=0.05)

        # Add updaters to the dots to follow the end of their respective curves
        start_dot_1.add_updater(lambda dot: dot.move_to(attractor_path_1.get_end()))
        start_dot_2.add_updater(lambda dot: dot.move_to(attractor_path_2.get_end()))
        start_dot_3.add_updater(lambda dot: dot.move_to(attractor_path_3.get_end()))
        start_dot_4.add_updater(lambda dot: dot.move_to(attractor_path_4.get_end()))

        # Display Lorenz equations
        # Define each equation separately
        eq1 = MathTex(r"\frac{dx}{dt} = \sigma(y - x)", font_size=36)
        eq2 = MathTex(r"\frac{dy}{dt} = x(\rho - z) - y", font_size=36)
        eq3 = MathTex(r"\frac{dz}{dt} = xy - \beta z", font_size=36)

        # Group the equations together and arrange them vertically
        lorenz_equations = VGroup(eq1, eq2, eq3).arrange(DOWN, aligned_edge=LEFT)
        lorenz_equations.move_to(UP * 1)

        self.add_fixed_in_frame_mobjects(lorenz_equations)
        self.wait(1)
        self.play(FadeOut(lorenz_equations))

        # Add axes and starting points to the scene
        # self.add(axes)
        self.play(FadeIn(axes), run_time=0.5)

        # Add rotation to the camera during the attractor animation
        self.move_camera(
            phi=60 * DEGREES,  # Initial elevation angle
            theta=-45 * DEGREES,  # Initial azimuth angle
            zoom=0.75,
            frame_center=(0, 0, 2),
        )
        self.begin_ambient_camera_rotation(rate=0.05)  # Slow continuous rotation

        # Animate both attractors
        self.add(start_dot_2, start_dot_3, start_dot_4, start_dot_1)
        self.play(
            Create(attractor_path_2),
            Create(attractor_path_3),
            Create(attractor_path_4),
            Create(attractor_path_1),
            run_time=evolution_time,
            rate_func=linear,
        )

        # Stop updaters after the animation
        start_dot_1.clear_updaters()
        start_dot_2.clear_updaters()
        start_dot_3.clear_updaters()
        start_dot_4.clear_updaters()

        # Animation finished indicator
        attractor_path_1.set_color(TEAL)
        attractor_path_2.set_color(GREEN)
        attractor_path_3.set_color(GREEN)
        attractor_path_4.set_color(GREEN)
        start_dot_1.set_color(TEAL)
        start_dot_2.set_color(GREEN)
        start_dot_3.set_color(GREEN)
        start_dot_4.set_color(GREEN)

        # Speed up camera
        self.stop_ambient_camera_rotation()
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(0.1)
        self.move_camera(
            zoom=1,
            frame_center=(0, 0, 3),
        )

        # Wait to observe the rotation
        self.wait(10)
