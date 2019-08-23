# setup CMSSW (without explicitly having a CMSSW release)
#source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /cvmfs/cms.cern.ch/slc7_amd64_gcc630/cms/cmssw/CMSSW_9_4_14_UL/src
eval `scramv1 runtime -csh`
cd -

setenv WorkArea ${PWD}/Analysis
if( $?PYTHONPATH == 0 ) then
   setenv PYTHONPATH ${PWD}/Analysis/TreeFilter/Core/python:${PWD}/Analysis/Util/python:${PWD}/Plotting
else 
   setenv PYTHONPATH ${PWD}/Analysis/TreeFilter/Core/python:${PWD}/Analysis/Util/python:${PWD}/Plotting:$PYTHONPATH
endif

