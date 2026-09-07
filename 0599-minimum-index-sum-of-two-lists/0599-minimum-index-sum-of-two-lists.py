class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        positions = {}
        
        for i, restaurant in enumerate(list1):
            positions[restaurant] = i
        
        minimum_sum = float('inf')
        result = []
        
        for j, restaurant in enumerate(list2):
            
            if restaurant in positions:
                
                index_sum = positions[restaurant] + j
                
                if index_sum < minimum_sum:
                    minimum_sum = index_sum
                    result = [restaurant]
                
                elif index_sum == minimum_sum:
                    result.append(restaurant)
        
        return result