'''Developed by Stitch'''
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import random
import copy

# init data
gainian_dict = {'积极防御': '是以积极的攻势行动，战胜进攻之敌的防御，亦称攻势防御、决战防御',
                '人民防空动员': '是指国家战时发动和组织人民群众防备敌人空袭所采取的措施，也可简称为人防动员，有的国家称为民防动员',
                '人民战争': '是被压迫阶级和被压迫民族为谋求自身的解放，发动和依靠广大人民群众所进行的战争',
                '人民战争的正义性': '是指战争的政治目的是符合被压迫阶级和被压迫民族根本利益的，是推动历史前进和社会进步的',
                '人民战争的群众性': '是指参加战争活动的人员较广泛，只要进行战争，各方都需要投入大量的人力、物力、财力',
                '国防': '是国家为防备和抵抗侵略，制止武装倾覆，保卫国家的主权、统一、领土完整和安全所进行的军事活动，以及与军事有关的政治、经济、外交、科技、教育等方面的活动',
                '国际战略力量': '是指在国际关系中能够独立地发挥作用，并对国际形势及国际战略的运用和发展具有巨大影响的国家或国家集团',
                '两极格局': '即两大战略力量之间的相互对立和相互斗争，对整个国际事务起着决定性影响的局面',
                '信息化作战平台': '是指采用信息技术研制或改造的，供武器装备执行作战任务的处所、载体或者器具的总称',
                '综合电子信息系统': '是按军队信息系统一体化原则和综合集成技术而构建的具有多种使命、多种功能的信息系统，是在战争中夺取信息优势、决策优势和全维优势的主要装备',
                '制导炸弹': '是指投放后能对其弹道进行控制并导向目标的航空炸弹，它是在普通航空炸弹的基础上增加制导装置而成的'}
jianda_dict = {'军事科学的功能': '为国家制定军事战略提供理论依据 为国家规划武装力量建设提供理论依据 为国家发展武器技术装备进行科学论证 为国家准备与实施战争提供理论依据',
               '大学生学习军事科学的意义': '大学生参加军事训练、学习军事科学是法定的公民义务，责无旁贷 大学生参加军事训练、学习军事科学有利于提高全民国防意识，振奋民族精神 '
                               '大学生参加军事训练、学习军事科学有利于加强国防后备力量建设 大学生参加军事训练、学习军事科学有利于培养德、智、体全面发展的“四有”新人',
               '现代国防的基本特征': '现代国防的概念内涵更丰富 现代国防是多种手段、多种斗争形式的角逐 现代国防是综合国力的较量 现代国防与国家经济建设关系更密切',
               '国防动员的意义': '动员是增强国防实力的重要措施 动员是增强国防威慑力的有效手段 动员是争取战争主动权的可靠保障',
               '国防动员的内容': '武装力量动员 国民经济动员 科学技术动员 人民防空动员 政治动员',
               '毛泽东军事思想的科学体系': '战争观与方法论 人民军队思想 人民战争思想 战略战术思想 国防建设思想',
               '毛泽东人民战争思想的基本理论观点': '战争的正义性是实行人民战争的政治基础 革命战争是群众的战争 人民群众是战争伟力之最深厚根源 兵民是胜利之本 人是战争胜负的决定因素',
               '信息化战争的主要特征': '武器装备的高度信息化 战争能量释放形态的信息主导化 战场空间的多维一体化 信息系统成为作战双方的主要打击目标 制信息权成为战场争夺的核心和基础 '
                             '基于网络信息体系的联合作战能力成为战斗力的基本形态 软杀伤与硬摧毁有机结合成为作战的普遍法则',
               '信息化陆上作战平台对作战的影响': '军队机动作战能力增强 陆军纵深攻击能力增大 战斗指挥和协同复杂 作战的非线性特征明显',
               '军队指挥控制系统的功能': '迅速收集和处理情报 自动查找和提取情报 辅助参谋人员拟制军事文书 实时观察战场情况 对武器进行自动控制 提高后勤指挥效率',
               '制导技术的种类': '自主式制导 寻的制导 遥控制导 复合制导',
               '精确制导武器的主要种类': '导弹 制导炸弹 制导炮弹 制导地雷 制导鱼雷'}
