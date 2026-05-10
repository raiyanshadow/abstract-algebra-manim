from manim import *


class S1_5(Scene):
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

        title = Text("More Terminology", font_size=48)
        title.to_edge(UP)
        divider = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=GRAY_C)
        divider.next_to(title, DOWN, buff=0.22)
        self.play(Write(title), FadeIn(divider))

        power_title = fit_tex("Powers in a monoid", 38, color=YELLOW)
        below(power_title, divider, 0.45)
        power_def = fit_math(
            r"x^n=\prod_{i=1}^{n}x",
            56,
            color=BLUE_B,
        )
        below(power_def, power_title, 0.45)
        power_words = fit_math(
            r"\text{This is the }n\text{-fold product of }x\text{ with itself.}",
            38,
        )
        below(power_words, power_def, 0.4)
        abelian_power = fit_math(
            r"(xy)^n=\prod_{i=1}^{n}xy=\prod_{i=1}^{n}x\cdot\prod_{i=1}^{n}y=x^ny^n",
            40,
            color=YELLOW,
        )
        below(abelian_power, power_words, 0.55)

        self.play(Write(power_title))
        self.play(Write(power_def))
        self.play(Write(power_words))
        self.play(Write(abelian_power))
        self.wait(1.8)

        clear_stage(keep=(title, divider))

        subset_title = fit_tex("Products of subsets", 38, color=YELLOW)
        below(subset_title, divider, 0.45)
        ss = fit_math(
            r"S,S'\subset G,\qquad SS'=\{xy:x\in S,\ y\in S'\}.",
            42,
            color=BLUE_B,
        )
        below(ss, subset_title, 0.42)
        gg = fit_math(r"GG=G", 56, color=YELLOW)
        below(gg, ss, 0.45)
        xs = fit_math(
            r"xS=\{x\}S=\{xy:y\in S\}",
            42,
        )
        below(xs, gg, 0.5)
        sx = fit_math(
            r"Sx=S\{x\}=\{yx:y\in S\}",
            42,
        )
        below(sx, xs, 0.32)

        self.play(Write(subset_title))
        self.play(Write(ss))
        self.play(Write(gg))
        self.play(Write(xs))
        self.play(Write(sx))
        self.wait(1.8)

        clear_stage(keep=(title, divider))

        sub_title = fit_tex("Submonoid", 38, color=YELLOW)
        below(sub_title, divider, 0.45)
        sub_1 = fit_math(
            r"H\subseteq G\text{ is a submonoid if it has the same unit element as }G",
            36,
            color=BLUE_B,
        )
        below(sub_1, sub_title, 0.42)
        sub_2 = fit_math(
            r"\text{and for every }x,y\in H,\ xy\in H.",
            42,
            color=BLUE_B,
        )
        below(sub_2, sub_1, 0.35)
        closed_words = fit_math(
            r"\text{That is, }H\text{ is closed under the law of composition of }G.",
            38,
            color=YELLOW,
        )
        below(closed_words, sub_2, 0.5)

        outer = RoundedRectangle(corner_radius=0.12, width=4.8, height=2.4, color=GRAY_B)
        outer.set_fill(GRAY_E, opacity=0.12)
        inner = RoundedRectangle(corner_radius=0.12, width=2.9, height=1.35, color=YELLOW)
        inner.set_fill(YELLOW_E, opacity=0.18)
        g_label = MathTex("G", font_size=34, color=GRAY_B).move_to(outer.get_corner(UR) + LEFT * 0.35 + DOWN * 0.25)
        h_label = MathTex("H", font_size=34, color=YELLOW).move_to(inner.get_corner(UL) + RIGHT * 0.35 + DOWN * 0.25)
        x_dot = Dot(inner.get_center() + LEFT * 0.45, color=BLUE_B)
        y_dot = Dot(inner.get_center() + RIGHT * 0.15, color=BLUE_B)
        xy_dot = Dot(inner.get_center() + DOWN * 0.35, color=GREEN_B)
        visual = VGroup(outer, inner, g_label, h_label, x_dot, y_dot, xy_dot)
        below(visual, closed_words, 0.45)

        self.play(Write(sub_title))
        self.play(Write(sub_1))
        self.play(Write(sub_2))
        self.play(Write(closed_words))
        self.play(Create(outer), Create(inner), Write(g_label), Write(h_label))
        self.play(FadeIn(x_dot), FadeIn(y_dot), FadeIn(xy_dot))
        self.wait(1.7)

        clear_stage(keep=(title, divider))

        examples_title = fit_tex("Examples of monoids", 38, color=YELLOW)
        below(examples_title, divider, 0.45)
        ex_1 = fit_math(r"\mathbb{Z}\text{ under addition}", 42, color=BLUE_B)
        below(ex_1, examples_title, 0.45)
        ex_2 = fit_math(r"\mathbb{N}\text{ under multiplication}", 42, color=BLUE_B)
        below(ex_2, ex_1, 0.38)
        ex_3 = fit_math(
            r"\text{homeomorphism classes of compact connected surfaces}",
            36,
            color=BLUE_B,
        )
        below(ex_3, ex_2, 0.45)
        ex_4 = fit_math(
            r"\text{under the operation of connected sum}",
            36,
            color=YELLOW,
        )
        below(ex_4, ex_3, 0.25)

        self.play(Write(examples_title))
        self.play(Write(ex_1))
        self.play(Write(ex_2))
        self.play(Write(ex_3))
        self.play(Write(ex_4))
        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=1.7,
        )
