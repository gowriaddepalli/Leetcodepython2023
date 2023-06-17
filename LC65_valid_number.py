class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        num = False
        exp = False
        sign = False
        dec = False

        for c in s:
            # check for number
            if c>= "0" and c<= "9":
                num = True
            # check for exponenent
            elif c == 'e' or c == "E":
                # check if num comes before exponent
                if exp or not num:
                    return False
                else:
                    # reset to check after exponent
                    exp,num,sign,dec = True, False, False, False
            # check for sign
            # check for exponent before sign
            elif c == "+" or c == "-":
                if sign or num or dec:
                    return False
                else:
                    sign = True
            elif c == ".":
                if dec or exp:
                    return False
                else:
                    dec = True
            else:
                return False
        return num 
