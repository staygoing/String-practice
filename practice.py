import re

def extract_and_format_number(input_string):
    # 使用正则表达式匹配字母和数字部分
    match = re.match(r'([a-zA-Z]+)(\d+(?:\.\d*)?)', input_string)

    if match:
        number_str = match.group(2)  # 获取数字部分的字符串

        if '.' in number_str:
            # 如果有小数点，保留两位小数但不四舍五入
            integer_part, decimal_part = number_str.split('.')
            formatted_number = integer_part + '.' + (decimal_part + '00')[:2]  # 截取小数点后两位
        else:
            # 如果没有小数点，补充两位小数
            formatted_number = number_str + '.00'

        return formatted_number

    else:
        return None  # 如果没有找到匹配的模式，返回None或者适合的错误提示

# 测试示例
input_str1 = "abcd123.456"
input_str2 = "abcd123"
input_str3 = "xyz789.1"

print(extract_and_format_number(input_str1))  # 输出: 123.45
print(extract_and_format_number(input_str2))  # 输出: 123.00
print(extract_and_format_number(input_str3))  # 输出: 789.10
