
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

and then you will be able to run the MINIAOD step (such as the ones stored in `configs/` directory) and adding a line as


will allow you to tune the reduced precion covariance matrix pT threhsold. For a preliminary study the configuration that have been taken into account are

|          | minPtForTrackProperties | minPtForLowQualityTrackProperties |
|----------|:-----------------------:|:---------------------------------:|
| Original |         0.95 GeV        |              0.5 GeV              |
| v0       |         0.1 GeV         |              inf (*)              |
| v1       |         0.5 GeV         |              0.3 GeV              |
| v2       |         0.3 GeV         |              0.1 GeV              |

and you can find the results for `TTbar` (*in update...*) events with `<PU> = 40,45,50,55,60,65` in the notebook `Sizes`. Here some examples of the results.


#### Packed Candidates Collection Avg Size
![miniaod_candidates_avg_unc](https://raw.githubusercontent.com/AdrianoDee/warehouse/master/img/miniaod_candidates_avg_unc.png)

#### MiniAOD Relative (to orginal) File Size
![miniaod_file_rel](https://raw.githubusercontent.com/AdrianoDee/warehouse/master/img/miniaod_file_rel.png)

#### File Size per Event
![miniaod_file_evt](https://raw.githubusercontent.com/AdrianoDee/warehouse/master/img/miniaod_file_evt.png)


