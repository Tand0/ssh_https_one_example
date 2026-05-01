#!/bin/bash

if [ -z "$1" ]; then
    echo "usage: $0 site.yml"
    exit 1
fi

ansible-playbook $1 -i hosts.yml --vault-password-file ~/.vault_pass
