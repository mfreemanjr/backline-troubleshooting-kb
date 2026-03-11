# Hardware — Nodes — Inventory — Boot

**BMC/CMC/CAR**
```bash
/usr/bin/isi_hwtools/isi_ipmicmc -d -V -a bmc|cmc|car
```

**DRAM / ECC**
```bash
/usr/bin/isi_hwtools/isi_hw_check -s -m safe.id.dram
/usr/bin/isi_hwtools/isi_hw_check -m safe.id.memsize | grep DRAM
```

!!! warning "⚠️ SAFETY — outage by design"
    Panic/reboot triggers below cause immediate outage — do **not** run on production clusters.

```bash
isi_rbm_panic <LNN>
kldload reboot_me
kldload panic_me
```
