#!/bin/bash

_relogio() {
  sleep 1
  s=$((s+1))
  export RETORNO=$s
  return
}

 
while true 
do
	_relogio
        echo $RETORNO > timeResult1.txt
done


