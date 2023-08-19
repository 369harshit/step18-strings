def shortest_palindrome(s):
    n = len(s)
    for i in range(n, -1, -1):
        if s[:i] == s[:i][::-1]:
            return s[i:][::-1] + s

# Example usage
s = "abcd"
result = shortest_palindrome(s)
print(result)  # Output: "dcbabcd"
