# -*- coding: utf-8 -*-
"""V2_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I67NA73IgsQTTo6Nly9PMClvC9mZBWH4
"""

myvar3 = np.array([[i for i in range(10)]])
myvar3.transpose()
expected3 = myvar3.transpose()
(expected3 == mytranspose(myvar3)).all()

myvar2 = np.array([1, 3, 5, None])
myvar2.transpose()
expected2 = myvar2.transpose()
(expected2 == mytranspose(myvar2)).all()