
def num_to_str(num):
    if num <=1:
        return ''
    else:
        return str(num)



#### pointer left and right
def compress(chars):
    left = 0
    right = 0

    while right < len(chars):
      letter = chars[right]
      count = 0
      while right < len(chars) and chars[right] == letter:
        count += 1
        right += 1
      chars[left] = letter
      left += 1
      if count > 1:
        for c in str(count):
          chars[left] = c
          left += 1
    print(chars)
    return left


# ours
def compress( chars) -> int:
    print(1)
    s = ''
    current_item = ''
    item_count = 0
    for item in chars:
        if current_item == item:
            item_count+=1
        else:
            # this is where new char appears 
            # append the rest to the array
            s += current_item + num_to_str(item_count)
            current_item = item
            item_count = 1
    s += current_item + num_to_str(item_count)
    for i in range(len(s)):
        chars[i] = s[i]
    chars = chars[:len(s)]
    print(chars)
    return len(chars)

a = compress(list("aabbccc"))

print(a)


