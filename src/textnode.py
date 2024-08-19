#Textnode class is a placeholder that acts as a data structure to organise MARKDOWN file for later conversion to HTML
class TextNode: 

    def __init__(self, text, text_type, url = None): #if nothing is passed URL is none by default

        self.text = text 
        self.text_type = text_type 
        self.url = url 

     #Sets up comparison behaviour for two TextNode objects based on the values of their text, type, and URL, rather than their instances in memory.
    def __eq__ (self, other):
        
        #returns true if they're 'equal'
        return (self.text, self.text_type, self.url) == (other.text, other.text_type, other.url) 

    #returns a string representation of the TextNode, for debugging and logging
    def __repr__(self): 

        return f"TextNode({self.text}, {self.text_type}, {self.url})"





