#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_deepwalk
----------------------------------

Tests for `deepwalk` module.
"""

import unittest
import tempfile
import os
from deepwalk import graph


class TestDeepwalk(unittest.TestCase):

    def setUp(self):
        # Create a simple test graph
        self.G = graph.Graph()
        self.G[1] = [2, 3]
        self.G[2] = [1, 3, 4]
        self.G[3] = [1, 2, 4]
        self.G[4] = [2, 3]

    def test_graph_creation(self):
        """Test basic graph creation"""
        self.assertEqual(len(self.G.nodes()), 4)
        self.assertTrue(self.G.has_edge(1, 2))
        self.assertFalse(self.G.has_edge(1, 4))

    def test_random_walk(self):
        """Test random walk generation"""
        walk = self.G.random_walk(5, start=1)
        self.assertEqual(len(walk), 5)
        self.assertEqual(walk[0], '1')

    def test_degree_calculation(self):
        """Test degree calculation"""
        degree = self.G.degree(1)
        self.assertEqual(degree, 2)

    def test_build_corpus(self):
        """Test corpus building"""
        corpus = graph.build_deepwalk_corpus(self.G, num_paths=2, path_length=3)
        self.assertEqual(len(corpus), 8)  # 4 nodes * 2 paths
        for walk in corpus:
            self.assertEqual(len(walk), 3)

    def test_load_edgelist(self):
        """Test loading from edgelist format"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.edgelist') as f:
            f.write("1 2\n2 3\n3 1\n")
            f.flush()
            
            try:
                G = graph.load_edgelist(f.name)
                self.assertEqual(len(G.nodes()), 3)
                self.assertTrue(G.has_edge(1, 2))
            finally:
                os.unlink(f.name)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()