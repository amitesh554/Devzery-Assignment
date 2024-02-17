
'''
The problem looked complex in the beginning, but it wasnt that much.

1) Though it can be solved using 2 loops where we can for a particular character what will be the max length of non repeating substring.

2) Time Complexity for above Solution will be O(n^2) and constant Space complexity

'''

'''
To make it optimal we have reduce the Time Complexity so for that we will use "Sliding Window Technique"

We will utilize a sliding window to dynamically adjust the substring under consideration, expanding or contracting based on the uniqueness of characters encountered.

Time Complexity-O(n) 
Space Complexity-O(n)---for using set()

'''





def LongestSubstring(s):
    #maxCnt stores the Maximum Lenght Non Repeating Substring
    
    maxCnt=0
    #ans stores the uniqueness of substring between i & j
    
    ans=set()
    #Two Pointers i and j initially will be at 0
    
    i=0
    j=0
    while(i<len(s) and j<len(s)):
        
        #we will check if the current character present in the set or not
        if s[j] not in ans:
            
            #if not then it is unique and will add in the set and calculate the current size of substring
            ans.add(s[j])
            
            #Move the j counter forward
            j+=1
            maxCnt=max(maxCnt,j-i)
        else:
            
            #if it is present then we will remove the character present at ith index move the ith counter
            ans.remove(s[i])
            i+=1

    return maxCnt
    
 
    
s=input()
print(LongestSubstring(s))






'''
s="abdacfga"
'''