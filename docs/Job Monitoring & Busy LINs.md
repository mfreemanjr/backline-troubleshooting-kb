# Job Monitoring & Busy LINs
**Busy vnodes**
```bash
isi_for_array -s 'for n in $(sysctl efs.bam.busy_vnodes | egrep "isi_job_d" | egrep -o "[[:alnum:]]{1,4}:[[:alnum:]]{4}:[[:alnum:]]{4}" | sort | uniq); do isi get -L "$n"; done'
```

**Continuous watch**
```bash
while true; do
  date; isi status -qpv;
  isi_for_array -X sysctl efs.lbm.drive_space | grep blkfree | sort -nk3 -t "=" | head;
  for i in $(isi job list|awk '/^[0-9].*Running/{print $1}'); do
    isi job view $i; isi job statistics view -v --job-id=$i | grep -o 'Workers: [0-9]*' | sort | uniq -c;
  done; sleep 60; echo;
done
```

> **Version‑specific notes**
> - 9.2+: higher worker scale
> - 9.3–9.4: better busy_vnodes correlation
