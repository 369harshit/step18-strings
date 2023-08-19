def longest_happy_prefix(s):
    n = len(s)
    
    for i in range(n - 1, 0, -1):
        prefix = s[:i]
        suffix = s[n - i:]
        
        if prefix == suffix:
            return prefix
    
    return ""

# Example usage
s = "level"
result = longest_happy_prefix(s)
print(result)  # Output: "l"
