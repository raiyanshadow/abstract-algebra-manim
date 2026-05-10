from manim import *
from manim.utils.rate_functions import smooth

class PreliminaryTransition(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e2e"
        title = Text("Preliminary", font_size=64)
        subtext = Text("Sets, Mappings, and Zorn's Lemma", font_size=32)

        group = VGroup(title, subtext)
        group.arrange(DOWN, buff=0.4)
        group.shift(UP * 1.2)

        self.play(Write(title), run_time=2, rate_func=smooth)
        self.wait(1)
        self.play(Write(subtext), run_time=2, rate_func=smooth)
        self.wait(1)

        self.play(
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2
        )