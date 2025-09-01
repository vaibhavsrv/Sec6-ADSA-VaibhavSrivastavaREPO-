def isPalindrome():
    s = input().strip()
    n = len(s)
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    odd_count = 0
    odd_char = None
    
    for char, count in freq.items():
        if count % 2 == 1:
            odd_count += 1
            odd_char = char

    if odd_count > 1:
        print("NO SOLUTION")
        return

    new_s = [""] * n
    left = 0

    for char in sorted(freq.keys()):
        count = freq[char]
        pairs = count // 2
        
        for _ in range(pairs):
            new_s[left] = char
            new_s[n - 1 - left] = char
            left += 1

    if odd_char:
        new_s[n // 2] = odd_char
    
    print("".join(new_s))

isPalindrome()