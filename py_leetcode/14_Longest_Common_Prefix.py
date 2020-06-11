from typing import List

def longestCommonPrefix(self, strs: List[str]) -> str:

    temp_prefix = []

    if len(strs) == 0: return ""
    if len(strs) == 1: return strs[0]

    strs.sort(key=len)

    for letter_indx in range(0, len(strs[0])): 
        need_to_append = False
        for item in range(0, len(strs)):
            if strs[item][letter_indx] != strs[0][letter_indx]:
                return "".join(temp_prefix)
            else:
                need_to_append = True

        if need_to_append:
            temp_prefix.append(strs[0][letter_indx])

    return "".join(temp_prefix)
    
#Another interesting solution

#     def longestCommonPrefix(self, strs):
#         prefix=""
#         if len(strs)==0: return prefix

#         for i in xrange(len(min(strs))):
#             c=strs[0][i]
#             if all(a[i]==c for a in strs):
#                 prefix+=c
#             else:
#                 break
#         return prefix

# JAVA
#     public String longestCommonPrefix(String[] strs) {
#     if (strs == null || strs.length == 0) return "";
#     for (int i = 0; i < strs[0].length() ; i++){
#         char c = strs[0].charAt(i);
#         for (int j = 1; j < strs.length; j ++) {
#             if (i == strs[j].length() || strs[j].charAt(i) != c)
#                 return strs[0].substring(0, i);             
#         }
#     }
#     return strs[0];
# }



# 