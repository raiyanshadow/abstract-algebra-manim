from manim import *


class Prelim9(Scene):
    def build_panel(self, heading, heading_color, center, a_y, b_y, mapping, a_count, b_count):
        panel_title = Text(heading, font_size=30, color=heading_color)
        panel_title.move_to(center + UP * 2.4)

        set_a = Ellipse(width=1.7, height=3.2, color=BLUE_D)
        set_a.set_fill(BLUE_E, opacity=0.18)
        set_a.move_to(center + LEFT * 1.1)

        set_b = Ellipse(width=1.7, height=3.2, color=GREEN_D)
        set_b.set_fill(GREEN_E, opacity=0.18)
        set_b.move_to(center + RIGHT * 1.1)

        label_a = MathTex("A").scale(0.8).next_to(set_a, DOWN, buff=0.12)
        label_b = MathTex("B").scale(0.8).next_to(set_b, DOWN, buff=0.12)

        a_points = VGroup(*[Dot(set_a.get_center() + UP * y, radius=0.05, color=BLUE_B) for y in a_y[:a_count]])
        b_points = VGroup(*[Dot(set_b.get_center() + UP * y, radius=0.05, color=GREEN_B) for y in b_y[:b_count]])

        arrows = VGroup(
            *[
                Arrow(a_points[i].get_right(), b_points[j].get_left(), buff=0.08, stroke_width=3)
                for i, j in mapping
            ]
        )
        arrows.set_color(YELLOW)

        panel = VGroup(panel_title, set_a, set_b, label_a, label_b, a_points, b_points, arrows)
        return panel, arrows

    def construct(self):
        self.camera.background_color = "#1e1e2e"
        title = Text("Mappings Between Sets", font_size=52)
        title.to_edge(UP)

        y_positions_4 = [1.1, 0.35, -0.35, -1.1]
        y_positions_3 = [0.9, 0.0, -0.9]

        injective_panel, injective_arrows = self.build_panel(
            "Injective",
            BLUE_B,
            center=LEFT * 4,
            a_y=y_positions_3,
            b_y=y_positions_4,
            mapping=[(0, 0), (1, 1), (2, 2)],
            a_count=3,
            b_count=4,
        )

        surjective_panel, surjective_arrows = self.build_panel(
            "Surjective",
            GREEN_B,
            center=ORIGIN,
            a_y=y_positions_4,
            b_y=y_positions_3,
            mapping=[(0, 0), (1, 1), (2, 2), (3, 2)],
            a_count=4,
            b_count=3,
        )

        bijective_panel, bijective_arrows = self.build_panel(
            "Bijective",
            YELLOW,
            center=RIGHT * 4,
            a_y=y_positions_3,
            b_y=y_positions_3,
            mapping=[(0, 0), (1, 1), (2, 2)],
            a_count=3,
            b_count=3,
        )

        general_map = MathTex(r"f:A\to B", font_size=54)
        mapping_effect = MathTex(r"x\mapsto f(x)", font_size=46)
        general_group = VGroup(general_map, mapping_effect).arrange(DOWN, buff=0.35)
        general_group.move_to(ORIGIN).shift(DOWN * 0.3)

        self.play(Write(title))
        self.play(Write(general_map))
        self.play(Write(mapping_effect))
        self.wait(0.8)
        self.play(FadeOut(general_group))

        note_inj = Text("one-to-one", font_size=22, color=BLUE_B).next_to(injective_panel, DOWN, buff=0.2)
        note_sur = Text("onto", font_size=22, color=GREEN_B).next_to(surjective_panel, DOWN, buff=0.2)
        note_bij = Text("one-to-one and onto", font_size=22, color=YELLOW).next_to(bijective_panel, DOWN, buff=0.2)

        combine = Tex(
            r"Theorem. A mapping $f : A \to B$ is bijective if and only if it is injective and surjective",
            color=YELLOW,
            font_size=32
        )
        combine.to_edge(DOWN)

        inj_definition = Tex(r"Definition. A mapping $f : A \to B$ is injective if and only if $\forall x, y \in A, f(x) = f(y) \Rightarrow x = y$", font_size=32)
        surj_definition = Tex(r"Definition. A mapping $f : A \to B$ is surjective if and only if $\forall x \in A, \exists y \in B$ such that $f(x) = y$", font_size=32)

        inj_definition.to_edge(DOWN)
        surj_definition.to_edge(DOWN)

        self.play(
            LaggedStart(
                *[Create(mob) for mob in injective_panel[:-1]],
                lag_ratio=0.06,
            ),
            LaggedStart(*[GrowArrow(a) for a in injective_arrows], lag_ratio=0.12),
            FadeIn(note_inj, shift=UP * 0.15),
            Write(inj_definition),
            run_time=2
        )

        self.wait(5)

        self.play(FadeOut(inj_definition), run_time=1, rate_func=smooth)

        self.wait(1)

        self.play(
            LaggedStart(
                *[Create(mob) for mob in surjective_panel[:-1]],
                lag_ratio=0.06,
            ),
            LaggedStart(*[GrowArrow(a) for a in surjective_arrows], lag_ratio=0.12),
            FadeIn(note_sur, shift=UP * 0.15),
            Write(surj_definition),
            run_time=2
        )

        self.wait(5)

        self.play(FadeOut(surj_definition), run_time=1, rate_func=smooth)
        
        self.wait(1)

        self.play(
            LaggedStart(
                *[Create(mob) for mob in bijective_panel[:-1]],
                lag_ratio=0.06,
            ),
            LaggedStart(*[GrowArrow(a) for a in bijective_arrows], lag_ratio=0.12),
            FadeIn(note_bij, shift=UP * 0.15),
        )

        self.play(Write(combine))
        self.wait(5)

        self.play(
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2
        )
