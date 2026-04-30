from manim import *


class Prelim12(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY

        title = Text("Commonly Used Sets", font_size=52)
        title.to_edge(UP)
        self.play(Write(title))

        bottom_panel = RoundedRectangle(corner_radius=0.16, width=8.4, height=2.2, color=GRAY_B)
        bottom_panel.set_fill(BLACK, opacity=0.25)
        bottom_panel.move_to(DOWN * 1.5)

        subtitle = Text("Example", font_size=32, color=YELLOW_A).move_to(bottom_panel.get_top() + DOWN * 0.3)

        card_specs = [
            (
                BLUE_B,
                BLUE_E,
                MathTex(r"\mathbb{Z}: \text{integers}=\{\ldots,-2,-1,0,1,2,\ldots\}", font_size=34),
                MathTex(r"-3,\,0,\,14 \in \mathbb{Z}", font_size=38),
            ),
            (
                GREEN_B,
                GREEN_E,
                MathTex(r"\mathbb{Q}: \text{rationals}=\left\{\frac{p}{q}:p,q\in\mathbb{Z},\,q\neq 0\right\}", font_size=33),
                MathTex(r"\frac{2}{3},\,-\frac{7}{5}\in\mathbb{Q}", font_size=38),
            ),
            (
                YELLOW_B,
                YELLOW_E,
                MathTex(r"\mathbb{R}: \text{real numbers}", font_size=40),
                MathTex(r"\sqrt{2},\,\pi \in \mathbb{R}", font_size=36),
            ),
            (
                ORANGE,
                ORANGE,
                MathTex(r"\mathbb{R}^n: \text{all }n\text{-tuples of real numbers}", font_size=34),
                MathTex(r"(1,2)\in\mathbb{R}^2,\ (0,-1,4)\in\mathbb{R}^3", font_size=34),
            ),
        ]

        self.play(Create(bottom_panel), FadeIn(subtitle, shift=UP * 0.2))

        current_card = None
        current_def = None
        current_example = None

        for border_color, fill_color, definition_tex, example_tex in card_specs:
            card = RoundedRectangle(corner_radius=0.14, width=8.8, height=1.8, color=border_color)
            card.set_fill(fill_color, opacity=0.2)
            card.move_to(UP * 0.85)
            definition_tex.move_to(card.get_center())
            example_tex.move_to(bottom_panel
.get_center())

            if current_card is None:
                self.play(Create(card), Write(definition_tex), Write(example_tex), run_time=1.3)
            else:
                self.play(
                    ReplacementTransform(current_card, card),
                    ReplacementTransform(current_def, definition_tex),
                    ReplacementTransform(current_example, example_tex),
                    run_time=1.1
                )
            self.wait(0.8)
            current_card = card
            current_def = definition_tex
            current_example = example_tex

        summary = Tex(
            r"$\mathbb{Z}\subseteq\mathbb{Q}\subseteq\mathbb{R}\subseteq\mathbb{C}$",
            font_size=34,
            color=YELLOW
        ).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)

        self.play(
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2
        )
