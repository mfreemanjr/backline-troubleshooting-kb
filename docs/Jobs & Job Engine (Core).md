# Jobs & Job Engine (Core)

**Core commands**
```bash
isi job list
isi job status <id>
isi job view <id>
isi job start <JobName>
isi job cancel <JobName or --job-id>
```

!!! warning "⚠️ SAFETY — service disruption risk"
    Prefer controlled restarts over hard terminations.

**Prefer service control (safer)**
```bash
isi services -a isi_job_d disable
sleep 60
isi services -a isi_job_d enable
```

**If directed by Support (last resort)**
```bash
isi_for_array -s killall -9 isi_job_d
```

> After restart, verify: `isi_for_array ps awux | grep job_d`

> **Version‑specific notes**
> - 8.0: JE redesign (coordinator/throttling)
> - 9.0–9.2: steadier coordinator
> - 9.3+: better handling of very large snapshots & CloudPools datasets
