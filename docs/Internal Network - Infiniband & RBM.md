# Internal Network — Infiniband & RBM
```bash
isi_for_array -sXI 'for i in $(isi_nodes %{name}":"%{internal_a_address}":"%{internal_b_address}); do ... done'
```

```bash
id=$(isi_nodes -L %{id}); sysctl efs.rbm.devices | grep -B4 "sock: 0x0"
```

> **Version‑specific notes**
> - 9.1+: clearer RBM device reporting
