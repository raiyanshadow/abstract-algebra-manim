from manim import *


class Prelim13(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY

        title = Text("Equivalence Relation", font_size=52)
        title.to_edge(UP)
        self.play(Write(title))

        setup = MathTex(
            r"\text{For a set }A,\ R\subseteq A\times A\ \text{is an equivalence relation if:}",
            font_size=36
        ).next_to(title, DOWN, buff=0.35)
        self.play(Write(setup))

        card = RoundedRectangle(corner_radius=0.14, width=11.6, height=2.15, color=BLUE_B)
        card.set_fill(BLUE_E, opacity=0.18)
        card.move_to(ORIGIN + DOWN * 0.3)

        reflexive_title = Text("Reflexive", font_size=36, color=BLUE_B).move_to(card.get_top() + DOWN * 0.45)
        reflexive_formula = MathTex(
            r"(x,x)\in R\ \text{for all }x\in A",
            font_size=42
        ).move_to(card.get_center() + DOWN * 0.15)

        symmetric_title = Text("Symmetric", font_size=36, color=GREEN_B).move_to(card.get_top() + DOWN * 0.45)
        symmetric_formula = MathTex(
            r"(x,y)\in R\ \Rightarrow\ (y,x)\in R",
            font_size=42
        ).move_to(card.get_center() + DOWN * 0.15)

        transitive_title = Text("Transitive", font_size=36, color=YELLOW).move_to(card.get_top() + DOWN * 0.45)
        transitive_formula = MathTex(
            r"(x,y)\in R\ \text{ and }\ (y,z)\in R\ \Rightarrow\ (x,z)\in R",
            font_size=38
        ).move_to(card.get_center() + DOWN * 0.15)

        self.play(Create(card), Write(reflexive_title), Write(reflexive_formula))
        self.wait(1.0)

        self.play(
            ReplacementTransform(reflexive_title, symmetric_title),
            ReplacementTransform(reflexive_formula, symmetric_formula)
        )
        self.wait(1.0)

        self.play(
            ReplacementTransform(symmetric_title, transitive_title),
            ReplacementTransform(symmetric_formula, transitive_formula)
        )
        self.wait(1.2)

        notation_box = RoundedRectangle(corner_radius=0.12, width=11.6, height=1.55, color=ORANGE)
        notation_box.set_fill(BLACK, opacity=0.3)
        notation_box.to_edge(DOWN, buff=0.4)

        notation = MathTex(
            r"\text{Given an equivalence relation }R\text{ on }A,\ "
            r"x\sim y\ \text{means}\ (x,y)\in R.",
            font_size=36
        ).move_to(notation_box)

        self.play(Create(notation_box), Write(notation))
        self.wait(2)

        self.play(
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2
        )
