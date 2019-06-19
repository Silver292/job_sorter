import unittest
from jobsorter import JobSorter
from jobsorter.exceptions import DependencyError


class TestSortJobs(unittest.TestCase):
    def test_empty_string_should_return_empty_string(self):
        """ No Jobs:
        When passed an empty string - 
        an empty string should be returned
        """

        result = JobSorter("").sort_jobs()
        self.assertEqual(result, "")

    def test_when_passed_independent_job_should_return_job(self):
        """ One job:
        When passed a dictionary of one job with no dependencies, 
        the function should return a list containing only the job.
        """

        result = JobSorter({"a": ""}).sort_jobs()
        self.assertEqual(result, ["a"])

    def test_multiple_jobs_no_dependencies(self):
        """ Multiple jobs no dependencies:
        When passed a dictionary of jobs with no dependencies
        the function should return the jobs in no particular order
        """

        jobs = {"a": "", "b": "", "c": ""}

        result = JobSorter(jobs).sort_jobs()
        self.assertCountEqual(result, ["a", "b", "c"])

    def test_multiple_jobs_one_dependency(self):
        """ Multiple jobs one dependency:
        When passed multiple jobs, one of which is dependent on
        another, the dependent job should be after its dependency
        in the returned list. 
        """

        jobs = {"a": "", "b": "c", "c": ""}

        result = JobSorter(jobs).sort_jobs()

        # all jobs should be in returned list
        self.assertCountEqual(result, list(jobs.keys()))
        self.assertContainsList(result, ["c", "b"])

    def test_multiple_jobs_with_dependencies(self):
        jobs = {"a": "", "b": "c", "c": "f", "d": "a", "e": "b", "f": ""}

        job_sorter = JobSorter(jobs)
        result = job_sorter.sort_jobs()

        # all jobs should be in returned list
        self.assertCountEqual(result, list(jobs.keys()))

        # check dependent order
        self.assertContainsList(result, ["f", "c", "b", "e"])
        self.assertContainsList(result, ["a", "b"])

    def test_jobs_cant_depend_on_themselves(self):
        """ If passed a job with a dependency on itself
        the function should throw an error.
        """
        
        jobs = {"a": "", "b": "", "c": "c"}
        self.assertRaises(DependencyError, JobSorter(jobs).sort_jobs)

    def test_assertContainsList(self):
        self.assertContainsList([1, 2, 3], [1, 2, 3])
        self.assertContainsList(["a", "b", "c"], ["a", "b", "c"])
        self.assertContainsList([1, 2, 3], [1])
        self.assertContainsList([1, 2, 3], [2, 3])
        self.assertContainsList([1, 2, 3], [1, 3])

        with self.assertRaises(AssertionError):
            self.assertContainsList([1, 2, 3], [3, 2, 1])
            self.assertContainsList([1, 2, 3], [2, 1])
            self.assertContainsList([1, 2, 3], [3, 1])
            self.assertContainsList([1, 2, 3], ["a", "b"])

    def assertContainsList(self, superset, expected_subset):
        """ Passes if superset contains items in order of expected subset.
        """
        actual_subset = list(filter(lambda x: x in expected_subset, superset))

        self.assertEqual(actual_subset, expected_subset)


if __name__ == "__main__":
    unittest.main()
