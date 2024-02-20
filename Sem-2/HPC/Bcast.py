#!/usr/bin/env python
# coding: utf-8

# In[3]:


from mpi4py import MPI
import numpy as np


# In[4]:


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print("Root process (Rank 0) is broadcasting data to other processes...")
else:
    print("Process", rank, "is waiting to receive broadcasted data from the root process (Rank 0)")

data = np.empty(1, dtype=int)
if rank == 0:
    data[0] = np.random.randint(0, 100)
comm.Bcast(data, root=0)

print("Process", rank, "received data:", data[0])

