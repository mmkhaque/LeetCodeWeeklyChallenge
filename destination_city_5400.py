class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        if len(paths) == 0 or not paths:
            return ""
        
        if len(paths) == 1:
            return paths[0][1]
        
        
        path_list = []
        node_names = []
        
        for idx, path in enumerate(paths):
            if path[0] not in node_names:
                node_names.append(path[0])
            if path[1] not in node_names:
                node_names.append(path[1])
                
        chosen_node = ''
        
        for node in node_names:
            flag = True
            for idx, path in enumerate(paths):
                if node == path[0]:
                    flag = False
                    node = ''
                    break
                else:
                    chosen_node = node
                    
            if flag == True:
                print(chosen_node)
                return chosen_node 
        
        
