class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[j] is true if s1[:i] and s2[:j] form s3[:i + j].
        dp = [False] * (len(s2) + 1)
        dp[0] = True

        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, len(s2) + 1):
                k = i + j - 1
                dp[j] = (
                    (dp[j] and s1[i - 1] == s3[k])
                    or (dp[j - 1] and s2[j - 1] == s3[k])
                )

        return dp[-1]