class Solution:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeMap: 
            shortUrl = self.base + str(len(self.encodeMap) + 1)
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
        return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeMap[shortUrl]

solution = Solution()

# Encode a URL
long_url = "https://leetcode.com/problems/design-tinyurl"
encoded_url = solution.encode(long_url)
print("Encoded URL:", encoded_url)

# Decode the URL back to the original URL
decoded_url = solution.decode(encoded_url)
print("Decoded URL:", decoded_url)