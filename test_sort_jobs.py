import unittest
from jobsorter import JobSorter


class TestSortJobs(unittest.TestCase):
    def test_empty_string_should_return_empty_string(self):
        """ No Jobs:
        When passed an empty string - 
        an empty string should be returned
        """

        job_sorter = JobSorter("")
        result = job_sorter.sort_jobs()
        self.assertEqual(result, "")

    def test_when_passed_independent_job_should_return_job(self):
        """ One job:
        When passed a dictionary of one job with no dependencies, 
        the function should return a list containing only the job.
        """

        job_sorter = JobSorter({"a": ""})
        result = job_sorter.sort_jobs()
        self.assertEqual(result, ["a"])

    def test_multiple_jobs_no_dependencies(self):
        """ Multiple jobs no dependencies:
        When passed a dictionary of jobs with no dependencies
        the function should return the jobs in no particular order
        """

        jobs = {"a": "", "b": "", "c": ""}
        job_sorter = JobSorter(jobs)
        result = job_sorter.sort_jobs()
        self.assertCountEqual(result, ["a", "b", "c"])

    def test_multiple_jobs_one_dependency(self):
        """ Multiple jobs one dependency:
        When passed multiple jobs, one of which is dependent on
        another, the dependent job should be after its dependency
        in the returned list. 
        """

        jobs = {"a": "", "b": "c", "c": ""}
        job_sorter = JobSorter(jobs)
        result = job_sorter.sort_jobs()

        # all jobs should be in returned list
        self.assertCountEqual(result, list(jobs.keys()))

        # get subset of job and dependencies
        expected_subset = ["c", "b"]
        actual_subset = list(filter(lambda x: x in expected_subset, result))

        # dependent jobs should be after dependencies
        self.assertEqual(actual_subset, expected_subset)

    def test_multiple_jobs_with_dependencies(self):
        jobs = {"a": "", "b": "c", "c": "f", "d": "a", "e": "b", "f": ""}

        job_sorter = JobSorter(jobs)
        result = job_sorter.sort_jobs()

        # all jobs should be in returned list
        self.assertCountEqual(result, list(jobs.keys()))

        # get subset of job and dependency
        expected_subset = ["f", "c", "b", "e"]
        actual_subset = list(filter(lambda x: x in expected_subset, result))

        # dependent job should be after dependency
        self.assertEqual(actual_subset, expected_subset)

        expected_subset = ["a", "b"]
        actual_subset = list(filter(lambda x: x in expected_subset, result))

        self.assertEqual(actual_subset, expected_subset)


if __name__ == "__main__":
    unittest.main()
