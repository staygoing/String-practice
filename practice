def extract_and_format_number(input_string):
    # 找到第一个数字字符的位置，标志字母部分的结束
    digit_start_index = next((i for i, c in enumerate(input_string) if c.isdigit()), -1)
    
    if digit_start_index == -1:
        # 如果没有找到数字部分，直接返回"00.00"
        return "00.00"
    
    # 从数字开始的位置开始找小数点
    dot_index = input_string.find('.', digit_start_index)
    
    if dot_index != -1:
        # 找到小数点，提取小数点后的数字部分，最多保留两位
        digits = []
        count = 0
        for char in input_string[dot_index + 1:]:
            if char.isdigit():
                digits.append(char)
                count += 1
                if count == 2:
                    break
            else:
                break
        
        # 如果不足两位，补足
        while count < 2:
            digits.append('0')
            count += 1
        
        return ''.join(digits[:2])  # 只保留两位小数
        
    else:
        # 没有小数点，直接补"00"
        return "00"

# 测试例子
input1 = "abcd123.456"
input2 = "abcd123"

output1 = extract_and_format_number(input1)
output2 = extract_and_format_number(input2)

print(output1)  # 输出 "123.45"
print(output2)  # 输出 "123.00"
