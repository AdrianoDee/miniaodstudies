from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()

import datetime, time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')

sites = ['T2_AT_Vienna', 'T2_BE_IIHE', 'T2_BE_UCL', 'T2_BR_SPRACE', 'T2_BR_UERJ',
 'T2_CH_*',
 'T2_DE_DESY', 'T2_DE_RWTH',
 'T2_EE_Estonia', 'T2_ES_CIEMAT', 'T2_ES_IFCA', 'T2_FI_HIP', 'T2_FR_CCIN2P3',
 'T2_FR_GRIF_IRFU', 'T2_FR_GRIF_LLR', 'T2_FR_IPHC', 'T2_GR_Ioannina', 'T2_HU_Budapest',
 'T2_IN_TIFR', 'T2_IT_Bari', 'T2_IT_Legnaro', 'T2_IT_Pisa', 'T2_IT_Rome', 'T2_KR_KISTI',
 'T2_PK_NCP', 'T2_PL_Swierk', 'T2_PL_Warsaw',
 'T2_PT_NCG_Lisbon', 'T2_RU_*',
 'T2_TR_METU', 'T2_TW_NCHC', 'T2_UA_KIPT', 'T2_UK_London_Brunel',
 'T2_UK_London_IC', 'T2_UK_SGrid_Bristol','T2_UK_SGrid_RALPP', 'T2_US_Caltech', 'T2_US_Florida',
 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Vanderbilt',
 'T2_US_Wisconsin',

 'T3_CH_PSI', 'T3_CN_PKU',
 'T3_ES_Oviedo', 'T3_GR_IASA', 'T3_HU_Debrecen',
 'T3_IN_PUHEP', 'T3_IN_TIFRCloud','T3_IT_*', 'T3_KR_*', 'T3_MX_*', 'T3_RU_*',
 #'T3_TW*', #Taiwan gives some troubles with file fetching
 'T3_UK_*', 'T3_US_Baylor','T3_US_Colorado',
 'T3_US_FIT', 'T3_US_FIU', 'T3_US_FNALLPC', 'T3_US_J*',
 'T3_US_Kansas', 'T3_US_MIT', 'T3_US_N*', 'T3_US_O*', 'T3_US_P*',
 'T3_US_R*', 'T3_US_S*', 'T3_US_T*', 'T3_US_UCD', 'T3_US_UCR',
 'T3_US_UMD']


NJOBS = 500
EVTPERJOB = 480

nEvents = NJOBS*EVTPERJOB
genname = 'bu'
y=2024

job_label = genname + "_PUFlat55To75_" + str(y)
myrun= genname + ".py"
myname=job_label

step1File = "step1.root"
step2File = "step2.root"
step3File = "step3_inAODSIM.root"
step3DQM  = "step3_inDQM.root"

#mini0 = "miniaod_0.root"
#mini1 = "miniaod_1.root"
#mini2 = "miniaod_2.root"
mini3 = "miniaod_3.root"
mini4 = "miniaod_4.root"
#mini5 = "miniaod_5.root"
miniO = "miniaod_original.root"

m4 = "miniaod_4_" + str(y) + ".py"
mo = "miniaod_original_" + str(y) + ".py"
m3 = "miniaod_3_" + str(y) + ".py"

s2 = "step2_" + str(y) + ".py"
s3 = "step3_" + str(y) + ".py" 
config.General.requestName = job_label+'_'+st
config.General.transferOutputs = True
config.General.transferLogs = False
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = myrun
config.JobType.inputFiles = [myrun,m4,mo,s2,s3,m3]

#,'release.tar','step3.py','miniaod_0.py','miniaod_1.py','miniaod_original.py','miniaod_2.py','miniaod_3.py','miniaod_4.py','miniaod_5.py']

config.JobType.disableAutomaticOutputCollection = True
config.JobType.eventsPerLumi = 1000
config.JobType.numCores = 4
config.JobType.maxMemoryMB      = 9000
config.JobType.maxJobRuntimeMin = 200 #int(float(EVTPERJOB)*2.5)
config.JobType.allowUndistributedCMSSW = True
config.JobType.scriptExe = 'production.sh'#'GEN-MiniAOD-Xb2chib1pipi_10p5.sh'
#config.JobType.scriptArgs = ['=Xb2chib1pipi','=10p5','=100000']
config.JobType.outputFiles = [step3DQM,step3File,mini4,miniO,mini3]#,mini0,mini1,mini2,miniO,mini3,mini4,mini5]

config.Data.outputPrimaryDataset = myname
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = EVTPERJOB#nEvents # the number of events here must match the number of events in the externalLHEProducer

config.Data.totalUnits = nEvents
config.Data.outLFNDirBase = '/store/user/adiflori/run3_miniaods/'# % (getUsernameFromSiteDB())
#config.Data.outputDatasetTag = 'RunIISummer17PrePremix-MC_v2_94X_mc2017_realistic_v11'+step
#config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publication = False
#config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'

config.Site.storageSite = 'T2_IT_Bari'
config.Site.blacklist = ["T2_BR_*","T2_IN_*","T2_CN_*"]#,"T2_US_*","T3_US_*"]
#config.Site.whitelist = sites #['T2_IT_*','T2_CH_*','T2_GE_*','T2_FR_*','T2_ES_*','T2_UK_*']
