#!/bin/bash

#
# Script to create a custom named TMUX session that 
# hosts the python3 session running my discord bot
#

sName="discord-bot"

if tmux ls | grep -q $sName; then
	tmux kill-session -t $sName
fi

tmux new-session -d -s "$sName" 'cd ~/discord/prodbot/ && ./start.sh'
