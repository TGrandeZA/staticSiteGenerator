import unittest 

from htmlnode import HTMLNode #import the htmlNode class for testing 

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

if __name__ == '__main__':
    unittest.main()





