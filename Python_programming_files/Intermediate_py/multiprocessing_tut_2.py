from multiprocessing import Pool

def job(num):
    return num * 2

if __name__ == '__main__':
    p = Pool(processes=20)
    data = p.map(job, range(20))#the last iterable can be anythin, list , a single num, range of values
    p.close()
    print(data)
