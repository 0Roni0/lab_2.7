#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    U = set("abcdefghijklmnopqrstuvwxyz")
    A = {'b', 'k', 'n', 'o', 'r'}
    B = {'a', 'b', 'k', 'u'}
    C = {'o', 'p'}
    D = {'a', 'm', 'n', 'y', 'z'}

    X = (A.union(B)).intersection(D)
    print(f'X= {X}')

    AA = U.difference(A)

    Y = (AA.intersection(D)).union(C.difference(B))
    print(f'Y = {Y}')
