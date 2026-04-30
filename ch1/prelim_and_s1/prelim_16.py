from manim import *


class Prelim16(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY
        text_width = 10.4

        def fit_math(src: str, size: int, color=None):
            mob = MathTex(src, font_size=size, color=color)
            if mob.width > text_width:
                mob.scale_to_fit_width(text_width)
            return mob

        title = Text("Induced Ordering on a Subset", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))

        divider = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=GRAY_C)
        divider.next_to(title, DOWN, buff=0.22)
        self.play(FadeIn(divider))

        setup = fit_math(
            r"\text{Let }(A,R)\text{ be an ordered set and }B\subseteq A.",
            42
        ).next_to(divider, DOWN, buff=0.45)
        setup.to_edge(LEFT, buff=0.9)
        self.play(Write(setup))

        line_1 = fit_math(
            r"R_0\ :=\ R\cap (B\times B)",
            56,
            color=YELLOW
        ).next_to(setup, DOWN, buff=0.55)
        line_1.to_edge(LEFT, buff=0.9)

        line_2 = fit_math(
            r"\text{Then }R_0\text{ is the ordering on }B\text{ induced by }R,",
            40
        ).next_to(line_1, DOWN, buff=0.45)
        line_2.to_edge(LEFT, buff=0.9)

        line_3 = fit_math(
            r"\text{i.e. the restriction of the ordering of }A\text{ to }B.",
            40
        ).next_to(line_2, DOWN, buff=0.28)
        line_3.to_edge(LEFT, buff=0.9)

        ex_label = Text("Example", font_size=30, color=GRAY_B).next_to(line_3, DOWN, buff=0.75)
        ex_label.to_edge(LEFT, buff=0.9)
        ex = fit_math(
            r"A=\mathbb{R},\ R=\le,\ B=(0,1)\ \Rightarrow\ R_0=\le\ \text{on }(0,1).",
            38
        ).next_to(ex_label, DOWN, buff=0.25)
        ex.to_edge(LEFT, buff=0.9)

        self.play(Write(line_1))
        self.play(Write(line_2))
        self.play(Write(line_3))
        self.play(FadeIn(ex_label, shift=UP * 0.1), Write(ex))
        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2
        )
