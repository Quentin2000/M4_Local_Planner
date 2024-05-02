
import numpy as np

input = [100,   1,   1,   1,   1,   1, 100,   1,   1,   1,   1, 100, 100,   1, 100, 100,   1,   1,
   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
   1,   1,   1,   1,   1,   1,   1,   1,   1,   1]

input2 = [100,   100,   100,   1,   1,   1, 100,   1,   1,   1,   1, 100, 100,   1, 100, 100,   1,   1,
   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
   1,   1,   1,   1,   1,   100,   1,   1,   100,   1,   1,   1,   1,   1,   1,   1,   1,   1,
   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
   1,   1,   1,   1,   1,   1,   1,   1,   1,   1]


output = np.minimum(20*np.array(input), 100)
output2 = np.minimum(40*np.array(input2), 100)

output3 = np.minimum(output, output2).astype(np.int8)

print(output)

output_list = output.tolist()

print(output_list)

print(type(output_list))