from manim import *


class Prelim11(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e2e"

        title = Text("Composition of Mappings", font_size=50)
        title.to_edge(UP)
        self.play(Write(title))

        # Triangle diagram: A -> B -> C and A -> C
        a_pos = LEFT * 4 + DOWN * 0.8
        b_pos = ORIGIN + UP * 1.1
        c_pos = RIGHT * 4 + DOWN * 0.8

        A = MathTex("A", font_size=52).move_to(a_pos)
        B = MathTex("B", font_size=52).move_to(b_pos)
        C = MathTex("C", font_size=52).move_to(c_pos)

        f_arrow = Arrow(A.get_right() + RIGHT * 0.1, B.get_left() + LEFT * 0.1, buff=0.2, stroke_width=4, color=BLUE_B)
        g_arrow = Arrow(B.get_right() + RIGHT * 0.1, C.get_left() + LEFT * 0.1, buff=0.2, stroke_width=4, color=GREEN_B)
        h_arrow = Arrow(A.get_right() + RIGHT * 0.2, C.get_left() + LEFT * 0.2, buff=0.2, stroke_width=4, color=YELLOW)

        f_label = MathTex("f", color=BLUE_B).next_to(f_arrow, UP, buff=0.1)
        g_label = MathTex("g", color=GREEN_B).next_to(g_arrow, UP, buff=0.1)
        h_label = MathTex("h", color=YELLOW).next_to(h_arrow, DOWN, buff=0.12)

        triangle_eq = MathTex(r"h = g\circ f", font_size=44, color=YELLOW).to_edge(DOWN)

        self.play(Write(A), Write(B), Write(C))
        self.play(GrowArrow(f_arrow), Write(f_label))
        self.play(GrowArrow(g_arrow), Write(g_label))
        self.play(GrowArrow(h_arrow), Write(h_label))
        self.play(Write(triangle_eq))
        self.play(
            Indicate(f_label, color=BLUE_B, scale_factor=1.15),
            Indicate(g_label, color=GREEN_B, scale_factor=1.15),
            Indicate(h_label, color=YELLOW, scale_factor=1.15),
            Indicate(triangle_eq.get_part_by_tex(r"g\circ f"), color=YELLOW, scale_factor=1.15),
        )
        self.wait(1.6)

        triangle_group = VGroup(A, B, C, f_arrow, g_arrow, h_arrow, f_label, g_label, h_label, triangle_eq)
        self.play(FadeOut(triangle_group))

        # Square diagram: A -> B -> D and A -> C -> D
        a2_pos = LEFT * 3.7 + UP * 1.1
        b2_pos = RIGHT * 3.7 + UP * 1.1
        c2_pos = LEFT * 3.7 + DOWN * 1.4
        d2_pos = RIGHT * 3.7 + DOWN * 1.4

        A2 = MathTex("A", font_size=52).move_to(a2_pos)
        B2 = MathTex("B", font_size=52).move_to(b2_pos)
        C2 = MathTex("C", font_size=52).move_to(c2_pos)
        D2 = MathTex("D", font_size=52).move_to(d2_pos)

        f2_arrow = Arrow(A2.get_right(), B2.get_left(), buff=0.2, stroke_width=4, color=BLUE_B)
        g2_arrow = Arrow(B2.get_bottom(), D2.get_top(), buff=0.22, stroke_width=4, color=GREEN_B)
        p2_arrow = Arrow(A2.get_bottom(), C2.get_top(), buff=0.22, stroke_width=4, color=PURPLE_B)
        q2_arrow = Arrow(C2.get_right(), D2.get_left(), buff=0.2, stroke_width=4, color=ORANGE)

        f2_label = MathTex("f", color=BLUE_B).next_to(f2_arrow, UP, buff=0.08)
        g2_label = MathTex("g", color=GREEN_B).next_to(g2_arrow, RIGHT, buff=0.08)
        p2_label = MathTex(r"\psi", color=PURPLE_B).next_to(p2_arrow, LEFT, buff=0.08)
        q2_label = MathTex(r"\phi", color=ORANGE).next_to(q2_arrow, DOWN, buff=0.08)

        square_eq = MathTex(r"g\circ f = \phi\circ\psi", font_size=44, color=YELLOW).to_edge(DOWN)

        self.play(Write(A2), Write(B2), Write(C2), Write(D2))
        self.play(GrowArrow(f2_arrow), GrowArrow(g2_arrow), Write(f2_label), Write(g2_label))
        self.play(GrowArrow(p2_arrow), GrowArrow(q2_arrow), Write(p2_label), Write(q2_label))
        self.play(Write(square_eq))
        self.play(
            Indicate(square_eq.get_part_by_tex(r"g\circ f"), color=BLUE_B, scale_factor=1.12),
            Indicate(square_eq.get_part_by_tex(r"\phi\circ\psi"), color=ORANGE, scale_factor=1.12),
        )
        self.wait(2)

        square_group = VGroup(
            A2, B2, C2, D2,
            f2_arrow, g2_arrow, p2_arrow, q2_arrow,
            f2_label, g2_label, p2_label, q2_label, square_eq
        )
        self.play(FadeOut(square_group))

        seq_title = Text("General Sequence Form", font_size=40, color=YELLOW_B).next_to(title, DOWN*2, buff=0.35)
        seq_sets = MathTex(r"\{A_i\}_{i=1}^{n},\quad \{B_j\}_{j=2}^{m}", font_size=36).next_to(seq_title, DOWN, buff=0.3)
        seq_f = MathTex(
            r"A_1 \xrightarrow{f_1} A_2 \xrightarrow{f_2} \cdots \xrightarrow{f_{n-1}} A_n",
            font_size=36
        ).next_to(seq_sets, DOWN, buff=0.35)
        seq_g = MathTex(
            r"A_1 \xrightarrow{g_1} B_2 \xrightarrow{g_2} \cdots \xrightarrow{g_{m-1}} B_m = A_n",
            font_size=36
        ).next_to(seq_f, DOWN, buff=0.35)
        seq_eq = MathTex(
            r"f_{n-1}\circ\cdots\circ f_1 \;=\; g_{m-1}\circ\cdots\circ g_1",
            font_size=42,
            color=YELLOW
        ).next_to(seq_g, DOWN, buff=0.5)

        self.play(Write(seq_title), Write(seq_sets), run_time=1.5)
        self.wait(1)
        self.play(Write(seq_f), run_time=1.5)
        self.wait(1)
        self.play(Write(seq_g), run_time=1.5)
        self.wait(1)
        self.play(Write(seq_eq), run_time=1.5)
        self.wait(1)
        self.play(
            Indicate(seq_eq.get_part_by_tex(r"f_{n-1}\circ\cdots\circ f_1"), color=BLUE_B, scale_factor=1.1),
            Indicate(seq_eq.get_part_by_tex(r"g_{m-1}\circ\cdots\circ g_1"), color=ORANGE, scale_factor=1.1),
        )
        self.wait(2)

        self.play(
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2
        )
