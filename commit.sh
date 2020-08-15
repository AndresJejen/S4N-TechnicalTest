#! /bin/bash

set -e

Branch="$(git symbolic-ref --short HEAD)"
echo "Current Branch $Branch"
echo "Commit Message: $1";
git add -A
git commit -m "$1"
git push origin "$Branch"

echo "¿Desplegar en Master?: [si/no]";
read res;

if test $res = "si"; then
    echo "Cargado a $Branch OK";
    git checkout master
    git pull origin master
    git merge "$Branch"
    git push origin master
    git checkout "$Branch"
    echo "Cargado a Master OK";
else
    echo "No Master";
fi
