# Events, Alerts & Clearing
```bash
isi alert list
isi alert cancel <alert_id>
```

**8.x event groups**
```bash
isi event groups bulk --ignore=true
isi event groups bulk --resolved=true --ignored=true
isi event groups modify --id=<id> --resolved=true
```

> **Version‑specific notes**
> - 8.0+: event group model replaces classic
> - 9.0+: faster bulk ops, better state
