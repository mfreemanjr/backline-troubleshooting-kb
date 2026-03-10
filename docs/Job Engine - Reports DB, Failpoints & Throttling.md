# Job Engine — Reports DB, Failpoints & Throttling

**Pin reports DB**
```bash
isi set -r -g retune -a random -p 3x -F --nodepool <npid> /ifs/.ifsvar/modules/jobengine/reports.db
```

**Reports DB (sqlite)**
```bash
cd /ifs/.ifsvar/modules/jobengine
sqlite3 reports.db
select job_id,progress,waiting_on_jid,status from jobs where progress='';
```

**Failpoint**
```bash
isi_for_array "isi_ufp -t -C isi_job_d_ufp skip_coord_update_needed_ret='return(0)'"
isi_for_array "isi_ufp -t -C isi_job_d_ufp skip_coord_update_needed_ret='off'"
```

**Throttle tuning (examples)**
```bash
isi_gconfig -t job-config impact.profiles.high.fixed_worker_count=1
isi_gconfig -t job-config impact.profiles.low.workers_per_core=0
```

> **Version‑specific notes**
> - 8.1–8.2: "database is locked" more common; 9.x reduces frequency
> - 9.1+: `core.load_balance_interval_sec` is impactful
