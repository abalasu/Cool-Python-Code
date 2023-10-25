import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.DataFrame({'one': [-1, np.nan, 2.5],
                   'two': ['foo', 'bar', 'baz'],
                   'three': [True, False, True]},
                   index=list('abc'))

print(df)
table = pa.Table.from_pandas(df)
print(table)
pq.write_table(table, 'd:/parquet/example.parquet')