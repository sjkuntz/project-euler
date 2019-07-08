"""Generate .org files for Project Euler."""
import os
from pathlib import Path

# Number of the last problem.
LAST = 677

for i in range(0,LAST//100+1):
    dirname = "./%i01/" % i
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    for j in range(0,10):
        filename = dirname + "project-euler-%i%i1.org" % (i,j)
        filepath = Path(filename)
        if not filepath.exists():
            first = i*100 + j*10 + 1
            filecontents = """#+TITLE: Project Euler solutions (#%i-%i)
#+AUTHOR: Steven Kuntz
#+EMAIL: stevenjkuntz@gmail.com
#+OPTIONS: num:nil toc:1
#+PROPERTY: header-args:python :session *python*
#+PROPERTY: header-args :results output :exports both

Initialize Python session with imports.

#+begin_src python :results none
import numpy as np
import timeit
#+end_src

* %i
** Q:
** A:
* %i
** Q:
** A:
* %i
** Q:
** A:
* %i
** Q:
** A:
* %i
** Q:
** A:
* %i
** Q:
** A:
* %i
** Q:
** A:
* %i
** Q:
** A:
* %i
** Q:
** A:
* %i
** Q:
** A:
            """ % ((first,first+9) + tuple(range(first,first+10)))
            with open(filename,"w") as file:
                file.write(filecontents)
