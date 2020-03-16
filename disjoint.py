"""
disjoint.py -- Disjoint set datastructure.

Also known as the Union-Find datastructure.  Based off of "Algorithm Design" by
Kleinberg and Tardos, section 4.6.

TODO(yberman) profile and improve perf if necessary.
"""

import random

class Disjoint:
    def __init__(self, iterator=None):
        self.parent = {}
        if iterator is None:
            return
        for x in iterator:
            self.parent[x] = x

    def add(self, x):
        self.parent[x] = x

    def __fast_root(self, x):
        """Find root without path compression."""
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def root(self, x):
        """Find the representative of the eq. class of x."""
        r = self.__fast_root(x)
        while True:
            next_x = self.parent[x]
            self.parent[x] = r
            if next_x == r:
                break
            x = next_x
        self.parent[x] = r
        return r

    def join(self, x, y):
        """Combine the eq. classes of x and y."""
        if random.random() < 0.5:
            x, y = y, x
        rx = self.root(x)
        ry = self.root(y)
        self.parent[rx] = ry

    def roots(self):
        for x in list(self.parent):
            self.parent[x] = self.__fast_root(x)
        return set(self.parent.values())

