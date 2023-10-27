![ci](https://img.shields.io/github/actions/workflow/status/pyamg/pyamg/ci.yml?style=flat-square&label=tests)
![lint](https://img.shields.io/github/actions/workflow/status/pyamg/pyamg/lint.yml?style=flat-square&label=lint)
![PyPI - Version](https://img.shields.io/pypi/v/pyamg?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyamg?style=flat-square)
![Codecov](https://img.shields.io/codecov/c/github/pyamg/pyamg?style=flat-square)
[![joss](https://joss.theoj.org/papers/10.21105/joss.05495/status.svg?style=flat-square)](https://doi.org/10.21105/joss.05495)

# Installation
PyAMG requires `numpy` and `scipy`

```
pip install pyamg
```

or from source:

```
pip install .
```

(`python setup.py install` will no longer work)

or with conda (see details below)

```
conda config --add channels conda-forge
conda install pyamg
```

# Introduction

PyAMG is a library of **Algebraic Multigrid (AMG)** solvers with a convenient Python interface.

![](https://raw.githubusercontent.com/pyamg/pyamg/main/docs/logo/pyamg_logo_withtext.png)

PyAMG is currently developed and maintained by
[Luke Olson](http://lukeo.cs.illinois.edu),
[Jacob Schroder](https://www.unm.edu/~jbschroder), and
[Ben Southworth](https://arxiv.org/a/southworth_b_1.html).
The organization of the project can be found in [`organization.md`](organization.md) and
examples of use can be found in [`pyamg-examples`](https://github.com/pyamg/pyamg-examples).

**Acknowledgements:**
PyAMG was created by
[Nathan Bell](http://wnbell.com/), 
[Luke Olson](http://lukeo.cs.illinois.edu), and
[Jacob Schroder](https://www.unm.edu/~jbschroder).
Portions of the project were partially supported by the NSF under award DMS-0612448.

# Citing

If you use PyAMG in your work, please consider using the following citation:

<pre>
@article{pyamg2023,
  author    = {Nathan Bell and Luke N. Olson and Jacob Schroder and Ben Southworth},
  title     = {{PyAMG}: Algebraic Multigrid Solvers in Python},
  journal   = {Journal of Open Source Software}
  year      = {2023},
  publisher = {The Open Journal},
  volume    = {8},
  number    = {87},
  pages     = {5495},
  doi       = {10.21105/joss.05495},
  url       = {https://doi.org/10.21105/joss.05495},
}
</pre>

# Getting Help

- For documentation see [http://pyamg.readthedocs.io/en/latest/](http://pyamg.readthedocs.io/en/latest/).

- Create an [issue](https://github.com/pyamg/pyamg/issues).

- Look at the [Tutorial](https://github.com/pyamg/pyamg/wiki/Tutorial) or the [examples](https://github.com/pyamg/pyamg-examples) (for instance  the [0_start_here](https://github.com/pyamg/pyamg-examples/blob/main/0_start_here/demo.py) example).

- Run the unit tests (`pip install pytest`):
  - With PyAMG installed and from a non-source directory:
  ```python
  import pyamg
  pyamg.test()
  ```
  - From the PyAMG source directory and installed (e.g. with `pip install -e .`):
  ```python
  pytest .
  ```

# What is AMG?

 AMG is a multilevel technique for solving large-scale linear systems with optimal or near-optimal efficiency.  Unlike geometric multigrid, AMG requires little or no geometric information about the underlying problem and develops a sequence of coarser grids directly from the input matrix.  This feature is especially important for problems discretized on unstructured meshes and irregular grids.

# PyAMG Features

PyAMG features implementations of:

- **Ruge-Stuben (RS)** or *Classical AMG*
- AMG based on **Smoothed Aggregation (SA)**

and experimental support for:

- **Adaptive Smoothed Aggregation (αSA)**
- **Compatible Relaxation (CR)**

The predominant portion of PyAMG is written in Python with a smaller amount of supporting C++ code for performance critical operations.

# Example Usage

PyAMG is easy to use!  The following code constructs a two-dimensional Poisson problem and solves the resulting linear system with Classical AMG.

````python
import pyamg
import numpy as np
A = pyamg.gallery.poisson((500,500), format='csr')  # 2D Poisson problem on 500x500 grid
ml = pyamg.ruge_stuben_solver(A)                    # construct the multigrid hierarchy
print(ml)                                           # print hierarchy information
b = np.random.rand(A.shape[0])                      # pick a random right hand side
x = ml.solve(b, tol=1e-10)                          # solve Ax=b to a tolerance of 1e-10
print("residual: ", np.linalg.norm(b-A*x))          # compute norm of residual vector
````

Program output:

<pre>
multilevel_solver
Number of Levels:     9
Operator Complexity:  2.199
Grid Complexity:      1.667
Coarse Solver:        'pinv2'
  level   unknowns     nonzeros
    0       250000      1248000 [45.47%]
    1       125000      1121002 [40.84%]
    2        31252       280662 [10.23%]
    3         7825        70657 [ 2.57%]
    4         1937        17971 [ 0.65%]
    5          483         4725 [ 0.17%]
    6          124         1352 [ 0.05%]
    7           29          293 [ 0.01%]
    8            7           41 [ 0.00%]

residual:  1.24748994988e-08
</pre>

# Conda

More information can be found at [conda-forge/pyamg-feedstock](https://github.com/conda-forge/pyamg-feedstock).

*Linux:*
[![Circle CI](https://circleci.com/gh/conda-forge/pyamg-feedstock.svg?style=shield)](https://circleci.com/gh/conda-forge/pyamg-feedstock)

*OSX:*
[![TravisCI](https://travis-ci.org/conda-forge/pyamg-feedstock.svg?branch=master)](https://travis-ci.org/conda-forge/pyamg-feedstock)

*Windows:*
[![AppVeyor](https://ci.appveyor.com/api/projects/status/github/conda-forge/pyamg-feedstock?svg=True)](https://ci.appveyor.com/project/conda-forge/pyamg-feedstock/branch/master)

*Version:*
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/pyamg/badges/version.svg)](https://anaconda.org/conda-forge/pyamg)

*Downloads:*
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/pyamg/badges/downloads.svg)](https://anaconda.org/conda-forge/pyamg)

Installing `pyamg` from the `conda-forge` channel can be achieved by adding `conda-forge` to your channels with:

```
conda config --add channels conda-forge
```

Once the `conda-forge` channel has been enabled, `pyamg` can be installed with:

```
conda install pyamg
```

It is possible to list all of the versions of `pyamg` available on your platform with:

```
conda search pyamg --channel conda-forge
```

# OpenMP

PyAMG handles OpenMP in the following way

    - The `has_flag()` function of `pybind11` is called, with either `-fopenmp` (Linux) or `-Xpreprocessor -fopenmp` (MacOS).  Then added to the build if present.

    - Every instance of OpenMP is limited to `#pragma` or `#ifdef _OPENMP`.  Each kernel in `amg_core` that has OpenMP should be buildable without.

    - To test, try `export OMP_NUM_THREADS=4; python test_omp.py` in `scripts/`

    - The AMG solve phase add threading by rewriting the sparse matrix-vector multiplications of `A`, `P`, and `R`, with `ml.solve(...., openmp=True)`.

#### MacOS
    - To enable OpenMP on macOS, `brew install libomp`

    - Then set environment variables, following https://scikit-learn.org/dev/developers/advanced_installation.html#macos-compilers-from-homebrew :
    ```
    export CC=/usr/bin/clang
    export CXX=/usr/bin/clang++
    export CPPFLAGS="$CPPFLAGS -Xpreprocessor -fopenmp"
    export CFLAGS="$CFLAGS -I$(brew --prefix libomp)/include"
    export CXXFLAGS="$CXXFLAGS -I$(brew --prefix libomp)/include"
    export LDFLAGS="$LDFLAGS -Wl,-rpath,$(brew --prefix libomp)/lib -L$(brew --prefix libomp)/lib -lomp"
    ```

    - Then `setup.py` will attempt to add `-Xpreprocessor -fopenmp` to the compiler and `-lomp` to the linker.

