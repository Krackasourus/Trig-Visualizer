import math
from src import report as r


class Triangle:
    def __init__(self, display_out, A=0, B=0, C=0, a=0, b=0, c=0, report=False):
        print(A)
        self.angle_a = A
        print(B)
        self.angle_b = B
        print(C)
        self.angle_c = C
        print(a)
        self.side_a = a
        print(b)
        self.side_b = b
        print(c)
        self.side_c = c
        self.isReporting = (report, display_out)

    def find_angles(self):
        r.report("Calculate Angles:\n", self.isReporting)
        if self.angle_a == 0:
            self.angle_a = (180 - self.angle_b - self.angle_c)
            r.report(f"A = 180 - {self.angle_b} - {self.angle_c}\n", self.isReporting)
        elif self.angle_b == 0:
            self.angle_b = (180 - self.angle_a - self.angle_c)
            r.report(f"B = 180 - {self.angle_a} - {self.angle_c}\n", self.isReporting)
        elif self.angle_c == 0:
            self.angle_c = (180 - self.angle_a - self.angle_b)
            r.report(f"C = 180 - {self.angle_a} - {self.angle_b}\n", self.isReporting)

    def find_sides(self):
        r.report("Calculate Sides:\n", self.isReporting)
        if self.side_a == 0:
            self.side_a = math.sqrt(math.pow(self.side_c, 2) - math.pow(self.side_b, 2))
            r.report(f"     Side a = √({self.side_c}\u00b2 - {self.side_b}\u00b2)\n", self.isReporting)
        elif self.side_b == 0:
            self.side_b = math.sqrt(math.pow(self.side_c, 2) - math.pow(self.side_a, 2))
            r.report(f"{self.side_c}\u00b2 = {self.side_a}\u00b2 + b\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2)} = {pow(self.side_a, 2)} + b\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2)} - {pow(self.side_a, 2)} = b\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2) - pow(self.side_a, 2)} = b\u00b2\n", self.isReporting)
            r.report(f"√b\u00b2 = √{pow(self.side_c, 2) - pow(self.side_a, 2)}\n", self.isReporting)
            r.report(f"b ≈ {round(math.sqrt(pow(self.side_c, 2) - pow(self.side_a, 2)), 3)}\n", self.isReporting)
        elif self.side_c == 0:
            self.side_c = math.sqrt(math.pow(self.side_a, 2) + math.pow(self.side_b, 2))
            r.report(f"     Side c = √({self.side_a}\u00b2 - {self.side_b}\u00b2)\n", self.isReporting)

    def create_from_function(self, function, numerator, denominator):
        r.report("Calculate from Function:\n", self.isReporting)
        r.report(f"{function}(A) = {numerator}/{denominator}\n", self.isReporting)
        if function == "sin":
            r.report(f"    a = {numerator}, b = ?, c = {denominator}\n", self.isReporting)
            r.report("--------Find missing side b:\n", self.isReporting)
            self.side_a = numerator
            self.side_b = math.sqrt(math.pow(denominator, 2) - math.pow(numerator, 2))
            self.side_c = denominator
            r.report(f"{self.side_c}\u00b2 = {self.side_a}\u00b2 + b\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2)} = {pow(self.side_a, 2)} + b\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2)} - {pow(self.side_a, 2)} = b\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2) - pow(self.side_a, 2)} = b\u00b2\n", self.isReporting)
            r.report(f"√b\u00b2 = √{pow(self.side_c, 2) - pow(self.side_a, 2)}\n", self.isReporting)
            r.report(f"b ≈ {round(math.sqrt(pow(self.side_c, 2) - pow(self.side_a, 2)), 3)}\n", self.isReporting)

        elif function == "cos":
            r.report(f"a =?, b = {numerator}, c = {denominator}\n", self.isReporting)
            r.report("--------Find missing side a:\n", self.isReporting)
            self.side_a = math.sqrt(math.pow(denominator, 2) - math.pow(numerator, 2))
            self.side_b = numerator
            self.side_c = denominator
            r.report(f"{self.side_c}\u00b2 = a\u00b2 + {self.side_b}\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2)} = a\u00b2 + {pow(self.side_b, 2)}\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2)} - {pow(self.side_b, 2)} = a\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2) - pow(self.side_b, 2)} = a\u00b2\n", self.isReporting)
            r.report(f"√a\u00b2 = √{pow(self.side_c, 2) - pow(self.side_b, 2)}\n", self.isReporting)
            r.report(f"a = {round(math.sqrt(pow(self.side_c, 2) - pow(self.side_b, 2)), 3)}\n",
                     self.isReporting)

        elif function == "tan":
            r.report(f"    a = {numerator}, b = {denominator}, c = ?\n", self.isReporting)
            r.report("--------Find missing side c:\n", self.isReporting)
            self.side_a = numerator
            self.side_b = denominator
            self.side_c = math.sqrt(math.pow(numerator, 2) + math.pow(denominator, 2))
            r.report(f"c\u00b2 = {self.side_a}\u00b2 + {self.side_b}\u00b2\n", self.isReporting)
            r.report(f"c\u00b2 = {pow(self.side_a, 2)} + {pow(self.side_b, 2)}\n", self.isReporting)
            r.report(f"c\u00b2 = {pow(self.side_a, 2) + pow(self.side_b, 2)}\n", self.isReporting)
            r.report(f"√c\u00b2 = √{pow(self.side_a, 2) + pow(self.side_b, 2)}\n", self.isReporting)
            r.report(f"c ≈ {round(math.sqrt(pow(self.side_a, 2) + pow(self.side_b, 2)), 3)}\n",
                     self.isReporting)

        elif function == "csc":
            r.report(f"    a = {denominator}, b = ?, c = {numerator}\n", self.isReporting)
            r.report("--------Find missing side b:\n", self.isReporting)
            self.side_a = denominator
            self.side_b = math.sqrt(math.pow(numerator, 2) - math.pow(denominator, 2))
            self.side_c = numerator
            r.report(f"{self.side_c}\u00b2 = {self.side_a}\u00b2 + b\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2)} = {pow(self.side_a, 2)} + b\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2)} - {pow(self.side_a, 2)} = b\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2) - pow(self.side_a, 2)} = b\u00b2\n", self.isReporting)
            r.report(f"√b\u00b2 = √{pow(self.side_c, 2) - pow(self.side_a, 2)}\n", self.isReporting)
            r.report(f"b ≈ {round(math.sqrt(pow(self.side_c, 2) - pow(self.side_a, 2)), 3)}\n",
                     self.isReporting)

        elif function == "sec":
            r.report(f"    a = ?, b = {denominator}, c = {numerator}\n", self.isReporting)
            r.report("--------Find missing side a:", self.isReporting)
            self.side_a = math.sqrt(math.pow(numerator, 2) - math.pow(denominator, 2))
            self.side_b = denominator
            self.side_c = numerator
            r.report(f"{self.side_c}\u00b2 = a\u00b2 + {self.side_b}\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2)} = a\u00b2 + {pow(self.side_b, 2)}\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2)} - {pow(self.side_b, 2)} = a\u00b2\n", self.isReporting)
            r.report(f"{pow(self.side_c, 2) - pow(self.side_b, 2)} = a\u00b2\n", self.isReporting)
            r.report(f"√a\u00b2 = √{pow(self.side_c, 2) - pow(self.side_b, 2)}\n", self.isReporting)
            r.report(f"a = {round(math.sqrt(pow(self.side_c, 2) - pow(self.side_b, 2)), 3)}\n",
                     self.isReporting)

        else:  # cot
            r.report(f"    a = {denominator}, b = {numerator}, c = ?\n", self.isReporting)
            r.report("--------Find missing side c:\n", self.isReporting)
            self.side_a = denominator
            self.side_b = numerator
            self.side_c = math.sqrt(math.pow(denominator, 2) + math.pow(numerator, 2))
            r.report(f"c\u00b2 = {self.side_a}\u00b2 + {self.side_b}\u00b2\n", self.isReporting)
            r.report(f"c\u00b2 = {pow(self.side_a, 2)} + {pow(self.side_b, 2)}\n", self.isReporting)
            r.report(f"c\u00b2 = {pow(self.side_a, 2) + pow(self.side_b, 2)}\n", self.isReporting)
            r.report(f"√c\u00b2 = √{pow(self.side_a, 2) + pow(self.side_b, 2)}\n", self.isReporting)
            r.report(f"c ≈ {round(math.sqrt(pow(self.side_a, 2) + pow(self.side_b, 2)), 3)}\n",
                     self.isReporting)

    def print_functions(self):
        r.report("----Six trigonometric functions of angle A:\n", self.isReporting)
        r.report(f"sin(A) = {round(self.side_a, 2)}/{round(self.side_c, 2)}\n"
                 f"cos(A) = {round(self.side_b, 2)}/{round(self.side_c, 2)}\n"
                 f"tan(A) = {round(self.side_a, 2)}/{round(self.side_b, 2)}\n"
                 f"csc(A) = {round(self.side_c, 2)}/{round(self.side_a, 2)}\n"
                 f"sec(A) = {round(self.side_c, 2)}/{round(self.side_b, 2)}\n"
                 f"cot(A) = {round(self.side_b, 2)}/{round(self.side_a, 2)}\n", self.isReporting)

    def print_info(self):
        r.report("\nresults:\n", self.isReporting)
        r.report("----Angles:\n", self.isReporting)
        r.report(f"A = {round(self.angle_a, 3)}\n"
                 f"B = {round(self.angle_b, 3)}\n"
                 f"C = {round(self.angle_c, 3)}\n", self.isReporting)
        r.report("----Sides:\n", self.isReporting)
        r.report(f"a = {round(self.side_a, 3)}\n"
                 f"b = {round(self.side_b, 3)}\n"
                 f"c = {round(self.side_c, 3)}\n", self.isReporting)
        self.print_functions()
