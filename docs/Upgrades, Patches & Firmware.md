# Upgrades, Patches & Firmware
```bash
isi upgrade view
isi upgrade nodes list
isi_upgrade_status
isi_upgrade_logs
```

**Retry last action**
```bash
isi upgrade cluster retry-last-action --nodes=3
```

**Patch/Package**
```bash
isi_for_array -s 'isi_patch list'
isi upgrade patches list
isi_for_array -s tail -30 /var/log/isi_pkg
isi pkg info --forced_local
isi pkg delete
```

**Firmware**
```bash
isi upgrade cluster firmware devices
rm /var/ifs/upgrade/firmware_status.json
```

> **Version‑specific notes**
> - 8.2+: clearer upgrade logs
> - 9.5–9.7: some drive FW rollouts may need a reboot to complete
