# Locking, Vnodes & Performance Signals
```bash
isi_for_array -X 'sysctl efs.lin.lock.initiator.oldest_waiter | grep -E "address|started"' | sort -nk4
```

```bash
isi_sysctl_cluster kern.maxvnodes=2000000
```

```bash
while true; do date; sysctl isi.lwext.mbuf_mem isi.lwext.mbuf_data isi.lwext.mbuf_fds kern.mbaudit; sleep 5; done
```
