class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        entries = {}
        # I'll iterate the list, putting each new entry into a Dict
        for entry in strs:
            as_sorted = str(sorted(entry))
            if as_sorted in entries.keys():
                existing = entries[as_sorted]
                existing.append(entry)
                entries[as_sorted] = existing
            else:
                entries[as_sorted] = [entry]
        result = [r for r in entries.values()]
        return result