all = """
课表
证书
机械设计
本科生
通信工程
奖学金
挂科
签到"""
ans = """"""
for i in all.split('\n'):
    ans += '\"' + i.strip() + '\"' + ',' + '\n'

print(ans)

