# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --conditions auto:phase1_2021_realistic --pileup_input das:/RelValMinBias_13/CMSSW_10_6_0_pre3-105X_postLS2_realistic_v6-v1/GEN-SIM -n 10 --era Run3 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2018,RAW2DIGI:RawToDigi_pixelOnly,RECO:reconstruction_pixelTrackingOnly,VALIDATION:@pixelTrackingOnlyValidation --datatier GEN-SIM-DIGI-RAW-RECO-HLTDEBUG --procModifiers gpu --geometry DB:Extended --pileup Run3_Flat55To75_PoissonOOTPU --filein file:step1.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.ProcessModifiers.gpu_cff import *
from Configuration.ProcessModifiers.pixelNtupleFit_cff import *
from FWCore.ParameterSet.VarParsing import VarParsing

def customizePixelTracksSoAonCPU(process) :

  process.load('RecoLocalTracker/SiPixelRecHits/siPixelRecHitHostSoA_cfi')
  process.load('RecoPixelVertexing.PixelTriplets.caHitNtupletCUDA_cfi')
  process.load('RecoPixelVertexing.PixelVertexFinding.pixelVertexCUDA_cfi')

  process.pixelTrackSoA = process.caHitNtupletCUDA.clone()
  process.pixelTrackSoA.onGPU = False
  process.pixelTrackSoA.pixelRecHitSrc = 'siPixelRecHitHostSoA'
  process.pixelVertexSoA = process.pixelVertexCUDA.clone()
  process.pixelVertexSoA.onGPU = False
  process.pixelVertexSoA.pixelTrackSrc = 'pixelTrackSoA'

  process.load('RecoPixelVertexing.PixelTrackFitting.pixelTrackProducerFromSoA_cfi')
  process.pixelTracks = process.pixelTrackProducerFromSoA.clone()
  process.load('RecoPixelVertexing.PixelVertexFinding.pixelVertexFromSoA_cfi')
  process.pixelVertices = process.pixelVertexFromSoA.clone()
  process.pixelTracks.pixelRecHitLegacySrc = 'siPixelRecHitHostSoA'
  process.siPixelRecHitHostSoA.convertToLegacy = True

  process.reconstruction_step += process.siPixelRecHitHostSoA+process.pixelTrackSoA+process.pixelVertexSoA

  return process


process = cms.Process('HLTPatatrack',Run3,pixelNtupleFit)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('HeterogeneousCore.CUDAServices.CUDAService_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_Run3_Flat55To75_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring("file:step2.root"),
    secondaryFileNames = cms.untracked.vstring()
)


process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-RECO-HLTDEBUG'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_hlt_patatrack.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition
#process.FEVTDEBUGHLTEventContent.outputCommands.append("drop *_*_*_HLTPatatrack")
#process.FEVTDEBUGHLTEventContent.outputCommands.append("keep *_*pixelTracks*_*_HLTPatatrack")
# Other statements
#process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/38806EE1-709B-404D-8744-485FFFEBCE77.root', '/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/6CF4F679-7EA3-0F42-841E-66DD4DD05943.root', '/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/037E40A0-0D58-BB43-B32D-34BA65435B27.root', '/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/644621DF-62ED-E34F-A25A-F9871DC2612C.root', '/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/41F88CCA-3E51-5441-B284-DF542FCEB6E5.root', '/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/3EC307BB-54BA-2443-90EA-FD926B91FA9A.root'])
#process.mix.input.fileNames = cms.untracked.vstring(['file:/home/adrianodif/b_trigger/minbias_run3/037E40A0-0D58-BB43-B32D-34BA65435B27.root',
#'file:/home/adrianodif/b_trigger/minbias_run3/38806EE1-709B-404D-8744-485FFFEBCE77.root',
#'file:/home/adrianodif/b_trigger/minbias_run3/3EC307BB-54BA-2443-90EA-FD926B91FA9A.root',
#'file:/home/adrianodif/b_trigger/minbias_run3/41F88CCA-3E51-5441-B284-DF542FCEB6E5.root',
#'file:/home/adrianodif/b_trigger/minbias_run3/644621DF-62ED-E34F-A25A-F9871DC2612C.root',
#'file:/home/adrianodif/b_trigger/minbias_run3/6CF4F679-7EA3-0F42-841E-66DD4DD05943.root'])

process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/38806EE1-709B-404D-8744-485FFFEBCE77.root', '/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/6CF4F679-7EA3-0F42-841E-66DD4DD05943.root', '/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/037E40A0-0D58-BB43-B32D-34BA65435B27.root', '/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/644621DF-62ED-E34F-A25A-F9871DC2612C.root', '/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/41F88CCA-3E51-5441-B284-DF542FCEB6E5.root', '/store/relval/CMSSW_10_6_0_pre3/RelValMinBias_13/GEN-SIM/105X_postLS2_realistic_v6-v1/10000/3EC307BB-54BA-2443-90EA-FD926B91FA9A.root'])

process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi_pixelOnly)
process.reconstruction_step = cms.Path(process.reconstruction_pixelTrackingOnly)
process.prevalidation_step = cms.Path(process.globalPrevalidationPixelTrackingOnly)
process.validation_step = cms.EndPath(process.globalValidationPixelTrackingOnly)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.reconstruction_step,process.prevalidation_step,process.validation_step,process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

process.MessageLogger.cerr.FwkReport.reportEvery = 5

process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(4)

# customisation of the process.
process = customizePixelTracksSoAonCPU(process)
# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
