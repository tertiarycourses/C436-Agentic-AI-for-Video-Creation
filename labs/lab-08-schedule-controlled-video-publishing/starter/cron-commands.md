# Hermes Cron Commands

```bash
hermes cron create "0 9 * * 2" "Use the self-contained prompt in starter/release-job-prompt.md" --skill harbour-bean-video --name "Weekly approved video release"
hermes cron list
hermes cron status
```

Create the job paused through Hermes chat or the supported edit command, inspect the returned job ID, trigger one dry run, then enable only after approval. Never edit `~/.hermes/cron/jobs.json` directly.
