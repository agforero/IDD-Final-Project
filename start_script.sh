#!/bin/bash

./writer.py &
./interface.py
kill %1 # this kills the writer process.
