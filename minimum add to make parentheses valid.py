def min_add_to_make_valid(s):
    open_count = 0
    close_count = 0
    
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1
            else:
                close_count += 1
    
    return open_count + close_count

# Example usage
s = "())"
result = min_add_to_make_valid(s)
print(result)  # Output: 2
