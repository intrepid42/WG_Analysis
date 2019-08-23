import os
from argparse import ArgumentParser

import scheduler_base
from scheduler_base import JobConf

p = ArgumentParser()
p.add_argument( '--run', dest='run', default=False, action='store_true', help='Run filtering' )
p.add_argument( '--check', dest='check', default=False, action='store_true', help='Run check of completion' )
p.add_argument( '--resubmit', dest='resubmit', default=False, action='store_true', help='Only submit missing output' )
p.add_argument( '--local', dest='local', default=False, action='store_true', help='Run locally' )
p.add_argument( '--step' , dest='step' , default=1    , type=int, help='Run overlap removal steps')
p.add_argument( '--test', dest='test', default=False, action='store_true', help='Run a test job' )
options = p.parse_args()

if not options.check :
    options.run = True
else :
    options.run = False

options.batch = ( not options.local )

### ATTENTION! Here you specify the directory containing the processed ntuples, on which you want to run FilterOverlap.
#base = '/data/users/fengyb/WGammaNtuple'
base = '/data/users/kakw/Resonances2016'

# ----------------------------
# The suffix that appears on the end of the output jobs
# ----------------------------

#args_pholap           = { 'function' : 'filter_photon', 'pt_cut' : ' > 10 ', 'nph_cut' : ' == 0 ' }
#args_PtMaxInc         = { 'function' : 'filter_photon', 'pt_cut' : ' > 180 ', 'nph_cut' : ' == 0' }
#args_PtMax130         = { 'function' : 'filter_photon', 'pt_cut' : ' > 550 ', 'nph_cut' : ' == 0' }
#args_PtMin130         = { 'function' : 'filter_photon', 'pt_cut' : ' > 180 ', 'nph_cut' : ' > 0' }
#args_PtMin500         = { 'function' : 'filter_photon', 'pt_cut' : ' > 550 ', 'nph_cut' : ' > 0 ' }
#args_HT               = { 'function' : 'filter_genht' , 'trueht_cut' :  ' < 100 ' }
#args_mtMax600         = { 'function' : 'filter_mtres' , 'mtres_cut' : ' < 600 ' }
#args_mtMax1300        = { 'function' : 'filter_mtres' , 'mtres_cut' : ' < 1300 ' }
#args_mtMax500         = { 'function' : 'filter_mtres' , 'mtres_cut' : ' < 500 ' }
#args_mtMax400         = { 'function' : 'filter_mtres' , 'mtres_cut' : ' < 400 ' }
#args_mtMin400Max1200  = { 'function' : 'filter_mtres' , 'mtres_cut' : ' >= 400 && < 1200 ' }
#args_mtMin1200        = { 'function' : 'filter_mtres' , 'mtres_cut' : ' >= 1200 ' }

### Note: the "year=2016" is just a dummy, to conform to the new definition of JobConf that includes year info.
### For this filter, it doesn't make any difference what the year is.

