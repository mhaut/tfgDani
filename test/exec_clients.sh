
numberPkg=4

for i in `seq 0 $numberPkg`
do
    python ../clientSim.py &
done
