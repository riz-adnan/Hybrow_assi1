def Anagram_check(s1, s2):
    
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
#both strings are now converted to lower case and whitespaces removed
    
    if len(s1) != len(s2):
        return False

#checking if same length
    s1_list = sorted(list(s1))
    s2_list = sorted(list(s2))

#strings are now sorted
    if s1_list == s2_list:
        return True
    else:
        return False






        