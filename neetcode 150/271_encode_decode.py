class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string = "".join([encoded_string, f"#{len(word)}{word}"])
        return encoded_string
    
    def decode(self, s: str) -> list[str]:
        decoded_string = []
        encoded_string = list(s)
        for key, val in enumerate(encoded_string):
            if val == "#":
                len = encoded_string[key+1]
                word = "".join(encoded_string[key+2:(key+int(len)+2)])
                decoded_string.append(word)
        return decoded_string
