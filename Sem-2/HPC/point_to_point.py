#!/usr/bin/env python
# coding: utf-8

# In[8]:


from mpi4py.futures import MPIPoolExecutor
from mpi4py import MPI
import numpy as np


# In[9]:


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    message = "Hello from process 0"
    comm.send(message, dest=1)
    
    received_message = comm.recv(source=1)
    print(f"Process 0 received message: {received_message}")
    
elif rank == 1:
    received_message = comm.recv(source=0)
    print(f"Process 1 received message: {received_message}")
    
    reply = "Hello from process 1"
    comm.send(reply, dest=0)


# In[ ]:




