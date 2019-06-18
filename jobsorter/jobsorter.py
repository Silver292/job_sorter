class JobSorter:
    def __init__(self, job_list):
        self.job_list = job_list

    def sort_jobs(self):

        if not self.job_list:
            return ""

        ordered_list = []

        for job, dependency in self.job_list.items():
            if not dependency and job not in ordered_list:
                ordered_list.append(job)
            elif (
                dependency
                and job not in ordered_list
                and dependency not in ordered_list
            ):
                ordered_list.extend(self.get_dependencies(job, []))
            elif dependency and job not in ordered_list:
                ordered_list.append(job)

        return list(ordered_list)

    def get_dependencies(self, job, dependencies):
        """ Returns a list of all dependencies in order 
        passed job will be the last element. 
        e.g a => b, b => c - when passed a will return [c,b,a]
        """
        dependency = self.job_list[job]
        if dependency:
            self.get_dependencies(dependency, dependencies)

        dependencies.append(job)

        return dependencies
