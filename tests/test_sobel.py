import pyclesperanto_prototype as cle
import numpy as np


def test_sobel():
    test1 = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1.41, 2, 1.41, 0],
        [0, 3.16, 2, 3.16, 0],
        [0, 3.16, 2, 3.16, 0],
        [0, 1.41, 2, 1.41, 0]
    ]))

    result = cle.create(test1)
    cle.sobel(test1, result)
    a = cle.pull(result)
    print(a)

    b = cle.pull(reference)
    assert (np.allclose(a, b, 0.01))
