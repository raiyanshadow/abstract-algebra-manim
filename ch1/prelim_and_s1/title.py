from manim import *
from manim.utils.rate_functions import smooth

class TitleSlide(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY
        title = Text("Abstract Algebra", font_size=64)
        subtitle1 = Text("Chapter 1: Groups", font_size=36)
        subtitle2 = Text("Preliminary and Monoids", font_size=36)
        author = Text("Based on Serge Lang", font_size=28)

        group = VGroup(title, subtitle1, subtitle2, author)
        group.arrange(DOWN, buff=0.4)
        group.shift(UP * 1.2)

        self.play(Write(title), run_time=3, rate_func=smooth)
        self.wait(1)
        self.play(FadeIn(subtitle1, shift=DOWN * 0.3), run_time=2.1)
        self.wait(1)
        self.play(FadeIn(subtitle2, shift=DOWN * 0.3), run_time=2.1)
        self.wait(1)
        self.play(FadeIn(author, shift=DOWN * 0.3), run_time=2.1)

        self.wait(0.5)
        self.clear()
