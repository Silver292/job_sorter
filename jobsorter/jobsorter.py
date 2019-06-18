from .helpers import UniqueList


class JobSorter:
    def __init__(self, job_list):
        self.job_list = job_list

    def sort_jobs(self):
        """ Returns a list of jobs in execution order. 
        Each job will be listed after its dependency.
        """

        if not self.job_list:
            return ""

        ordered_list = UniqueList()

        for job, dependency in self.job_list.items():
            if dependency:
                self.get_dependencies(job, ordered_list)
            else:
                ordered_list.append(job)

        return ordered_list

    def get_dependencies(self, job, dependencies):
        """ Returns a list of all dependencies in order 
        passed job will be the last element. 
        Jobs will be appended to the list passed as an argument.
        e.g a => b, b => c - when passed a will return [c,b,a]
        """
        dependency = self.job_list[job]
        if dependency:
            self.get_dependencies(dependency, dependencies)

        dependencies.append(job)

        return dependencies
