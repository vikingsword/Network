import jieba


def smart_segmentation(text):
    # 使用jieba进行中文分词
    words = list(jieba.cut(text))

    # 定义常见句子终止标点符号
    end_punctuations = ['。', '！', '？']

    # 根据标点符号进行语境分段
    segments = []
    segment = []
    for word in words:
        segment.append(word)
        if word in end_punctuations:
            segments.append(''.join(segment))
            segment = []

    # 如果最后一段不以句号结尾，则将其加入segments中
    if segment:
        segments.append(''.join(segment))

    return segments


if __name__ == '__main__':
    text = "　　第一卷。　　夜的第一章：奏鸣。　　　　年，秋。　　淅沥沥的小雨从灰色苍穹之上坠落，轻飘飘的淋在城市街道上。　　时值秋季，时不时还能看到没打伞的行人，用手挡在头顶匆匆而过。　　狭窄的军民胡同里，正有一个十七八岁的少年，与一位老爷子对坐在超市小卖部旁边的雨棚下面。　　雨棚之外的全世界灰暗，地面都被雨水沁成了浅黑色，只有雨棚下的地面还留着一片干燥地带，就像是整个世界都只剩下这一块净土。　　他们面前摆着一张破旧的木质象棋盘，头顶上是红色的福来超市招牌。　　将军，少年庆尘说完便站起身来，留下头发稀疏的老头呆坐着。　　少年庆尘看了对方一眼平静说道：不用挣扎了。　　我还可以老头不甘心的说道：这才下到十三步啊　　言辞中，老头对于自己十三步便丢盔弃甲的局面，感到有些难堪。　　庆尘并没有解释什么，棋盘上已杀机毕露，正是图穷匕见的最后时刻。　　少年面孔干净，眼神澄澈，只是穿着朴素的校服坐在那里，就像是把身边的世界都给净化的透明了一些。　　老头将手里举起的棋子给扔到了棋盘上，弃子认输。　　庆尘旁若无人的走进旁边超市的柜台里，从柜台下面的零钱篮子里拿了块钱揣进兜里。　　老头骂骂咧咧的看着庆尘：每天都要输给你块钱！我上午刚从老李老张那里赢来块钱，这会儿就全输给你了！　　庆尘揣好钱，然后坐回棋盘旁边开始复盘：要不是他们已经不愿意跟我下棋了，我也不至于非要通过你来赢钱。你需要面子，我需要钱，很公平合理。　　你就吃定我了是吧？老头嘟囔道：算命的说我能活到七十八岁，我现在才五十，这要是每天输你块钱，我得输出去多少钱？　　但我还教你下象棋去赢回面子，庆尘平静的回答道：这样算下来你并不亏。　　老头嘟囔道：但你这两天教的都是些没用的东西。　　庆尘看了他一眼：不要这样说自己。　　老头：？？？　　老头没好气的将棋盘重新摆好，然后急切道：行了行了，复盘吧。　　这一刻，庆尘忽然低头。　　那刚刚流逝过去的时间，像是从他脑中回放一般。　　当头袭来的炮，楚河汉界上的悍卒，在脑海里一一回荡。　　不止这些。　　还有下棋时从他们身旁路过的大叔，手里提着刚买的四个烧饼，刚出炉的烧饼晕开一些水汽，在透明塑料袋里染上了一层白雾。　　穿着白色裙子的小女孩撑伞走过，她小皮鞋的鞋面上还有两只漂亮的蝴蝶。　　苍穹之上，飘摇的雨水落在胡同里，晶莹剔透。　　胡同尽头，路公交车从狭窄的胡同口一闪而过，有一个穿着米色风衣的女人举伞奔向公交车站。　　脚步声，雨水汇入路旁窨井盖时的流水声，这些嘈杂的声音反而显得世界格外寂静。　　这一切，庆尘都不曾忘记，虽然回忆起来有些困难。　　但困难，不代表不可以。　　这古怪的记忆力，是庆尘与生俱来的天赋，就像是他随手从时间长河里抽取了一条存档，然后读取了那片存档磁条里的画面。　　庆尘忍住大脑的眩晕感，捏起了棋盘上的棋子。　　老头顿时不说话了，双眼全神贯注的盯着棋盘，每局之后的复盘也是赌局约定条款。　　庆尘负责教棋，老头输钱之后学棋。　　这一幕有些诡异，庆尘没有少年人面对长者时应有的谦虚与腼腆，反而像是老师一样。　　对方也并不觉得这有什么。　　红方炮二平五，黑方的炮八平五，红马二进三，黑马八进七，红方车一进一，黑方车九平八庆尘一步步挪动着棋子。　　老头眼睛都不眨一下，前面都是正常开局，可他想不通怎么到了第六步，自己明明吃了对方的马，却突然陷入了颓势。　　弃马十三招的精髓就在于第六步的进车弃马，这是撕开防线的杀手锏，庆尘静静的说着：你前天和王城公园里那个老头下的棋我看了，他喜欢顺跑开局，你拿这弃马十三招打他没有问题。　　对面的老爷子陷入深深沉思，然后小声问道：真能赢他？　　一个星期内学会我教你的弃马十三招，你就可以把面子找回来了，庆尘说道：毕竟他下的也不怎么样。　　老头面色上露出一丝喜色。　　但他又突然问道：学一个星期能赢他，那我学棋多久可以赢你？　　雨棚之下，庆尘认真思虑起来：算命的说你能活七十八岁吗那来不及了。　　老头面色一滞：你少说两句我说不定能活到七十九咦，你这会儿应该在上晚自习啊，今天怎么放学这么早？　　他知道庆尘是高二学生，今天周二，所以两条街外的十三中这时候应该正在晚自习。　　庆尘想了想回答道：我在等人。　　等人？老头愣了一下。　　庆尘起身看向雨棚外面的细雨，目光飘摇在雨幕中。　　老头说道：庆尘你小子下棋这么厉害，怎么不去参加象棋比赛？你不是说你缺钱吗，得了冠军也有钱拿啊。　　少年庆尘摇摇头：我只是将许多棋谱都记在了脑子里而已，并不是我下棋有多么厉害。记忆力并不代表分析能力，跟你们下下还行，真遇上高手就露怯了。我的路不在这里，下棋只是暂时的。　　全都记在脑子里老头感慨了一下：我以前觉得，过目不忘这种事情都是别人瞎编的。　　雨缓缓停了。　　就在此时，老头忽然发现庆尘愣了一下，他顺着少年的目光，朝着军民胡同尽头看去，正巧看到一对夫妻牵着一个小男孩走来。　　交流好书关注公众号【书友大本营】。现在关注可领现金红包！　　中年女子穿着精致的风衣，手里提着一个蛋糕盒子，盒子上系着紫色且好看的缎带。　　灰蒙蒙的世界也挡不住三人身上的喜悦神色，庆尘转身就走，留下老头坐在福来超市门口的雨棚下轻声叹气。　　中年女子看到了庆尘的背影，她开口喊了庆尘的名字，但庆尘头也没回的消失在了胡同的另一端出口。　　胡同两边的墙很旧了，白色墙壁脱落后，留下一块一块斑驳的红砖模样。　　庆尘要等的人来了，但他又不想等了。　"
    segments = smart_segmentation(text)
    for segment in segments:
        print(segment)
