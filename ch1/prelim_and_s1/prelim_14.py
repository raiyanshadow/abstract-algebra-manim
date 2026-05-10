from manim import *


class Prelim14(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e2e"

        title = Text("Equivalence Classes and Well-Defined Maps", font_size=46)
        title.to_edge(UP)
        self.play(Write(title))

        setup_text = MathTex(
            r"\text{Let }A\text{ be a set with equivalence relation }R."
            r"\ \text{Let }\mathcal{E}=A/{\sim}\text{ be the set of equivalence classes.}",
            font_size=33
        ).next_to(title, DOWN, buff=0.45)

        class_line_1 = MathTex(
            r"[x]=\{y\in A: y\sim x\}\in\mathcal{E}",
            font_size=42
        )
        class_line_2 = MathTex(
            r"x\sim y\ \Longrightarrow\ [x]=[y]",
            font_size=38
        )
        class_group = VGroup(class_line_1, class_line_2).arrange(DOWN, buff=0.45).move_to(DOWN * 0.2)

        self.play(Write(setup_text))
        self.play(Write(class_line_1))
        self.play(Write(class_line_2))
        self.wait(1.2)

        map_line_1 = MathTex(
            r"\text{Define a map on classes: }f:\mathcal{E}\to B.",
            font_size=38
        )
        map_line_2 = MathTex(
            r"\text{Often we first give a formula on representatives }x\in A,",
            font_size=31
        )
        map_line_3 = MathTex(
            r"\text{then check it depends only on the class }[x].",
            font_size=31
        )
        map_group = VGroup(map_line_1, map_line_2, map_line_3).arrange(DOWN, buff=0.35).move_to(DOWN * 0.3)

        self.play(
            ReplacementTransform(class_group, map_group),
        )
        self.wait(1.2)

        wd_line_1 = MathTex(
            r"\text{If }x\sim y\ \Rightarrow\ \phi(x)=\phi(y),"
            r"\ \text{then }f([x])=\phi(x)\text{ is independent of representative.}",
            font_size=30
        )
        wd_line_2 = MathTex(
            r"\text{So }f:\mathcal{E}\to B\ \text{is well-defined.}",
            font_size=38,
            color=YELLOW
        )
        wd_group = VGroup(wd_line_1, wd_line_2).arrange(DOWN, buff=0.5).move_to(DOWN * 0.45)

        self.play(ReplacementTransform(map_group, wd_group))
        self.wait(2)

        self.play(
            LaggedStart(*[FadeOut(mob) for mob in self.mobjects], lag_ratio=0.05),
            run_time=2
        )
