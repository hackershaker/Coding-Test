from unittest import TestCase, main
import importlib

p86052 = importlib.import_module("86052")

class testClass(TestCase):

    def testvalidord(self):
        self.assertEqual(p86052.validord([1,2], ["SL", "LR"]), (1,0))
        self.assertEqual(p86052.validord([-1,0], ["SL", "LR"]), (1,0))

    def testReflect(self):
        # L
        self.assertEqual(p86052.reflect((1,0), (-1,0), ["SL", "LR"]), ((1,1), (0,1)))
        self.assertEqual(p86052.reflect((1,0), (1,0), ["SL", "LR"]), ((1,1), (0,-1)))
        self.assertEqual(p86052.reflect((1,0), (0,-1), ["SL", "LR"]), ((0,0), (-1,0)))
        self.assertEqual(p86052.reflect((1,0), (0,1), ["SL", "LR"]), ((0,0), (1,0)))

        self.assertEqual(p86052.reflect((1,1), (0,1), ["LSR", "SLR", "LRS"]), ((0,1), (1,0)))
        self.assertEqual(p86052.reflect((1,1), (0,-1), ["LSR", "SLR", "LRS"]), ((2,1), (-1,0)))
        self.assertEqual(p86052.reflect((1,1), (1,0), ["LSR", "SLR", "LRS"]), ((1,0), (0,-1)))
        self.assertEqual(p86052.reflect((1,1), (-1,0), ["LSR", "SLR", "LRS"]), ((1,2), (0,1)))

        #R
        self.assertEqual(p86052.reflect((1,1), (0,1), ["SL", "LR"]), ((0,1), (-1,0)))
        self.assertEqual(p86052.reflect((1,1), (0,-1), ["SL", "LR"]), ((0,1), (1,0)))
        self.assertEqual(p86052.reflect((1,1), (1,0), ["SL", "LR"]), ((1,0), (0,1)))
        self.assertEqual(p86052.reflect((1,1), (-1,0), ["SL", "LR"]), ((1,0), (0,-1)))

        self.assertEqual(p86052.reflect((1,2), (0,1), ["LSR", "SLR", "LRS"]), ((2,2), (-1,0)))
        self.assertEqual(p86052.reflect((1,2), (0,-1), ["LSR", "SLR", "LRS"]), ((0,2), (1,0)))
        self.assertEqual(p86052.reflect((1,2), (1,0), ["LSR", "SLR", "LRS"]), ((1,0), (0,1)))
        self.assertEqual(p86052.reflect((1,2), (-1,0), ["LSR", "SLR", "LRS"]), ((1,1), (0,-1)))

        #S
        self.assertEqual(p86052.reflect((0,0), (0,1), ["SL", "LR"]), ((0,1), (0,1)))
        self.assertEqual(p86052.reflect((0,0), (0,-1), ["SL", "LR"]), ((0,1), (0,-1)))
        self.assertEqual(p86052.reflect((0,0), (1,0), ["SL", "LR"]), ((1,0), (1,0)))
        self.assertEqual(p86052.reflect((0,0), (-1,0), ["SL", "LR"]), ((1,0), (-1,0)))

        self.assertEqual(p86052.reflect((0,1), (0,1), ["LSR", "SLR", "LRS"]), ((0,2), (0,1)))
        self.assertEqual(p86052.reflect((0,1), (0,-1), ["LSR", "SLR", "LRS"]), ((0,0), (0,-1)))
        self.assertEqual(p86052.reflect((0,1), (1,0), ["LSR", "SLR", "LRS"]), ((2,1), (1,0)))
        self.assertEqual(p86052.reflect((0,1), (-1,0), ["LSR", "SLR", "LRS"]), ((1,1), (-1,0)))

    def testsolution(self):
        testcase = [
            (["SL", "LR"], [16]),
            (["S"], [1, 1, 1, 1]),
            (["R", "R"], [4, 4]),
            (["R", "R"], [4, 4]),
            (["LSR"], [1,1,4,6]),
            (["LS"], [1,1,6]),
        ]
        for grid, answer in testcase:
            result = p86052.testsolution(grid)
            for path in result:
                for r in path:
                    print(r[0], end=' ')
                    if r[1] == (1,0): print("ᐱ", end=" ")
                    if r[1] == (-1,0): print("ᐯ", end=" ")
                    if r[1] == (0,1): print("ᐳ", end=" ")
                    if r[1] == (0,-1): print("ᐸ", end=" ")
                print("\n")
            self.assertEqual(p86052.solution(grid), answer, f"{grid}, {answer}")
            print("===================================================================")
if __name__=="__main__":
    main()