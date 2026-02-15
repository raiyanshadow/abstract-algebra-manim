from manim import *


class Prelim10(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY

        title = Text("Inverse Image, Image, and Restriction", font_size=44)
        title.to_edge(UP)
        self.play(Write(title))

        set_a = Ellipse(width=2.4, height=4.3, color=BLUE_D)
        set_a.set_fill(BLUE_E, opacity=0.2)
        set_a.move_to(LEFT * 3 + DOWN * 0.15)

        set_b = Ellipse(width=2.8, height=4.6, color=GREEN_D)
        set_b.set_fill(GREEN_E, opacity=0.2)
        set_b.move_to(RIGHT * 3 + DOWN * 0.15)

        label_a = MathTex("A").next_to(set_a, DOWN, buff=0.12)
        label_b = MathTex("B").next_to(set_b, DOWN, buff=0.12)
        map_label = MathTex(r"f:A\to B", font_size=46).move_to(UP * 1.5)

        a1 = Dot(set_a.get_center() + UP * 1.1 + LEFT * 0.15, color=BLUE_B)
        a2 = Dot(set_a.get_center() + UP * 0.2 + LEFT * 0.05, color=BLUE_B)
        a3 = Dot(set_a.get_center() + DOWN * 0.9 + LEFT * 0.1, color=BLUE_B)

        b1 = Dot(set_b.get_center() + UP * 1.25 + RIGHT * 0.05, color=GREEN_B)
        b2 = Dot(set_b.get_center() + UP * 0.35 + RIGHT * 0.05, color=GREEN_B)
        b3 = Dot(set_b.get_center() + DOWN * 0.55 + RIGHT * 0.02, color=GREEN_B)
        b4 = Dot(set_b.get_center() + DOWN * 1.35 + RIGHT * 0.02, color=GREEN_B)

        arr1 = Arrow(a1.get_right(), b1.get_left(), buff=0.08, stroke_width=3, color=YELLOW)
        arr2 = Arrow(a2.get_right(), b2.get_left(), buff=0.08, stroke_width=3, color=YELLOW)
        arr3 = Arrow(a3.get_right(), b3.get_left(), buff=0.08, stroke_width=3, color=YELLOW)
        core_diagram = VGroup(
            set_a, set_b, label_a, label_b, map_label,
            a1, a2, a3, b1, b2, b3, b4, arr1, arr2, arr3
        )

        self.play(
            Create(set_a), Create(set_b), Write(label_a), Write(label_b), Write(map_label),
            FadeIn(VGroup(a1, a2, a3, b1, b2, b3, b4))
        )
        self.play(GrowArrow(arr1), GrowArrow(arr2), GrowArrow(arr3))
        self.wait(0.6)

        b_prime = Ellipse(width=1.6, height=2.2, color=TEAL_A)
        b_prime.set_fill(TEAL_D, opacity=0.25)
        b_prime.move_to(set_b.get_center() + UP * 0.1)
        label_b_prime = MathTex(r"B'").scale(0.8).next_to(b_prime, RIGHT, buff=0.08)

        inverse_text = MathTex(
            r"f^{-1}(B')=\{x\in A\mid f(x)\in B'\}",
            font_size=36
        ).to_edge(DOWN).shift(LEFT * 1.1)
        inverse_note_text = Tex(
            r"Inverse image under $f$:\\"
            r"$x\in f^{-1}(B') \Leftrightarrow f(x)\in B'$",
            font_size=26
        )
        inverse_note_bg = RoundedRectangle(
            corner_radius=0.12,
            width=inverse_note_text.width + 0.35,
            height=inverse_note_text.height + 0.28,
            color=YELLOW_D
        )
        inverse_note_bg.set_fill(BLACK, opacity=0.82)
        inverse_note_bg.set_stroke(width=2)
        inverse_note = VGroup(inverse_note_bg, inverse_note_text).to_corner(UR).shift(LEFT * 0.2 + DOWN * 0.7)
        inverse_text.set_color_by_tex(r"f^{-1}(B')", YELLOW)

        self.play(Create(b_prime), Write(label_b_prime))
        self.play(
            core_diagram.animate.shift(LEFT * 1.1),
            b_prime.animate.shift(LEFT * 1.1),
            label_b_prime.animate.shift(LEFT * 1.1),
            Write(inverse_text),
            Write(inverse_note)
        )
        preimage_part = inverse_text.get_part_by_tex(r"f^{-1}(B')")
        self.play(
            Indicate(b2, color=TEAL_A, scale_factor=1.2),
            Indicate(b3, color=TEAL_A, scale_factor=1.2),
            Indicate(a2, color=YELLOW, scale_factor=1.2),
            Indicate(a3, color=YELLOW, scale_factor=1.2),
            Indicate(preimage_part, color=YELLOW, scale_factor=1.12),
            run_time=1.2
        )
        self.wait(1.6)

        image_text = MathTex(
            r"f(A)=\{f(x)\mid x\in A\}",
            font_size=36
        ).to_edge(DOWN).shift(LEFT * 1.1)
        image_note_text = Tex(r"$f(A)$ is the image of $f$", font_size=28)
        image_note_bg = RoundedRectangle(
            corner_radius=0.12,
            width=image_note_text.width + 0.35,
            height=image_note_text.height + 0.28,
            color=YELLOW_D
        )
        image_note_bg.set_fill(BLACK, opacity=0.82)
        image_note_bg.set_stroke(width=2)
        image_note = VGroup(image_note_bg, image_note_text).move_to(inverse_note)

        image_points = VGroup(b1, b2, b3)
        image_box = SurroundingRectangle(image_points, color=YELLOW, buff=0.2)
        self.play(
            Transform(inverse_text, image_text),
            ReplacementTransform(inverse_note, image_note)
        )
        image_part = inverse_text.get_part_by_tex(r"f(A)")
        if image_part is None:
            image_part = inverse_text
        self.play(Create(image_box))
        self.play(
            Indicate(image_points, color=YELLOW, scale_factor=1.12),
            Indicate(image_part, color=YELLOW, scale_factor=1.12)
        )
        self.wait(1.4)

        a_prime = Ellipse(width=1.55, height=2.1, color=PURPLE_A)
        a_prime.set_fill(PURPLE_D, opacity=0.22)
        a_prime.move_to(set_a.get_center() + DOWN * 0.35)
        label_a_prime = MathTex(r"A'").scale(0.8).next_to(a_prime, LEFT, buff=0.08)

        restriction_text = MathTex(
            r"A'\subseteq A,\quad f|_{A'}:A'\to f(A')",
            font_size=36
        ).to_edge(DOWN).shift(LEFT * 1.1)
        restriction_note_text = Tex(
            r"$f|_{A'}$ is the restriction\\",
            r"of $f$ under A'",
            font_size=26
        )
        restriction_note_bg = RoundedRectangle(
            corner_radius=0.12,
            width=restriction_note_text.width + 0.35,
            height=restriction_note_text.height + 0.28,
            color=ORANGE
        )
        restriction_note_bg.set_fill(BLACK, opacity=0.82)
        restriction_note_bg.set_stroke(width=2)
        restriction_note = VGroup(restriction_note_bg, restriction_note_text).move_to(image_note)

        restricted_arrow_2 = Arrow(a2.get_right(), b2.get_left(), buff=0.08, stroke_width=5, color=ORANGE)
        restricted_arrow_3 = Arrow(a3.get_right(), b3.get_left(), buff=0.08, stroke_width=5, color=ORANGE)
        image_aprime_box = SurroundingRectangle(VGroup(b2, b3), color=ORANGE, buff=0.18)

        self.play(
            FadeOut(image_box),
            Create(a_prime),
            Write(label_a_prime),
            Transform(inverse_text, restriction_text),
            ReplacementTransform(image_note, restriction_note)
        )
        restriction_part = inverse_text.get_part_by_tex(r"f|_{A'}")
        if restriction_part is None:
            restriction_part = inverse_text
        restriction_part.set_color(ORANGE)
        self.play(
            GrowArrow(restricted_arrow_2),
            GrowArrow(restricted_arrow_3),
            Create(image_aprime_box),
            Indicate(restriction_part, color=ORANGE, scale_factor=1.12),
        )
        self.wait(2)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )
