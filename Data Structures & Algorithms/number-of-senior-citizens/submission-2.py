
from decimal import Decimal
 
class Solution:
    def countSeniors(self, details: List[str]) -> int:

        print(details[0])

        age_list = []

        for val in details:
            age_list.append(val[11:13])

        res = 0

        for val in age_list:
            if Decimal(val) > 60:
                res+=1
        
        return res

        

           

        
        