import tracemalloc
from unittest import TestCase, main
import importlib


problem = importlib.import_module('cheapest-flights-within-k-stops')


class testClass(TestCase):
    testcase = [
        ((4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1), 700),
        ((5,[[0,1,2],[0,2,5],[0,3,3],[0,4,6],[2,1,1],[3,1,3],[4,1,2],[2,3,5],[2,4,3],[3,4,6],],0,4,3), 6),
    ]


    def test1000(self):
        solution = problem.Solution()
        for case, answer in testClass.testcase:
            tracemalloc.start()
            self.assertEqual(solution.findCheapestPrice(*case), answer)
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')

            for stat in top_stats[:10]:
                print(stat)


if __name__=='__main__':
    main()