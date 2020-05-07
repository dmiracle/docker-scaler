#!/bin/bash
SERVICES=$(docker service ls | grep _app)
i=0
echo ${SERVICES[1]}

for S in $SERVICES
do
    i=$(($i+1))
    echo $i
    echo $S
done 

