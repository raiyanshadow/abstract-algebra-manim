from manim import *


class Prelim18(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e2e"
        text_width = 10.4

        def fit_math(src: str, size: int, color=None):
            mob = MathTex(src, font_size=size, color=color)
            if mob.width > text_width:
                mob.scale_to_fit_width(text_width)
            return mob

        title = Text("Zorn's Lemma", font_size=44)
        title.to_edge(UP)
        self.play(Write(title))

        divider = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=GRAY_C)
        divider.next_to(title, DOWN, buff=0.22)
        self.play(FadeIn(divider))

        setup = fit_math(
            r"\text{If every totally ordered subset of an ordered set }A",
            40
        ).next_to(divider, DOWN, buff=0.45)
        setup.to_edge(LEFT, buff=0.9)

        zorn_stmt = fit_math(
            r"\text{has an upper bound in }A,\text{ then }A\text{ has a maximal element.}",
            40,
            color=YELLOW
        ).next_to(setup, DOWN, buff=0.35)
        zorn_stmt.to_edge(LEFT, buff=0.9)

        self.play(Write(setup))
        self.play(Write(zorn_stmt))

        eq_1 = fit_math(
            r"\text{This is used as an existence principle:}",
            38
        ).next_to(zorn_stmt, DOWN, buff=0.8)
        eq_1.to_edge(LEFT, buff=0.9)
        eq_2 = fit_math(
            r"\text{check chain upper bounds } \Longrightarrow \text{ conclude a maximal element exists.}",
            36
        ).next_to(eq_1, DOWN, buff=0.28)
        eq_2.to_edge(LEFT, buff=0.9)

        self.play(Write(eq_1))
        self.play(Write(eq_2))
        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2
        )
