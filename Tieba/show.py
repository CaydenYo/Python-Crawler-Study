a = """
    学习:[
        专业,真题,考试,补考,毕业,复习,题目,
        考生,专业课,图书馆,学费,英语,成绩,
        活动,自习,上课,教室,复习资料,学分,
        课程,高数,毕设,自习室,课表,证书,
        本科生,奖学金,四级,挂科,签到,看书,
        比赛,重修,教材,课件,试卷,大赛,论文,
        学习,作业
    ],
    公选专业:[
        公选课,土木工程,通信工程,软件工程,机械设计,
        信息工程,上课,教室,公选,试题库,选课
    ],
    新生:[
        新生,报考,招生,调剂,录取,高校,宽带,
        老乡,高三,高中,通知书,新人,迎新,
        高考,军训,学生会
    ],
    校内生活:[
        老乡,单身,宿舍,寝室,室友,求购,桌游,
        校园卡,校园网,开学,学生会,食堂,翡翠湖校区,
        宽带,南区,老校区,屯溪路校区,社团,饭卡,
        快递,空调,女朋友,游戏,吃饭,协会,二手,
        学生证,人生,周末,校医院,补办,超市,注册,
        转让,银行卡,外卖,吉他,睡觉,好吃,表白
    ],
    校外生活:[
        电影,单身,求购,桌游,租房,暑期,健身房,
        暑假,驾校,放假,兼职,合租,女朋友,游戏,
        家教,吃饭,二手,人生,周末,租房子,寒假,
        万达,超市,转让,银行卡,大学城,吉他,
        睡觉,好吃,表白
    ],
    就业:[
        工作,大四,宣讲,面试,实习,笔试,本科,
        招聘,公司,工资,初试,就业,培训,毕业生,
        人生,岗位,宣讲会,福利,简历,创业,
        待遇,通知书,企业
    ],
    考研:[
        考研,复习,复试,方向,研友,笔试,考研资料,
        辅导班,通知书,面试,推免,题目,复习资料,
        真题,保研,研究生,报考,备考,读研,英语,
        招生,调剂,录取,高校,专硕,高数,本校,合租,
        初试,硕士,志愿,分数线,毕业生,导师,科目
    ]
    
"""

a = a.replace('\n', '')
a = a.replace('\"', '')
a = a.replace(' ', '')
print(a)