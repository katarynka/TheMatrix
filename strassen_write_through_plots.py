import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

katarzyna = True

if katarzyna:
    sys.path.append("/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix")
    path = "/home/katarzyna/Documents/school/applied_algo/exam/fresh_copy/TheMatrix/"
else:
    sys.path.append("/home/gustavgyrst/Desktop/AA_Final/TheMatrix")
    path = "/home/gustavgyrst/Desktop/AA_Final/TheMatrix/"

plot_path = "experiments/Results/plots/"


m_ticks = [0,2,4,8,16,32,64]
n = 128

m_label = [str(tick) for tick in m_ticks]

n_legend = ["n=128"]

#### WRITE THROUGH

# write_through_path = "experiments/Results/write_through_m_experiments/"

# name = "n128_recursive_write_through_n_fixed_mtest_ktob.csv" #### modify filename


# write_through_df = pd.read_csv(path + write_through_path +  name)

# write_through_df['nano_seconds/runtime'] = write_through_df.apply(lambda x: (1000000000*x['time(s)']) / n**3, axis=1)    


# print(write_through_df)


# #### PLOTTING

# fig = plt.figure()
# ax = fig.gca()

# # plot scaled runtime in nanosec
# # ax.errorbar(write_through_df['n'], write_through_df['nano_seconds/runtime'], capsize = 3.0, marker = 'o')
# # ax.set_ylabel("time (nano s)")


# # plot actual time in sec
# ax.errorbar(write_through_df['n'], write_through_df['time(s)'], capsize = 3.0, marker = 'o')
# ax.set_ylabel("time (s)")

# # ax.set_yscale('log', base=2)
# # ax.set_xscale('log', base=2)
# plt.xticks(m_ticks, m_label)

# ax.set_xlabel("m")
# ax.legend(n_legend)

# #save plot as pdf
# plt.savefig(path+plot_path+ "recursive_write_through_fixed_n_actual_time_res.pdf")





#### STRASSEN
strassen_path = "experiments/Results/strassen_m_experiments/"

name = "n128_strassen_n_fixed_mtest_ktob.csv"

strassen_df = pd.read_csv(path + strassen_path +  name)
print(strassen_df)

    # df = df[df.index > 1]
strassen_df['nano_seconds/runtime'] = strassen_df.apply(lambda x: (1000000000*x['time(s)']) / n**2.8, axis=1)
    


print(strassen_df)


#### PLOTTING

fig = plt.figure()
ax = fig.gca()


ax.errorbar(strassen_df['n'], strassen_df['nano_seconds/runtime'], capsize = 3.0, marker = 'o')
ax.set_ylabel("time (nano s)")

# ax.errorbar(strassen_df['n'], strassen_df['time(s)'], capsize = 3.0, marker = 'o')
# ax.set_ylabel("time (s)")

ax.set_yscale('log', base=2)
# ax.set_xscale('log', base=2)
plt.xticks(m_ticks, m_label)

#outside for-loop
ax.set_xlabel("m")
ax.legend(n_legend)

#save plot as pdf
plt.savefig(path+plot_path+ "strassen_fixed_n_scaled_runtime.pdf")