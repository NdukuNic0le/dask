import numpy as np
import pandas as pd

import dask
import dask.dataframe as dd

from dask.distributed import Client

def main(): 
    data_dict = {
        "a": np.arange(5000),
        "b": np.random.randn(5000),
        "c": np.random.choice(["a", "b", "c"], 5000)
    }

    df = pd.DataFrame(data_dict)

    ddf = dd.from_pandas(df, npartitions=10)

    sum_df = ddf.groupby("c").sum()
    mean_df = ddf.groupby("c").mean()

    #mean_df.visualize() pip install visualizing software first - graphviz

    @dask.delayed
    def increment (x: int) -> int:
        return x + 1
    
    @dask.delayed
    def add(x: int, y: int) -> int:
        return x + y
    
    a = increment(1)
    b = increment(2)
    c = add (a, b)

    c.visualize()
    c = c.compute()

    print (sum_df.compute())
    print (mean_df.compute())
    print (c)



if __name__ == "__main__":
    client = Client()
    main()