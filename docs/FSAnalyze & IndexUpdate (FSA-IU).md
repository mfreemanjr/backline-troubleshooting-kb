# FSAnalyze & IndexUpdate (FSA‑IU)

**Modes**
```bash
isi_gconfig -t job-config jobs.fsa.snap_based_mode=true
isi_gconfig fsa.use_snapshot=false
```

**Remediation**
```bash
isi job cancel fsanalyze; isi job cancel indexupdate
isi_gconfig fsa.du_has_dpid=true
isi job start indexupdate; isi job start fsanalyze
```

**Index cleanup**
```bash
/usr/bin/isi_index_mod -ll
isi_index_mod -rk cluster_lin_index
isi_changelist_mod -x -l
```

> **Version‑specific notes**
> - 8.0: FSA snap debuts
> - 8.2.1–8.2.2: major stability fixes
> - 9.x: faster treewalks & better detection
