class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        left,right=0,len(matrix[0])
        top,button=0,len(matrix)

        while top<button and left<right:

            #case1 iterate through top and update top
            for i in range(left,right):
                ans.append(matrix[top][i])
            top+=1

            #case2 iterate through the right and update it 
            for i in range(top,button):
                ans.append(matrix[i][right-1])
            right-=1
            
            if not( top<button and left<right):
                break

            #case3 iterate through the button and update it
            for i in range(right-1,left-1,-1):
                ans.append(matrix[button-1][i])
            button-=1

            #case4 iterate through the left and update it
            for i in range(button-1,top-1,-1):
                ans.append(matrix[i][left])
            left+=1
            
        return ans
            