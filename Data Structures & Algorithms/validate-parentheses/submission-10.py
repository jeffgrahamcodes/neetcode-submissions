class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "{[(":
                stack.append(ch)
            elif ch in "}" and stack and stack[-1] == "{":
                del stack[-1]
            elif ch in "]" and stack and stack[-1] == "[":
                del stack[-1]
            elif ch in ")" and stack and stack[-1] == "(":
                del stack[-1]
            elif ch in "}])" and not stack:
                return False
            elif ch in "}" and stack and stack[-1] != "{":
                return False
            elif ch in "]" and stack and stack[-1] != "[":
                return False
            elif ch in ")" and stack and stack[-1] != "(":
                return False
            
        if stack:
            return False

        return True

        