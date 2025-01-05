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

        points_1 = generate_lorenz_points(starting_state_1, t_max=evolution_time)
        points_2 = generate_lorenz_points(starting_state_2, t_max=evolution_time)

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

        # Add starting points (dots) for both attractors
        start_dot_1 = Dot3D(axes.c2p(*points_1[0]), color=BLUE, radius=0.05)
        start_dot_2 = Dot3D(axes.c2p(*points_2[0]), color=RED, radius=0.05)

        # Add updaters to the dots to follow the end of their respective curves
        start_dot_1.add_updater(lambda dot: dot.move_to(attractor_path_1.get_end()))
        start_dot_2.add_updater(lambda dot: dot.move_to(attractor_path_2.get_end()))

        # Add axes and starting points to the scene
        self.add(axes)

        # Add rotation to the camera during the attractor animation
        self.move_camera(
            phi=60 * DEGREES,  # Initial elevation angle
            theta=-45 * DEGREES,  # Initial azimuth angle
            zoom=0.75,
            frame_center=(0, 0, 2),
        )
        self.begin_ambient_camera_rotation(rate=0.05)  # Slow continuous rotation

        # Animate both attractors
        self.add(start_dot_2, start_dot_1)
        self.play(
            Create(attractor_path_2),
            Create(attractor_path_1),
            run_time=evolution_time,
            rate_func=linear,
        )

        # Stop updaters after the animation
        start_dot_1.clear_updaters()
        start_dot_2.clear_updaters()

        # Animation finished indicator
        attractor_path_1.set_color(TEAL)
        attractor_path_2.set_color(GREEN)
        start_dot_1.set_color(TEAL)
        start_dot_2.set_color(GREEN)

        # Speed up camera
        self.stop_ambient_camera_rotation()
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(0.1)
        self.move_camera(
            zoom=1,
            frame_center=(0, 0, 3),
        )

        # Wait to observe the rotation
        self.wait(10)
