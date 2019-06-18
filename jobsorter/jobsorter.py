class JobSorter:
    def __init__(self, job_list):
        self.job_list = job_list

    def sort_jobs(self):

        if not self.job_list:
            return ""

        ordered_list = []

        for job, dependency in self.job_list.items():
            # don't add duplicate jobs
            if not dependency and job not in ordered_list:
                ordered_list.append(job)
            elif dependency:
                # get the root dependency, then add the job
                ordered_list.append(self.get_root_dependency(dependency))
                ordered_list.append(job)

        return list(ordered_list)

    def get_root_dependency(self, job):
        """ Returns root dependency for a job
        Currently does not return the jobs in between
        e.g a => b, b => c - when passed a will return c
        """
        dependency = self.job_list[job]
        if not dependency:
            return job
        else:
            return self.get_root_dependency(dependency)
