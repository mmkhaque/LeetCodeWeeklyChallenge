import re


class Solution:
    def entityParser(self, text: str) -> str:
        
        if text is None:
            return ''
        
        if len(text) == 1:
            return text
        
        '''
        Quotation Mark: the entity is &quot; and symbol character is ".
        Single Quote Mark: the entity is &apos; and symbol character is '.
        Ampersand: the entity is &amp; and symbol character is &.
        Greater Than Sign: the entity is &gt; and symbol character is >.
        Less Than Sign: the entity is &lt; and symbol character is <.
        Slash: the entity is &frasl; and symbol character is /.
        '''
        
        text = re.sub(r'&quot;', '\"', text)
        text = re.sub(r'&apos;', '\'', text)
        text = re.sub(r'&amp;', '&', text)
        text = re.sub(r'&gt;', '>', text)
        text = re.sub(r'&lt;', '<', text)
        text = re.sub(r'&frasl;', '/', text)
        
        print(text)
        
        return text
                     
        
        
        
