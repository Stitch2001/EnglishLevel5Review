# init data
u5_dict = {'我们可以发现好多严重问题': 'we can identify a number of serious problems',
           '使人类丧失创造力，社会关系毫无人情味': 'eclipse human creativity and dehumanize social relations',
           '全球不平等会扼杀市场和资本主义的增长': 'Global inequality contributes to stifling the growth of markets and of capitalism',
           '在追求利润的过程中变得越来越冷漠无情和毫无道德': 'becomes increasingly soulless and unethical in its pursuit of profit',
           '认同全球消费资本主义的价值观': 'embrace the values of global consumer capitalism',
           '世界上存在强烈的同质化倾向': 'the existence of powerful homogenizing tendencies in the world',
           '重振地方文化特色': 'reinvigorate local cultural niches',
           '并非不可兼容': 'are not necessarily incompatible',
           '身份认同感较不稳定': 'a less stable sense of identity',
           '世界文化流动的复杂性': 'the complexity of global cultural flows'}
u6_dict = {'跨国界污染是对我们集体生存的另一个严重威胁': 'Transboundary pollution represents another grave danger to our collective survival',
           '导致国际社会协调一致共同努力': 'resulted in a coordinated international effort',
           '至少是临界水平的两倍': 'at least twice as high as the critical level',
           '人类引发的气候变化问题出现了': 'the issue of human-induced climate change has emerged',
           '发布了一份关于......的报告，报告内容详尽全面，令人震惊': 'released a comprehensive and alarming report on',
           '全球气温的显著上升已经导致了.....': 'These significant increases in global temperatures have been leading to',
           '导致全球海平面上升了22英尺': 'result in a global rise of sea levels of 22 feet',
           '威胁地球海洋健康的唯一严重问题': 'the only serious problems threatening the health of our planet\'s oceans',
           '对地球的海洋环境造成了毁灭性的影响': 'have had a devastating impact on Earth\'s marine environments',
           '所有这些潜在的灾难性环境问题的主要特征': 'The central feature of all these potentially disastrous environmental problems'}
u7_dict = {'源源不断地向它们的读者灌输市场全球主义的主张': 'feed their readers a steady diet of market-globalist claims',
           '只要说得出名字，他们就有能力生产出来': 'have the capacity to produce what they name',
           '经常出现在......': 'occur with great regularity in',
           '兜售其政治经济议题': 'to sell their political and economic agenda',
           '植根于自我监管市场的理念': 'is anchored in the idea of the self-regulating market',
           '促进个人自由与物质进步': 'further individual liberty and material progress',
           '利用政府的权力来削弱和消除那些限制市场的社会政策和制度': 'utilize the powers of government to weaken and eliminate those social '
                                          'policies and institutions that curtail the market',
           '能胜任这个艰巨的任务': 'up to this ambitious task',
           '与......形成鲜明的对比': 'stand in stark contrast to',
           '发挥极其积极的作用': 'play an extremely active role'}
u8_dict = {'违反国际法': 'in violation of international law',
           '全球金融危机的持续影响': 'the lingering effects of the Global Financial Crisis',
           '超出...的能力所及': 'beyond the reach of',
           '阻止甚至扭转先前的全球化趋势': 'stopping and even reversing previous globalization trends',
           '国际贸易的快速增长与资本的大量流动': 'the rapid growth of international trade, and a huge flow of capital',
           '在全球传播其政治制度与文化价值观念': 'spread its political system and cultural values across the globe',
           '这些社会变革进程必须得有一个道德和伦理上的指引': 'these transformative social processes must have a moral compass and an ethical '
                                      'polestar',
           '保护普遍的人权而不毁坏人类进化的命脉：文化多样性': 'protects universal human rights without destroying the cultural diversity '
                                       'that is the lifeblood of human evolution'}
u5keys = [key for key in u5_dict.keys()]
u6keys = [key for key in u6_dict.keys()]
u7keys = [key for key in u7_dict.keys()]
u8keys = [key for key in u8_dict.keys()]
keys = []
for key in u5_dict.keys():
    keys.append(key)
for key in u6_dict.keys():
    keys.append(key)
for key in u7_dict.keys():
    keys.append(key)
for key in u8_dict.keys():
    keys.append(key)

for key in u7_dict.keys():
    print(key)
    answer = input()
    if answer.lower() == u7_dict.get(key).lower():
        pass
    else:
        print(u7_dict.get(key))