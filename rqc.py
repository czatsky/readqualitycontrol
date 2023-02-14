from statistics import mean
import gzip

# ad = input()
if __name__ == "__main__":
    with gzip.open(input(), 'rb+') as a:
        file = a.read()
        data = file.decode('utf-8')
        f1 = ((data).splitlines()[1::4])

    # ad2 = input()
    with gzip.open(input(), 'rb+') as a2:
        file2 = a2.read()
        data2 = file2.decode('utf-8')
        f12 = ((data2).splitlines()[1::4])

    # ad3 = input()
    with gzip.open(input(), 'rb+') as a3:
        file3 = a3.read()
        data3 = file3.decode('utf-8')
        f13 = ((data3).splitlines()[1::4])

class Datass:
    def __init__(self, f):
        self.f = f
        self.alphas = []
        self.lenghts = []
        self.lenset = set()
        self.meanp = []
        self.ns = []
        self.ki = set()
        self.readsn = []
        self.repeats = []
        self.repeats = self.an()

    def an(self):
        # alphas = []
        # lenghts = []
        lenset = set()
        meanp = []
        # ns = []
        # readsn = []
        for i in self.f:
            self.alphas.append(i)
            meanper = (((i.count('G') + i.count('C')) / (
                        i.count('A') + i.count('T') + i.count('G') + i.count('C') + i.count('N')) * 100))
            meanp.append(meanper)
            self.avg = round((mean(meanp)),2)
            self.lenghts.append(len(i))
            lenset.add(len(i))
            if i.count('N') > 0:
                npers = (i.count('N') / len(i)) * 100
                self.ns.append(npers)
                self.readsn.append(i)
        return self.repeats

    def rep(self):
        from collections import Counter
        cnt = Counter(self.alphas)
        for key, value in dict(cnt).items():
            if value > 1:
                self.repeats.append(value)
                self.ki.add(key)
        return self.repeats

    def test(self):
        print('Reads in the file =', len(self.alphas))
        print(f'Reads sequence average length = {round(mean(self.lenghts))}')
        print('')
        print('Repeats =',((len(self.repeats))-len(self.ki))) #!
        print(f'Reads with Ns = {len(self.readsn)}')
        print('')
        print('GC content average = ',(self.avg),'%',sep='')
        print(f'Ns per read sequence = {round((sum(self.ns) / (len(self.alphas))), 2)}%')

set1 = (len(Datass(f1).readsn),len(Datass(f1).repeats))
set2 = (len(Datass(f12).readsn),len(Datass(f12).repeats))
set3 = (len(Datass(f13).readsn),len(Datass(f13).repeats))

alll = [set1, set2, set3]

if min(alll) == set1:
    (Datass(f1).test())
if min(alll) == set2:
    (Datass(f12).test())
if min(alll) == set3:
    (Datass(f13).test())
