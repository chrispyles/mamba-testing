import nbformat as nbf
from glob import glob


PATHS = [
    "out/autograder/proj03.ipynb",
    "out/student/proj03.ipynb",
]


def main():
    for p in PATHS:
        nb = nbf.read(p, as_version=nbf.NO_CONVERT)
        nb.cells.insert(0, nbf.v4.new_code_cell("%pip install -q otter-grader"))
        nbf.write(nb, p)


if __name__ == "__main__":
    main()
