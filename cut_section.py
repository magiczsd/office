#Written by magiczsd
#此代码实现将一段文字按规定的数量大致分段，前后误差一句话左右，分段会按照标点符号来划分，优先'。！？；'，最后按'，'划分。
# coding=utf-8
import math
class CutSection(object):
    def __init__(self, text,wordNumber):#wordNumber为切割的字数数量
        self.text = text
        self.wordNumber = wordNumber
    def cutSection(self):
        sectionCounts = math.ceil(len(self.text)/self.wordNumber)#确定需要按多少字标准分几段，以400字为例
        sectionLists = []#用于存放分段的文章
        firstIndexList = []
        for i in range(0,sectionCounts+10):#
            length = len(self.text)#每一次循环计算剩余的文章长度
            try:
                firstIndex1 = self.text.index('。',-self.wordNumber)#找出倒数401个字符串里的第一个句号在全文中的索引
                firstIndexList.append(firstIndex1)
            except:
                pass
            try:
                firstIndex2 = self.text.index('？', -self.wordNumber)
                firstIndexList.append(firstIndex2)
            except:
                pass
            try:
                firstIndex3 = self.text.index('！', -self.wordNumber)
                firstIndexList.append(firstIndex3)
            except:
                pass
            try:
                firstIndex4 = self.text.index('；', -self.wordNumber)
                firstIndexList.append(firstIndex4)
                #print(firstIndex4)
            except:
                pass
            try:
                firstIndex5 = self.text.index(' ', -self.wordNumber)#如果没有空格，则空格数量为0
            except:
                firstIndex5 = 0
            try:
                firstIndex6 = self.text.index('，', -self.wordNumber)#如果没有逗号，则逗号数量为0
            except:
                firstIndex6 = 0
            #如果。；？！在文中的位置不是在文章末尾，则按最前面的符号的索引值取值，如果在末尾，但是有逗号，那么取最前面的逗号索引值，如果没有逗号，则按最前面的空格索引值 取值
            firstIndexList.append(length - 1)#如果一个标点符号没有，又不加入length - 1的话  列表会是一个空列表，min方法会报错
            if min(firstIndexList) < length - 1:#如果有。？！；的索引值小于总长度-1，那么说明截取的400字里有其中一种标点符号，那么取值，会按这个标点符号所在的位置右边截取
                firstIndex = min(firstIndexList)
            elif firstIndex6 < length - 1 and firstIndex6 != 0:#如果文章中没有。？！；，那么先判断逗号的索引值是不是小于总长度-1，同时还要满足最少有一个逗号，也就是索引值不能为0
                firstIndex = firstIndex6
            elif firstIndex5 != 0:
                firstIndex = firstIndex5#如果文章中什么标点符号都没有，则按空格截取
            else:
                firstIndex = -1#取-1的目的是为了让下面的[-(length - firstIndex - 1):]变成[-length :]，这样self.text[-length :]就是截取剩余的所有self.text
            lastSection = self.text[-(length - firstIndex - 1):]  # 截取最后一段文章，剩余的文章长度-倒数400字符中第一个取值在剩余文章中的索引，可以得到该句号之后的文章长度，再减去1，即表示从句号右边的字符开始，整体添加一个-号，即表示倒数
            sectionLists.append(lastSection)
            self.text = self.text.replace(lastSection, '')#将lastSection替换成空白，也就是直接去除已经截取的部分，
            if len(self.text) < self.wordNumber or len(self.text) == self.wordNumber:
                sectionLists.append(self.text)
                break
        return sectionLists
if __name__ == '__main__':
    text = '中国人民银行日前发布第18号公告称，人民币是中国的法定货币，人民币现金是中国境内最基础的支付手段，任何单位和个人不得拒收。公告明确，不得排斥和歧视现金支付。消费及支付方式创新要坚持有利于畅通支付流通环境、有利于保障民生、有利于提升公众的幸福感和获得感，不得采取歧视性或非便利性措施排斥现金支付，造成“数字鸿沟”。中国人民银行有关负责人表示，今年新冠肺炎疫情的出现，对现金收付环境产生了新的影响，拒收现金问题有所反弹：一是部分医疗、出行、水电煤气等基本公共服务以及普通生活消费等领域由原本的“面对面”线下场景逐步变为线上办理，有的甚至取消了现场服务；二是“非接触式”等新消费模式很多没有考虑现金收付需求，造成部分群体特别是老年人消费及支付障碍；三是一些商户服务人员热衷于引导顾客安装APP、关注小程序，容易产生歧视、排斥现金情况。为解决上述问题，中国人民银行发布第18号公告，旨在进一步普及现金收付规范要求，促成社会各界达成维护人民币法定地位的共识，共建多元化支付条件下的现金和谐流通环境。中国人民银行方面表示，打造多元化支付条件下的现金和谐流通环境，将主要聚焦以下五项工作：一是采取多种措施，保障公众合理、安全、顺畅地使用现金；二是持续优化人民币设计水平，发挥其文化传播功能；三是强化大额现金管理，提高现金流通效率；四是支持多元化支付方式发展，尊重公众支付选择权，鼓励相关经营主体在保障现金收付渠道通畅的前提下，选择安全合法的非现金支付工具；五是不断完善现金服务基础设施、提升现金服务水平。据介绍，此次发布的第18号公告与2018年发布的第10号公告相比，内容更加全面和具体。首先，第18号公告从现金收付的整体生态环境出发，将现金流通、使用和管理的主体划分为现金收付主体、现金收付服务主体及现金生态主体等三大类。其次，聚焦公众日常生活消费的高频场景，明确了行政事业性收费、基本公共服务、交通运输、大中型商业机构、小微经济主体以及线下无人销售、线上网络经营等不同现金收付主体、不同场景、不同支付方式下的现金收付要求，进一步厘清了拒收现金行为边界。最后，对各类金融机构、非银行支付机构及自助服务机具厂商等现金服务主体提出指导性意见，并对相关行业主管部门、基层社区和社会公众提出倡议，号召大家共同维护现金流通生态环境。公告指出，公众享有自主选择支付方式的权利，因现金支付受到排斥或歧视的，应保留证据，并及时向中国人民银行当地分支机构反映，依法维权。公众应培养良好的现金使用习惯，自觉爱护人民币、维护人民币形象。任何单位和个人存在拒收现金或者采取歧视性措施排斥现金支付等违法违规行为的，由中国人民银行分支机构会同当地有关部门依法予以查处。（记者 徐佩玉）'
    wordNumber = 400
    list = CutSection(text,wordNumber).cutSection()
    for i in range(0,len(list)):
        print(list[i],len(list[i]))
        print(i,'------------------------')
