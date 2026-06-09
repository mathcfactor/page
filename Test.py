from manim import *

class FactorDemo(Scene):
    def setup(self):
        self.camera.background_color = WHITE

    def construct(self):
        t1 = MathTex("25 - 16", color=BLACK).scale(1.5).to_edge(UP)
        t2 = MathTex("(5-4)(5+4)", color=BLACK).scale(1.5).to_edge(UP)
        t3 = MathTex("(1)(9)", color=BLACK).scale(1.5).to_edge(UP)
        t4 = MathTex("9", color=BLACK).scale(1.5).to_edge(UP)
        checkmark = MathTex(r"\checkmark", color=GREEN).scale(2).next_to(t4, RIGHT)

        self.add(t1)
        self.wait(1)
        self.play(Transform(t1, t2))
        self.wait(1)
        self.play(Transform(t1, t3))
        self.wait(1)
        self.play(Transform(t1, t4))
        self.wait(1)
        self.play(FadeIn(checkmark))
        self.wait(1)