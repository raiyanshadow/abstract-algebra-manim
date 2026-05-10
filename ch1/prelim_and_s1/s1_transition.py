from manim import *
from manim.utils.rate_functions import smooth


class S1Transition(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e2e"

        chapter = Text("Chapter 1: Groups", font_size=62)
        section = MathTex(
            r"\mathcal{S}1:\ \text{Monoids}",
            font_size=46,
            color=YELLOW,
        )

        accent = Line(LEFT * 3.7, RIGHT * 3.7, stroke_width=2, color=GRAY_C)
        accent.next_to(chapter, DOWN, buff=0.28)
        section.next_to(accent, DOWN, buff=0.38)

        group = VGroup(chapter, accent, section)
        group.move_to(UP * 0.35)

        self.play(Write(chapter), run_time=2.0, rate_func=smooth)
        self.play(Create(accent), run_time=0.9, rate_func=smooth)
        self.play(FadeIn(section, shift=DOWN * 0.2), run_time=1.6, rate_func=smooth)
        self.wait(1.4)
        self.play(FadeOut(group, shift=UP * 0.2), run_time=1.2)
