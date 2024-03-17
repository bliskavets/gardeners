#!/bin/bash
cat <<EOF | sudo tee -a .bashrc
# Test if nvidia-smi returns a 0 return code. If not, we print an error.
RED='\033[0;31m'
NC='\033[0m' # No Color
nvidia-smi > /dev/null
[ ! $? -eq 0 ] && echo -e "${RED}############ \n### \n  CAUTION : NVIDIA-SMI FAILED AND NEED TO BE CHECKED ! \n### \n############ ${NC}"
EOF
