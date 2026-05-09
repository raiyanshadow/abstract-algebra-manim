from manim import *


class Prelim20(Scene):
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

        def mc_picture(scale=1.0):
            axis = Line(DOWN * 2.3, UP * 2.3, color=GRAY_B, stroke_width=4)
            c_y = -0.35
            fc_y = 0.85

            lower = Rectangle(width=1.8, height=1.95, stroke_width=0)
            lower.set_fill(BLUE_E, opacity=0.28)
            lower.move_to(axis.get_center() + DOWN * 1.2)

            upper = Rectangle(width=1.8, height=1.45, stroke_width=0)
            upper.set_fill(GREEN_E, opacity=0.28)
            upper.move_to(axis.get_center() + UP * 1.58)

            c_dot = Dot(axis.point_from_proportion((c_y + 2.3) / 4.6), color=YELLOW)
            fc_dot = Dot(axis.point_from_proportion((fc_y + 2.3) / 4.6), color=GREEN_B)
            c_label = MathTex("c", font_size=34, color=YELLOW).next_to(c_dot, LEFT, buff=0.2)
            fc_label = MathTex("f(c)", font_size=34, color=GREEN_B).next_to(fc_dot, LEFT, buff=0.2)
            lower_label = MathTex("x\\le c", font_size=30, color=BLUE_B).next_to(lower, RIGHT, buff=0.24)
            upper_label = MathTex("f(c)\\le x", font_size=30, color=GREEN_B).next_to(upper, RIGHT, buff=0.24)

            pic = VGroup(lower, upper, axis, c_dot, fc_dot, c_label, fc_label, lower_label, upper_label)
            pic.scale(scale)
            return pic

        title = Text("Lemma A", font_size=46)
        title.to_edge(UP)
        divider = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=GRAY_C)
        divider.next_to(title, DOWN, buff=0.22)
        self.play(Write(title), FadeIn(divider))

        extreme_title = fit_tex("Extreme Point", 38, color=YELLOW)
        below(extreme_title, divider, 0.45)
        extreme_def = fit_math(
            r"c\in M\text{ is extreme if }x\in M,\ x\le c\Rightarrow f(x)\le c.",
            40,
        )
        below(extreme_def, extreme_title, 0.42)
        mc_def = fit_math(
            r"M_c=\{x\in M:x\le c\text{ or }f(c)\le x\}",
            46,
            color=BLUE_B,
        )
        below(mc_def, extreme_def, 0.5)
        lemma = fit_math(
            r"\text{Lemma A: }M_c=M\text{ for every extreme point }c\text{ of }M.",
            38,
            color=YELLOW,
        )
        below(lemma, mc_def, 0.55)

        self.play(Write(extreme_title))
        self.play(Write(extreme_def))
        self.play(Write(mc_def))
        self.play(Write(lemma))
        self.wait(1.4)

        clear_stage(keep=(title, divider))

        visual_title = fit_tex("The two pieces of the set", 38, color=YELLOW)
        below(visual_title, divider, 0.45)
        pic = mc_picture(scale=1.0)
        below(pic, visual_title, 0.5)
        caption = fit_math(
            r"M_c\text{ contains everything below }c\text{ and everything above }f(c).",
            36,
            color=BLUE_B,
        )
        below(caption, pic, 0.45)

        self.play(Write(visual_title))
        self.play(FadeIn(pic, shift=UP * 0.1))
        self.play(Write(caption))
        self.wait(1.5)

        clear_stage(keep=(title, divider))

        prove_adm = fit_math(
            r"\text{It is enough to show that }M_c\text{ is admissible.}",
            42,
            color=YELLOW,
        )
        below(prove_adm, divider, 0.45)
        because = fit_math(
            r"M_c\subseteq M,\quad a\in M_c,\quad "
            r"M=\bigcap\{\text{admissible subsets of }A\}.",
            36,
        )
        below(because, prove_adm, 0.42)
        conclusion = fit_math(
            r"M_c\text{ admissible}\Rightarrow M\subseteq M_c\Rightarrow M_c=M.",
            42,
            color=BLUE_B,
        )
        below(conclusion, because, 0.5)

        self.play(Write(prove_adm))
        self.play(Write(because))
        self.play(Write(conclusion))
        self.wait(1.3)

        clear_stage(keep=(title, divider))

        closed_title = fit_tex("First: closure under f", 38, color=YELLOW)
        below(closed_title, divider, 0.45)
        let_x = fit_math(r"\text{Let }x\in M_c.", 44)
        below(let_x, closed_title, 0.45)
        case_1 = fit_math(
            r"x<c\text{ and }f(x)\le c\Rightarrow f(x)\in M_c.",
            40,
            color=BLUE_B,
        )
        below(case_1, let_x, 0.42)
        case_2 = fit_math(
            r"x=c\Rightarrow f(x)=f(c)\in M_c.",
            42,
            color=BLUE_B,
        )
        below(case_2, case_1, 0.35)
        case_3 = fit_math(
            r"f(c)\le x\le f(x)\Rightarrow f(c)\le f(x)\Rightarrow f(x)\in M_c.",
            36,
            color=BLUE_B,
        )
        below(case_3, case_2, 0.35)
        closed = fit_math(r"\therefore\ f(M_c)\subseteq M_c.", 48, color=YELLOW)
        below(closed, case_3, 0.45)

        self.play(Write(closed_title))
        self.play(Write(let_x))
        self.play(Write(case_1))
        self.play(Write(case_2))
        self.play(Write(case_3))
        self.play(Write(closed))
        self.wait(1.5)

        clear_stage(keep=(title, divider))

        closure_visual_title = fit_tex("Closure picture", 38, color=YELLOW)
        below(closure_visual_title, divider, 0.45)
        closure_pic = mc_picture(scale=0.86).shift(RIGHT * 2.7 + DOWN * 0.15)
        closure_pic[7].set_opacity(0)
        closure_pic[8].set_opacity(0)
        x_low = Dot(closure_pic[2].point_from_proportion(0.22), color=BLUE_B)
        fx_low = Dot(closure_pic[2].point_from_proportion(0.34), color=BLUE_B)
        x_high = Dot(closure_pic[2].point_from_proportion(0.76), color=GREEN_B)
        fx_high = Dot(closure_pic[2].point_from_proportion(0.88), color=GREEN_B)
        low_arrow = Arrow(x_low.get_center(), fx_low.get_center(), buff=0.08, color=BLUE_B)
        high_arrow = Arrow(x_high.get_center(), fx_high.get_center(), buff=0.08, color=GREEN_B)
        low_label = MathTex("x", font_size=24, color=BLUE_B).next_to(x_low, RIGHT, buff=0.3)
        low_label.shift(DOWN * 0.18)
        fx_low_label = MathTex("f(x)", font_size=24, color=BLUE_B).next_to(fx_low, RIGHT, buff=0.3)
        fx_low_label.shift(UP * 0.18)
        high_label = MathTex("x", font_size=24, color=GREEN_B).next_to(x_high, RIGHT, buff=0.3)
        high_label.shift(DOWN * 0.18)
        fx_high_label = MathTex("f(x)", font_size=24, color=GREEN_B).next_to(fx_high, RIGHT, buff=0.3)
        fx_high_label.shift(UP * 0.18)
        visual_note = fit_math(
            r"x\in M_c\Rightarrow f(x)\text{ lands in one of the same two pieces.}",
            34,
            color=YELLOW,
        ).shift(LEFT * 2.75 + DOWN * 0.2)
        visual_note.scale_to_fit_width(4.4)
        visual_group = VGroup(
            closure_pic, x_low, fx_low, x_high, fx_high,
            low_arrow, high_arrow, low_label, fx_low_label, high_label, fx_high_label,
            visual_note,
        )

        self.play(Write(closure_visual_title))
        self.play(FadeIn(closure_pic), Write(visual_note))
        self.play(FadeIn(x_low), Write(low_label))
        self.play(GrowArrow(low_arrow), FadeIn(fx_low), Write(fx_low_label))
        self.play(FadeIn(x_high), Write(high_label))
        self.play(GrowArrow(high_arrow), FadeIn(fx_high), Write(fx_high_label))
        self.wait(1.3)

        clear_stage(keep=(title, divider))

        lub_title = fit_tex("Second: least upper bounds", 36, color=YELLOW)
        below(lub_title, divider, 0.45)
        t_def = fit_math(
            r"\text{Let }T\text{ be a nonempty totally ordered subset of }M_c.",
            38,
        )
        below(t_def, lub_title, 0.42)
        b_def = fit_math(
            r"\text{Let }b\text{ be the least upper bound of }T\text{ in }M.",
            38,
            color=BLUE_B,
        )
        below(b_def, t_def, 0.35)
        lub_case_1 = fit_math(
            r"\forall x\in T,\ x\le c\Rightarrow b\le c\Rightarrow b\in M_c.",
            40,
        )
        below(lub_case_1, b_def, 0.45)
        lub_case_2 = fit_math(
            r"\exists x\in T,\ f(c)\le x\Rightarrow f(c)\le x\le b\Rightarrow b\in M_c.",
            36,
        )
        below(lub_case_2, lub_case_1, 0.35)
        adm_done = fit_math(
            r"\therefore\ M_c\text{ is admissible, so }M_c=M.",
            46,
            color=YELLOW,
        )
        below(adm_done, lub_case_2, 0.5)

        self.play(Write(lub_title))
        self.play(Write(t_def))
        self.play(Write(b_def))
        self.play(Write(lub_case_1))
        self.play(Write(lub_case_2))
        self.play(Write(adm_done))
        self.wait(2)

        clear_stage(keep=(title, divider))

        lub_visual_title = fit_tex("Least upper bound picture", 38, color=YELLOW)
        below(lub_visual_title, divider, 0.45)
        axis_1 = Line(DOWN * 1.7, UP * 1.7, color=GRAY_B, stroke_width=4).shift(LEFT * 3)
        c_dot_1 = Dot(axis_1.point_from_proportion(0.72), color=YELLOW)
        b_dot_1 = Dot(axis_1.point_from_proportion(0.63), color=BLUE_B)
        t_dots_1 = VGroup(
            Dot(axis_1.point_from_proportion(0.2), color=BLUE_B),
            Dot(axis_1.point_from_proportion(0.36), color=BLUE_B),
            Dot(axis_1.point_from_proportion(0.5), color=BLUE_B),
        )
        labels_1 = VGroup(
            MathTex("T", font_size=30, color=BLUE_B).next_to(t_dots_1, LEFT, buff=0.24),
            MathTex("b", font_size=30, color=BLUE_B).next_to(b_dot_1, LEFT, buff=0.2),
            MathTex("c", font_size=30, color=YELLOW).next_to(c_dot_1, RIGHT, buff=0.2),
            MathTex("b\\le c", font_size=34, color=YELLOW).next_to(axis_1, DOWN, buff=0.35),
        )

        axis_2 = Line(DOWN * 1.7, UP * 1.7, color=GRAY_B, stroke_width=4).shift(RIGHT * 3)
        fc_dot_2 = Dot(axis_2.point_from_proportion(0.42), color=GREEN_B)
        x_dot_2 = Dot(axis_2.point_from_proportion(0.55), color=GREEN_B)
        b_dot_2 = Dot(axis_2.point_from_proportion(0.78), color=BLUE_B)
        t_dots_2 = VGroup(
            Dot(axis_2.point_from_proportion(0.28), color=BLUE_B),
            x_dot_2,
            Dot(axis_2.point_from_proportion(0.66), color=BLUE_B),
        )
        labels_2 = VGroup(
            MathTex("f(c)", font_size=30, color=GREEN_B).next_to(fc_dot_2, LEFT, buff=0.2),
            MathTex("x", font_size=30, color=GREEN_B).next_to(x_dot_2, RIGHT, buff=0.2),
            MathTex("b", font_size=30, color=BLUE_B).next_to(b_dot_2, LEFT, buff=0.2),
            MathTex("f(c)\\le b", font_size=34, color=YELLOW).next_to(axis_2, DOWN, buff=0.35),
        )
        lub_visual = VGroup(axis_1, c_dot_1, b_dot_1, t_dots_1, labels_1, axis_2, fc_dot_2, b_dot_2, t_dots_2, labels_2)
        below(lub_visual, lub_visual_title, 0.45)

        self.play(Write(lub_visual_title))
        self.play(FadeIn(axis_1), FadeIn(axis_2))
        self.play(FadeIn(t_dots_1), FadeIn(t_dots_2))
        self.play(FadeIn(b_dot_1), FadeIn(b_dot_2), FadeIn(c_dot_1), FadeIn(fc_dot_2))
        self.play(Write(labels_1), Write(labels_2))
        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2,
        )
