# Cluster Health & Status
```bash
isi status -qpv
isi services -a
isi devices
isi cluster view
isi network interfaces list
isi auth status
```

**System & drive stats**
```bash
isi statistics system list --nodes=all
isi statistics drive list --nodes=all --sort=queued --limit=10
isi statistics heat list --limit 10 --long --event contended,blocked
```

> **Version‑specific notes**
> - 9.2+: better scaling under high node counts
> - 9.3–9.4: improved drive telemetry (busy/queued)
