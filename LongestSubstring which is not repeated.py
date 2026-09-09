#sliding window apporach find the longest substring which is not repeated
s= input("Enter a string")
left= 0
maximum= 0
longest= ' '
window= set()
for right in range(len(s)):
    while s[right] in window:
        window.remove(s[left])
        left+=1
    window.add(s[right])
    if right-left+1> maximum:
        maximum=right-left+1
        longest= s[left:right+1]
print("Longest substring:",longest)
print("Longest substring length:",maximum)