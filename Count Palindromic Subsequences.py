def is_palindrome(s):
    return s == s[::-1]

def count_palindromic_subsequences(s):
    n = len(s)
    count = 0
    
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_palindrome(substring):
                count += 1
    
    return count

# Example usage
s = "pqqr"
result = count_palindromic_subsequences(s)
print(result)  # Output: 11
