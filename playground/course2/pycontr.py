from random import shuffle
import unittest

def test_sort_algorithm_stable():
    print("- sort algorithm is stable:", end=" ")
    passed = True

    for A1 in ([[100] for i in range(5)],
               [[1, 2], [1, 2], [2, 2], [2, 2], [2, 3], [2, 3]],
               [[5, 2] for i in range(30)] + [[10, 5] for i in range(30)]):
        shuffle(A1)
        A2 = sorted(list(A1))  # here we are cheating: standard sort is stable
        sort_algorithm(A1)
        # to test stability we will check A1[i] not equals A2[i], but is A2[i]
        passed &= all(x is y for x, y in zip(A1, A2))

    print("Ok" if passed else "Fail")
    return passed


def sort_algorithm(A):
    """
  Sorting of list on place. Using Bubble Sort algorithm.
  """
    N = len(A)
    for i in range(N - 1):
        for k in range(N - 1):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]




test_sort_algorithm_stable()