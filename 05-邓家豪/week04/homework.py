# week3作业

# 词典；每个词后方存储的是其词频，词频仅为示例，不会用到，也可自行修改
Dict = {"经常": 0.1,
        "经": 0.05,
        "有": 0.1,
        "常": 0.001,
        "有意见": 0.1,
        "歧": 0.001,
        "意见": 0.2,
        "分歧": 0.2,
        "见": 0.05,
        "意": 0.05,
        "见分歧": 0.05,
        "分": 0.1}

# 待切分文本
sentence = "经常有意见分歧"


# 实现全切分函数，输出根据字典能够切分出的所有的切分方式
def all_cut(sentence, Dict):
    # TODO
    target = []
    length = len(sentence)

    # 递归函数，用于生成所有可能的切分方式
    def backtrack(start, path):
        if start == length:
            target.append(path.copy())
            return
        for i in range(start, length):
            word = sentence[start:i + 1]
            if word in Dict:
                path.append(word)
                backtrack(i + 1, path)
                path.pop()

    backtrack(0, [])
    return target


# 目标输出;顺序不重要
target = [
    ['经常', '有意见', '分歧'],
    ['经常', '有意见', '分', '歧'],
    ['经常', '有', '意见', '分歧'],
    ['经常', '有', '意见', '分', '歧'],
    ['经常', '有', '意', '见分歧'],
    ['经常', '有', '意', '见', '分歧'],
    ['经常', '有', '意', '见', '分', '歧'],
    ['经', '常', '有意见', '分歧'],
    ['经', '常', '有意见', '分', '歧'],
    ['经', '常', '有', '意见', '分歧'],
    ['经', '常', '有', '意见', '分', '歧'],
    ['经', '常', '有', '意', '见分歧'],
    ['经', '常', '有', '意', '见', '分歧'],
    ['经', '常', '有', '意', '见', '分', '歧']
]

if __name__ == '__main__':
    result = all_cut(sentence, Dict)
    print(result)
    # [['经', '常', '有', '意', '见', '分', '歧'], ['经', '常', '有', '意', '见', '分歧'],
    #  ['经', '常', '有', '意', '见分歧'], ['经', '常', '有', '意见', '分', '歧'], ['经', '常', '有', '意见', '分歧'],
    #  ['经', '常', '有意见', '分', '歧'], ['经', '常', '有意见', '分歧'], ['经常', '有', '意', '见', '分', '歧'],
    #  ['经常', '有', '意', '见', '分歧'], ['经常', '有', '意', '见分歧'], ['经常', '有', '意见', '分', '歧'],
    #  ['经常', '有', '意见', '分歧'], ['经常', '有意见', '分', '歧'], ['经常', '有意见', '分歧']]
