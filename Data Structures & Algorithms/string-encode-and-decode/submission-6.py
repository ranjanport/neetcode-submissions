class Solution:
    def encode(self, strs: List[str]) -> str:
        a = ""
        for item in strs:
            a = a + str(len(item)) + "//\\" + item + "//\\"

        return a

    def decode(self, s: str) -> List[str]:
        decoded_seq = s.split("//\\")[:-1]
        decoded_list = []
        for i in range(1, len(decoded_seq), 2):
            decoded_list.append(decoded_seq[i])
        return decoded_list