jobs1 = [
    ### 1. FIRST UNCOMMENT AND RUN OVER THIS BLOCK
    JobConf(base, 'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'               , tags=['HT']      , suffix='TrueHTOlap',year=2016),
    JobConf(base, 'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'   , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8' , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'   , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'  , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'   , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'   , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'  , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'               , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'               , tags=['pholap'] , suffix = 'PhOlap'  ,year=2016),
#    JobConf(base, 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'          , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
#    JobConf(base, 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'          , tags=['pholap'] , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'            , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'   , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),
    JobConf(base, 'WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'                , tags=['PtMaxInc'], suffix = 'PhCutMax',year=2016),
    JobConf(base, 'WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'                 , tags=['PtMaxInc'], suffix = 'PhCutMax',year=2016),
    JobConf(base, 'WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'        , tags=['PtMax130'], suffix = 'PhCutMax',year=2016),
    JobConf(base, 'WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'         , tags=['PtMax130'], suffix = 'PhCutMax',year=2016),
    JobConf(base, 'WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'        , tags=['PtMin500'], suffix = 'PhCutMin',year=2016),
    JobConf(base, 'WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'         , tags=['PtMin500'], suffix = 'PhCutMin',year=2016),

## 2017 
#    JobConf(base, 'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', tags=['HT'], suffix='TrueHTOlap', year =2017),
#    JobConf(base, 'WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8'   , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
#    JobConf(base, 'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8' , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
#    JobConf(base, 'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8'   , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
#    JobConf(base, 'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8'  , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
#    JobConf(base, 'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8'   , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
#    JobConf(base, 'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8'   , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
#    JobConf(base, 'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8'  , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
#    JobConf(base, 'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8'               , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
#    JobConf(base, 'WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8'               , tags=['pholap']  , suffix = 'PhOlap' ,year=2017),
#    JobConf(base, 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8'          , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
#    JobConf(base, 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8'          , tags=['pholap']  , suffix = 'PhOlap' ,year=2017),
#    JobConf(base, 'TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8'            , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
#    JobConf(base, 'TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8', tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
#    JobConf(base, 'TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8'   , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),
##    JobConf(base, 'WGToLNuG_TuneCP5_13TeV-amcatnloFXFX-pythia8'                , tags=['PtMaxInc'], suffix = 'PhCutMax',year=2017),
##    JobConf(base, 'WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8'                 , tags=['PtMaxInc'], suffix = 'PhCutMax',year=2017),
##    JobConf(base, 'WGToLNuG_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8'        , tags=['PtMax130'], suffix = 'PhCutMax',year=2017),
##    JobConf(base, 'WGToLNuG_PtG-130_TuneCP5_13TeV-madgraphMLM-pythia8'         , tags=['PtMax130'], suffix = 'PhCutMax',year=2017),
##    JobConf(base, 'WGToLNuG_PtG-500_TuneCP5_13TeV-amcatnloFXFX-pythia8'        , tags=['PtMin500'], suffix = 'PhCutMin',year=2017),
##    JobConf(base, 'WGToLNuG_PtG-500_TuneCP5_13TeV-madgraphMLM-pythia8'         , tags=['PtMin500'], suffix = 'PhCutMin',year=2017),
]

jobs2 = [
    ### 2. WHEN STEP 1 IS DONE, COMMENT THAT BLOCK, AND UNCOMMENT AND RUN OVER THIS BLOCK
    JobConf(base, 'WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8PhCutMax', tags=['PtMin130'], suffix = 'PhCutMin',year=2016),
    JobConf(base, 'WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-madgraphMLM-pythia8PhCutMax' , tags=['PtMin130'], suffix = 'PhCutMin',year=2016),
    JobConf(base, 'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8TrueHTOlap'     , tags=['pholap']  , suffix = 'PhOlap'  ,year=2016),

    JobConf(base, 'WGToLNuG_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8PhCutMax', tags=['PtMin130'], suffix = 'PhCutMin',year=2017),
    JobConf(base, 'WGToLNuG_PtG-130_TuneCP5_13TeV-madgraphMLM-pythia8PhCutMax' , tags=['PtMin130'], suffix = 'PhCutMin',year=2017),
    JobConf(base, 'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8TrueHTOlap'     , tags=['pholap']  , suffix = 'PhOlap'  ,year=2017),

    ### 3. DON'T RUN OVER THESE; AS FAR AS I KNOW, I DON'T THINK WE NEED THESE
    ##JobConf(base, 'WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8PhCutMax'                , tags=['mtMax600']       , suffix = 'MTResCut'),
    ##JobConf(base, 'WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8PhCutMaxPhCutMin', tags=['mtMax1300']      , suffix = 'MTResCut'),
    ##JobConf(base, 'WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8PhCutMax'                 , tags=['mtMax500']       , suffix = 'MTResCut'),
    ##JobConf(base, 'WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-madgraphMLM-pythia8PhCutMaxPhCutMin' , tags=['mtMax1300']      , suffix = 'MTResCut'),
    ##JobConf(base, 'WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'                        , tags=['mtMax400']       , suffix = 'MTResCut'),
    ##JobConf(base, 'WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'                         , tags=['mtMax400']       , suffix = 'MTResCut'),
    ##JobConf(base, 'WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'                , tags=['mtMin400Max1200'], suffix = 'MTResCut'),
    ##JobConf(base, 'WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'                 , tags=['mtMin400Max1200'], suffix = 'MTResCut'),
    ##JobConf(base, 'WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'                , tags=['mtMin1200']      , suffix = 'MTResCut'),
    ##JobConf(base, 'WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'                 , tags=['mtMin1200']      , suffix = 'MTResCut'),
]

