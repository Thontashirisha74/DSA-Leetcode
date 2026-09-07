class Solution:
    def longestWord(self, words: list[str]) -> str:

        word_set = set(words)
        answer = ""

        for word in words:

            valid = True

            # Check all prefixes
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break

            if valid:
                if len(word) > len(answer):
                    answer = word

                elif len(word) == len(answer) and word < answer:
                    answer = word

        return answer