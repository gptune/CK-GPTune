#!/bin/bash

source ~/.bash_profile

sh patch_mac.sh

ck detect soft:lib.gptune
ck detect soft:lib.openmpi
