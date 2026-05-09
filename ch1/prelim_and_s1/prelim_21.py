from manim import *


class Prelim21(Scene):
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

        title = Text("Lemma B", font_size=46)
        title.to_edge(UP)
        divider = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=GRAY_C)
        divider.next_to(title, DOWN, buff=0.22)
        self.play(Write(title), FadeIn(divider))

        statement = fit_math(
            r"\text{Lemma B: every element of }M\text{ is an extreme point.}",
            42,
            color=YELLOW,
        )
        below(statement, divider, 0.45)
        e_def = fit_math(
            r"E=\{c\in M:c\text{ is an extreme point of }M\}",
            42,
            color=BLUE_B,
        )
        below(e_def, statement, 0.45)
        nonempty = fit_math(r"E\neq\varnothing\text{ since }a\in E.", 44)
        below(nonempty, e_def, 0.45)

        self.play(Write(statement))
        self.play(Write(e_def))
        self.play(Write(nonempty))
        self.wait(1.2)

        clear_stage(keep=(title, divider))

        f_title = fit_tex("Show closure under f", 38, color=YELLOW)
        below(f_title, divider, 0.45)
        start = fit_math(r"\text{Let }c\in E\text{ and }x\in M\text{ with }x<f(c).", 40)
        below(start, f_title, 0.42)
        lemma_a = fit_math(
            r"\text{By Lemma A, }M=M_c,\text{ so }x<c\text{ or }x=c.",
            40,
            color=BLUE_B,
        )
        below(lemma_a, start, 0.38)
        case_1 = fit_math(r"x<c\Rightarrow f(x)\le c\le f(c).", 44)
        below(case_1, lemma_a, 0.42)
        case_2 = fit_math(r"x=c\Rightarrow f(x)=f(c).", 44)
        below(case_2, case_1, 0.35)
        f_closed = fit_math(r"\therefore\ f(c)\in E,\quad\text{so }f(E)\subseteq E.", 44, color=YELLOW)
        below(f_closed, case_2, 0.45)

        self.play(Write(f_title))
        self.play(Write(start))
        self.play(Write(lemma_a))
        self.play(Write(case_1))
        self.play(Write(case_2))
        self.play(Write(f_closed))
        self.wait(1.5)

        clear_stage(keep=(title, divider))

        lub_title = fit_tex("Least Upper Bounds in E", 38, color=YELLOW)
        below(lub_title, divider, 0.45)
        t_def = fit_math(
            r"\text{Let }T\text{ be a nonempty totally ordered subset of }E.",
            38,
        )
        below(t_def, lub_title, 0.42)
        b_def = fit_math(
            r"\text{Let }b\text{ be the least upper bound of }T\text{ in }M.",
            38,
            color=BLUE_B,
        )
        below(b_def, t_def, 0.35)
        goal = fit_math(
            r"\text{To prove }b\in E,\text{ let }x\in M\text{ and assume }x<b.",
            38,
        )
        below(goal, b_def, 0.42)
        impossible = fit_math(
            r"\exists c\in T,\ f(c)\le x\Rightarrow c\le f(c)\le x,"
            r"\text{ so }x\text{ is an upper bound of }T.",
            32,
        )
        below(impossible, goal, 0.35)
        contradiction = fit_math(
            r"\text{Then }b\le x,\text{ impossible since }x<b.",
            38,
            color=RED_B,
        )
        below(contradiction, impossible, 0.35)

        self.play(Write(lub_title))
        self.play(Write(t_def))
        self.play(Write(b_def))
        self.play(Write(goal))
        self.play(Write(impossible))
        self.play(Write(contradiction))
        self.wait(1.5)

        clear_stage(keep=(title, divider))

        finish_title = fit_tex("Therefore b is Extreme", 38, color=YELLOW)
        below(finish_title, divider, 0.45)
        by_lemma_a = fit_math(
            r"\text{From Lemma A, }x\le c\text{ for some }c\in T.",
            42,
            color=BLUE_B,
        )
        below(by_lemma_a, finish_title, 0.45)
        less_case = fit_math(r"x<c\Rightarrow f(x)\le c\le b.", 44)
        below(less_case, by_lemma_a, 0.42)
        equal_case = fit_math(r"x=c\Rightarrow c=x<b,\text{ so }f(x)\le b.", 40)
        below(equal_case, less_case, 0.35)
        b_extreme = fit_math(r"b\in E.", 54, color=YELLOW)
        below(b_extreme, equal_case, 0.45)
        e_adm = fit_math(
            r"E\text{ is admissible, so }E=M.",
            46,
            color=YELLOW,
        )
        below(e_adm, b_extreme, 0.45)

        self.play(Write(finish_title))
        self.play(Write(by_lemma_a))
        self.play(Write(less_case))
        self.play(Write(equal_case))
        self.play(Write(b_extreme))
        self.play(Write(e_adm))
        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2,
        )
