#!/usr/bin/env bash
if [ -n "$CREDENTIALS_DIRECTORY" ] && [ -f "$CREDENTIALS_DIRECTORY/restic" ]; then
    cat "$CREDENTIALS_DIRECTORY/restic"
else
    secret-tool lookup service restic account Sintax
fi

# Setup with:
# systemd-creds --user encrypt --name=restic ~/.config/resticprofile/default-key.encrypted
# secret-tool store --label="Restic" service restic account REPONAME
# Override systemd service:
# [Service]
# LoadCredentialEncrypted=restic:/home/rojikku/.config/resticprofile/default-key.encrypted