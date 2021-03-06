from thread import start_new_thread
import time

work = []
done = []
def run(idx, num):
    print "thread %d starting" % idx, work
    for i in xrange(num):
        t = work.pop()
        work.append(t - 1)
        if i % 100000 == 0:
            print idx, i
    done.append(num)
    print "thread %d done" % idx

print "starting!"

nthreads = 1
N = 20000000 / nthreads
for i in xrange(nthreads):
    work.append(N)
for i in xrange(nthreads):
    t = start_new_thread(run, (i, N))

while len(done) < nthreads:
    time.sleep(0.1)

# print work
assert sum(work) == 0
print work
