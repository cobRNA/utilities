#!/bin/bash

#set -e
#set -x


# Bash script creating new Python3.11 virtual environment
# Usage: ./create_env.sh [DIR_NAME]
# [DIR_NAME] argument is optional, if absent or exists the prompt will appear
# E.g.
# ./create_env.sh new_python_project
# New vent will appear in the new_python_project directory


if [ $# -eq 0 ]; then
echo "Enter new directory name: "
read dirname

else
dirname=$1
fi

while (test -d $dirname)
do
  echo "Directory exists."
  echo "Enter new directory name: "
  read dirname
done

if !(test -d $dirname); then
  echo "New directory created."
  #mkdir $dirname
  #cd $dirname
  python3.11 -m venv $dirname
  source $dirname/bin/activate
  python -m pip install --upgrade pip
  python -m pip install pip-tools black pylint mypy
  python -m pip install notebook
  python -m ipykernel install --user --name=$dirname
fi

echo "Press [ENTER] to exit."
read -s
exit
