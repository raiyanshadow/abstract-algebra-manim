from manim import *
from manim.utils.rate_functions import smooth

class Preliminary5(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY
        text1 = MathTex(r"\{A_i\}_{i \in I}", font_size=96).move_to(UP*3)

        self.play(Write(text1), run_time=1)
        self.wait(1)
        text2 = Tex(r"$I$ is an indexing set", font_size=64).next_to(text1, DOWN)

        self.play(Write(text2), run_time=3)
        self.wait(3)
        self.play(FadeOut(text2), run_time=1)
        self.wait(1)

        center = Mobject().move_to(DOWN)

        text3 = MathTex(r"\bigcup_{i \in I}{A_i}", font_size=96).next_to(center, LEFT*6)
        text4 = MathTex(r"\bigcap_{i \in I}{A_i}", font_size=96).next_to(center, RIGHT*6)

        self.play(Write(text3), Write(text4), run_time=3, rate_func=smooth)
        self.wait(4)

        self.play(text3.animate.scale(1.5), run_time=2, rate_func=smooth)
        self.play(text3.animate.scale(1/1.5), run_time=1)

        self.wait(2)

        self.play(text4.animate.scale(1.5), run_time=2, rate_func=smooth)
        self.play(text4.animate.scale(1/1.5), run_time=1)

        self.wait(2)

        self.play(FadeOut(text1, text3, text4), run_time=2, rate_func=smooth)
        self.wait(1)