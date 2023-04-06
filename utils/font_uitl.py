import time

# 颜色转换
def color_chinese_code(color):
    if color == '红色':
        return 'FF0000'
    elif color == '蓝绿':
        return '25A6B4'
    elif color == '橙色':
        return 'FF9900'
    elif color == '绿色':
        return '009900'
    elif color == '黄色':
        return 'CCCC00'
    elif color == '粉色':
        return 'FF00CC'
    elif color == '蓝色':
        return '1525E0'
    elif color == '茶色':
        return 'A5C498'



# log输入统一格式
def log_out_format(date, color='黑色'):
    code = color_chinese_code(color)
    times = time.strftime('%Y %a %b %d %H:%M:%S', time.localtime())
    date = str(date)
    date.replace(f'\n', '')
    # logWrite(f'<font color = #CC66FF>{times}</font>    <font color = #{code}>{date}</font>')
    return f'<font color = #CC66FF>{times}</font>    <font color = #{code}>{date}</font>'
    # print(f'{times}    {date}')