if options.step==0:
    jobs= jobs1[0]
if options.step==1:
    jobs= jobs1
if options.step==2:
    jobs= jobs2

options.nFilesPerJob = 1
options.nproc = 2
options.treename='UMDNTuple/EventTree'
options.exename='RunAnalysis'
options.copyInputFiles=True
options.enableKeepFilter=False
if options.test :
    options.nproc = 1
    options.nFilesPerJob = 10
    options.totalEvents = 1001
    options.nJobs = 1
    options.batch = False
    options.local = True

### ATTENTION! Here you list the ntuple types (from RecoResonance) that you want to process, which is also the name of the subdirectory containing them.
input_dirs =[
               #'LepGamma_elg_2019_08_20_beta/',
               #'LepGamma_mug_2019_08_19_beta/',
               #'LepLep_mumu_2019_08_19_beta/',
#               'LepLep_elel_2019_08_20_beta/',
               'LepLep_elel_2019_08_05/',
              #'LepLep_mumu_2019_03_14',#'LepLep_elel_2018_08_13',
              #'LepGammaNoPhId_elg_2019_03_17','LepGammaNoPhId_mug_2019_03_17',
              #'SingleLepNoPhId_el_2019_03_17','SingleLepNoPhId_mu_2019_03_17',
]

module = 'Conf.py'

configs = []

for input_dir in input_dirs : 

    configs.append( {
                     'module' : module,
                     'args' : {},
                     'input' : input_dir, 
                     'output' : base + '/' + input_dir,
                     'tag' : 'olap', 
                     #'args_tag_pholap'           : { 'function' : 'filter_photon', 'pt_cut' : ' > 10 ', 'nph_cut' : ' == 0 ', 'isPromptFS_cut' : ' == True ' },
                     'args_tag_pholap'           : { 'function' : 'filter_photon', 'pt_cut' : ' > 10 ', 'nph_cut' : ' == 0 ' },
                     'args_tag_PtMaxInc'         : { 'function' : 'filter_photon', 'pt_cut' : ' > 180 ', 'nph_cut' : ' == 0' },
                     'args_tag_PtMax130'         : { 'function' : 'filter_photon', 'pt_cut' : ' > 550 ', 'nph_cut' : ' == 0' },
                     'args_tag_PtMin130'         : { 'function' : 'filter_photon', 'pt_cut' : ' > 180 ', 'nph_cut' : ' > 0' },
                     'args_tag_PtMin500'         : { 'function' : 'filter_photon', 'pt_cut' : ' > 550 ', 'nph_cut' : ' > 0 ' },
                     'args_tag_HT'               : { 'function' : 'filter_genht' , 'trueht_cut' :  ' < 100 ' },
                     'args_tag_mtMax600'         : { 'function' : 'filter_mtres' , 'mtres_cut' : ' < 600 ' },
                     'args_tag_mtMax1300'        : { 'function' : 'filter_mtres' , 'mtres_cut' : ' < 1300 ' },
                     'args_tag_mtMax500'         : { 'function' : 'filter_mtres' , 'mtres_cut' : ' < 500 ' },
                     'args_tag_mtMax400'         : { 'function' : 'filter_mtres' , 'mtres_cut' : ' < 400 ' },
                     'args_tag_mtMin400Max1200'  : { 'function' : 'filter_mtres' , 'mtres_cut' : ' >= 400 && < 1200 ' },
                     'args_tag_mtMin1200'        : { 'function' : 'filter_mtres' , 'mtres_cut' : ' >= 1200 ' },
    })


scheduler_base.RunJobs( jobs, configs, options)

