import pandas as pd
import pyarrow as py
import time

def timeit(func):
    """ Timeit Function prints the elapsed time of a function """
    def inner(file_name):
        start_time = time.time()
        df1 = func(file_name)
        end_time = time.time()
        print('Elapsed Time is ', end_time - start_time)
        return df1
    return inner

@timeit
def load_df_reg(file_name):
    df = pd.read_csv(file_name)
    return df

@timeit
def load_df_pyarrow(file_name):
    df_pyarrow = pd.read_csv(file_name, engine="pyarrow")
    return df_pyarrow

df1 = load_df_reg("d:/pythondata/input_test.csv")
df2 = load_df_pyarrow("d:/pythondata/input_test.csv")
print(type(df1))
print(type(df2))
print(df1.describe())
print(df2.describe())
i = 0
j = 0
st = time.time()
for x in range(len(df1)):
    i = i+1
et = time.time()
print('Elapsed Time ', et-st)
st = time.time()
for x in range(len(df2)):
    j = j+1
et = time.time()
print('Elapsed Time ', et-st)
print(i, j)

print(timeit.__doc__)
print(help(timeit))