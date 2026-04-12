class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        
        for i in range(len(operations)):
            if operations[i].lstrip('-').isdigit():
                scores.append(int(operations[i]))
            elif operations[i] == "+":
                scores.append(scores[-1] + scores[-2])
            elif operations[i] == "D":
                last_score = scores[-1]
                scores.append(scores[-1] * 2)
            elif operations[i] == "C":
                del scores[-1]

        total = 0
        for score in scores:
            total += score
            
        return total
