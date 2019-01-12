import time, random

print('on GO, hit ENTER!')
time.sleep(2)
for i in range(0,40):
    print(' ')
print('3...')
time.sleep(2)
for i in range(0,40):
    print(' ')
print('2..')
time.sleep(2)
for i in range(0,40):
    print(' ')
print('1..')
time.sleep(1)
for i in range(0,40):
    print(' ')
time.sleep(random.randint(2,6))
print('!!__GO__!!')
tic = time.perf_counter()
a = input()
toc = time.perf_counter()
timeSpent = toc-tic
print('your time was ' + str(timeSpent) + ' seconds')
time.sleep(5)
