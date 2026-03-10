# Drives — Health, Smartfail, Stalls & Boot Flash

**List & smartfail**
```bash
isi devices drive list --format=table -v
isi devices -a smartfail -d 2:35
```

**Boot flash wear**
```bash
isi_for_array -s 'isi_radish -a /dev/ad*' | grep "Percent Life" | grep -v Used
```

**Drive stalls (logs)**
```bash
grep 'changed to stalled' */varlog.tar/log/messages | grep -o 'node [0-9]* drive [0-9]* changed to stalled' | sort | uniq -c
```

!!! warning "⚠️ SAFETY — internal test entry point"
    **NEVER** run on **L3 SSD**; use only when instructed by Support.

```bash
isi_test_thread "lbm_drive_stats(<LNUM>)"
```
