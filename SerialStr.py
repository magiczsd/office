#Written by magiczsd
#主要功能：从一窜字符串里找出不同的字符串连续出现的最多个数
# coding=utf-8
class SerialStr(object):
    def __init__(self,st):
        self.st = st
    def SerialNumbers(self):
        st_list = list(set(self.st))
        st_len = len(self.st)
        series_list = []
        for s in st_list:
            for n in range(self.st.count(s), 1,-1):
                if s*n in self.st:
                    series_list.append({'st':s,'num':n})
                    break
        series_list = sorted(series_list, key = lambda x : x['num'], reverse = True)
        return series_list
if __name__ == '__main__':
    st = '1232hjhhh1222kjasdas57d2398ascknxzcxznczxnccncnllkeqwjenajdac,z.,..,zxmc,mkjnbqjkwbjkasldkaslnncxzkjhehrjkndfkkkkdfjjknakndlka'
    n = SerialStr(st).SerialNumbers()
    print(n)