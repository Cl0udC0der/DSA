
# My implementation which uses an import, 3ms
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        topk = defaultdict(int)

        for x in nums:
            topk[x] += 1

        return heapq.nlargest(k, topk, key=topk.get)


# Same implementation w different syntax, much more logically comprehensible and clear
class Solution(object):     
    def topKFrequent(self, nums, k):
        # iterate through nums
            # if not in dict
                # add to dict: key = k, value = 1
            # else (already seen)
                # key = k, value +=1
        tracker = {}
        for num in nums:
            if num not in tracker:
                tracker[num] = 1
            else:
                tracker[num] = tracker[num] + 1

        # sort and convert into sorted list
        sorted_items = sorted(tracker.items(), key = lambda item: item[1], reverse=True)

        out = []
        for i in range(0,k):
            out.append(sorted_items[i][0])
        # print the values of the first k elements
        return out