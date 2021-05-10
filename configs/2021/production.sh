
JOB_NAME='new_miniaod'    # "${2#*=}"

#ConfigReleaseReco=CMSSW_11_2_0

echo "================= PB: CMSRUN starting Step 1 ====================" >> job.log

cmsRun -j ${JOB_NAME}_step1.log -p PSet.py
#cmsRun -j step1.log -p step1.py

echo "================= PB: CMSRUN starting Step 2 ====================" >> job.log

cmsRun -j ${JOB_NAME}_step2.log -p step2_2021.py

echo "================= PB: CMSRUN starting Step 2 ====================" >> job.log

cmsRun -j ${JOB_NAME}_step3.log -p step3_2021.py

echo "================= PB: CMSRUN starting MiniAODs  ====================" >> job.log

cmsRun -j ${JOB_NAME}_mini0.log -p miniaod_3_2021.py
cmsRun -j ${JOB_NAME}_mini1.log -p miniaod_4_2021.py
#cmsRun -j ${JOB_NAME}_mini1.log -p miniaod_2.py
cmsRun -e -j FrameworkJobReport.xml -p miniaod_original_2021.py

echo "================= PB: End ====================" >> job.log


