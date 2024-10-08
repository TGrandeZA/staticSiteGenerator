import unittest 

from htmlnode import HTMLNode, LeafNode, ParentNode 


class TesthtmlNode(unittest.TestCase): 
    #testcase 1
    def test_no_props(self): # no properties 
        node = HTMLNode(tag = 'a', value = "link", props = None)
        self.assertEqual(node.props_to_html(), '')

    #testcase 2
    def test_1_props(self): # 1 property
        node = HTMLNode(tag='a', value='link', props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    #testcase 3 
    def test_multiple_props(self): #multiple properties 
        #target: Determines how the linked document will be opened. Common value is _blank, which opens the link in a new tab.
        node = HTMLNode(tag='a', value='link', props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

class TestLeafNode(unittest.TestCase): #LeafNode unit tests
    
    #testcase 1 
    def test_leafnode_with_props(self): #with property 
       
        node = LeafNode(value = "Click me!", tag = "a", props = {"href": "https://www.google.com"})
        
       
        expected_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_html)

    #testcase 2
    def test_leafnode_without_props(self): #without property

        node = LeafNode(value = "This is a paragraph", tag = "p")

        expected_html = "<p>This is a paragraph</p>"
        self.assertEqual(node.to_html(), expected_html)
    
    #testcase 3
    def test_leafnode_without_value(self): #without value

     with self.assertRaises(ValueError):
         node = LeafNode(value = None, tag = "a", props = {"href": "https://www.google.com"})
         node.to_html()

    #testcase 4
    def test_leafnode_without_tag(self): #without tag 

        node = LeafNode(value = "Click me!", tag = None, props = {"href": "https://www.google.com"})

        expected_html = "Click me!"
        self.assertEqual(node.to_html(), expected_html)
    #testcase 5
    def test_leafnode_without_tag_property(self): #without tag and property

        node = LeafNode(value = "Click me!", tag = None, props = None )

        expected_html = "Click me!"
        self.assertEqual(node.to_html(), expected_html)

class TestParentNode(unittest.TestCase): #ParentNode unit tests
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    

if __name__ == '__main__':
    unittest.main()





