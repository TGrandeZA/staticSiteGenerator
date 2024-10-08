from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"
#Textnode class is a placeholder/intermediary that acts as a data structure to organise MARKDOWN file for later conversion to HTML
class TextNode: 

    def __init__(self, text, text_type, url = None): #if nothing is passed URL is none by default

        self.text = text 
        self.text_type = text_type 
        self.url = url 

     #Sets up comparison behaviour for two TextNode objects based on the values of their text, type, and URL, rather than their instances in memory.
    def __eq__ (self, other):
        
        #returns true if they're 'equal'
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    #returns a string representation of the TextNode, for debugging and logging
    def __repr__(self): 

        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")
    






