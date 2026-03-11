# Risky Commands (Read First)

!!! warning "⚠️ SAFETY WARNING — High‑risk operations"
    The commands below can cause **service impact**, **node panics**, or **data unavailability** if misused.

    **Run only with explicit guidance and maintenance windows, capture pre/post‑state, and have rollback.**

- `killall` / `killall -9` *(e.g., `isi_job_d`)* — may abruptly terminate core daemons.
- `isi_test_thread "lbm_drive_stats(<LNUM>)"` — **NEVER** run on **L3 SSD**; internal testing only.
- `isi_rbm_panic`, `kldload reboot_me`, `kldload panic_me` — force reboot/panic; **outage by design**.
