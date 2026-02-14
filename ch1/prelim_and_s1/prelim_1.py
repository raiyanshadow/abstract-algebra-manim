from manim import *
from manim.utils.rate_functions import smooth

class Preliminary1(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY
        setA = MathTex("A", font_size=96).to_edge(UP).move_to(LEFT)
        setB = MathTex("B", font_size=96).next_to(setA, RIGHT, buff=1)

        self.play(FadeIn(setA), run_time=1, rate_func=smooth)
        self.play(FadeIn(setB), run_time=1, rate_func=smooth)

        self.wait(2)

        self.play(
            setA.animate.shift(UP*3 + LEFT * 1.5),
            setB.animate.shift(UP*3 + RIGHT * 1.5),
            run_time=1,
            rate_func=smooth
        )

        self.wait(1)