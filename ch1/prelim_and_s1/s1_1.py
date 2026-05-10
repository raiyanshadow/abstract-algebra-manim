from manim import *


class S1_1(Scene):
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

        title = Text("Law of Composition", font_size=48)
        title.to_edge(UP)

        divider = Line(
            LEFT * 5.8,
            RIGHT * 5.8,
            stroke_width=2,
            color=GRAY_C,
        )
        divider.next_to(title, DOWN, buff=0.22)

        self.play(Write(title), FadeIn(divider))

        law = fit_math(r"S\times S\to S", 58, color=YELLOW)
        below(law, divider, 0.55)

        law_text = fit_math(
            r"\text{Let }S\text{ be a set. This map is called a law of composition on }S.",
            36,
        )
        below(law_text, law, 0.45)

        ambient = RoundedRectangle(
            width=7.2,
            height=2.8,
            corner_radius=0.18,
            color=BLUE_B,
            stroke_width=2.5,
        )
        ambient.set_fill(BLUE_E, opacity=0.08)

        ambient_label = MathTex(
            "S",
            font_size=40,
            color=BLUE_B,
        )
        ambient_label.next_to(ambient, UP, buff=0.12)

        x_dot = Dot(
            ambient.get_left() + RIGHT * 1.4 + UP * 0.55,
            radius=0.08,
            color=YELLOW,
        )

        y_dot = Dot(
            ambient.get_left() + RIGHT * 2.2 + DOWN * 0.45,
            radius=0.08,
            color=YELLOW,
        )

        xy_dot = Dot(
            ambient.get_right() + LEFT * 1.5,
            radius=0.09,
            color=GREEN_B,
        )

        x_label = MathTex("x", font_size=34)
        x_label.next_to(x_dot, UP, buff=0.1)

        y_label = MathTex("y", font_size=34)
        y_label.next_to(y_dot, DOWN, buff=0.1)

        xy_label = MathTex(
            "xy",
            font_size=36,
            color=GREEN_B,
        )
        xy_label.next_to(xy_dot, RIGHT, buff=0.12)

        op_symbol = MathTex(
            r"\cdot",
            font_size=54,
            color=YELLOW,
        )

        midpoint = (x_dot.get_center() + y_dot.get_center()) / 2
        op_symbol.move_to(midpoint + RIGHT * 1.0)

        arrow1 = CurvedArrow(
            x_dot.get_right(),
            xy_dot.get_left() + UP * 0.08,
            angle=-0.25,
            color=GRAY_B,
            stroke_width=2.5,
        )

        arrow2 = CurvedArrow(
            y_dot.get_right(),
            xy_dot.get_left() + DOWN * 0.08,
            angle=0.25,
            color=GRAY_B,
            stroke_width=2.5,
        )

        product_picture = VGroup(
            ambient,
            ambient_label,
            x_dot,
            y_dot,
            xy_dot,
            x_label,
            y_label,
            xy_label,
            op_symbol,
            arrow1,
            arrow2,
        )

        below(product_picture, law_text, 0.65)

        product_text = fit_math(
            r"\text{The image of }(x,y)\text{ is called the product of }x\text{ and }y,\text{ written }xy.",
            34,
        )
        below(product_text, product_picture, 0.45)

        self.play(Write(law))
        self.play(Write(law_text))

        self.play(
            Create(ambient),
            Write(ambient_label),
        )

        self.play(
            FadeIn(x_dot),
            FadeIn(y_dot),
            Write(x_label),
            Write(y_label),
        )

        self.play(
            Create(arrow1),
            Create(arrow2),
            FadeIn(xy_dot),
            Write(xy_label),
        )

        self.play(Write(product_text))

        self.wait(1.4)

        clear_stage(keep=(title, divider))

        sum_note = fit_math(
            r"x+y\text{ is the sum only if }x+y=y+x.",
            46,
            color=YELLOW,
        )
        below(sum_note, divider, 0.55)

        assoc_title = fit_tex(
            "Associativity",
            38,
            color=YELLOW,
        )
        below(assoc_title, sum_note, 0.7)

        assoc = fit_math(
            r"x(yz)=(xy)z\quad\Longleftrightarrow\quad"
            r"\text{the law of composition is associative.}",
            38,
        )
        below(assoc, assoc_title, 0.35)

        self.play(Write(sum_note))
        self.play(Write(assoc_title))
        self.play(Write(assoc))

        self.wait(1.5)

        clear_stage(keep=(title, divider))

        unit_title = fit_tex(
            "Unit Element",
            38,
            color=YELLOW,
        )
        below(unit_title, divider, 0.45)

        unit = fit_math(
            r"e\in S,\quad ex=x=xe\quad\Rightarrow\quad e\text{ is the unit element of }S.",
            40,
            color=BLUE_B,
        )
        below(unit, unit_title, 0.42)

        unique = fit_math(
            r"\text{The unit element must be unique.}",
            42,
            color=YELLOW,
        )
        below(unique, unit, 0.45)

        monoid = fit_math(
            r"G\text{ is a monoid if it has a unit element and an associative law of composition.}",
            36,
        )
        below(monoid, unique, 0.6)

        self.play(Write(unit_title))
        self.play(Write(unit))
        self.play(Write(unique))
        self.play(Write(monoid))

        self.wait(2)

        self.play(
            FadeOut(divider),
            LaggedStart(
                *[FadeOut(mob) for mob in self.mobjects],
                lag_ratio=0.05,
            ),
            run_time=1.7,
        )