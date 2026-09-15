# Hermes Kanban Commands

```bash
hermes kanban create "Research approved claims" --assignee researcher
hermes kanban create "Create video master" --assignee video-producer
hermes kanban create "Review exact master" --assignee independent-reviewer
hermes kanban create "Approve exact payload" --assignee human-owner
hermes kanban create "Upload private to YouTube" --assignee youtube-uploader
hermes kanban list
```

Use the returned task IDs with the current Hermes `kanban link` help. Do not invent IDs. Request review before completion and keep the upload task blocked until both review and human approval parents are done.
