class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""+str(len(strs))+"#"
        for i in strs:
            encoded += str(len(i))+"#"
        encoded += "".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        numbers = []
        num = ""
        for i in s:
            if i == "#":
                break
            else:
                num += i
        numbers.append(int(num))

        start = len(str(numbers[0])) + 1

        for j in range(numbers[0]):
            num = ""
            for k in s[start:]:
                if k == "#":
                    break
                else:
                    num += k
            numbers.append(int(num))
            start = start + len(str(numbers[-1])) + 1
        strs = []
        for i in range(len(numbers)-1):
            word = s[start:start+numbers[i+1]]
            start = start+numbers[i+1]
            strs.append(word)
        return strs
