# Auto generated configuration file
# using: 
# Revision: 1.232.2.6 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/jpsiToMuMu_pythia6EvtGenFSR_2TeV76.py -s GEN:ProductionFilterSequence --eventcontent RECOSIM --datatier GEN-SIM --conditions START39_V7HI::All --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.VtxSmearedRealisticPPbBoost8TeVCollision_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/jpsiToMuMu_pythia6EvtGenFSR_2TeV76.py nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)
process.maxEvents = cms.untracked.PSet(
    output = cms.untracked.int32(5000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
	wantSummary = cms.untracked.bool(True)
)

# random seed option 1
process.RandomNumberGeneratorService.generator.initialSeed = _N_ 
process.RandomNumberGeneratorService.VtxSmeared.initialSeed = _N_ 
process.RandomNumberGeneratorService.g4SimHits.initialSeed = _N_ 
process.RandomNumberGeneratorService.mix.initialSeed = _N_ 
process.RandomNumberGeneratorService.mixData.initialSeed = _N_ 
process.RandomNumberGeneratorService.simSiStripDigis.initialSeed = _N_ 
process.RandomNumberGeneratorService.simEcalUnsuppressedDigis.initialSeed = _N_ 
process.RandomNumberGeneratorService.simHcalUnsuppressedDigis.initialSeed = _N_ 
process.RandomNumberGeneratorService.simMuonDTDigis.initialSeed = _N_ 
process.RandomNumberGeneratorService.simMuonCSCDigis.initialSeed = _N_ 
process.RandomNumberGeneratorService.simMuonRPCDigis.initialSeed = _N_ 
process.RandomNumberGeneratorService.simCastorDigis.initialSeed = _N_ 

# random seeds option 2
##from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
##randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
##randSvc.populate()


##from Configuration.AlCa.GlobalTag import GlobalTag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'STARTHI53_V17::All'

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'STARTHI53_V17::All', '')

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(5023.0),
    crossSection = cms.untracked.double(49118161.0),
    ##filterEfficiency = cms.untracked.double(1.4e-04),
    filterEfficiency = cms.untracked.double(1),
    maxEventsToPrint = cms.untracked.int32(0),
    ExternalDecays = cms.PSet(
        EvtGen = cms.untracked.PSet(
            operates_on_particles = cms.vint32(0),
            use_default_decay = cms.untracked.bool(False),
            decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
            user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Bu_JpsiK.dec'),
            list_forced_decays = cms.vstring('MyB+','MyB-'),
       ),
        parameterSets = cms.vstring('EvtGen')
    ),
    PythiaParameters = cms.PSet(
	pythiaUESettingsBlock,
	bbbarSettings = cms.vstring('MSEL = 1'), # This is a vector of ParameterSet names to be read, in this order
	parameterSets = cms.vstring(
		'pythiaUESettings',
		'bbbarSettings')
    )
)

process.bfilter = cms.EDFilter(
	"PythiaFilter",
	MaxEta = cms.untracked.double(9999.),
	MinEta = cms.untracked.double(-9999.),
	ParticleID = cms.untracked.int32(521)
)

process.jpsifilter = cms.EDFilter(
	"PythiaDauVFilter",
	verbose	= cms.untracked.int32(0), ### >10 : print more information
	NumberDaughters = cms.untracked.int32(2),
	MotherID = cms.untracked.int32(521),
	ParticleID = cms.untracked.int32(443),
	DaughterIDs = cms.untracked.vint32(13,-13),
	MinPt = cms.untracked.vdouble(0.0,0.0),
	MinEta = cms.untracked.vdouble(-9999.,-9999.),
	MaxEta = cms.untracked.vdouble(9999.,9999.)
)

process.kfilter = cms.EDFilter(
	"PythiaDauVFilter",
	verbose	= cms.untracked.int32(0), ### >10 : print more information
	NumberDaughters = cms.untracked.int32(2),
	MotherID = cms.untracked.int32(0),
	ParticleID = cms.untracked.int32(521),
	DaughterIDs = cms.untracked.vint32(443,321),
	MinPt = cms.untracked.vdouble(0.,0.0),
	MinEta = cms.untracked.vdouble(-9999.,-9999.),
	MaxEta = cms.untracked.vdouble(9999.,9999.)
)

