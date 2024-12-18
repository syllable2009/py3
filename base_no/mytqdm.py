from tqdm import tqdm
import time
from tqdm import trange

# for i in tqdm(range(60)):
#     pass
#     time.sleep(0.5)

# for i in trange(5):
#         pass
#         time.sleep(0.5)

print((lambda x, y: x+y)(2, 4))
print((lambda x, y: x if x < y else y )( 1, 2 ))
print(map(lambda x: x*2, [1,2,3,4,5]) )