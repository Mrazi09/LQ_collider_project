#!/bin/bash

cd /scratch_p/jpedropino/1-LQCollider-project/ZZ
for i in {1..6}; do
rm -r Folder_commands_$i.sh 2> /dev/null
touch Folder_commands_$i.sh 2> /dev/null
echo "define j = g u c d s u~ c~ d~ s~ b b~" >> Folder_commands_$i.sh
echo "p p > z z, (z > l+ l-), (z > l- l+)" >> Folder_commands_$i.sh
echo "add process p p > z z j, (z > l+ l-), (z > l- l+)" >> Folder_commands_$i.sh
echo "add process p p > z z j j, (z > l+ l-), (z > l- l+)" >> Folder_commands_$i.sh
echo "add process p p > z z j j j, (z > l+ l-), (z > l- l+)" >> Folder_commands_$i.sh
echo "output Backgrounds/ZZ_$i" >> Folder_commands_$i.sh
echo "exit" >> Folder_commands_$i.sh
done


for i in {1..6}; do
rm -r Production_commands_$i.sh 2> /dev/null
touch Production_commands_$i.sh 2> /dev/null
echo "#!/bin/bash" >> Production_commands_$i.sh
echo "#SBATCH -n 1" >> Production_commands_$i.sh
echo "#SBATCH --cpus-per-task=1" >> Production_commands_$i.sh
echo "#SBATCH --mem-per-cpu=10500mb" >> Production_commands_$i.sh
echo "#SBATCH --mail-type=ALL" >> Production_commands_$i.sh
echo "#SBATCH --mail-user=jpedropino@ua.pt" >> Production_commands_$i.sh
echo " " >> Production_commands_$i.sh
echo "cd /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0" >> Production_commands_$i.sh
echo "./bin/mg5_aMC /scratch_p/jpedropino/1-LQCollider-project/ZZ/Folder_commands_$i.sh" >> Production_commands_$i.sh
echo "cd /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0" >> Production_commands_$i.sh
echo "./bin/mg5_aMC /scratch_p/jpedropino/1-LQCollider-project/ZZ/Scan_commands_$i.sh" >> Production_commands_$i.sh
echo "" >> Production_commands_$i.sh
echo "cd /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/Backgrounds/ZZ_$i/bin" >> Production_commands_$i.sh
echo "./cleanall" >> Production_commands_$i.sh
echo "" >> Production_commands_$i.sh
echo "cd /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/Backgrounds/ZZ_$i/Events/run_01" >> Production_commands_$i.sh
echo "find . -name \"*.hepmc.gz\" -type f -delete" >> Production_commands_$i.sh
echo "find . -name \"*.hepmc\" -type f -delete" >> Production_commands_$i.sh
echo "File=\$(find . -name \"*.root\" -type f)" >> Production_commands_$i.sh
echo "mv \$File ZZ_$i.root" >> Production_commands_$i.sh
done

for i in {1..6}; do
rm -r Scan_commands_$i.sh 2> /dev/null
touch Scan_commands_$i.sh 2> /dev/null
echo "!cp /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/Backgrounds/ZZ_$i/Cards/pythia8_card_default.dat /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/Backgrounds/ZZ_$i/Cards/pythia8_card.dat" >> Scan_commands_$i.sh
echo "!cp /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/Backgrounds/ZZ_$i/Cards/delphes_card_ATLAS.dat /home/jpedropino@UA.PT/Workstation/MadGraph/MG5_aMC_v2_7_0/Backgrounds/ZZ_$i/Cards/delphes_card.dat" >> Scan_commands_$i.sh
echo "launch Backgrounds/ZZ_$i" >> Scan_commands_$i.sh
echo "3" >> Scan_commands_$i.sh
echo "set nevents 100000" >> Scan_commands_$i.sh
echo "set ebeam1 6800" >> Scan_commands_$i.sh
echo "set ebeam2 6800" >> Scan_commands_$i.sh
echo "set iseed $RANDOM" >> Scan_commands_$i.sh
echo "exit" >> Scan_commands_$i.sh
done


for i in {1..6}; do
rm -r Submit_job_$i.sh 2> /dev/null
touch Submit_job_$i.sh 2> /dev/null
echo "#!/bin/bash" >> Submit_job_$i.sh
echo "#SBATCH -n 1" >> Submit_job_$i.sh
echo "#SBATCH --cpus-per-task=1" >> Submit_job_$i.sh
echo "#SBATCH --mem-per-cpu=10500mb" >> Submit_job_$i.sh
echo "#SBATCH --mail-type=ALL" >> Submit_job_$i.sh
echo "#SBATCH --mail-user=jpedropino@ua.pt" >> Submit_job_$i.sh
echo " " >> Submit_job_$i.sh
echo "cd /scratch_p/jpedropino/1-LQCollider-project/ZZ" >> Submit_job_$i.sh 
echo "chmod +x Folder_commands_$i.sh Production_commands_$i.sh Scan_commands_$i.sh" >> Submit_job_$i.sh 
echo "sbatch ./Production_commands_$i.sh 2> /dev/null" >> Submit_job_$i.sh 
done


for i in {1..6}; do
chmod +x Submit_job_$i.sh
./Submit_job_$i.sh
done