'''
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.832 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.275 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        processParameters = cms.vstring('MSEL=61          ! Quarkonia', 
            'MDME(858,1) = 0  ! 0.060200    e-    e+', 
            'MDME(859,1) = 1  ! 0.060100    mu-  mu+', 
            'MDME(860,1) = 0  ! 0.879700    rndmflav        rndmflavbar', 
            'MSTP(142)=2      ! turns on the PYEVWT Pt re-weighting routine', 
            'PARJ(13)=0.750   ! probability that a c or b meson has S=1', 
            'PARJ(14)=0.162   ! probability that a meson with S=0 is produced with L=1, J=1', 
            'PARJ(15)=0.018   ! probability that a meson with S=1 is produced with L=1, J=0', 
            'PARJ(16)=0.054   ! probability that a meson with S=1 is produced with L=1, J=1', 
            'MSTP(145)=0      ! choice of polarization', 
            'MSTP(146)=0      ! choice of polarization frame ONLY when mstp(145)=1', 
            'MSTP(147)=0      ! particular helicity or density matrix component when mstp(145)=1', 
            'MSTP(148)=1      ! possibility to allow for final-state shower evolution, extreme case !', 
            'MSTP(149)=1      ! if mstp(148)=1, it determines the kinematics of the QQ~3S1(8)->QQ~3S1(8)+g branching', 
            'PARP(141)=1.16   ! New values for COM matrix elements', 
            'PARP(142)=0.0119 ! New values for COM matrix elements', 
            'PARP(143)=0.01   ! New values for COM matrix elements', 
            'PARP(144)=0.01   ! New values for COM matrix elements', 
            'PARP(145)=0.05   ! New values for COM matrix elements', 
            'PARP(146)=9.28   ! New values for COM matrix elements', 
            'PARP(147)=0.15   ! New values for COM matrix elements', 
            'PARP(148)=0.02   ! New values for COM matrix elements', 
            'PARP(149)=0.02   ! New values for COM matrix elements', 
            'PARP(150)=0.085  ! New values for COM matrix elements', 
            'BRAT(861)=0.202  ! chi_2c->J/psi gamma', 
            'BRAT(862)=0.798  ! chi_2c->rndmflav rndmflavbar', 
            'BRAT(1501)=0.013 ! chi_0c->J/psi gamma', 
            'BRAT(1502)=0.987 ! chi_0c->rndmflav rndmflavbar', 
            'BRAT(1555)=0.356 ! chi_1c->J/psi gamma', 
            'BRAT(1556)=0.644 ! chi_1c->rndmflav rndmflavbar'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters', 
            'CSAParameters'),
        CSAParameters = cms.vstring('CSAMODE = 6     ! cross-section reweighted quarkonia')
    )
)
'''
##process.ProductionFilterSequence = cms.Sequence(process.generator)
process.ProductionFilterSequence = cms.Sequence(process.generator*process.bfilter*process.jpsifilter*process.kfilter)


# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    ##outputCommands = process.FEVTSIMEventContent.outputCommands,
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_genParticles_*_*'
        ),
    fileName = cms.untracked.string(
        ##'test.root'
	'_output_file_'
	),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)


# Path and EndPath definitions
##process.generation_step = cms.Path(process.pgen)
process.generation_step = cms.Path(process.randomEngineStateProducer*process.VtxSmeared*process.genParticles)

process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# avoid problem with unknown pdg code
process.hiGenParticles.abortOnUnknownPDGCode = cms.untracked.bool(False)


# seeds
##from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
##randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
##randSvc.populate()

##print process.RandomNumberGeneratorService.dumpConfig()

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.FEVTDEBUGoutput_step)

# special treatment in case of production filter sequence
for path in process.paths: 
    getattr(process,path)._seq = process.ProductionFilterSequence*getattr(process,path)._seq
