
# We collect here code snippets
We can also post on gist, e.g. https://gist.github.com/cmaurini

## Methods to solve linear systems

## Save to file

Write in XDFM format for paraview


```python
with df.XDMFFile(mesh.mpi_comm(), "output/u.xdmf") as file:
        file.write(us,  0)
```

Write in XDFM format for checkpointing 


```python
with df.XDMFFile(mesh.mpi_comm(), "output/u-cp.xdmf") as file:
        file.write_checkpoint(us, "us-cp", 0, append=False)
```

and then to read back


```python
with df.XDMFFile(mesh.mpi_comm(), "output/u-cp.xdmf") as file:
        file.read(us, "us-cp", 0)
```
