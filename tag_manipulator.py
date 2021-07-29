import re

class TagManipulator():    
    def parse_string(self, tags, regex=""):
        result = []

        tempResult = re.split( regex, tags )
        
        for i in range(0, len(tempResult)):


            if( len(tempResult[i]) > 0 ):
                item = tempResult[i]
                item = re.sub('[\W_]+', '', item)
                if len(item) > 0:
                    result.append(tempResult[i].strip())  

        return result