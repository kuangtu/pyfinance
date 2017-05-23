# -*- coding:utf-8 -*-
import numpy as np

def test():
    x = np.array([1,2,3])
    print x
    print x.mean()
    print x.sum()
    print x.std()

    y = np.random.rand(50)
    print y

if __name__ == '__main__':
    test()