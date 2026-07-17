class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        result = []
        a = len(arr)

        for num in arr:
            if num == 0:
                result.append(0)
                result.append(0)
            else:
                result.append(num)   

            if len(result) >= a:
                    break  

        for i in range(a):
            arr[i] = result[i]                       

    