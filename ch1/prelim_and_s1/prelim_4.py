from manim import *
from manim.utils.rate_functions import smooth

class Preliminary4(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e2e"

        setA = MathTex("A", font_size=96).move_to(UP*3 + LEFT * 1)
        setB = MathTex("B", font_size=96).move_to(UP*3 + RIGHT * 1)

        intersect = MathTex(r"\cap", font_size=96).next_to(setA, RIGHT, buff=0.4)
        left = Circle(radius=1.5, color=YELLOW, fill_opacity=1, stroke_width=0)
        right = Circle(radius=1.5, color=ORANGE, fill_opacity=1, stroke_width=0)
        x = VGroup(left, right).arrange(RIGHT, buff=-1)

        box = Rectangle(color=BLUE, height=6, width=10).next_to(intersect, DOWN, buff=1).surround(x)

        text1 = MathTex(r"A \cap B = \{x : x \in A \:\text{and}\: x\in B\}", font_size=64).next_to(box, DOWN*1.5)
        text2 = MathTex(r"A \backslash B = \{x : x \in A \:\text{and}\: x \notin B\}", font_size=64).next_to(box, DOWN*1.5)
        text3 = MathTex(r"B \backslash A = \{x : x \notin A \:\text{and}\: x \in B\}", font_size=64).next_to(box, DOWN*1.5)


        inter = Intersection(left, right)
        inter.set_fill(color=interpolate_color(ORANGE, YELLOW, 0.5), opacity=1)

        delete = MathTex(r"\backslash", font_size=96).next_to(setA, RIGHT, buff=0.4)

        diffAB = Difference(left, right)
        diffAB.set_fill(WHITE, opacity=1).set_stroke(width=0)

        diffBA = Difference(right, left)
        diffBA.set_fill(WHITE, opacity=1).set_stroke(width=0)

        self.add(setA)
        self.add(setB)
        self.add(box)
        self.add(x)
        self.add(inter)
        self.add(text1)
        self.add(intersect)

        self.wait(1)

        self.play(FadeOut(intersect), FadeOut(text1), run_time=1, rate_func=smooth)

        self.wait(1)

        self.play(FadeIn(delete), run_time=1, rate_func = smooth)

        self.wait(1)

        self.play(left.animate.set_opacity(0.2),
                  right.animate.set_opacity(0.2),
                  inter.animate.set_opacity(0.2),
                  FadeIn(diffAB),
                  Write(text2),
                  run_time=2,
                  rate_func=smooth)
        
        self.wait(3)

        self.play(FadeOut(diffAB),
                  FadeIn(diffBA),
                  Transform(text2, text3),
                  Swap(setA, setB),
                  run_time=3,
                  rate_func=smooth)
        
        self.wait(6)

        self.play(FadeOut(diffBA),
                  left.animate.set_opacity(1),
                  right.animate.set_opacity(1),
                  inter.animate.set_opacity(1),
                  Swap(setA, setB),
                  FadeOut(text2),
                  FadeOut(delete),
                  run_time=3,
                  rate_func=smooth)
        
        self.wait(1)

        self.play(FadeOut(setA), FadeOut(setB), FadeOut(left), FadeOut(right), FadeOut(box), FadeOut(inter), run_time=2, rate_func=smooth)
        self.wait(1)

        