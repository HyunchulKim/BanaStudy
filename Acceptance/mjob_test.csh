#!/bin/csh
cd _in_dir_
#cms
eval `scramv1 runtime -csh`
cd -
cmsRun _in_dir_/_input_py_
#rfcp _output_file_ _out_dir_/_output_file_
#mv _output_file_ _in_dir_
##cmsStage _output_file_ /store/user/hckim/MCsample_pythia6Upsilons_538HI/pythia6_Ups1S_boosted_totevt1M_20130115/_output_file_
##cmsStage _output_file_ /store/user/hckim/MCsample_pythia6Charms_538HI/pythia6_Psi2S_boosted_5023GeV_default_totevt5M_20130210/_output_file_
########cmsStage _output_file_ /store/user/hckim/MCsample_pythia6Charms_538HI/pythia6_PromptJpsi_boosted_5023GeV_default_totevt5M_20130210/_output_file_
##rm -rf _in_dir_/_output_file_
cp _output_file_ _in_dir_/
#scp _output_file_ hckim@lxplus435.cern.ch:/tmp/hckim/
#rm -rf _in_dir_/_output_file_
