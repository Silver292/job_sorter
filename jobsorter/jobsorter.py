from .helpers import UniqueList
from .exceptions import DependencyError


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

        for job in self.job_list.keys():
            self.get_dependencies(job, ordered_list)

        return ordered_list

    def get_dependencies(self, job, dependencies, dependency_chain=None):
        """ Returns a list of all dependencies in order 
        passed job will be the last element. 
        Jobs will be appended to the list passed as an argument.
        e.g a => b, b => c - when passed a will return [c,b,a]
        """
        # create dependency chain, can't use default arg as
        # it is only evaluated on function definition
        # see: https://docs.python-guide.org/writing/gotchas/
        if not dependency_chain:
            dependency_chain = []

        dependency = self.job_list[job]

        if dependency:
            self.check_depends_on_self(job, dependency)
            self.check_circular_dependency(dependency, dependency_chain)
            self.get_dependencies(dependency, dependencies, dependency_chain)

        dependencies.append(job)

        return dependencies

    def check_depends_on_self(self, job, dependency):
        if job == dependency:
            raise DependencyError(
                "Jobs cannot depend on themselves", f"{job}:{dependency}"
            )

    def check_circular_dependency(self, dependency, dependency_chain):
        if dependency in dependency_chain:
            raise DependencyError(
                "Jobs cannot have circular dependencies",
                f"{' => '.join(dependency_chain)} => {dependency}",
            )
        else:
            dependency_chain.append(dependency)
