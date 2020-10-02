
JOB_NAME='new_miniaod'    # "${2#*=}"

ConfigReleaseReco=CMSSW_11_2_0_pre6

echo "=================  Starting cmssw environment prepration ====================" >> job.log

#cat /proc/cpuinfo

export SCRAM_ARCH=slc7_amd64_gcc820
export VO_CMS_SW_DIR=/cvmfs/cms.cern.sh
source $VO_CMS_SW_DIR/cmsset_default.sh


tar -xvf release.tar

cd ${ConfigReleaseReco}/src
scramv1 b ProjectRename
scram b 
eval `scram runtime -sh`
cd ../../


echo "================= PB: Input Paramateres ========================================">> job.log
#echo $JOB_NAME
#echo $NEVENTS
#echo $NCORES

echo "================= PB: CMSRUN starting Step 1 ====================" >> job.log

cmsRun -j ${JOB_NAME}_step1.log -p PSet.py
#cmsRun -j step1.log -p step1.py

echo "================= PB: CMSRUN starting Step 2 ====================" >> job.log

cmsRun -j ${JOB_NAME}_step2.log -p step2.py

echo "================= PB: CMSRUN starting Step 2 ====================" >> job.log

cmsRun -j ${JOB_NAME}_step3.log -p step3.py

echo "================= PB: CMSRUN starting MiniAODs  ====================" >> job.log

cmsRun -j ${JOB_NAME}_mini0.log -p miniaod_0.py
cmsRun -j ${JOB_NAME}_mini1.log -p miniaod_1.py
cmsRun -j ${JOB_NAME}_mini1.log -p miniaod_2.py
cmsRun -e -j FrameworkJobReport.xml -p miniaod_original.py

echo "================= PB: End ====================" >> job.log

echo $CMSSW_BASE

echo "done"








