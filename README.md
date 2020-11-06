
# MiniAOD Studies
Repository for MiniAOD Studies for CMS BPAG.

## Track Details & Covariance Matrix 

A first approach to understand if miniAOD may be used for *"all"* BPAG analysis would be to act on the [PFPackedCandidateProducer](https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/PatAlgos/plugins/PATPackedCandidateProducer.cc) lowering the pT thresholds:

- `minPtForTrackProperties` that selects the minimum threhsold so that a track is stored (i.e. with its covariance matrix) with full precision ([here](https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/PatAlgos/plugins/PATPackedCandidateProducer.cc#L133)) and set by default to 0.95 ([here](https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/PatAlgos/python/slimming/packedPFCandidates_cfi.py#L19))
- the minimun for a track to be stored with a reduced precision covariance matrix, hard coded to be 0.5 ([here](https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/PatAlgos/plugins/PATPackedCandidateProducer.cc#L308))

In order to make also the latter configurable at run time a new variable `minPtForLowQualityTrackProperties` is defined in `PATPackedCandidateProducer` to select a threshold different from 0.5 GeV. All the (few) changes are stored in a branch of CMSSW_11_2_X: [miniaodsizes](https://github.com/AdrianoDee/cmssw/tree/miniaodsizes).

To be able to run with it merge the topic in your local repo

```
cmsrel CMSSW_11_2_0_pre6
cd CMSSW_11_2_0_pre6/src/
git cms-init
git cms-merge-topic adrianodee:miniaodsizes
scram b -j 8
```

and then you will be able to run the MINIAOD step (such as the ones stored in `configs/` directory) and adding a couple of lines as

```
process.packedPFCandidates.minPtForTrackProperties = x
process.packedPFCandidates.minPtForLowQualityTrackProperties = cms.double(0.1)
```

will allow you to tune the reduced precion covariance matrix pT threhsold. For a preliminary study the configuration that have been taken into account are

|          | minPtForTrackProperties | minPtForLowQualityTrackProperties |
|----------|:-----------------------:|:---------------------------------:|
| Original |         0.95 GeV        |              0.50 GeV             |
| v0       |         0.10 GeV        |              inf (*)              |
| v1       |         0.50 GeV        |              0.10 GeV             |
| v2       |         0.30 GeV        |              0.10 GeV             |
| v3       |         0.95 GeV        |              0.00 GeV             |
| v4       |         0.00 GeV        |              inf (*)              |
| v5       |         0.50 GeV        |              0.25 GeV             |

###### (*)in this case this threshold doesn't have any effect

and you can find the results for `TTbar` (*in update...*) events with `<PU> = 40,45,50,55,60,65` in the notebook `Sizes`. Here some examples of the results.


#### Packed Candidates Collection Avg Size
![miniaod_candidates_avg_unc](https://raw.githubusercontent.com/AdrianoDee/warehouse/master/img/miniaod_candidates_avg_unc.png)

#### MiniAOD Relative (to orginal) File Size
![miniaod_file_rel](https://raw.githubusercontent.com/AdrianoDee/warehouse/master/img/miniaod_file_rel.png)

#### File Size per Event
![miniaod_file_evt](https://raw.githubusercontent.com/AdrianoDee/warehouse/master/img/miniaod_file_evt.png)


### Sample locations

All the samples have been produced with 11_2_0_pre6 and GT 'auto:phase1_2021_realistic’ (i.e. 112X_mcRun3_2021_realistic_v7)

|                | location                                                      | events                            | config                            |
|----------------|:-------------------------------------------------------------:|:---------------------------------:|:---------------------------------:|
| dstar (pT>3.9) | /eos/cms/store/group/phys_bphys/miniaodstudies/dstar/         |              ~90k                 |   [DStarToD0Pi_D0KPi_pT3p9](https://github.com/AdrianoDee/miniaodstudies/blob/main/configs/DStarToD0Pi_D0KPi_DStarFilter_13TeV_GEN_SIM.py)   |
| dstar (pT>0.5) | /eos/cms/store/group/phys_bphys/miniaodstudies/dstar_liowpt/  |              ~50k                 |   [DStarToD0Pi_D0Kpi_pT0p5](https://github.com/AdrianoDee/miniaodstudies/blob/main/configs/DStarToD0Pi_D0KPi_DStarFilter_13TeV_LowPt_GEN_SIM.py)
| bsjpsiphi      | /eos/cms/store/group/phys_bphys/miniaodstudies/bsjpsiphi/     |              ~50k                 |             [BsToJpsiPhi](https://github.com/AdrianoDee/miniaodstudies/blob/main/configs/BsToJpsiPhi_GEN_SIM.py)           |
| qcd_muon       | /eos/cms/store/group/phys_bphys/miniaodstudies/qcd_muon/      |              ~60k                 |             [QCD](https://github.com/AdrianoDee/miniaodstudies/blob/main/configs/QCD_GEN_SIM.py)                      |
| --             |                                                               |                                   |                                   |