lunshu_dict = {'历史唯物主义的方法论': '研究和指导战争必须认识战争规律 研究和指导战争必须着眼其特点，着眼其发展 研究和指导战争，要关照全局，把握关节 研究和指导战争，要使主观指导符合客观实际',
               '国际战略格局演变的动因与过程': '国际战略格局的演变，从根本上说，是决定这种格局的国际战略力量及其相互关系的重大改变 国际战略格局的演变，是内外部因素共同作用的结果 '
                                 '国际战略格局演变的过程反映了国际战略力量之间的矛盾和斗争的发展过程',
               '国际战略格局演变的规律性特点': '国际战略格局演变的必然性和偶然性关系 国际战略格局演变的量变到质变过程 国际战略格局演变的渐变和突变方式', }
gainian_keys = [key for key in gainian_dict.keys()]
jianda_keys = [key for key in jianda_dict.keys()]
lunshu_keys = [key for key in lunshu_dict.keys()]
keys = []
for key in gainian_dict.keys():
    keys.append(key)
for key in jianda_dict.keys():
    keys.append(key)
for key in lunshu_dict.keys():
    keys.append(key)
keys = copy.deepcopy(keys)
random.shuffle(keys)
gainian_idx, jianda_idx, lunshu_idx, idx = 0, 0, 0, 0
right_count, wrong_count = 0, 0
FONT = ('Times New Roman', 20)


def renew_ui():
    count['text'] = '已经背了%d个，其中正确%d个，错误%d个' % (right_count+wrong_count, right_count, wrong_count)


def submit(self=None):
    global gainian_idx, jianda_idx, lunshu_idx, idx, right_count, wrong_count
    q = question['text']
    rightAnswer = gainian_dict.get(q, 0)
    if not rightAnswer:
        rightAnswer = jianda_dict.get(q, 0)
    if not rightAnswer:
        rightAnswer = lunshu_dict.get(q, 0)
    if rightAnswer.replace(' ','\n') == str(answer.get(0.0, tk.END)).strip():
        msg.showinfo('提示', '你对了！')
        right_count += 1
        unit = scrollBar.get()
        if unit == '概念题':
            question['text'] = gainian_keys[gainian_idx]
            gainian_idx += 1
            if gainian_idx == len(gainian_keys):
                gainian_idx = 0
        elif unit == '简答题':
            question['text'] = jianda_keys[jianda_idx]
            jianda_idx += 1
            if jianda_idx == len(jianda_keys):
                jianda_idx = 0
        elif unit == '论述题':
            question['text'] = lunshu_keys[lunshu_idx]
            lunshu_idx += 1
            if lunshu_idx == len(lunshu_keys):
                lunshu_idx = 0
        elif unit == '乱序':
            question['text'] = keys[idx]
            idx += 1
            if idx == len(gainian_keys) + len(jianda_keys) + len(lunshu_keys):
                idx = 0
    else:
        msg.showerror('你错了！', '正确答案是：\n' + str(rightAnswer).replace(' ','\n'))
        wrong_count += 1
    answer.delete(0.0, tk.END)
    renew_ui()

print(len(gainian_keys) + len(jianda_keys) + len(lunshu_keys))
# create form
mainForm = tk.Tk()
mainForm.resizable(0, 0)
mainForm.title('一起背军理（B卷专属）')

scrollBar = ttk.Combobox(mainForm, width=78, font=FONT)
scrollBar.grid(row=0, padx=5, pady=5)
scrollBar['value'] = ('概念题', '简答题', '论述题', '乱序')
scrollBar.configure(state='readonly')
scrollBar.set('概念题')

question = ttk.Label(mainForm, width=80, font=FONT)
question.grid(row=1, padx=5, pady=5)

question['text'] = gainian_keys[0]

answer = tk.Text(mainForm, width=80, height=7, font=FONT)
answer.grid(row=2, padx=5, pady=5)
answer.bind("<Delete>", submit)

submitButton = tk.Button(mainForm, text='提交', command=submit, width=74, font=FONT)
submitButton.grid(row=3, padx=5, pady=5)

alert = ttk.Label(mainForm, width=80, font=FONT)
alert['text'] = '注意：不要打句号。按键盘上的Delete提交。'
alert.grid(row=4, padx=5, pady=5)

count = ttk.Label(mainForm, width=80, font=FONT)
count['text'] = '已经背了0个，其中正确0个，错误0个'
count.grid(row=5, padx=5, pady=5)

mainForm.mainloop()
