#!/bin/bash
set -ev
nohup pipenv run server > ./ci-build.log &
pipenv run mn >> ./ci-build-nm.log &
sleep 60 && exit 0
