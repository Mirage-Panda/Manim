from manim import *
import numpy as np
from scipy.integrate import solve_ivp


# Define the Lorenz system
def lorenz_system(t, state, sigma=10, rho=28, beta=8 / 3):  # rho=28
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


# Solve the Lorenz system
# To slow down, decrease t_max (total time)
# Original rtol=1e-8
def generate_lorenz_points(starting_state, t_max=20, dt=0.01):
    t_values = np.arange(0, t_max, dt)
    solution = solve_ivp(
        lorenz_system,
        t_span=(0, t_max),
        y0=starting_state,
        t_eval=t_values,
        rtol=1e-6,
        atol=1e-9,
    )
    return np.array(solution.y).T  # Transpose to get (x, y, z) points


class LorenzAttractor(ThreeDScene):  # Use ThreeDScene for 3D rotations

    def construct(self):
        # Generate points
        starting_state = [10, 10, 10]
        points = generate_lorenz_points(starting_state)

        # Set up axes
        axes = ThreeDAxes(
            x_range=[-50, 50, 5],
            y_range=[-50, 50, 5],
            z_range=[0, 50, 5],
            axis_config={"color": GRAY, "stroke_width": 2},
        )

        # Create a path for the attractor
        attractor_path = VMobject(color=BLUE, stroke_width=2)
        attractor_path.set_points_smoothly([axes.c2p(*point) for point in points])

        # Add axes to the scene
        self.add(axes)

        # Add rotation to the camera during the attractor animation
        self.move_camera(
            phi=60 * DEGREES,  # Initial elevation angle
            theta=-45 * DEGREES,  # Initial azimuth angle
            zoom=0.75,
            frame_center=(0, 0, 2),
        )
        self.begin_ambient_camera_rotation(rate=0.05)  # Slow continuous rotation

        # Animate the attractor
        self.play(Create(attractor_path), run_time=15, rate_func=linear)

        # Animation finished indicator
        attractor_path.set_color(GREEN)

        # Speed up camera
        self.stop_ambient_camera_rotation
        self.begin_ambient_camera_rotation(rate=0.1)

        # Wait to observe the rotation
        self.wait(10)
