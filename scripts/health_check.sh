#!/bin/bash
log_infp() { echo "[INFO]" $1; }
log_infp "Hello check running"
log_infp "User: $(whoami)"
log_infp "Uptime: $(uptime)"
