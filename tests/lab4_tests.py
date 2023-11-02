import unittest
from src.lab4 import read_input, shortest_path, write_result


class TestShortestPath(unittest.TestCase):
    def test_shortest_path_empty_input(self):
        matrix = []
        result = shortest_path(matrix)
        self.assertEqual(result, -1)

    def test_shortest_path_no_path(self):
        matrix = [[0, 0, 0], [1, 0, 1], [0, 1, 0]]
        result = shortest_path(matrix)
        self.assertEqual(result, -1)

    def test_shortest_path_valid_input(self):
        input_matrix = read_input('input.txt')
        result = shortest_path(input_matrix)
        write_result(result, 'output.txt')

        with open('expected.txt', 'r') as expected_file:
            expected_result = int(expected_file.read().strip())
        self.assertEqual(result, expected_result)
