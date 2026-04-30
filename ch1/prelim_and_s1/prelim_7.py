from manim import *
import numpy as np


class Prelim7(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY

        title = Tex("Subsets").to_edge(UP)
        self.play(Write(title))

        main_center = DOWN*1
        B = Circle(radius=1.85, color=BLUE).move_to(main_center)
        A = Circle(radius=0.95, color=GREEN).move_to(B.get_center() + UP * 0.1)
        label_B = MathTex("B").next_to(B, UP, buff=0.12)
        label_A = MathTex("A").next_to(A, UP, buff=0.12)

        self.play(Create(B), Create(A), Write(label_B), Write(label_A))
        self.wait(0.6)

        subset_note = MathTex("A \\subseteq B").next_to(title, DOWN, buff=0.35)
        self.play(Write(subset_note))
        self.wait(0.8)

        center_A = A.get_center()
        angles = np.linspace(0, 2 * np.pi, 5)[:-1]
        elems = VGroup(*[Dot(center_A + 0.45 * np.array([np.cos(t), np.sin(t), 0]), color=YELLOW) for t in angles])
        labels = VGroup(
            *[
                MathTex(f"a_{i+1}").scale(0.58).move_to(
                    elems[i].get_center() + 0.22 * np.array([np.cos(angles[i]), np.sin(angles[i]), 0])
                )
                for i in range(len(elems))
            ]
        )
        self.play(FadeIn(elems), Write(labels))
        self.wait(1.0)

        first_example_group = VGroup(B, A, label_B, label_A, elems, labels, subset_note)
        self.wait(1)
        self.play(FadeOut(first_example_group))
        self.wait(0.3)

        C = Circle(radius=1.0, color=RED).move_to(ORIGIN + LEFT * 0.35 + DOWN * 0.35)
        label_C = MathTex(r"C").next_to(C, UP, buff=0.12)
        A2 = Circle(radius=1.0, color=GREEN).move_to(ORIGIN + RIGHT * 0.15 + DOWN * 0.25)
        label_A2 = MathTex(r"A'").next_to(A2, UP, buff=0.12)

        self.play(Create(C), Write(label_C))
        self.wait(0.4)
        self.play(Create(A2), Write(label_A2))
        self.wait(0.6)

        outside_point = Dot(A2.get_center() + RIGHT * 0.85, color=YELLOW)
        outside_label = MathTex(r"x").scale(0.7).next_to(outside_point, RIGHT, buff=0.12)
        self.play(FadeIn(outside_point), Write(outside_label))
        self.wait(0.6)

        left_diagram = VGroup(C, A2, label_C, label_A2, outside_point, outside_label)
        not_subset_note = Tex(r"$A' \not\subseteq C$").next_to(left_diagram, DOWN, buff=0.25)
        self.play(Write(not_subset_note))
        self.play(Indicate(not_subset_note, scale_factor=1.1))
        self.wait(1.0)

        self.play(FadeOut(left_diagram), FadeOut(not_subset_note))
        self.wait(0.4)

        summary = Tex(r"If every element of $A$ is in $B$, then $A \subseteq B$")
        proper_note = Tex(r"If $A \neq B$, then $A$ is a proper subset of $B$ (proper means $A \subset B$).")
        proper_note.next_to(summary, DOWN, buff=0.3).scale(0.85)

        self.play(Write(summary))
        self.play(Write(proper_note))
        self.wait(3.2)

        self.play(
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2
        )
