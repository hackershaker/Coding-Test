class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        groups = []
        for string in strs:
            if not groups:
                groups.append({string})
            else:
                samegroup = []
                for idx in range(len(groups)):
                    for element in groups[idx]:
                        if self.isSameGroup(element, string):
                            samegroup.append(idx)
                            break
                if samegroup:
                    self.union(groups, samegroup, string)
                else:
                    groups.append({string})
        print(groups)
        return len(groups)

    def isSameGroup(self, str1, str2):
        if str1 == str2:
            return True
        arr = []
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                arr.extend([str1[i], str2[i]])
        if len(arr) == 4 and arr[1] == arr[2] and arr[0] == arr[3]:
            return True
        return False

    def union(self, groups, idxs, string):
        groups[idxs[0]].add(string)
        for i in range(1, len(idxs)):
            groups[idxs[0]] |= groups[idxs[i]]
        for i in range(len(idxs)-1, 0, -1):
            del groups[idxs[i]]
