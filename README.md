
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
cmsenv
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



### Sample locations

All the samples have been produced with 11_2_0_pre6 and GT 'auto:phase1_2021_realistic’ (i.e. 112X_mcRun3_2021_realistic_v7)

|                | location                                                      | events                            | config                            |
|----------------|:-------------------------------------------------------------:|:---------------------------------:|:---------------------------------:|
| dstar (pT>3.9) | /eos/cms/store/group/phys_tracking/bphstudies/miniaodstudies/dstar/         |              ~90k                 |   [DStarToD0Pi_D0KPi_pT3p9](https://github.com/AdrianoDee/miniaodstudies/blob/main/configs/DStarToD0Pi_D0KPi_DStarFilter_13TeV_GEN_SIM.py)   |
| dstar (pT>0.5) | /eos/cms/store/group/phys_tracking/bphstudies/miniaodstudies/dstar_lowpt/   |              ~50k                 |   [DStarToD0Pi_D0Kpi_pT0p5](https://github.com/AdrianoDee/miniaodstudies/blob/main/configs/DStarToD0Pi_D0KPi_DStarFilter_13TeV_LowPt_GEN_SIM.py)
| bsjpsiphi      | /eos/cms/store/group/phys_tracking/bphstudies/miniaodstudies/bsjpsiphi/     |              ~50k                 |             [BsToJpsiPhi](https://github.com/AdrianoDee/miniaodstudies/blob/main/configs/BsToJpsiPhi_GEN_SIM.py)           |
| qcd_muon       | /eos/cms/store/group/phys_tracking/bphstudies/miniaodstudies/qcd_muon/      |              ~60k                 |             [QCD](https://github.com/AdrianoDee/miniaodstudies/blob/main/configs/QCD_GEN_SIM.py)                      |
| bupsik         | /eos/cms/store/group/phys_tracking/bphstudies/miniaodstudies/bupsik/         |              ~30k                 |             [BuPsiK](https://github.com/AdrianoDee/miniaodstudies/blob/main/configs/BuToPsi2SK_Psi2SToJpsiPiPi_BMuonFilter_DGamma0_TuneCP5_13TeV_GEN_SIM.py)                     |
| xilambda       | /eos/cms/store/group/phys_tracking/bphstudies/miniaodstudies/xi/            |              ~50k                 |             [Xi](https://github.com/AdrianoDee/miniaodstudies/blob/main/configs/XiMinus_13TeV_GEN_SIM.py)                     |


## Checking the LUT

In order to check the LUT for the covariance you may merge https://github.com/AdrianoDee/cmssw/tree/miniaodbph branch in your CMSSW (11_2_X)

```
cmsrel CMSSW_11_2_0_pre6
cd CMSSW_11_2_0_pre6/src/
cmsenv
git cms-init
git cms-merge-topic adrianodee:miniaodbph
git cms-checkdeps -a 
scram b -j 8
```

or (in 11_3_X)

```
cmsrel CMSSW_11_3_0_pre2
cd CMSSW_11_3_0_pre2/src/
cmsenv
git cms-init
git cms-merge-topic adrianodee:miniaodbph-113
scram b -j 8
```

This would allow you to access the covariance matrix (for the `pseudoTrack` of the `PackedCandidate`) even when `hasTrackDetails()` is `false` and the track is attached to the candidate. In order to get the track reference in this setup check before the `covarianceVersion` to be `==1` (or simply `>0`) with the method `covarianceVersion()`from [here](https://github.com/AdrianoDee/cmssw/blob/miniaodbph/DataFormats/PatCandidates/interface/PackedCandidate.h#L672) and then get the `reco::Track` with the method `pseudoTrack()` from [here](https://github.com/AdrianoDee/cmssw/blob/miniaodbph/DataFormats/PatCandidates/interface/PackedCandidate.h#L773).


### Multiple conditions samples

Under `/eos/cms/store/group/phys_tracking/run3_miniaod/` you may find `BuToPsiK`, `PsiToJPsiPiPi` and `DStarToD0Pi` samples for multiple conditions

| Sample | Year | Scenario  | Path                                                            | Events |
|--------|------|-----------|-----------------------------------------------------------------|--------|
| bu     | 2021 | baseline  | /eos/cms/store/group/phys_tracking/run3_miniaod/bu/2021/        | 61k    |
|        |      | 2018_failC | /eos/cms/store/group/phys_tracking/run3_miniaod/bu/2021_failC/  | 61k    |
|        |      | 2018_failD | /eos/cms/store/group/phys_tracking/run3_miniaod/bu/2021_failD/  | 60k    |
|        |      | mis-align | /eos/cms/store/group/phys_tracking/run3_miniaod/bu/2021_align/  | 78k    |
|        | 2024 | baseline  | /eos/cms/store/group/phys_tracking/run3_miniaod/bu/2024/        | 57k    |
|        |      | 2018_failC | /eos/cms/store/group/phys_tracking/run3_miniaod/bu/2024_failC/  | 75k    |
|        |      | 2018_failD | /eos/cms/store/group/phys_tracking/run3_miniaod/bu/2024_failD/  | 54k    |
| psi    | 2021 | baseline  | /eos/cms/store/group/phys_tracking/run3_miniaod/psi/2021/       | 67k    |
|        |      | 2018_failC | /eos/cms/store/group/phys_tracking/run3_miniaod/psi/2021_failC/ | 50k    |
|        |      | 2018_failD | /eos/cms/store/group/phys_tracking/run3_miniaod/psi/2021_failD/ | 190k   |
|        |      | mis-align | /eos/cms/store/group/phys_tracking/run3_miniaod/psi/2021_align/ | 125k   |
|        | 2024 | baseline  | /eos/cms/store/group/phys_tracking/run3_miniaod/psi/2024/       | 110k   |
|        |      | 2018_failC | /eos/cms/store/group/phys_tracking/run3_miniaod/psi/2024_failC/ | 178k   |
|        |      | 2018_failD | /eos/cms/store/group/phys_tracking/run3_miniaod/psi/2024_failD/ | 87k    |
| ds     | 2021 | baseline  | /eos/cms/store/group/phys_tracking/run3_miniaod/ds_lowpt/2021/        | 180k    |
|        |      | 2018_failD | /eos/cms/store/group/phys_tracking/run3_miniaod/ds_lowpt/2021_failD/  | 115k   |
|        |      | mis-align | /eos/cms/store/group/phys_tracking/run3_miniaod/ds_lowpt/2021_align/  | 210k   |
|        | 2024 | baseline  | /eos/cms/store/group/phys_tracking/run3_miniaod/ds_lowpt/2024/        | 250k    |
|        |      | 2018_failD | /eos/cms/store/group/phys_tracking/run3_miniaod/ds_lowpt/2024_failD/  | 100k   |

#### Baseline 2021/2024 conditions

* __2021__ :  113X_mcRun3_2021_realistic_v2

* __2024__ : 113X_mcRun3_2024_realistic_v2

#### Failures & Mis-align

To apply the failures & mis-alignment scenarios use one (or both) the customizers in [customize_failures.py](https://github.com/AdrianoDee/miniaodstudies/blob/main/configs/customize_failures.py). To apply one of the pixel failures scenarios listed [here](https://twiki.cern.ch/twiki/bin/viewauth/CMS/SiPixelPhase1FailureScenarios#Failure_Scenario_studies_in_2018) use:

```
from customize_failures import *
customize_failures(process,S)
```

with `S=A,B,C,D,E,F,G or H`. In the samples listed above `S` is set to `C` and `D`

To use the misalignment simulation scenario use

```
from customize_failures import *
customize_alignment(process)
```
