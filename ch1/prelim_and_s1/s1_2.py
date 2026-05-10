from manim import *


class S1_2(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e2e"
        text_width = 10.7
        x_anchor = 0

        def fit_math(src: str, size: int = 38, color=None):
            mob = MathTex(src, font_size=size, color=color)
            if mob.width > text_width:
                mob.scale_to_fit_width(text_width)
            return mob

        def fit_tex(src: str, size: int = 36, color=None):
            mob = Tex(src, font_size=size, color=color)
            if mob.width > text_width:
                mob.scale_to_fit_width(text_width)
            return mob

        def below(mob, target, buff=0.35):
            mob.next_to(target, DOWN, buff=buff)
            mob.set_x(x_anchor)
            return mob

        def clear_stage(keep=()):
            keep = set(keep)
            mobs = [mob for mob in self.mobjects if mob not in keep]
            if mobs:
                self.play(
                    LaggedStart(*[FadeOut(mob) for mob in mobs], lag_ratio=0.04),
                    run_time=1.1,
                )

        title = Text("Products in a Monoid", font_size=48)
        title.to_edge(UP)
        divider = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=GRAY_C)
        divider.next_to(title, DOWN, buff=0.22)
        self.play(Write(title), FadeIn(divider))

        setup = fit_math(
            r"x_1,\dots,x_n\in G,\qquad n\in\{1,2,\dots\}",
            42,
        )
        below(setup, divider, 0.55)
        prod_def = fit_math(
            r"\prod_{i=1}^n x_i=x_1\dots x_n=(x_1\dots x_{n-1})x_n",
            46,
            color=YELLOW,
        )
        below(prod_def, setup, 0.45)

        dots = VGroup(*[Dot(color=BLUE_B) for _ in range(5)]).arrange(RIGHT, buff=0.55)
        dot_labels = VGroup(
            MathTex("x_1", font_size=28),
            MathTex("x_2", font_size=28),
            MathTex("x_3", font_size=28),
            MathTex("\\cdots", font_size=28),
            MathTex("x_n", font_size=28),
        )
        for dot, label in zip(dots, dot_labels):
            label.next_to(dot, DOWN, buff=0.15)
        product_line = VGroup(dots, dot_labels)
        below(product_line, prod_def, 0.65)

        self.play(Write(setup))
        self.play(Write(prod_def))
        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.12))
        self.play(Write(dot_labels))
        self.wait(1.5)

        clear_stage(keep=(title, divider))

        assoc_text = fit_tex("By associativity, we can say that", 36, color=YELLOW)
        below(assoc_text, divider, 0.5)
        split_product = fit_math(
            r"\prod_{\alpha=1}^{m}x_{\alpha}\cdot"
            r"\prod_{\beta=1}^{n}x_{m+\beta}"
            r"=\prod_{i=1}^{m+n}x_i",
            46,
            color=BLUE_B,
        )
        below(split_product, assoc_text, 0.5)
        empty = fit_math(
            r"e=\prod_{i=1}^{0}x_i",
            56,
            color=YELLOW,
        )
        below(empty, split_product, 0.65)
        empty_words = fit_math(
            r"\text{Thus the unit element is the empty product.}",
            40,
        )
        below(empty_words, empty, 0.35)

        self.play(Write(assoc_text))
        self.play(Write(split_product))
        self.play(Write(empty))
        self.play(Write(empty_words))
        self.wait(1.8)

        clear_stage(keep=(title, divider))

        comm_title = fit_tex("Commutative Law of Composition", 38, color=YELLOW)
        below(comm_title, divider, 0.45)
        comm_def = fit_math(
            r"xy=yx\quad\text{for all }x,y\in S.",
            48,
            color=BLUE_B,
        )
        below(comm_def, comm_title, 0.45)
        abelian = fit_math(
            r"\text{If the law of composition of a monoid }G\text{ is commutative, then }G\text{ is Abelian.}",
            36,
            color=YELLOW,
        )
        below(abelian, comm_def, 0.65)

        self.play(Write(comm_title))
        self.play(Write(comm_def))
        self.play(Write(abelian))
        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=1.7,
        )
