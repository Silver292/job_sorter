import unittest
from jobsorter import JobSorter


class TestSortJobs(unittest.TestCase):
    def test_empty_string_should_return_empty_string(self):
        """ No Jobs:
        When passed an empty string - 
        an empty string should be returned
        """

        result = JobSorter.sort_jobs("")
        self.assertEqual(result, "")

    def test_when_passed_independent_job_should_return_job(self):
        """One job:
        When passed a dictionary of one job with no dependencies, 
        the function should return a list containing only the job.
        """

        result = JobSorter.sort_jobs({"a": ""})
        self.assertEqual(result, ["a"])




if __name__ == "__main__":
    unittest.main()
