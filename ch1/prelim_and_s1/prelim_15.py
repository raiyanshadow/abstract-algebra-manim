from manim import *


class Prelim15(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e2e"

        title = Text("Ordering", font_size=52)
        title.to_edge(UP)
        self.play(Write(title))

        setup = MathTex(
            r"\text{An ordering of a set S is a relation, written $x \preceq  y$, for $x, y \in S$ such that",
            font_size=38
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(setup))

        card = RoundedRectangle(corner_radius=0.14, width=11.0, height=3.0, color=BLUE_B)
        card.set_fill(BLUE_E, opacity=0.2)
        card.move_to(DOWN * 0.2)

        reflexive = MathTex(r"\text{Reflexive: }x\preceq x", font_size=40)
        antisymmetric = MathTex(
            r"\text{Antisymmetric: }x\preceq y,\ y\preceq x\Rightarrow x=y",
            font_size=37
        )
        transitive = MathTex(
            r"\text{Transitive: }x\preceq y,\ y\preceq z\Rightarrow x\preceq z",
            font_size=37
        )
        total_order = MathTex(
            r"\text{If additionally }\forall x,y\in S,\ x\preceq y\text{ or }y\preceq x,"
            r"\ \text{then it is a total ordering.}",
            font_size=31,
            color=YELLOW
        )
        props = VGroup(reflexive, antisymmetric, transitive, total_order).arrange(
            DOWN, aligned_edge=LEFT, buff=0.22
        )
        props.move_to(card.get_center())

        self.play(Create(card), Write(reflexive))
        self.play(Write(antisymmetric))
        self.play(Write(transitive))
        self.play(Write(total_order))
        self.wait(1.0)

        examples_box = RoundedRectangle(corner_radius=0.12, width=11.0, height=1.7, color=YELLOW_D)
        examples_box.set_fill(BLACK, opacity=0.3)
        examples_box.to_edge(DOWN, buff=0.35)
        examples = MathTex(
            r"(\mathcal P(S),\subseteq),\ (\mathbb{N},\le)",
            font_size=34
        ).move_to(examples_box)

        self.play(Create(examples_box), Write(examples))
        self.wait(2)

        self.play(LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05), run_time=2)
