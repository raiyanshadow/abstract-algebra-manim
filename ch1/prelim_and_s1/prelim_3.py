from manim import *
from manim.utils.rate_functions import smooth

class Preliminary3(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e2e"

        setA = MathTex("A", font_size=96).move_to(UP*3 + LEFT * 1)
        setB = MathTex("B", font_size=96).move_to(UP*3 + RIGHT * 1)
        union = MathTex(r"\cup", font_size=96).next_to(setA,RIGHT,buff=0.4)
        intersect = MathTex(r"\cap", font_size=96).next_to(setA, RIGHT, buff=0.4)
        left = Circle(radius=1.5, color=YELLOW, fill_opacity=1, stroke_width=0)
        right = Circle(radius=1.5, color=ORANGE, fill_opacity=1, stroke_width=0)
        x = VGroup(left, right).arrange(RIGHT, buff=-1)

        box = Rectangle(color=BLUE, height=6, width=10).next_to(union, DOWN, buff=1).surround(x)
        text1 = MathTex(r"A \cup B = \{x : x \in A \: \text{or} \: x \in B\}", font_size=64).next_to(box, DOWN*1.5)
        text2 = MathTex(r"A \cap B = \{x : x \in A \:\text{and}\: x\in B\}", font_size=64).next_to(box, DOWN*1.5)

        inter = Intersection(left, right)
        inter.set_fill(color=interpolate_color(ORANGE, YELLOW, 0.5), opacity=1)

        self.add(setA)
        self.add(setB)
        self.add(union)
        self.add(box)
        self.add(x)
        self.add(inter)
        self.add(text1)

        self.play(FadeOut(union), FadeOut(text1), run_time=1, rate_func=smooth)

        self.wait(1)

        self.play(FadeIn(intersect), run_time=1, rate_func=smooth)
        
        self.wait(3)

        self.play(
            left.animate.set_opacity(0.2),
            right.animate.set_opacity(0.2),
            inter.animate.set_fill(WHITE, opacity=1),
            run_time=2,
            rate_func=smooth
        )

        self.wait(1)

        self.play(Write(text2), run_time=2, rate_func=smooth)
        self.wait(3)

        self.play(
            left.animate.set_opacity(1),
            right.animate.set_opacity(1),
            inter.animate.set_fill(interpolate_color(ORANGE, YELLOW, 0.5)),
            run_time=1,
            rate_func=smooth
        )

        self.wait(1)
        