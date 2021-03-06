from matplotlib import pyplot as plt
from typing import List, Dict, Tuple


from components.page_replacement.algorithms.algorithm import Algorithm
from components.page_replacement.process import Process


class MemoryManager:

    COLORS = ['red', 'blue', 'purple', 'orange', 'green']

    def __init__(self, num_of_pages: int):
        self.pages = self.__setup_pages(num_of_pages)

    def __setup_pages(self, num_of_pages: int) -> List[int]:
        """
        Setup list of pages allowed to be used by processes
        :param num_of_pages: number of pages in memory
        :return: list of pages
        """
        self.pages = [i for i in range(1, num_of_pages)]
        return self.pages

    def __execute(self, algorithm: Algorithm, process: Process):
        """
        Execute process
        :param algorithm: Algorithm inheriting class
        :param processes: list of processes
        :return:
        """
        alg = algorithm(len(self.pages), process)
        alg.execute()
        return alg.get_history(), alg.get_deficiencies(), alg.get_name()

    def __plot_results(self, deficiencies: List, names: List[str]) -> None:
        """
        Plots results and compare algorithms
        :param deficiencies: list of page rewounds
        :param names: names of algorithms
        :return:
        """
        bar_heights = [len(dfn) for dfn in deficiencies]
        plt.bar(x=names, height=bar_heights, color=self.COLORS)
        plt.show()

    def setup_processes(self, length_of_process: int, num_of_pages: int):
        self.process = Process(length_of_process, num_of_pages)

    def execute_all(self, algorithms: List[Algorithm]) -> Tuple[list, list]:
        """
        Execute all algorithms
        :param algorithms: list of algorithm inheriting classes
        :return:
        """
        deficiencies = list()
        histories = list()
        names = list()
        for algorithm in algorithms:
            history, defs, name = self.__execute(algorithm, self.process)
            names.append(name)
            histories.append(history)
            deficiencies.append(defs)
        #self.__plot_results(deficiencies, names)
        return deficiencies, names
