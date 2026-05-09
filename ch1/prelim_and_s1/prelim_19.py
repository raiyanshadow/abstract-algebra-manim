from manim import *


class Prelim19(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e2e"
        text_width = 10.7
        x_anchor = 0

        def fit_math(src: str, size: int = 38, color=None):
            mob = MathTex(src, font_size=size, color=color)
            if mob.width > text_width:
                mob.scale_to_fit_width(text_width)
            return mob

        def fit_tex(src: str, size: int = 34, color=None):
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
                    run_time=1.2,
                )

        title = Text("Zorn's Lemma Proof", font_size=46)
        title.to_edge(UP)
        divider = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=GRAY_C)
        divider.next_to(title, DOWN, buff=0.22)
        self.play(Write(title), FadeIn(divider))

        strict_title = fit_tex("Strictly Inductively Ordered", 38, color=YELLOW)
        below(strict_title, divider, 0.45)
        strict_def_1 = fit_math(
            r"A\text{ is strictly inductively ordered iff every nonempty}",
            40,
        )
        below(strict_def_1, strict_title, 0.4)
        strict_def_2 = fit_math(
            r"\text{totally ordered subset has a least upper bound.}",
            40,
            color=BLUE_B,
        )
        below(strict_def_2, strict_def_1, 0.32)
        setup = fit_math(
            r"\text{Assume }A\neq\varnothing\text{ and }A\text{ is partially ordered by }\le.",
            38,
        )
        below(setup, strict_def_2, 0.55)

        self.play(Write(strict_title))
        self.play(Write(strict_def_1))
        self.play(Write(strict_def_2))
        self.play(Write(setup))
        self.wait(1.4)

        clear_stage(keep=(title, divider))

        inc_title = fit_tex("Increasing Map", 38, color=YELLOW)
        below(inc_title, divider, 0.45)
        inc_def = fit_math(
            r"f:A\to A\text{ is increasing if }\forall x\in A,\ x\le f(x).",
            42,
            color=BLUE_B,
        )
        below(inc_def, inc_title, 0.45)
        theorem = fit_tex("Bourbaki-Witt Theorem", 38, color=YELLOW)
        below(theorem, inc_def, 0.7)
        theorem_statement = fit_math(
            r"A\neq\varnothing,\ A\text{ strictly inductively ordered},\ f\text{ increasing}"
            r"\Rightarrow \exists x_0\in A,\ f(x_0)=x_0.",
            35,
        )
        below(theorem_statement, theorem, 0.35)

        self.play(Write(inc_title))
        self.play(Write(inc_def))
        self.play(Write(theorem))
        self.play(Write(theorem_statement))
        self.wait(1.5)

        clear_stage(keep=(title, divider))

        adm_title = fit_tex("Admissible Sets", 38, color=YELLOW)
        below(adm_title, divider, 0.45)
        start = fit_math(r"\text{Let }a\in A\text{ and }B\subseteq A\text{ with }a\in B.", 40)
        below(start, adm_title, 0.42)
        adm_1 = fit_math(r"B\text{ is admissible if }f(B)\subseteq B", 42, color=BLUE_B)
        below(adm_1, start, 0.42)
        adm_2 = fit_math(
            r"\text{and least upper bounds of non-empty totally ordered subsets lie in }B.",
            36,
            color=BLUE_B,
        )
        below(adm_2, adm_1, 0.32)
        adm_consequence = fit_math(
            r"\text{Thus }B\text{ is strictly inductively ordered.}",
            42,
            color=YELLOW,
        )
        below(adm_consequence, adm_2, 0.55)

        self.play(Write(adm_title))
        self.play(Write(start))
        self.play(Write(adm_1))
        self.play(Write(adm_2))
        self.play(Write(adm_consequence))
        self.wait(1.5)

        clear_stage(keep=(title, divider))

        m_title = fit_tex("Construct M", 38, color=YELLOW)
        below(m_title, divider, 0.45)
        m_def = fit_math(
            r"M=\bigcap\{B\subseteq A:B\text{ is admissible}\}",
            46,
            color=BLUE_B,
        )
        below(m_def, m_title, 0.45)
        m_nonempty = fit_math(r"a\in M,\quad\text{so }M\neq\varnothing.", 42)
        below(m_nonempty, m_def, 0.45)
        m_closed = fit_math(r"x\in M\Rightarrow f(x)\in M,\quad\text{so }f(M)\subseteq M.", 40)
        below(m_closed, m_nonempty, 0.42)
        iterate = fit_math(
            r"f(a),\ f(f(a)),\ \ldots,\ f^{(n)}(a)\in M.",
            44,
            color=YELLOW,
        )
        below(iterate, m_closed, 0.5)

        self.play(Write(m_title))
        self.play(Write(m_def))
        self.play(Write(m_nonempty))
        self.play(Write(m_closed))
        self.play(Write(iterate))
        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2,
        )
