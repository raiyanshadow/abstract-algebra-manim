from manim import *


class Prelim22(Scene):
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

        def subset_box(width, height, color, label):
            box = RoundedRectangle(
                corner_radius=0.12,
                width=width,
                height=height,
                color=color,
                stroke_width=3,
            )
            box.set_fill(color, opacity=0.12)
            tag = MathTex(label, font_size=30, color=color)
            tag.move_to(box.get_corner(UL) + RIGHT * 0.48 + DOWN * 0.28)
            return VGroup(box, tag)

        title = Text("Bourbaki-Witt to Zorn", font_size=46)
        title.to_edge(UP)
        divider = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=GRAY_C)
        divider.next_to(title, DOWN, buff=0.22)
        self.play(Write(title), FadeIn(divider))

        bw_title = fit_tex("Finish Bourbaki-Witt", 38, color=YELLOW)
        below(bw_title, divider, 0.45)
        mx = fit_math(
            r"x,y\in M,\quad x\text{ extreme},\quad y\in M_x",
            42,
            color=BLUE_B,
        )
        below(mx, bw_title, 0.45)
        total = fit_math(
            r"y\le x\text{ or }x\le f(x)\le y,\quad\text{so }M\text{ is totally ordered.}",
            38,
        )
        below(total, mx, 0.4)
        lub = fit_math(
            r"\text{There exists a least upper bound }b\in M.",
            40,
        )
        below(lub, total, 0.45)
        fixed = fit_math(r"b\le f(b)\le b\Rightarrow f(b)=b.", 50, color=YELLOW)
        below(fixed, lub, 0.45)

        self.play(Write(bw_title))
        self.play(Write(mx))
        self.play(Write(total))
        self.play(Write(lub))
        self.play(Write(fixed))
        self.wait(1.6)

        clear_stage(keep=(title, divider))

        zorn_statement = fit_tex("Zorn's Lemma", 38, color=YELLOW)
        below(zorn_statement, divider, 0.45)
        stmt_1 = fit_math(
            r"\text{If }S\text{ is nonempty, inductively ordered, and partially ordered,}",
            38,
        )
        below(stmt_1, zorn_statement, 0.42)
        stmt_2 = fit_math(
            r"\text{then there exists a maximal element in }S.",
            42,
            color=BLUE_B,
        )
        below(stmt_2, stmt_1, 0.35)
        a_def = fit_math(
            r"A=\{X\subseteq S:X\neq\varnothing\text{ and }X\text{ is totally ordered}\}",
            38,
            color=YELLOW,
        )
        below(a_def, stmt_2, 0.55)

        self.play(Write(zorn_statement))
        self.play(Write(stmt_1))
        self.play(Write(stmt_2))
        self.play(Write(a_def))
        self.wait(1.4)

        clear_stage(keep=(title, divider))

        ordered_title = fit_tex("Order A by Inclusion", 38, color=YELLOW)
        below(ordered_title, divider, 0.45)
        order = fit_math(r"X,Y\in A,\quad X\le Y\text{ means }X\subseteq Y.", 42)
        below(order, ordered_title, 0.45)
        t_def = fit_math(
            r"T=\{X_i\}_{i\in I}\text{ a totally ordered subset of }A.",
            40,
            color=BLUE_B,
        )
        below(t_def, order, 0.42)
        z_def = fit_math(r"Z=\bigcup_{i\in I}X_i.", 52, color=YELLOW)
        below(z_def, t_def, 0.45)
        z_tot = fit_math(
            r"x,y\in Z\Rightarrow x\in X_i,\ y\in X_j\text{ for some }i,j\in I.",
            36,
        )
        below(z_tot, z_def, 0.45)
        z_lub = fit_math(
            r"\text{Since }T\text{ is totally ordered by inclusion, }Z\text{ is totally ordered.}",
            36,
        )
        below(z_lub, z_tot, 0.32)

        self.play(Write(ordered_title))
        self.play(Write(order))
        self.play(Write(t_def))
        self.play(Write(z_def))
        self.play(Write(z_tot))
        self.play(Write(z_lub))
        self.wait(1.5)

        clear_stage(keep=(title, divider))

        inclusion_visual_title = fit_tex("The union is the least upper bound", 36, color=YELLOW)
        below(inclusion_visual_title, divider, 0.45)
        z_box = subset_box(5.7, 3.05, YELLOW, "Z")
        below(z_box, inclusion_visual_title, 0.5)
        center = z_box[0].get_center()
        x3 = subset_box(4.45, 2.3, TEAL_B, "X_3").move_to(center + DOWN * 0.05)
        x2 = subset_box(3.2, 1.55, GREEN_B, "X_2").move_to(center + DOWN * 0.12)
        x1 = subset_box(2.0, 0.85, BLUE_B, "X_1").move_to(center + DOWN * 0.18)
        nested = VGroup(z_box, x3, x2, x1)
        dots = VGroup(
            Dot(x1[0].get_center() + LEFT * 0.25, color=WHITE),
            Dot(x2[0].get_center() + RIGHT * 0.45, color=WHITE),
            Dot(x3[0].get_center() + RIGHT * 1.15 + DOWN * 0.25, color=WHITE),
            Dot(z_box[0].get_center() + RIGHT * 2.05 + UP * 0.8, color=WHITE),
        )
        union_note = fit_math(
            r"X_1\subseteq X_2\subseteq X_3\subseteq Z",
            42,
            color=YELLOW,
        )
        below(union_note, nested, 0.45)

        self.play(Write(inclusion_visual_title))
        self.play(Create(z_box), FadeIn(dots[3]))
        self.play(Create(x3), FadeIn(dots[2]))
        self.play(Create(x2), FadeIn(dots[1]))
        self.play(Create(x1), FadeIn(dots[0]))
        self.play(Write(union_note))
        self.wait(1.6)

        clear_stage(keep=(title, divider))

        strict_title = fit_tex("A is Strictly Inductively Ordered", 36, color=YELLOW)
        below(strict_title, divider, 0.45)
        union = fit_math(
            r"\bigcup_{i\in I}X_i\text{ is the least upper bound of }T.",
            42,
            color=BLUE_B,
        )
        below(union, strict_title, 0.45)
        strict = fit_math(
            r"\therefore\ A\text{ is partially ordered and strictly inductively ordered.}",
            38,
            color=YELLOW,
        )
        below(strict, union, 0.45)
        no_max = fit_math(
            r"\text{Suppose }A\text{ does not have a maximal element.}",
            40,
        )
        below(no_max, strict, 0.55)
        choose = fit_math(
            r"\forall\Omega\in A,\ \exists\Omega'\in A\text{ such that }\Omega<\Omega'.",
            38,
        )
        below(choose, no_max, 0.35)

        self.play(Write(strict_title))
        self.play(Write(union))
        self.play(Write(strict))
        self.play(Write(no_max))
        self.play(Write(choose))
        self.wait(1.5)

        clear_stage(keep=(title, divider))

        larger_visual_title = fit_math(
            r"\text{For each }\Omega\in A,\text{ choose }\Omega'\in A\text{ with }\Omega<\Omega'",
            32,
            color=YELLOW,
        )
        below(larger_visual_title, divider, 0.45)
        omega = subset_box(2.5, 1.55, BLUE_B, "\\Omega").shift(LEFT * 2.3 + DOWN * 0.1)
        omega_prime = subset_box(3.55, 2.25, YELLOW, "\\Omega'").shift(RIGHT * 2.3 + DOWN * 0.1)
        new_dot = Dot(omega_prime[0].get_center() + RIGHT * 1.05 + UP * 0.42, color=RED_B)
        arrow = Arrow(omega.get_right(), omega_prime.get_left(), buff=0.35, color=YELLOW)
        arrow_label = MathTex("f(\\Omega)=\\Omega'", font_size=36, color=YELLOW).next_to(arrow, UP, buff=0.18)
        strict_containment = fit_math(
            r"\Omega<\Omega'",
            54,
            color=YELLOW,
        )
        below(strict_containment, VGroup(omega, omega_prime), 0.5)

        self.play(Write(larger_visual_title))
        self.play(Create(omega))
        self.play(Create(omega_prime), FadeIn(new_dot))
        self.play(GrowArrow(arrow), Write(arrow_label))
        self.play(Write(strict_containment))
        self.wait(1.4)

        clear_stage(keep=(title, divider))

        contradiction_title = fit_tex("Contradiction", 38, color=YELLOW)
        below(contradiction_title, divider, 0.45)
        f_def = fit_math(
            r"f:A\to A,\qquad f(\Omega)=\Omega'.",
            48,
            color=BLUE_B,
        )
        below(f_def, contradiction_title, 0.45)
        bw = fit_math(
            r"\text{Bourbaki-Witt gives }\exists\Omega_0\in A\text{ with }f(\Omega_0)=\Omega_0.",
            36,
        )
        below(bw, f_def, 0.45)
        contradiction = fit_math(
            r"\Omega_0<f(\Omega_0)=\Omega_0",
            54,
            color=RED_B,
        )
        below(contradiction, bw, 0.5)
        maximal = fit_math(
            r"\text{Thus }A\text{ has a maximal element }X_0.",
            42,
            color=YELLOW,
        )
        below(maximal, contradiction, 0.5)

        self.play(Write(contradiction_title))
        self.play(Write(f_def))
        self.play(Write(bw))
        self.play(Write(contradiction))
        self.play(Write(maximal))
        self.wait(1.6)

        clear_stage(keep=(title, divider))

        fixed_visual_title = fit_math(
            r"\text{But Bourbaki-Witt gives }f(\Omega_0)=\Omega_0",
            36,
            color=YELLOW,
        )
        below(fixed_visual_title, divider, 0.45)
        omega0 = subset_box(2.9, 1.85, BLUE_B, "\\Omega_0").shift(LEFT * 2.6)
        same_omega0 = subset_box(2.9, 1.85, BLUE_B, "f(\\Omega_0)").shift(RIGHT * 2.6)
        fixed_arrow = Arrow(omega0.get_right(), same_omega0.get_left(), buff=0.35, color=BLUE_B)
        equality = MathTex("=", font_size=58, color=BLUE_B).move_to(fixed_arrow)
        red_cross = Cross(equality, stroke_color=RED_B, stroke_width=6)
        impossible_text = fit_math(
            r"\Omega_0<f(\Omega_0)\text{ but }f(\Omega_0)=\Omega_0",
            42,
            color=RED_B,
        )
        below(impossible_text, VGroup(omega0, same_omega0), 0.55)

        self.play(Write(fixed_visual_title))
        self.play(Create(omega0), Create(same_omega0))
        self.play(GrowArrow(fixed_arrow))
        self.play(FadeOut(fixed_arrow), Write(equality))
        self.play(Create(red_cross), Write(impossible_text))
        self.wait(1.5)

        clear_stage(keep=(title, divider))

        final_title = fit_tex("Maximal Element of S", 38, color=YELLOW)
        below(final_title, divider, 0.45)
        upper = fit_math(
            r"\text{Let }m\text{ be an upper bound of }X_0.",
            42,
            color=BLUE_B,
        )
        below(upper, final_title, 0.45)
        suppose = fit_math(r"x\in S\text{ and }m\le x.", 46)
        below(suppose, upper, 0.42)
        extend = fit_math(
            r"X_0\cup\{x\}\text{ is totally ordered.}",
            44,
            color=YELLOW,
        )
        below(extend, suppose, 0.42)
        contradiction_x0 = fit_math(
            r"\text{This contradicts maximality of }X_0\text{ unless }x=m.",
            38,
        )
        below(contradiction_x0, extend, 0.45)
        result = fit_math(r"\therefore\ m\text{ is maximal in }S.", 54, color=YELLOW)
        below(result, contradiction_x0, 0.5)

        self.play(Write(final_title))
        self.play(Write(upper))
        self.play(Write(suppose))
        self.play(Write(extend))
        self.play(Write(contradiction_x0))
        self.play(Write(result))
        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2,
        )
