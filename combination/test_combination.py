import unittest
import itertools

from combination import combination


class CombinationTests(unittest.TestCase):
    def test_combination_empty(self):
        gen = combination("")
        self.assertRaises(ValueError, gen.next)

    def test_combination_1_letter(self):
        input_word = "r"
        output_list = map(lambda x: "".join(["r" for i in range(x)]),
                          range(1, 6))
        # equivalent to
        # output_list = ['r', 'rr', 'rrr', 'rrrr', 'rrrrr']
        result_5th = [word for word in
                      itertools.islice(combination(input_word), 5)]
        self.assertEqual(sorted(output_list), sorted(result_5th))

    def test_combination_3_letters(self):
        input_word = "ors"
        output_list = ['o', 'r', 's', 'or', 'os', 'rs', 'so', 'ro', 'sr',
                       'rr', 'ss', 'oo']
        result_12th = [word for word in
                       itertools.islice(combination(input_word), 12)]
        self.assertEqual(sorted(output_list), sorted(result_12th))


if __name__ == '__main__':
    unittest.main()
