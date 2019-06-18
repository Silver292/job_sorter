class JobSorter:
    @staticmethod
    def sort_jobs(job_list):

        if not job_list:
            return ""

        return list(job_list.keys())

