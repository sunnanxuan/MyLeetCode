class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if sum(candidates) < target or candidates[0] > target:
            return []
        res = []
        used = set()
        stack_used = set()
        stack = []
        for i in range(len(candidates)):
            if candidates[i] < target:
                if tuple([candidates[i]]) not in stack_used:
                    stack.append([i, candidates[i], [candidates[i]]])
                    stack_used.add(tuple([candidates[i]]))
            elif candidates[i] == target:
                if (candidates[i],) not in used:
                    res.append([candidates[i]])
                    used.add((candidates[i],))
            elif candidates[i] > target:
                break
        while stack:
            i, sm, arr = stack.pop()
            for j in range(i + 1, len(candidates)):
                if candidates[j] + sm == target:
                    if tuple(arr + [candidates[j]]) not in used:
                        res.append(arr + [candidates[j]])
                        used.add(tuple(arr + [candidates[j]]))
                elif candidates[j] + sm < target:
                    narr = arr + [candidates[j]]
                    if tuple(narr) not in stack_used:
                        stack.append([j, candidates[j] + sm, narr])
                        stack_used.add(tuple(narr))
                else:
                    break
        return res


