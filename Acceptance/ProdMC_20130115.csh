#!/bin/sh -f
#############################################
#### bash shell script to make batch job ####
#### by Dongho Moon                      ####
#############################################
#### modified  by Hyunchul Kim           ####
#############################################

#### Set up the paramters

#nFile=500 ## total number of files
echo Now processing !!!!
echo $nFile

curdir=$(pwd)


# for BtoJ/Psi sample
##nFile=400 ## total number of files
##skelpyname=generator_skel_pythiagunbtoJpsi_GENRECO_regit_20121220
##outputdir=/castor/cern.ch/user/h/hckim/cms392/pythia6_BtoJpsitoMuMu_GEN_2.76TeV_bfiltered_totevt10M ### output directory, don't end with "/"
##outputdir=$(pwd)

##outname=pythiagunbtoJpsi_GENRECO_regit_evt500_v2_ ## end with _
##workpy=pythiagunbtoJpsi_GENRECO_regit_evt500_v2_ ## end with _
##job=pythiagunbtoJpsi_GENRECO_regit_evt500_v2_ ## end with _

# for prompt J/Psi sample
#nFile=1000 ## total number of files
#skelpyname = generator_skel_promptjpsi
#outputdir=/castor/cern.ch/user/h/hckim/cms392/pythia6_PromptJpsitoMuMu_GEN_2.76TeV_totevt10M ### output directory, don't end with "/"
#outname=pythia6_PromptJpsitoMuMu_GEN_2.76TeV_evt10k_ ## end with _
#workpy=pythia6_PromptJpsitoMuMu_GEN_2.76TeV_evt10k_ ## end with _
#job=pythia6_PromptJpsitoMuMu_GEN_2.76TeV_evt10k_ ## end with _

# for upsilons sample
nFile=2000 ## total number of files
skelpyname=test_ButoJpsiK_boosted_GEN
outputdir=$(pwd)

##skelpyname=test_Ups1S_unboosted_GEN

###jobname=pythia6_ButoJpsiK_boosted_default_evt10k_20130418_ ## end with _
##outname=pythiagunbtoJpsi_GENRECO_regit_evt500_v2_ ## end with _
##workpy=pythiagunbtoJpsi_GENRECO_regit_evt500_v2_ ## end with _
##job=pythiagunbtoJpsi_GENRECO_regit_evt500_v2_ ## end with _

##jobname=pythia6_Ups1S_unboosted_GEN_evt2k_20130115_ ## end with _

##jobname=pythia6_ButoJpsiK_boosted_GENre2_evt100k_20130916_ ## end with _
jobname=pythia6_ButoJpsiK_boosted_GENre2_withFilter_evt5k_20131113_ ## end with _


echo Making cfg and csh file

#### Making the input bunchs ####

i=1001

#while [ $i -le $nFile ]
while [ $i -le 1100 ]
do 
    awk -v p=$jobname$i.root -v p1=$i '{gsub("_output_file_",p); gsub("_N_",p1); print;}' $skelpyname.py > $jobname$i.py;
    awk -v p=$(pwd) -v p2=$jobname$i.py -v p3=$jobname$i.root -v p4=$outputdir '{gsub("_in_dir_",p); gsub("_input_py_",p2); gsub("_output_file_",p3); gsub("_out_dir_",p4); print;}' mjob_test.csh > $jobname$i.csh
    i=$(expr $i + 1);
done

#### Submitting ####

#i=1
i=1001
#while [ $i -le $nFile ]
while [ $i -le 1100 ]
do
    echo Job submitting $i
    bsub -R "pool>10000" -q 1nd -J $jobname$i < $jobname$i.csh
    #sleep 5
    i=$(expr $i + 1);
done

