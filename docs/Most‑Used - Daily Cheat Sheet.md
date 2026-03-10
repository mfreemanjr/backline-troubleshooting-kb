# Most‑Used / Daily Cheat Sheet

## Cluster and services
```bash
isi status
isi services -a
isi devices
isi statistics query current
isi events list --reduced
isi alert list --show-active
```

## Jobs
```bash
isi job list
isi job status
isi job view <id>
isi job statistics view --job-id <id> -v
```

## Networking quick view
```bash
isi networks list interfaces -v
netstat -n | grep 445   # SMB
netstat -n | grep 2049  # NFS
```
