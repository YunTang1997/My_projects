# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/21
desc: 括号匹配问题
"""


from 栈的基础实现 import LStack


def check_parens(text):
    """括号配对检查函数，text是被检查的正文串"""
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {")": "(", "]": "[", "}": "{"}  # 表示配对关系的字典


    def parentheses(text):
        """括号生成器，每次调用返回text里的下一括号及其位置"""
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield  text[i], i
            i += 1

    st = LStack()  # 用栈来存放找到的开括号

    for pr, i in parentheses(text):  # 对text里各括号和位置迭代
        if pr in open_parens:  # 开括号，压进栈并继续
            st.push(pr)
        elif opposite[pr] != st.top():  # 不匹配就是失败，退出
            print("Unmatching is found at", i, "for", pr)
            return False
        else:
            st.pop()

    print("All parenthesses are correctly matched.")
    return True


if __name__ == '__main__':

    test1 = "121(577[4577{475}jj]jjfj)"
    print(check_parens(test1))
    test2 = "121(577[4577475}jj]jjfj)"
    print(check_parens(test2))
    test3 = "([{}])"
    print(check_parens(test3))
