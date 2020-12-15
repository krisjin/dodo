#!/bin/bash
parms=$1
#echo "begin to execute zip job,parms:$parms"
spark-submit run.py $parms
#echo "end to execute zip job!"
