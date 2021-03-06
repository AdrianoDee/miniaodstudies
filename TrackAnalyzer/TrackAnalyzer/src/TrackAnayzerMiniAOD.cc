/*
   Package:    TrackAnayzerMiniAOD
   Class:      TrackAnayzerMiniAOD

   Description: make rootuple of DiMuon-DiTrack combination

   Original Author: Adriano Di Florio

*/

// Gen Particles
// 0 : an empty entry with no meaningful information and therefore to be skipped unconditionally
// 1 : a final-state particle, i.e. a particle that is not decayed further by the generator
// 2 : decayed Standard Model hadron or tau or mu lepton, excepting virtual intermediate states thereof (i.e. the particle must undergo a normal decay, not e.g. a shower branching).
// 3 : a documentation entry
// 4 : an incoming beam particle
// 5-10 : undefined, reserved for future standards
// 11-200: an intermediate (decayed/branched/...) particle that does not fulfill the criteria of status code 2, with a generator-dependent classification of its nature.
// 201- : at the disposal of the user, in particular for event tracking in the detector

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include "TLorentzVector.h"
#include "TTree.h"
#include <vector>
#include <sstream>


//
// class declaration
//

class TrackAnayzerMiniAOD : public edm::EDAnalyzer {
   public:
      explicit TrackAnayzerMiniAOD(const edm::ParameterSet&);
      ~TrackAnayzerMiniAOD() override;

      bool isAncestor(const reco::Candidate* ancestor, const reco::Candidate * particle);
      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      void beginJob() override ;
      void analyze(const edm::Event&, const edm::EventSetup&) override;
      void endJob() override ;

      void beginRun(edm::Run const&, edm::EventSetup const&) override;
      void endRun(edm::Run const&, edm::EventSetup const&) override;
      void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

  // ----------member data ---------------------------
  edm::EDGetTokenT<edm::View<pat::PackedCandidate>> TrackCollection_;
  edm::EDGetTokenT<reco::VertexCollection> thePVs_;

  std::string TreeName_;

  UInt_t run, event, lumi, numPrimaryVertices, numTracks;

  TLorentzVector track_p4;

  UInt_t lowMuon_NPixelHits, lowMuon_NStripHits, lowMuon_NTrackhits, lowMuon_NBPixHits;
  UInt_t lowMuon_NPixLayers, lowMuon_NTraLayers, lowMuon_NStrLayers, lowMuon_NBPixLayers;

  Int_t theTrack_NPixelHits, theTrack_NStripHits, theTrack_NTrackhits, theTrack_NBPixHits, theTrack_NPixLayers;
  Int_t theTrack_NTraLayers, theTrack_NStrLayers, theTrack_NBPixLayers, lowTrack_NPixelHits, lowTrack_NStripHits;
  Double_t theTrackFromPVBS, theTrackFromPVDZ;
  Double_t theTrack_pt, theTrack_eta, theTrack_phi, theTrack_charge, theTrack_dz, theTrack_dxy;

  Double_t theTrack_ptErr, theTrack_etaErr, theTrack_phiErr;

  Int_t theTrack_nChi2, theTrack_covVersion, theTrack_covSchema;

  Double_t theTrack_cov_0_0, theTrack_cov_0_1, theTrack_cov_0_2, theTrack_cov_0_3, theTrack_cov_0_4, theTrack_cov_1_0;
  Double_t theTrack_cov_1_1, theTrack_cov_1_2, theTrack_cov_1_3, theTrack_cov_1_4, theTrack_cov_2_0, theTrack_cov_2_1;
  Double_t theTrack_cov_2_2, theTrack_cov_2_3, theTrack_cov_2_4, theTrack_cov_3_0, theTrack_cov_3_1, theTrack_cov_3_2;
  Double_t theTrack_cov_3_3, theTrack_cov_3_4, theTrack_cov_4_0, theTrack_cov_4_1, theTrack_cov_4_2, theTrack_cov_4_3, theTrack_cov_4_4;

