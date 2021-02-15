from CondCore.CondDB.CondDB_cfi import *

def customize_alignment(process):
        
        process.load("CondCore.DBCommon.CondDBCommon_cfi")
        process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
        
        import CalibTracker.Configuration.Common.PoolDBESSource_cfi

        process.GlobalTag.toGet = cms.VPSet(
                                                                cms.PSet(record = cms.string("TrackerAlignmentRcd"),
                                                                                 tag = cms.string("TrackerAlignment_Phase1Realignment_CRUZET_1M_CRAFT_1M_v1"),
                                                                                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),),

                                                                cms.PSet(record = cms.string("TrackerAlignmentErrorExtendedRcd"),
                                                                                 tag = cms.string("TrackerAlignmentExtendedErrors_BPIX50_FPIX50_TIB20_TOB20_TID40_TEC40"),
                                                                                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),),
                                           )

def customize_failures(process,scen="d"):

        S = "SiPixelQuality_Phase1FailureScenario_2018" + scen

        process.SiPixelQualityDBReader = cms.ESSource("PoolDBESSource",
                        BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
                        DBParameters = cms.PSet(
                                messageLevel = cms.untracked.int32(0),
                                authenticationPath = cms.untracked.string('')),

                        connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                        toGet = cms.VPSet(
                                        cms.PSet(record = cms.string('SiPixelQualityFromDbRcd'),
                                                tag = cms.string(S),))
                                        )

        process.es_prefer_Quality = cms.ESPrefer("PoolDBESSource","SiPixelQualityDBReader")

