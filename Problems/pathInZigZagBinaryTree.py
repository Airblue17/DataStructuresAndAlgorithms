class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        
        level = -1
        currentMaxNodeVal = 0 
        
        while label > currentMaxNodeVal:
            level +=1
            currentMaxNodeVal += 2**level
        
        traversal = []
        while label>0:
            traversal.append(label)
            level_max = currentMaxNodeVal
            level_min = (currentMaxNodeVal - 2**level)+1
            label = (level_max+level_min - label)//2
            level -= 1
            currentMaxNodeVal = level_min-1
            
                    
        return traversal[::-1]