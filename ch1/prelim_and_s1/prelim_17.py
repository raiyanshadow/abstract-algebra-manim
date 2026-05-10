from manim import *


class Prelim17(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e2e"
        text_width = 10.4

        def fit_math(src: str, size: int, color=None):
            mob = MathTex(src, font_size=size, color=color)
            if mob.width > text_width:
                mob.scale_to_fit_width(text_width)
            return mob

        def fit_tex(src: str, size: int, color=None):
            mob = Tex(src, font_size=size, color=color)
            if mob.width > text_width:
                mob.scale_to_fit_width(text_width)
            return mob

        title = Text("Upper Bounds and Maximal Elements", font_size=46)
        title.to_edge(UP)
        self.play(Write(title))

        divider = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=GRAY_C)
        divider.next_to(title, DOWN, buff=0.22)
        self.play(FadeIn(divider))

        setup = fit_math(
            r"\text{Let }A\text{ be an ordered set, with ordering } R \text{ , and }S\subseteq A.",
            42
        ).next_to(divider, DOWN, buff=0.45)
        setup.to_edge(LEFT, buff=0.9)
        self.play(Write(setup))

        ub_1 = fit_math(
            r"u\in A\text{ is an upper bound of }S\text{ if }s \preceq u\text{ for all }s\in S.",
            40
        ).next_to(setup, DOWN, buff=0.6)
        ub_1.to_edge(LEFT, buff=0.9)
        ub_2 = fit_math(
            r"\text{(equivalently: }s\le u\text{ for all }s\in S\text{).}",
            36
        ).next_to(ub_1, DOWN, buff=0.3)
        ub_2.to_edge(LEFT, buff=0.9)

        max_text = fit_math(
            r"m\in A\text{ is maximal if }m \preceq x\Rightarrow x=m\ \text{for all }x\in A.",
            39,
            color=YELLOW
        ).next_to(ub_2, DOWN, buff=0.65)
        max_text.to_edge(LEFT, buff=0.9)

        self.play(Write(ub_1))
        self.play(Write(ub_2))
        self.play(Write(max_text))

        note = fit_tex(
            r"A greatest element is maximal, but not conversely.",
            36,
            color=GRAY_B
        ).next_to(max_text, DOWN, buff=0.75)
        note.to_edge(LEFT, buff=0.9)

        self.play(Write(note))
        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2
        )
