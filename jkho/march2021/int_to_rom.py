class Solution:
    def intToRoman(self, num: int) -> str:
        dict1 = {
            1000: 'M',
            900: 'CM',
            400: 'CD',
            500: 'D',
            100: 'C',
            90:'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            4: 'IV',
            9: 'IX',
            5: 'V',
            1: 'I',
        }
        roman = ''
        for i in sorted(dict1.keys(),reverse= True):
            roman += dict1[i]*(num//i)
            num -= (num // i)*i

            
            
        return roman