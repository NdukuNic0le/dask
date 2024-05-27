from dask.distributed import Client, LocalCluster

def main():
   cluster = LocalCluster()
   client = Client(cluster) 

   print(cluster.scheduler)
   print(cluster.workers)
   print(client)


if __name__ == "__main__":
    main()