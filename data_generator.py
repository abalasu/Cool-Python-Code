import pandas as pd
from faker import Faker
"""
def generate_data(field_name, field_type, length, minimum, maximum, description, number_of_recs):
    Faker.seed(0)
    locale_list=['en_US']
    fake = Faker(locale_list)
    generated_list = []
    i = 0
    if description == 'Phone':
        while i < number_of_recs:
           value = fake.phone_number()
           generated_list.append(value)
           i += 1
        return generated_list   
    if description == 'Address':
        while i < number_of_recs:
           value = fake.address()
           generated_list.append(value)
           i += 1
        return generated_list
    if description == 'City':
        while i < number_of_recs:
           value = fake.city()
           generated_list.append(value)
           i += 1
        return generated_list   
    if description == 'First Name':
        while i < number_of_recs:
           name = fake.first_name()
           generated_list.append(name)
           i += 1
        return generated_list   
    if description == 'Last Name':
        while i < number_of_recs:
           name = fake.last_name()
           generated_list.append(name)
           i += 1
        return generated_list
    if description == 'Number':
        while i < number_of_recs:
           value = fake.random_int(min=minimum, max=maximum)
           generated_list.append(value)
           i += 1
        return generated_list   

    return 

df = pd.read_csv('d:/pythondata/datastructure.csv')
number_of_recs = 50000
df2 = pd.DataFrame()

field_names = df.columns
gen_list = []
for i in df.index:
    field_name = df['Field_Name'][i]
    field_type = df['Field_Type'][i]	
    length = df['Length'][i]	
    minimum	= df['Min'][i]
    maximum	= df['Max'][i]
    description = df['Description'][i]
    gen_list = generate_data(field_name, field_type, length, minimum, maximum, description, number_of_recs)
    df2[field_name] = gen_list

df2.to_csv('d:/pythondata/generated.csv',index=False)

"""

import pyarrow as py
import time
import pyarrow.parquet as pq
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

#df1 = load_df_reg("d:/pythondata/generated.csv")
#table = py.Table.from_pandas(df1)
#pq.write_table(table, 'd:/parquet/generated.parquet')

start_time = time.time()
df1 = pd.read_csv("d:/pythondata/generated.csv",engine='c')
end_time = time.time()
print('Elapsed Time is ', end_time - start_time)


start_time = time.time()
df1 = pd.read_parquet("d:/parquet/generated.parquet",engine='fastparquet') 
end_time = time.time()
print('Elapsed Time is ', end_time - start_time)
