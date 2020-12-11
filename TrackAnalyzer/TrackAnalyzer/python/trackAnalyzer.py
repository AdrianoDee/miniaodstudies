import FWCore.ParameterSet.Config as cms
process = cms.Process('2mu2k')

from FWCore.ParameterSet.VarParsing import VarParsing

import sys
sys.path.append("mclists/")

par = VarParsing ('analysis')

par.register ('data',
                                  "debug",
                                  VarParsing.multiplicity.singleton,
                                  VarParsing.varType.string,
                                  "Dataset")

par.register ('v',
                                  3,
                                  VarParsing.multiplicity.singleton,
                                  VarParsing.varType.int,
                                  "MiniAOD version")

par.register ('T',
                                  4,
                                  VarParsing.multiplicity.singleton,
                                  VarParsing.varType.int,
                                  "Threads & Streams")

par.register ('e',
                                  -1,
                                  VarParsing.multiplicity.singleton,
                                  VarParsing.varType.int,
                                  "Max Events")

par.parseArguments()

from mc_files import *

here = ["file:miniaod_0_1.root","file:./miniaod_1_1.root","file:./miniaod_2_1.root","file:./miniaod_original_1.root"]
fileLists = {"here": here, "debug" :  super_dummy, "dstar": fast_list, "bsjpsiphi" : bsjpsiphi,
             "dstar_official": dstar_official, "new_bu":new_bu, "ttbar" : ttbar}

files = fileLists[par.data]

v=par.data

if par.v == -1:
    files = [f for f in files if "original" in f]
for i in range(6):
    if par.v == i:
        files = [f for f in files if "_"+str(i)+"_" in f or "miniaod_"+str(i)+".root" in f]
        v = i

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
# process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
# process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '112X_mcRun3_2021_realistic_v7', '')

if "bs" in par.data:
    process.GlobalTag = GlobalTag(process.GlobalTag, '100X_upgrade2018_realistic_v10', '')
if "dstar_official" in par.data:
    process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun3_2023_realistic_v3', '')

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True))

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(files),
    #eventsToProcess = cms.untracked.VEventRange(eventsToProcess),
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(par.e))

process.TFileService = cms.Service("TFileService",
        fileName = cms.string('track_analyzer'+ par.data  + '_' + str(v) +'.root'),
)


process.TrackAnalyzer = cms.EDAnalyzer('TrackAnayzerMiniAOD',
    PFCandidates     = cms.InputTag('packedPFCandidates'),
    PrimaryVertex    = cms.InputTag("offlineSlimmedPrimaryVertices"),
    TreeName         = cms.string('Tracks')
)

# End of customisation functions
process.options.numberOfThreads=cms.untracked.uint32(par.T)
process.options.numberOfStreams=cms.untracked.uint32(par.T)

process.p = cms.Path(process.TrackAnalyzer)
process.schedule = cms.Schedule([process.p])
