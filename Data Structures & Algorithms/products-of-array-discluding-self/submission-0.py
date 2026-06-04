class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zeros += 1

        products = []
        for num in nums:
            if zeros > 1:
               products.append(0) 
            elif zeros == 0:
                products.append(int(product/num))
            elif num != 0:
                products.append(0)
            else:
                products.append(product)


        return products
        