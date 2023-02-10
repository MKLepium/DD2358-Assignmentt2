import numpy as np
import matplotlib.pyplot as plt

# array size:  50, Flops/s:  6.452213581502256e+06
# array size: 100, Flops/s:  8.456655341569153e+06
# array size: 150, Flops/s:  5.86158766211901e+06
# array size: 200, Flops/s:  4.700520412733408e+06
numpy = [6.452213581502256e+06, 8.456655341569153e+06, 5.86158766211901e+06, 4.700520412733408e+06]

# array size:  50, Flops/s:  6.279273737621226e+06
# array size: 100, Flops/s:  11.460815920013299e+06
# array size: 150, Flops/s:  5.831359680297444e+06
# array size: 200, Flops/s:  4.5058934535707475e+06
lists = [6.279273737621226e+06, 11.460815920013299e+06, 5.831359680297444e+06, 4.5058934535707475e+06]

# array size:  50, Flops/s:  6.316115830078326e+06
# array size: 100, Flops/s:  11.703580386807087e+06
# array size: 150, Flops/s:  5.961116375030808e+06
# array size: 200, Flops/s:  4.864849510306772e+06
arrays = [6.316115830078326e+06, 11.703580386807087e+06, 5.961116375030808e+06, 4.864849510306772e+06]

x = [50, 100, 150, 200]


plt.plot(x, numpy, "o", label="numpy")
plt.plot(x, lists, "o", label="lists")
plt.plot(x, arrays, "o", label="arrays")
plt.legend()
plt.xlabel("array size")
plt.ylabel("Flops/s")
plt.savefig("plot.png")