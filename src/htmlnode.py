#HTMLNode class will represent a "node" in an HTML document tree like a <p> tag and its contents, or an <a> tag and its contents
#It's purpose-built to render itself as HTML. 
#way to represent a piece of an HTML document in a structured, programmable manner. 

class HTMLNode: 

    def __init__(self, tag= None, value = None, children = None, props = None) :
       
        self.tag = tag          # Initialize tag, possibly None
        self.value = value      # Initialize value, possibly None --> Value inside the tag
        self.children = children    # Initialize children, possibly None --> list of HTMLNode objects representing the children of this node
        self.props = props      # Initialize props, possibly None --> A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) representing a hyperlink, meaning: <a href="https://www.example.com">Visit Example</a>, "Visit Example" is the link text.}
                                #props = properties 

    def to_html(self): 
        raise NotImplementedError 

    def props_to_html(self):

        if self.props == None: 
            return ""
        
        parts = []
        for key, value in self.props.items(): 

            parts.append(f'{key}="{value}"')

    # Join the parts with spaces and return with a leading space
        return ' ' + ' '.join(parts)

    def __repr__(self):

        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    



                
            