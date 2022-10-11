import regex as re
import sys


class parser:

    def __init__(self, f):
        self.re = self.genRE()
        self.f = f

    def genRE(self):
        return re.compile(r'[\S\s]*?<eor>', re.I | re.M)

    def getField(self, f, t):
        p = r'<{}:(\d+)>(.*?)$'.format(f)
        r = re.search(p, t, flags=re.M)
        if r:
            text = r.group(2)
            len = int(r.group(1))
            return text[0:len]
        else:
            return ''

    def parse(self):
        t = ''
        with open(self.f, 'r') as f:
            while True:
                try:
                    l = f.readline()
                    if not l:
                        break
                    t += l
                except UnicodeDecodeError:
                    continue
        list_qso = self.re.findall(t)
        for qso in list_qso:
            call = self.getField(r'call', qso)
            freq = self.getField(r'freq', qso)
            mode = self.getField(r'mode', qso)
            date = self.getField(r'qso_date', qso)
            time = self.getField(r'time_on', qso)
            rsts = self.getField(r'time_on', qso)
            rstr = self.getField(r'rst_rcvd', qso)
            name = self.getField(r'name', qso)
            comment = self.getField(r'comment', qso)
            yield call, freq, mode, date, time, rsts, rstr, name, comment


if __name__ == '__main__':
    p = parser(sys.argv[1])
    l = p.parse()
    for q in l:
        # print(r'===========================================')
        print(q[0],q[8])
        # print(r'===========================================')
