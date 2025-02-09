import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_eq_instance_type(self):
        node1 = TextNode("text", "type", "url")
        node2 = "not a TextNode"
        self.assertFalse(node1 == node2)

    def test_eq_text_not_equal(self):
        node1 = TextNode("text1", "type", "url")
        node2 = TextNode("text2", "type", "url")
        self.assertFalse(node1 == node2)

    def test_eq_text_type_not_equal(self):
        node1 = TextNode("text", "type1", "url")
        node2 = TextNode("text", "type2", "url")
        self.assertFalse(node1 == node2)

    def test_eq_url_not_equal(self):
        node1 = TextNode("text", "type", "url1")
        node2 = TextNode("text", "type", "url2")
        self.assertFalse(node1 == node2)

    def test_eq_all_not_equal(self):
        node1 = TextNode("text1", "type1", "url1")
        node2 = TextNode("text2", "type2", "url2")
        self.assertFalse(node1 == node2)

    def test_eq_all_equal(self):
        node1 = TextNode("text", "type", "url")
        node2 = TextNode("text", "type", "url")
        self.assertTrue(node1 == node2)

    def test_eq_url_none_not_equal(self):
        node1 = TextNode("text", "type", "url1")
        node2 = TextNode("text", "type", None)
        self.assertFalse(node1 == node2)

    def test_eq_text_none_not_equal(self):
        node1 = TextNode("text1", "type", "url")
        node2 = TextNode(None, "type", "url")
        self.assertFalse(node1 == node2)

    def test_eq_text_type_none_not_equal(self):
        node1 = TextNode("text", "type1", "url")
        node2 = TextNode("text", None, "url")
        self.assertFalse(node1 == node2)

    def test_eq_all_none_not_equal(self):
        node1 = TextNode("text", "type", "url")
        node2 = TextNode(None, None, None)
        self.assertFalse(node1 == node2)


if __name__ == "__main__":
    unittest.main()
