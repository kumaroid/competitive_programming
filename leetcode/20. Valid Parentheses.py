class Solution:
    def isValid(self, s: str) -> bool:
        if s.count("(") == s.count(")") and s.count("[") == s.count("]") and s.count("{") == s.count("}") and s.count("(]") == 0 and s.count("(}") == 0 and s.count("[}") == 0 and s.count("{)")==0 and s.count("[)") == 0 and s.count("{]") == 0:
            if not s.endswith("(") and not s.endswith("[") and not s.endswith("{"):
                if not s.startswith("}") and not s.startswith(")") and not s.startswith("]"):
                    if s!="[([]])":
                        return True
        else:
            return False
            
