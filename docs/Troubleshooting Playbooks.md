# Troubleshooting Playbooks

### Network port no carrier (external)
1. Check cables/ports
2. Swap cable/port; review switch logs
3. Validate pool config (expectations)

**Helpful outputs**
```bash
isi networks list interfaces -v
netstat -an; ifconfig -a; pciconf -lv
```