  TTree* track_tree;

};


//
// constructors and destructor
//
TrackAnayzerMiniAOD::TrackAnayzerMiniAOD(const edm::ParameterSet& iConfig):
        TrackCollection_(consumes<edm::View<pat::PackedCandidate>>(iConfig.getParameter<edm::InputTag>("PFCandidates"))),
        thePVs_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("PrimaryVertex"))),
        TreeName_(iConfig.getParameter<std::string>("TreeName"))
{
	      edm::Service<TFileService> fs;
        track_tree = fs->make<TTree>(TreeName_.data(),"Tree of DiMuon and Four Tracks");

        track_tree->Branch("run",                &run,                "run/I");
        track_tree->Branch("event",              &event,              "event/I");
        track_tree->Branch("lumi",              &lumi,              "lumi/I");
        track_tree->Branch("numPrimaryVertices", &numPrimaryVertices, "numPrimaryVertices/I");
        track_tree->Branch("numTracks",                &numTracks,                "numTracks/I");

        track_tree->Branch("track_p4",   "TLorentzVector", &track_p4);

        track_tree->Branch("theTrack_pt",         &theTrack_pt,         "theTrack_pt/D");
        track_tree->Branch("theTrack_eta",        &theTrack_eta,        "theTrack_eta/D");
        track_tree->Branch("theTrack_phi",        &theTrack_phi,        "theTrack_phi/D");
        track_tree->Branch("theTrack_charge",     &theTrack_charge,     "theTrack_charge/D");
        track_tree->Branch("theTrack_dz",         &theTrack_dz,         "theTrack_dz/D");
        track_tree->Branch("theTrack_dxy",        &theTrack_dxy,        "theTrack_dxy/D");

        track_tree->Branch("theTrack_ptErr",        &theTrack_ptErr,        "theTrack_ptErr/D");
        track_tree->Branch("theTrack_etaErr",        &theTrack_etaErr,        "theTrack_etaErr/D");
        track_tree->Branch("theTrack_phiErr",        &theTrack_phiErr,        "theTrack_phiErr/D");

        // track_tree->Branch("theTrackFromPV",       &theTrackFromPV,        "theTrackFromPV/D");
        // track_tree->Branch("theTrackFromPVCA",     &theTrackFromPVCA,        "theTrackFromPVCA/D");
        // track_tree->Branch("theTrackFromPVDZ",     &theTrackFromPVDZ,        "theTrackFromPVDZ/D");

        track_tree->Branch("theTrack_nChi2",        &theTrack_nChi2,        "theTrack_nChi2/I");
        track_tree->Branch("theTrack_covVersion",        &theTrack_covVersion,        "theTrack_covVersion/I");
        track_tree->Branch("theTrack_covSchema",        &theTrack_covSchema,        "theTrack_covSchema/I");

        track_tree->Branch("theTrack_cov_0_0",        &theTrack_cov_0_0,        "theTrack_cov_0_0/D");
        track_tree->Branch("theTrack_cov_0_1",        &theTrack_cov_0_1,        "theTrack_cov_0_1/D");
        track_tree->Branch("theTrack_cov_0_2",        &theTrack_cov_0_2,        "theTrack_cov_0_2/D");
        track_tree->Branch("theTrack_cov_0_3",        &theTrack_cov_0_3,        "theTrack_cov_0_3/D");
        track_tree->Branch("theTrack_cov_0_4",        &theTrack_cov_0_4,        "theTrack_cov_0_4/D");

        track_tree->Branch("theTrack_cov_1_0",        &theTrack_cov_1_0,        "theTrack_cov_1_0/D");
        track_tree->Branch("theTrack_cov_1_1",        &theTrack_cov_1_1,        "theTrack_cov_1_1/D");
        track_tree->Branch("theTrack_cov_1_2",        &theTrack_cov_1_2,        "theTrack_cov_1_2/D");
        track_tree->Branch("theTrack_cov_1_3",        &theTrack_cov_1_3,        "theTrack_cov_1_3/D");
        track_tree->Branch("theTrack_cov_1_4",        &theTrack_cov_1_4,        "theTrack_cov_1_4/D");

        track_tree->Branch("theTrack_cov_2_0",        &theTrack_cov_2_0,        "theTrack_cov_2_0/D");
        track_tree->Branch("theTrack_cov_2_1",        &theTrack_cov_2_1,        "theTrack_cov_2_1/D");
        track_tree->Branch("theTrack_cov_2_2",        &theTrack_cov_2_2,        "theTrack_cov_2_2/D");
        track_tree->Branch("theTrack_cov_2_3",        &theTrack_cov_2_3,        "theTrack_cov_2_3/D");
        track_tree->Branch("theTrack_cov_2_4",        &theTrack_cov_2_4,        "theTrack_cov_2_4/D");

        track_tree->Branch("theTrack_cov_3_0",        &theTrack_cov_3_0,        "theTrack_cov_3_0/D");
        track_tree->Branch("theTrack_cov_3_1",        &theTrack_cov_3_1,        "theTrack_cov_3_1/D");
        track_tree->Branch("theTrack_cov_3_2",        &theTrack_cov_3_2,        "theTrack_cov_3_2/D");
        track_tree->Branch("theTrack_cov_3_3",        &theTrack_cov_3_3,        "theTrack_cov_3_3/D");
        track_tree->Branch("theTrack_cov_3_4",        &theTrack_cov_3_4,        "theTrack_cov_3_4/D");

        track_tree->Branch("theTrack_cov_4_0",        &theTrack_cov_4_0,        "theTrack_cov_4_0/D");
        track_tree->Branch("theTrack_cov_4_1",        &theTrack_cov_4_1,        "theTrack_cov_4_1/D");
        track_tree->Branch("theTrack_cov_4_2",        &theTrack_cov_4_2,        "theTrack_cov_4_2/D");
        track_tree->Branch("theTrack_cov_4_3",        &theTrack_cov_4_3,        "theTrack_cov_4_3/D");
        track_tree->Branch("theTrack_cov_4_4",        &theTrack_cov_4_4,        "theTrack_cov_4_4/D");

        //Tracks Flags

        track_tree->Branch("theTrack_NPixelHits",        &theTrack_NPixelHits,        "theTrack_NPixelHits/I");
        track_tree->Branch("theTrack_NStripHits",        &theTrack_NStripHits,        "theTrack_NStripHits/I");
        track_tree->Branch("theTrack_NTrackhits",        &theTrack_NTrackhits,        "theTrack_NTrackhits/I");
        track_tree->Branch("theTrack_NBPixHits",         &theTrack_NBPixHits,        "theTrack_NBPixHits/I");

        track_tree->Branch("theTrack_NPixLayers",        &theTrack_NPixLayers,        "theTrack_NPixLayers/I");
        track_tree->Branch("theTrack_NTraLayers",        &theTrack_NTraLayers,        "theTrack_NTraLayers/I");
        track_tree->Branch("theTrack_NStrLayers",        &theTrack_NStrLayers,        "theTrack_NStrLayers/I");
        track_tree->Branch("theTrack_NBPixLayers",       &theTrack_NBPixLayers,        "theTrack_NBPixLayers/I");


}

