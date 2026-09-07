class Solution:
    def removeComments(self, source: list[str]) -> list[str]:

        result = []
        in_block = False
        current = []

        for line in source:

            i = 0

            # Start a new output line only if
            # we are not continuing from a previous block comment
            if not in_block:
                current = []

            while i < len(line):

                # If currently inside /* ... */
                if in_block:

                    # Check for block comment ending
                    if i + 1 < len(line) and line[i:i + 2] == "*/":
                        in_block = False
                        i += 2
                    else:
                        i += 1

                else:

                    # Line comment: ignore rest of line
                    if i + 1 < len(line) and line[i:i + 2] == "//":
                        break

                    # Block comment starts
                    elif i + 1 < len(line) and line[i:i + 2] == "/*":
                        in_block = True
                        i += 2

                    # Normal code
                    else:
                        current.append(line[i])
                        i += 1

            # Add line only if it has code and
            # we are not inside a continuing block comment
            if current and not in_block:
                result.append("".join(current))

        return result