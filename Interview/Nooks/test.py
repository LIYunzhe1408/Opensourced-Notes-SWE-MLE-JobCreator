import unittest
from main import find_degree_of_separation

class TestFindDegreeOfSeparation(unittest.TestCase):

    # Test 1: Same URL returns 0
    def test_same_url(self):
        url1 = "https://en.wikipedia.org/wiki/Point_of_sale"
        url2 = "https://en.wikipedia.org/wiki/Point_of_sale"
        result = find_degree_of_separation(url1, url2)
        self.assertEqual(result, 0)

    # Test 2: Non-Wikipedia URL should return Infinity
    def test_non_wikipedia_url(self):
        url1 = "https://example.com"
        url2 = "https://en.wikipedia.org/wiki/Point_of_sale"
        result = find_degree_of_separation(url1, url2)
        self.assertEqual(result, -1)

    # Test 3: Direct link returns 1
    def test_direct_link(self):
        url1 = "https://en.wikipedia.org/wiki/Sales"
        url2 = "https://en.wikipedia.org/wiki/Point_of_sale"
        result = find_degree_of_separation(url1, url2)
        self.assertEqual(result, 1)

    # Test 4: Indirect link
    def test_indirect_link(self):
        url1 = "https://en.wikipedia.org/wiki/Random_walk"
        url2 = "https://en.wikipedia.org/wiki/Megalodon"
        result = find_degree_of_separation(url1, url2)
        self.assertEqual(result, 3)

    # Test 5: Indirect link 2
    def test_indirect_link_2(self):
        url1 = "https://en.wikipedia.org/wiki/Sales"
        url2 = "https://en.wikipedia.org/wiki/E-commerce"
        result = find_degree_of_separation(url1, url2)
        self.assertEqual(result, 2)

    # Test 6: No link between articles
    def test_no_link(self):
        url1 = "https://en.wikipedia.org/wiki/Quantum_mechanics"
        #orphan page
        url2 = "https://en.wikipedia.org/wiki/Robert_Sann_Aung"
        result = find_degree_of_separation(url1, url2)
        self.assertEqual(result, -1)

    # Test 7: Invalid Wikipedia URL
    def test_invalid_wikipedia_url(self):
        url1 = "https://en.wikipedia.org/wiki/Sales"
        url2 = "https://en.wikipedia.org/wiki/Invalid_Page"
        result = find_degree_of_separation(url1, url2)
        self.assertEqual(result, -1)  # Assume page does not exist

if __name__ == "__main__":
    unittest.main()
