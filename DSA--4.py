# write a code to check whether the given 2 strings are sorted or not
s1=input("Enter 1st string:").replace(' ','').lower()
s2=input("Enter 2nd string:").replace(' ','').lower()
if len(s1) !=len(s2):
    print("Not anagram")
elif sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("not anagram....")