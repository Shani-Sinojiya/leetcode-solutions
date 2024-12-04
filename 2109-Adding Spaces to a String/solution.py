class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        result = []
        space_set = set(spaces)  # Convert list to set for O(1) lookup
        
        for i in range(len(s)):
            if i in space_set:
                result.append(" ")  # Insert space if index is in the set
            result.append(s[i])  # Append the character

        # If a space is needed at the end (edge case)
        if len(s) in space_set:
            result.append(" ")

        return "".join(result)  # Join the list into a final string

