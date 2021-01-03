class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        if len(boxTypes) == 0 or truckSize == 0:
            return 0
        
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        #print(boxTypes)
        #print(boxTypes[0][1])
        
        total_boxes = 0
        output_boxes = 0
        
        for box in boxTypes:
            
            if truckSize == 0:
                break
            
            if box[0] <= truckSize:
                truckSize -= box[0]
                output_boxes += box[0] * box[1]
                #print('using box[0] ', box[0])
            else:
                while truckSize !=0:
                    truckSize -= 1
                    output_boxes += box[1]
                    #print('using -1', box[0])

            #print(output_boxes, total_boxes, box[0], truckSize)
                
        print(output_boxes)
        
        return output_boxes
                
        
        
