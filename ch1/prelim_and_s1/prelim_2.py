from manim import *
from manim.utils.rate_functions import smooth

class Preliminary2(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY

        setA = MathTex("A", font_size=96).move_to(UP*3 + LEFT * 1.5)
        setB = MathTex("B", font_size=96).move_to(UP*3 + RIGHT * 1.5)
        text = MathTex(r"A \cup B = \{x : x \in A \: \text{or} \: x \in B\}", font_size=64)

        self.add(setA)
        self.add(setB)

        self.play(
            setA.animate.shift(RIGHT * 0.5),
            setB.animate.shift(LEFT * 0.5),
            run_time=1,
            rate_func=smooth
        )

        self.wait(0.5)

        union = MathTex(r"\cup", font_size=96).next_to(setA,RIGHT,buff=0.4)
        self.play(FadeIn(union), run_time=1, rate_func=smooth)

        self.wait(2)


        left = Circle(radius=1.5, stroke_width=0).set_fill(ORANGE, opacity=0.85)
        right = Circle(radius=1.5, stroke_width=0).set_fill(YELLOW, opacity=0.85)

        x = VGroup(left, right).arrange(RIGHT, buff=-1)

        box = Rectangle(color=BLUE, height=6, width=10).next_to(union, DOWN, buff=1).surround(x)
        
        self.play(Create(box))

        self.wait(0.3)

        
        self.play(FadeIn(x, shift=UP*0.3), run_time=0.8, rate_func=smooth)

        inter = Intersection(left, right)
        inter.set_fill(color=interpolate_color(ORANGE, YELLOW, 0.5), opacity=1)

        self.play(FadeIn(inter), run_time=0.5, rate_func=smooth)

        self.bring_to_front(setA)
        self.bring_to_front(setB)
        self.play(
            setA.animate.shift(DOWN * 3 + LEFT * 0.5),
            setB.animate.shift(DOWN * 3 + RIGHT * 0.5),
            FadeOut(union),
            run_time=1,
            rate_func=smooth
        )

        self.wait(1)

        self.play(left.animate.scale(1.5))
        self.wait(0.5)
        self.play(left.animate.scale(2/3))

        self.wait(1)

        self.play(right.animate.scale(1.5))
        self.wait(0.5)
        self.play(right.animate.scale(2/3))

        self.wait(1)

        self.play(inter.animate.scale(1.5))
        self.wait(0.5)
        self.play(inter.animate.scale(2/3))

        self.wait(1)

        self.play(
            setA.animate.shift(UP * 3 + RIGHT * 0.5),
            setB.animate.shift(UP * 3 + LEFT * 0.5),
            FadeIn(union),
            run_time=1,
            rate_func=smooth
        )

        self.wait(1)

        # Turn everything white to represent union
        self.play(
            left.animate.set_fill(WHITE, opacity=1),
            right.animate.set_fill(WHITE, opacity=1),
            FadeOut(inter),
            run_time=2,
            rate_func=smooth
        )

        self.wait(3)

        text.next_to(box, DOWN*1.5)
        self.play(Write(text), run_time=2, rate_func=smooth)
        self.wait(4)

        self.play(
            left.animate.set_fill(ORANGE),
            right.animate.set_fill(YELLOW),
            FadeIn(inter),
            run_time=1,
            rate_func=smooth
        )

        self.wait(1)
