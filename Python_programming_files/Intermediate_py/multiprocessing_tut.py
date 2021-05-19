import multiprocessing

def spawn(num):
    print("Spawned! {}".format(num))

if __name__ == '__main__':
    for i in range(55):
        p = multiprocessing.Process(target=spawn, args =(i,))
        # when there is only one argument remember the comma after the arg_name
        p.start()
        # use p.join when you want to do the proceses subsequently and not randomly
        p.join()

'''
import multiprocessing

def spawn():
    print('Spawned')

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn)
        p.start()
        p.join()
'''
