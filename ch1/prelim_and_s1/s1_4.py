from manim import *


class S1_4(Scene):
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

        title = Text("Proposition 1.1: Induction Step", font_size=44)
        title.to_edge(UP)
        divider = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=GRAY_C)
        divider.next_to(title, DOWN, buff=0.22)
        self.play(Write(title), FadeIn(divider))

        step = fit_tex("Induction step: n $\geq$ 1", 38, color=YELLOW)
        below(step, divider, 0.45)
        assume = fit_math(
            r"\text{Assume for all natural numbers }m<n,\text{ the proposition holds.}",
            36,
        )
        below(assume, step, 0.4)
        k_line = fit_math(
            r"\text{Let }k\in[n]\text{ such that }\psi(k)=n.",
            40,
            color=BLUE_B,
        )
        below(k_line, assume, 0.45)
        exists = fit_math(r"\text{Such }k\text{ exists by bijectivity of }\psi.", 38)
        below(exists, k_line, 0.35)

        self.play(Write(step))
        self.play(Write(assume))
        self.play(Write(k_line))
        self.play(Write(exists))
        self.wait(1.5)

        clear_stage(keep=(title, divider))

        split_title = fit_math(r"\text{Move the term }x_n\text{ into view}", 38, color=YELLOW)
        below(split_title, divider, 0.45)
        split = fit_math(
            r"\prod_{i=1}^{n}x_{\psi(i)}"
            r"=\prod_{\alpha=1}^{k-1}x_{\psi(\alpha)}\cdot x_n\cdot"
            r"\prod_{\beta=1}^{n-k}x_{\psi(k+\beta)}",
            36,
            color=BLUE_B,
        )
        below(split, split_title, 0.45)
        note = fit_math(
            r"\text{Note that }x_{\psi(k)}=x_n.",
            42,
            color=YELLOW,
        )
        below(note, split, 0.55)

        self.play(Write(split_title))
        self.play(Write(split))
        self.play(Write(note))
        self.wait(1.6)

        clear_stage(keep=(title, divider))

        phi_title = fit_tex("Define a new bijection", 38, color=YELLOW)
        below(phi_title, divider, 0.45)
        phi_type = fit_math(r"\phi:[n-1]\to[n-1]", 48, color=BLUE_B)
        below(phi_type, phi_title, 0.42)
        phi_def = fit_math(
            r"\phi(i)=\begin{cases}\psi(i)&i<k\\\psi(i+1)&i\ge k\end{cases}",
            44,
            color=YELLOW,
        )
        below(phi_def, phi_type, 0.45)

        self.play(Write(phi_title))
        self.play(Write(phi_type))
        self.play(Write(phi_def))
        self.wait(1.6)

        clear_stage(keep=(title, divider))

        align_title = fit_tex("Then", 38, color=YELLOW)
        below(align_title, divider, 0.45)
        line_1 = fit_math(
            r"\prod_{\alpha=1}^{k-1}x_{\psi(\alpha)}\cdot x_n\cdot"
            r"\prod_{\beta=1}^{n-k}x_{\psi(k+\beta)}",
            36,
        )
        below(line_1, align_title, 0.42)
        line_2 = fit_math(
            r"=\prod_{\alpha=1}^{k-1}x_{\phi(\alpha)}\cdot x_n\cdot"
            r"\prod_{\beta=1}^{n-k}x_{\phi(k+\beta-1)}",
            35,
            color=BLUE_B,
        )
        below(line_2, line_1, 0.35)
        line_3 = fit_math(
            r"=\prod_{i=1}^{n-1}x_{\phi(i)}\cdot x_n",
            44,
            color=YELLOW,
        )
        below(line_3, line_2, 0.42)

        self.play(Write(align_title))
        self.play(Write(line_1))
        self.play(Write(line_2))
        self.play(Write(line_3))
        self.wait(1.6)

        clear_stage(keep=(title, divider))

        finish_title = fit_tex("Use the induction hypothesis", 38, color=YELLOW)
        below(finish_title, divider, 0.45)
        since = fit_math(
            r"\phi\text{ is a bijection and }n-1<n.",
            42,
            color=BLUE_B,
        )
        below(since, finish_title, 0.45)
        final_eq = fit_math(
            r"\prod_{i=1}^{n-1}x_{\phi(i)}\cdot x_n"
            r"=\prod_{i=1}^{n-1}x_i\cdot x_n"
            r"=\prod_{i=1}^{n}x_i",
            40,
            color=YELLOW,
        )
        below(final_eq, since, 0.45)
        done = fit_math(r"\text{as needed.}", 44)
        below(done, final_eq, 0.45)

        self.play(Write(finish_title))
        self.play(Write(since))
        self.play(Write(final_eq))
        self.play(Write(done))
        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=1.7,
        )
