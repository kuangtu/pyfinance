# -*- coding:utf-8 -*-


def pv_f(fv, r, n):
    """
    计算现金当前值
    :param fv:
    :param r: 折现率（年）
    :param n: 年
    :return:
    """
    return fv/(1+r)**n

def perp_f(c, R):
    """
    计算永续年金
    :param c:
    :param R:
    :return:
    """
    return c/R

if __name__ == '__main__':
    pv = pv_f(100, 0.1 , 2)
    print pv
