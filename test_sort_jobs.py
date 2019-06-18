import unittest
from jobsorter import JobSorter


class TestSortJobs(unittest.TestCase):
    def test_empty_string_should_return_empty_string(self):
        """ When passed an empty string - 
        an empty string should be returned
        """

        result = JobSorter.sort_jobs('')
        self.assertEqual(result, '')


if __name__ == "__main__":
    unittest.main()
