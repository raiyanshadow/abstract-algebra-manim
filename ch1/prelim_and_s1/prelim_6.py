from manim import *
from manim.utils.rate_functions import smooth
import numpy as np

class Preliminary6(ThreeDScene):
    def construct(self):
        self.camera.background_color = DARK_GRAY

        title = Tex(r"Building Dimensions via Cartesian Products", font_size=42)
        subtitle = MathTex(r"[0,1] \;\to\; [0,1]^2 \;\to\; [0,1]^3")
        subtitle.next_to(title, DOWN)

        self.play(Write(title), FadeIn(subtitle, shift=DOWN))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        line = NumberLine(
            x_range=[0, 1, 1],
            length=5,
            include_numbers=True
        ).shift(DOWN * 2)

        label_1d = MathTex(r"[0,1]").next_to(line, DOWN)
        label_2d = MathTex(r"[0,1]\times[0,1]").next_to(line, DOWN)
        label_2d_actual = MathTex(r"[0, 1]^2").next_to(line, DOWN)

        self.play(Create(line), Write(label_1d))
        self.wait(3)
        
        self.remove(line)
        line = NumberLine(
            x_range=[0, 1, 1],
            length=5,
            include_numbers=False
        ).shift(DOWN*2)
        self.play(line.animate.move_to(UP))
        lines = VGroup()
        for y in np.linspace(-2, 2, 15):
            l = line.copy().shift(UP * y)
            l.set_stroke(opacity=0.25)
            lines.add(l)

        square = Square(side_length=5)
        square.move_to(lines.get_center())
        square.set_stroke(width=3)

        self.play(
            LaggedStart(*[TransformFromCopy(line, l) for l in lines], lag_ratio=0.05),
            run_time=2
        )
        self.play(Create(square), FadeOut(line), Transform(label_1d, label_2d))
        self.wait(1)
        self.play(Transform(label_1d, label_2d_actual))
        self.wait(1)

        self.play(FadeOut(lines), FadeOut(label_1d), FadeOut(square))

        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)

        base_square = Square(side_length=4)
        base_square.move_to(ORIGIN)

        layers = VGroup()
        for z in np.linspace(-1, 3, 15):
            s = base_square.copy().shift(OUT * z)
            s.set_stroke(opacity=0.25)
            layers.add(s)

        cube = Cube(side_length=4).shift(OUT)
        cube.set_fill(BLUE_E, opacity=0.12)
        cube.set_stroke(width=2)

        label_3d = MathTex(r"[0,1]^2 \times [0,1]").to_edge(DOWN)
        label_3d_actual = MathTex(r"[0,1]^3").to_edge(DOWN)
        label_3d.set_opacity(0)
        label_3d_actual.set_opacity(0)
        self.add_fixed_in_frame_mobjects(label_3d, label_3d_actual)

        self.play(
            LaggedStart(*[Create(s) for s in layers], lag_ratio=0.05),
            run_time=2.5
        )
        self.wait(1)

        self.begin_ambient_camera_rotation(rate=0.32)

        self.play(Create(cube), Write(label_3d), label_3d.animate.set_opacity(1), run_time=2)
        self.wait(2)

        self.play(Transform(label_3d, label_3d_actual), label_3d_actual.animate.set_opacity(1), run_time=2)
        self.wait(3)

        self.play(FadeOut(label_3d_actual), FadeOut(cube), FadeOut(layers), run_time=3)

        self.stop_ambient_camera_rotation()