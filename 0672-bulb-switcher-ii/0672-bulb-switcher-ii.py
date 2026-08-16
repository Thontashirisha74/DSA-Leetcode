class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n, 6)

        start = (1 << n) - 1

        states = {start}

        for _ in range(presses):
            new_states = set()

            for state in states:
                # Button 1: flip all bulbs
                new_states.add(state ^ ((1 << n) - 1))

                # Button 2: flip even-positioned bulbs
                mask = 0
                for i in range(2, n + 1, 2):
                    mask |= 1 << (i - 1)
                new_states.add(state ^ mask)

                # Button 3: flip odd-positioned bulbs
                mask = 0
                for i in range(1, n + 1, 2):
                    mask |= 1 << (i - 1)
                new_states.add(state ^ mask)

                # Button 4: flip bulbs 1,4,7,10,...
                mask = 0
                for i in range(1, n + 1, 3):
                    mask |= 1 << (i - 1)
                new_states.add(state ^ mask)

            states = new_states

        return len(states)