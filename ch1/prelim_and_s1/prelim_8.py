from manim import *


class Prelim8(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY
        title = Text("Cardinality of a Set", font_size=56)
        title.to_edge(UP)

        set_box = RoundedRectangle(corner_radius=0.2, width=5.6, height=3.2)
        set_box.set_stroke(BLUE_D, width=4)
        set_box.set_fill(BLUE_E, opacity=0.15)

        elements = VGroup(
            MathTex("a"),
            MathTex("b"),
            MathTex("c"),
            MathTex("d"),
        )
        elements.arrange_in_grid(rows=2, cols=2, buff=0.8)
        elements.move_to(set_box.get_center())

        set_label = MathTex("A").next_to(set_box, DOWN*1.5, buff=0.2)

        cardinality_expr = MathTex(r"\#(A)=4")
        cardinality_expr.scale(1.4)
        cardinality_expr.to_edge(RIGHT).shift(UP * 0.3)
        cardinality_expr.set_color(YELLOW)

        arrow = Arrow(
            start=set_box.get_right() + RIGHT * 0.1,
            end=cardinality_expr.get_left() + LEFT * 0.2,
            buff=0.1,
            stroke_width=6,
        )
        arrow.set_color(YELLOW)

        cardinality_note = Text("size (cardinality)", font_size=32)
        cardinality_note.next_to(cardinality_expr, DOWN, buff=0.3)
        cardinality_note.set_color(YELLOW_A)

        self.play(Write(title))
        self.play(Create(set_box), FadeIn(elements, shift=UP * 0.2), Write(set_label), run_time=1)
        self.wait(4)

        self.play(
            GrowArrow(arrow),
            Write(cardinality_expr),
            FadeIn(cardinality_note, shift=UP * 0.2),
        )
        self.wait(2)

        emphasis = SurroundingRectangle(cardinality_expr, color=YELLOW, buff=0.2)
        self.play(Create(emphasis))
        self.wait(1)

        self.play(
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2
        )
