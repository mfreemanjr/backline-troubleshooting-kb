# Logs & Elvis Logsets
```
/mnt/sondgst1nv1/
*-*/varlog.tar/log/messages*
nodes_info
```

```bash
cat <Node>-*/varlog.tar/log/idi.log | grep -Eo '[0-9a-f]:[0-9a-f]{4}:[0-9a-f]{4}::[0-9A-H]{4,}' | sort | uniq
```
