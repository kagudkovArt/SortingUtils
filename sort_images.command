#!/bin/bash

# Go to home directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd ~
# You can change what anaconda version you want at
# https://repo.continuum.io/archive/
# Anaconda3-4.1.1-MacOSX-x86_64.sh
FILE=Anaconda3-2019.07-MacOSX-x86_64.sh
ANACONDA_DIR=~/anaconda

if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist"
    curl -Ok https://repo.continuum.io/archive/Anaconda3-2019.07-MacOSX-x86_64.sh
fi

if [ ! -d "$ANACONDA_DIR" ]; then
    echo "installing anaconda"
    yes | bash Anaconda3-2019.07-MacOSX-x86_64.sh -b -p ~/anaconda
    source ~/anaconda/bin/activate
    conda init
    # Refresh basically
    source ~/.bash_profile

    yes | conda update conda
fi

ENV=sorting_util_env
ENVS=$(conda env list | awk '{print $1}' )

echo "$ENVS"

if [[ $ENVS = *"$ENV"* ]]; then
    echo "$ENV exists"
    source activate "$ENV"
else
    echo "$ENV doesn't exist"
    yes | conda create --name $ENV
    conda activate "$ENV"
    yes | conda install -c conda-forge opencv
fi

cd $SCRIPT_DIR
echo "run sort_images.py"
python sort_images.py
