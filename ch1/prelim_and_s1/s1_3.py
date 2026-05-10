from manim import *


class S1_3(Scene):
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

        title = Text("Proposition 1.1", font_size=48)
        title.to_edge(UP)
        divider = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=GRAY_C)
        divider.next_to(title, DOWN, buff=0.22)
        self.play(Write(title), FadeIn(divider))

        hyp = fit_math(
            r"G\text{ is an Abelian monoid},\qquad x_1,\dots,x_n\in G.",
            38,
        )
        below(hyp, divider, 0.45)
        bracket = fit_math(
            r"[i]=\{x\in\mathbb{N}:1\le x\le i\}",
            44,
            color=BLUE_B,
        )
        below(bracket, hyp, 0.42)
        psi = fit_math(
            r"\psi:[n]\to[n]\text{ is a bijective mapping.}",
            42,
            color=BLUE_B,
        )
        below(psi, bracket, 0.35)
        claim = fit_math(
            r"\prod_{i=1}^{n}x_{\psi(i)}=\prod_{i=1}^{n}x_i",
            56,
            color=YELLOW,
        )
        below(claim, psi, 0.55)

        self.play(Write(hyp))
        self.play(Write(bracket))
        self.play(Write(psi))
        self.play(Write(claim))
        self.wait(1.8)

        clear_stage(keep=(title, divider))

        proof = fit_tex("Proof by strong induction on n", 38, color=YELLOW)
        below(proof, divider, 0.45)
        base_title = fit_tex("Base case: n = 1", 38, color=YELLOW)
        below(base_title, proof, 0.55)
        one = fit_math(r"[1]=\{1\}", 48, color=BLUE_B)
        below(one, base_title, 0.4)
        psi_one = fit_math(r"\psi(1)=1", 48, color=BLUE_B)
        below(psi_one, one, 0.32)
        base_eq = fit_math(
            r"\prod_{i=1}^{1}x_{\psi(i)}=x_1=\prod_{i=1}^{1}x_i",
            48,
            color=YELLOW,
        )
        below(base_eq, psi_one, 0.45)
        base_done = fit_math(r"\text{so the base case holds.}", 40)
        below(base_done, base_eq, 0.38)

        self.play(Write(proof))
        self.play(Write(base_title))
        self.play(Write(one))
        self.play(Write(psi_one))
        self.play(Write(base_eq))
        self.play(Write(base_done))
        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=1.7,
        )
