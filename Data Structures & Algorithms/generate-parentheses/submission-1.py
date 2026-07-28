class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opened = 0
        closed = 0
        string = ""
        ar = []
        def generate(string: str, opened:int, closed:int):
            # print(string, n, opened, closed)
            if n == opened and n==closed:
                ar.append(string)
                # print(ar)
            elif n != opened and opened == closed:
                generate(string+"(", opened+1, closed)
            elif n != opened and opened > closed:
                generate(string+"(", opened+1, closed)
                generate(string+")", opened, closed+1)
            else:
                generate(string+")", opened, closed+1)

        generate("", opened, closed)
        return ar