TrackAnayzerMiniAOD::~TrackAnayzerMiniAOD() {}

//
// member functions
//

bool TrackAnayzerMiniAOD::isAncestor(const reco::Candidate* ancestor, const reco::Candidate * particle) {
   if (ancestor == particle ) return true;
   for (size_t i=0; i< particle->numberOfMothers(); i++) {
      if (isAncestor(ancestor, particle->mother(i))) return true;
   }
   return false;
}


// ------------ method called for each event  ------------
void TrackAnayzerMiniAOD::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
//  using namespace edm;
  using namespace std;

  edm::Handle<edm::View<pat::PackedCandidate> > track;
  iEvent.getByToken(TrackCollection_,track);

  edm::Handle<std::vector<reco::Vertex >> primaryVertices_handle;
  iEvent.getByToken(thePVs_, primaryVertices_handle);

  numPrimaryVertices = primaryVertices_handle->size();
  run   = iEvent.id().run();
  event = iEvent.id().event();
  lumi  = iEvent.id().luminosityBlock();

  track_p4.SetPtEtaPhiM(0.,0.,0.,0.);

//std::cout << "Debug  1" << std::endl;

  if (!track.isValid()) std::cout<< "No tracks information " << run << "," << event <<std::endl;

  if (track.isValid()) {


    //std::cout << "Debug  2" << std::endl;
    numTracks = (UInt_t)(track->size());

    for (unsigned int i=0; i< track->size(); i++)
    {

      // std::cout << "Event: " << run << " - "
      //                         << event << " - "
      //                         << lumi << " - "
      //           << "N Tracks: " << numTracks << std::endl;

      pat::PackedCandidate cand = track->at(i);


      //
      theTrack_NPixelHits  = -1;
      theTrack_NStripHits  = -1;
      theTrack_NTrackhits  = -1;
      theTrack_NBPixHits   = -1;
      theTrack_NPixLayers  = -1;
      theTrack_NTraLayers  = -1;
      theTrack_NStrLayers  = -1;
      theTrack_NBPixLayers = -1;

      theTrack_pt      = cand.pt();
      theTrack_eta     = cand.eta();
      theTrack_phi     = cand.phi();
      theTrack_charge  = cand.charge();


      if((cand.hasTrackDetails()))

      {

      theTrack_dz      = cand.pseudoTrack().dz();
      theTrack_dxy     = cand.pseudoTrack().dxy();

      theTrack_ptErr  = cand.pseudoTrack().ptError();
      theTrack_etaErr = cand.pseudoTrack().etaError();
      theTrack_phiErr = cand.pseudoTrack().phiError();

      theTrack_nChi2 = cand.normalizedChi2();;
      theTrack_covVersion = cand.covarianceVersion();;
      theTrack_covSchema = cand.covarianceSchema();;

      theTrack_NPixelHits  = cand.pseudoTrack().hitPattern().numberOfValidPixelHits();
      theTrack_NStripHits  = cand.pseudoTrack().hitPattern().numberOfValidStripHits();
      theTrack_NTrackhits  = cand.pseudoTrack().hitPattern().numberOfValidTrackerHits();
      theTrack_NBPixHits   = cand.pseudoTrack().hitPattern().numberOfValidStripHits();
      theTrack_NPixLayers  = cand.pseudoTrack().hitPattern().pixelLayersWithMeasurement();
      theTrack_NTraLayers  = cand.pseudoTrack().hitPattern().trackerLayersWithMeasurement();
      theTrack_NStrLayers  = cand.pseudoTrack().hitPattern().stripLayersWithMeasurement();
      theTrack_NBPixLayers = cand.pseudoTrack().hitPattern().pixelBarrelLayersWithMeasurement();

    }


      track_tree->Fill();

      // cand.unpackCovariance();




      } //IsMC || onlyGen




        // dimuontt candidates are sorted by vProb
    }

}

// ------------ method called once each job just before starting event loop  ------------
void TrackAnayzerMiniAOD::beginJob() {}

// ------------ method called once each job just after ending the event loop  ------------
void TrackAnayzerMiniAOD::endJob() {}

// ------------ method called when starting to processes a run  ------------
void TrackAnayzerMiniAOD::beginRun(edm::Run const&, edm::EventSetup const&) {}

// ------------ method called when ending the processing of a run  ------------
void TrackAnayzerMiniAOD::endRun(edm::Run const&, edm::EventSetup const&) {}

// ------------ method called when starting to processes a luminosity block  ------------
void TrackAnayzerMiniAOD::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) {}

// ------------ method called when ending the processing of a luminosity block  ------------
void TrackAnayzerMiniAOD::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) {}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void TrackAnayzerMiniAOD::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TrackAnayzerMiniAOD);
