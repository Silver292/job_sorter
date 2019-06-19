# Job Sorter

Code challenge to create a function that will take a hash map of jobs in the format of ``` job => dependency ``` and return a list
containing the jobs in the order they should be executed. This list should take into consideration job dependencies.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Requirements

- Python 3.7+
- pip

### Installation

Clone the repository:

```shell
$ git clone https://github.com/Silver292/job_sorter.git
```

Move into the directory

```shell
$ cd job_sorter
```

Install python virtual environments if necessary:

```shell
$ python -m pip install virtualenv
```

Create a virtual environment to use the package:

``` shell
$ python -m virtualenv .env
```

Activate the environment:

Windows:
``` shell
$ .env\Scripts\activate.bat
```

Other:
```shell
$ source bin/activate
```

Install required packages:

``` shell
(.env) $ pip install -r requirements.txt 
```

![install_jobsorter](https://user-images.githubusercontent.com/5542588/59770964-c93ab000-92a0-11e9-8243-527105300f1a.gif)

## Usage

The package can be used by importing the class into a Python script.

``` python
from jobsorter import JobSorter

# hash map of job:dependency
jobs = {'a':'', 'b':'c', 'c':'a'} 

exec_order = JobSorter(jobs).sort_jobs()

# exec_order is ['a', 'c', 'b']
```

Alternatively the class can be imported and used in the interactive shell:

```shell
(.env) $ python 
```
![interactive_shell_jobsorter](https://user-images.githubusercontent.com/5542588/59771038-e5d6e800-92a0-11e9-9ca5-3d49f8b94967.gif)


## Running the tests

Unit tests are ran using the **unittest** package.

```shell
(.env) $  python -m unittest discover -s tests
```

![tests_jobsorter](https://user-images.githubusercontent.com/5542588/59771063-f1c2aa00-92a0-11e9-8258-2bda09a99e4d.gif)

## Authors

* **Tom Scott** - *Initial work* 
