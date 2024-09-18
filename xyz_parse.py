#!/usr/bin/env python
# coding: utf-8

# In[18]:


# import modules
import os
import glob
import argparse


# In[19]:


valid_gaussian_functionals = [
    'HF', 'B3LYP', 'B3P86', 'O3LYP', 'B3PW91', 
    'APFD', 'wB97XD', 'LC-wHPBE', 'CAM-B3LYP', 'MN15', 
    'M11', 'SOGGA11X', 'N12SX', 'MN12SX', 'PW6B95', 
    'PW6B95D3', 'M08HX', 'M06', 'M06HF', 'M062X', 
    'M05', 'M052X', 'HSEH1PBE', 'PBE1PBE', 'OHSE1PBE', 
    'OHSE2PBE', 'PBEh1PBE', 'B1B95', 'B1LYP', 'mPW1PW91', 
    'mPW1LYP', 'mPW1PBE', 'mPW3PBE', 'B98', 'B971', 
    'B972', 'TPSSh', 'tHCTHhyb', 'BMK', 'HISSbPBE', 
    'X3LYP', 'BHandH', 'BHandHLYP', 'HFS', 'XAlpha', 
    'VSXC', 'HCTH', 'HCTH93', 'HCTH147', 'HCTH407', 
    'tHCTH', 'B97D', 'M06L', 'SOGGA11', 'M11L', 
    'N12', 'MN15L', 'SVWN', 'SVWN5', 'SLYP', 
    'SPL', 'SP86', 'SPW91', 'SB95', 'SPBE', 
    'STPSS', 'SRevTPSS', 'SKCIS', 'SBRC', 'SPKZB', 
    'XAVWN', 'XAVWN5', 'XALYP', 'XAPL', 'XAP86', 
    'XAPW91', 'XAB95', 'XAPBE', 'XATPSS', 'XARevTPSS', 
    'XAKCIS', 'XABRC', 'XAPKZB', 'BVWN', 'BVWN5', 
    'BLYP', 'BPL', 'BP86', 'BPW91', 'BB95', 
    'BPBE', 'BTPSS', 'BRevTPSS', 'BKCIS', 'BBRC', 
    'BPKZB', 'PW91VWN', 'PW91VWN5', 'PW91LYP', 'PW91PL', 
    'PW91P86', 'PW91PW91', 'PW91B95', 'PW91PBE', 'PW91TPSS', 
    'PW91RevTPSS', 'PW91KCIS', 'PW91BRC', 'PW91PKZB', 'mPWVWN', 
    'mPWVWN5', 'mPWLYP', 'mPWPL', 'mPWP86', 'mPWPW91', 
    'mPWB95', 'mPWPBE', 'mPWTPSS', 'mPWRevTPSS', 'mPWKCIS', 
    'mPWBRC', 'mPWPKZB', 'G96VWN', 'G96VWN5', 'G96LYP', 
    'G96PL', 'G96P86', 'G96PW91', 'G96B95', 'G96PBE', 
    'G96TPSS', 'G96RevTPSS', 'G96KCIS', 'G96BRC', 'G96PKZB', 
    'PBEVWN', 'PBEVWN5', 'PBELYP', 'PBEPL', 'PBEP86', 
    'PBEPW91', 'PBEB95', 'PBEPBE', 'PBETPSS', 'PBERevTPSS', 
    'PBEKCIS', 'PBEBRC', 'PBEPKZB', 'OVWN', 'OVWN5', 
    'OLYP', 'OPL', 'OP86', 'OPW91', 'OB95', 
    'OPBE', 'OTPSS', 'ORevTPSS', 'OKCIS', 'OBRC', 
    'OPKZB', 'TPSSVWN', 'TPSSVWN5', 'TPSSLYP', 'TPSSPL', 
    'TPSSP86', 'TPSSPW91', 'TPSSB95', 'TPSSPBE', 'TPSSTPSS', 
    'TPSSRevTPSS', 'TPSSKCIS', 'TPSSBRC', 'TPSSPKZB', 'RevTPSSVWN', 
    'RevTPSSVWN5', 'RevTPSSLYP', 'RevTPSSPL', 'RevTPSSP86', 'RevTPSSPW91', 
    'RevTPSSB95', 'RevTPSSPBE', 'RevTPSSTPSS', 'RevTPSSRevTPSS', 'RevTPSSKCIS', 
    'RevTPSSBRC', 'RevTPSSPKZB', 'BRxVWN', 'BRxVWN5', 'BRxLYP', 
    'BRxPL', 'BRxP86', 'BRxPW91', 'BRxB95', 'BRxPBE', 
    'BRxTPSS', 'BRxRevTPSS', 'BRxKCIS', 'BRxBRC', 'BRxPKZB', 
    'PKZBVWN', 'PKZBVWN5', 'PKZBLYP', 'PKZBPL', 'PKZBP86', 
    'PKZBPW91', 'PKZBB95', 'PKZBPBE', 'PKZBTPSS', 'PKZBRevTPSS', 
    'PKZBKCIS', 'PKZBBRC', 'PKZBPKZB', 'wPBEhVWN', 'wPBEhVWN5', 
    'wPBEhLYP', 'wPBEhPL', 'wPBEhP86', 'wPBEhPW91', 'wPBEhB95', 
    'wPBEhPBE', 'wPBEhTPSS', 'wPBEhRevTPSS', 'wPBEhKCIS', 'wPBEhBRC', 
    'wPBEhPKZB', 'PBEhVWN', 'PBEhVWN5', 'PBEhLYP', 'PBEhPL', 
    'PBEhP86', 'PBEhPW91', 'PBEhB95', 'PBEhPBE', 'PBEhTPSS', 
    'PBEhRevTPSS', 'PBEhKCIS', 'PBEhBRC', 'PBEhPKZB', 'MP2', 
    'MP3', 'MP4', 'MP4(DQ)', 'MP4(SDQ)', 'MP4(SDTQ)', 
    'MP5', 'B2PLYP', 'mPW2PLYP', 'B2PLYPD', 'mPW2PLYPD', 
    'B2PLYPD3', 'DSDPBEP86', 'PBE0DH', 'PBEQIDH', 'CCD', 
    'CCSD', 'CC', 'CCSD(T)', 'CCSD-T', 'CIS', 
    'CID', 'CISD', 'CI', 'CASSCF', 'BD', 
    'QCISD', 'BD(T)', 'QCISD(TQ)', 'AM1', 'PM3', 
    'PM3MM', 'PM6', 'PDDG', 'PM7', 'DFTB', 
    'DFTBA', 'CBS-4M', 'CBS-QB3', 'CBS-APNO', 'G1', 
    'G2', 'G3', 'G4', 'G2MP2', 'G3MP2', 
    'G4MP2', 'W1U', 'W1BD'
]


# In[20]:


valid_orca_functionals = [
   'HFS', 'LDA', 'LSD', 'VWN', 'VWN3', 
   'VWN5', 'PWLDA', 'BP', 'BP86', 'BLYP', 
   'OLYP', 'GLYP', 'XLYP', 'PW91', 'mPWPW', 
   'mPWLYP', 'PBE', 'RPBE', 'REVPBE', 'PWP', 
   'B1LYP', 'B3LYP', 'CAM-B3LYP', 'B3LYP/G', 'O3LYP', 
   'X3LYP', 'B1P', 'B3P', 'B3PW', 'PW1PW', 
   'mPW1PW', 'mPWLYP', 'PBE0', 'PW6B95', 'BHANDHLYP', 
   'TPSS', 'TPSSh', 'TPSS0', 'M06', 'M062X', 
   'M06L', 'B97M-V', 'B97M-D3BJ', 'SCANfunc', 'wB97', 
   'wB97X', 'wB97X-D3', 'wB97X-D3BJ', 'wB97X-V', 'wB97M-V', 
   'wB97M-D3BJ', 'LC-BLYP', 'B2PLYP', 'mPW2PLYP', 'mPW2PLYP-D', 
   'B2GP-PLYP', 'B2K-PLYP', 'B2T-PLYP', 'PWPB95', 'DSD-BLYP', 
   'DSD-PBEP86', 'DSD-PBEB95', 'wB2PLYP', 'wB2GP-PLYP', 'CCSD', 
   'CCSD(T)', 'AOX-CCSD', 'AOX-CCSD(T)', 'AO-CCSD', 'AO-CCSD(T)', 
   'MO-CCSD', 'MO-CCSD(T)', 'QCISD', 'QCISD(T)', 'AOX-QCISD', 
   'AOX-QCISD(T)', 'AO-QCISD', 'AO-QCISD(T)', 'MO-QCISD', 'MO-QCISD(T)', 
   'CPF/1', 'CPF/2', 'CPF/3', 'NCPF/1', 'NCPF/2', 
   'NCPF/3', 'AOX-CPF/1', 'AOX-CPF/2', 'AOX-CPF/3', 'AOX-NCPF/1', 
   'AOX-NCPF/2', 'AOX-NCPF/3', 'AO-CPF/1', 'AO-CPF/2', 'AO-CPF/3', 
   'AO-NCPF/1', 'AO-NCPF/2', 'AO-NCPF/3', 'MO-CPF/1', 'MO-CPF/2', 
   'MO-CPF/3', 'MO-NCPF/1', 'MO-NCPF/2', 'MO-NCPF/3', 'CEPA/0', 
   'CEPA/1', 'CEPA/2', 'CEPA/3', 'NCEPA/1', 'NCEPA/2', 
   'NCEPA/3', 'AOX-CEPA/1', 'AOX-CEPA/2', 'AOX-CEPA/3', 'AOX-NCEPA/1', 
   'AOX-NCEPA/2', 'AOX-NCEPA/3', 'AO-CEPA/1', 'AO-CEPA/2', 'AO-CEPA/3', 
   'AO-NCEPA/1', 'AO-NCEPA/2', 'AO-NCEPA/3', 'MO-CEPA/1', 'MO-CEPA/2', 
   'MO-CEPA/3', 'MO-NCEPA/1', 'MO-NCEPA/2', 'MO-NCEPA/3', 'ACPF', 
   'NACPF', 'AOX-ACPF', 'AOX-NACPF', 'AO-ACPF', 'AO-NACPF', 
   'MO-ACPF', 'MO-NACPF', 'AQCC', 'AOX-AQCC', 'AO-AQCC', 
   'MO-AQCC', 'CISD', 'MO-CISD', 'pCCSD/1a', 'pCCSD/2a', 
   'SCS-MP2', 'MP2', 'MP3', 'SCS-MP3', 'DMRG', 
   'NEVPT2', 'SC-NEVPT2', 'RI-NEVPT2', 'FIC-NEVPT2', 'CASPT2', 
   'RI-CASPT2', 'DCD-CAS(2)', 'RI-DCD-CAS(2)', 'ZINDO/1', 'ZINDO/2', 
   'ZINDO/S', 'NDDO/1', 'NDDO/2', 'MNDO', 'AM1', 
   'PM3', 'HF-3c', 'PBEh-3c', 'HF', 'CCSD-F12', 
   'CCSD-F12/RI', 'CCSD-F12D/RI', 'CCSD(T)-F12', 'CCSD(T)-F12/RI', 'CCSD(T)-F12D/RI', 
   'RI-CCSD', 'RI-CCSD-F12/RI', 'RI-CCSD(T)', 'RI-CCSD(T)-F12/RI', 'RI34-CCSD', 
   'RI34-CCSD(T)', 'QCISD-F12', 'QCISD-F12/RI', 'QCISD(T)-F12', 'QCISD(T)-F12/RI', 
   'RI-QCISD', 'RI-QCISD-F12/RI', 'RI-QCISD(T)', 'RI-QCISD(T)-F12/RI', 'RI34-QCISD', 
   'RI34-QCISD(T)', 'RI-CPF/1', 'RI-CPF/2', 'RI-CPF/3', 'RI-NCPF/1', 
   'RI-NCPF/2', 'RI-NCPF/3', 'RI34-CPF/1', 'RI34-CPF/2', 'RI34-CPF/3', 
   'RI34-NCPF/1', 'RI34-NCPF/2', 'RI34-NCPF/3', 'RI-CEPA/1', 'RI-CEPA/2', 
   'RI-CEPA/3', 'RI-NCEPA/1', 'RI-NCEPA/2', 'RI-NCEPA/3', 'RI34-CEPA/1', 
   'RI34-CEPA/2', 'RI34-CEPA/3', 'RI34-NCEPA/1', 'RI34-NCEPA/2', 'RI34-NCEPA/3', 
   'RI-ACPF', 'RI-NACPF', 'RI-AQCC', 'RI-CISD', 'RI34-CISD', 
   'MRACPF', 'LPNO-CCSD', 'DLPNO-CCSD', 'DLPNO-CCSD(T)', 'DLPNO-CCSD(T1)', 
   'DLPNO-CCSD-F12', 'DLPNO-CCSD-F12/D', 'DLPNO-CCSD(T)-F12', 'DLPNO-CCSD(T)-F12/D', 'DLPNO2013-CCSD', 
   'DLPNO2013-CCSD(T)', 'DLPNO2013-CCSD-F12', 'DLPNO-MP2', 'DLPNO-SCS-MP2', 'DLPNO-MP2-F12', 
   'DLPNO-MP2-F12/D', 'LPNO-CEPA/1', 'LPNO-CEPA/2', 'LPNO-CEPA/3', 'LPNO-NCEPA/1', 
   'LPNO-NCEPA/2', 'LPNO-NCEPA/3', 'LPNO-VCEPA/1', 'LPNO-CPF/1', 'LPNO-CPF/2', 
   'LPNO-CPF/3', 'LPNO-NCPF/1', 'LPNO-NCPF/2', 'LPNO-NCPF/3', 'LPNO-QCISD', 
   'LPNO-pCCSD/1a', 'LPNO-pCCSD/2a', 'MP2RI', 'RI-MP2', 'RI-SCS-MP2', 
   'SCS-RI-MP2', 'OO-RI-MP2', 'OO-RI-SCS-MP2', 'MP2-F12', 'MP2-F12-RI', 
   'MP2-F12D-RI', 'FIC-MRCI', 'FIC-DDCI3', 'FIC-CEPA0', 'FIC-ACPF', 
   'FIC-AQCC', 'MRCI', 'MRCI+Q', 'MRACPF', 'MRAQCC', 
   'MRDDCI1', 'MRDDCI2', 'MRDDCI3', 'MRDDCI1+Q', 'MRDDCI2+Q', 
   'MRDDCI3+Q', 'SORCI', 'B97-D', 'B97-D3', 'EOM-CCSD', 
   'EOM-DLPNO-CCSD', 'STEOM-CCSD', 'STEOM-DLPNO-CCSD', 'ADC2'
]


# In[25]:


valid_gaussian_basis = [
    'STO-3G', 'STO-3G*', '3-21G', '3-21+G', '3-21G*', '3-21+G*',
    '6-21G', '6-21G*', '6-21G**', '6-21G(d)', '6-21G(d,p)',
    '4-31G', '4-31G*', '4-31G**', '4-31G(d)', '4-31G(d,p)',
    '6-31G', '6-31+G', '6-31++G', '6-31G*', '6-31G**',
    '6-31G(d)', '6-31G(2d)', '6-31G(2df)', '6-31G(d,p)', '6-31G(2d,p)',
    '6-31G(2d,2p)', '6-31G(2df,2p)', '6-31G(2d,2pd)', '6-31G(2df,2pd)',
    '6-31G(3d)', '6-31G(3df)', '6-31G(3d,3p)', '6-31G(3df,3p)',
    '6-31G(3d,3pd)', '6-31G(3df,3pd)', '6-31+G*', '6-31+G**',
    '6-31+G(d)', '6-31+G(2d)', '6-31+G(2df)', '6-31+G(d,p)', '6-31+G(2d,p)',
    '6-31+G(2d,2p)', '6-31+G(2df,2p)', '6-31+G(2d,2pd)', '6-31+G(2df,2pd)',
    '6-31+G(3d)', '6-31+G(3df)', '6-31+G(3d,3p)', '6-31+G(3df,3p)',
    '6-31+G(3d,3pd)', '6-31+G(3df,3pd)', '6-31++G*', '6-31++G**',
    '6-31++G(d)', '6-31++G(2d)', '6-31++G(2df)', '6-31++G(d,p)', '6-31++G(2d,p)',
    '6-31++G(2d,2p)', '6-31++G(2df,2p)', '6-31++G(2d,2pd)', '6-31++G(2df,2pd)',
    '6-31++G(3d)', '6-31++G(3df)', '6-31++G(3d,3p)', '6-31++G(3df,3p)',
    '6-31++G(3d,3pd)', '6-31++G(3df,3pd)', '6-31G(d\')', '6-31G(d\'f)', '6-31G(d\',p\')',
    '6-31G(d\'f,p\')', '6-31+G(d\')', '6-31+G(d\'f)', '6-31+G(d\',p\')', '6-31+G(d\'f,p\')',
    '6-31++G(d\')', '6-31++G(d\'f)', '6-31++G(d\',p\')', '6-31++G(d\'f,p\')',
    '6-311G', '6-311G*', '6-311G**', '6-311G(d)', '6-311G(2d)',
    '6-311G(2df)', '6-311G(d,p)', '6-311G(2d,p)', '6-311G(2d,2p)',
    '6-311G(2df,2p)', '6-311G(2d,2pd)', '6-311G(2df,2pd)', '6-311G(2d,3p)',
    '6-311G(2df,3p)', '6-311G(2d,3pd)', '6-311G(2df,3pd)', '6-311G(3d)',
    '6-311G(3df)', '6-311G(3d,p)', '6-311G(3d,2p)', '6-311G(3d,3p)',
    '6-311G(3df,3p)', '6-311G(3d,3pd)', '6-311G(3df,3pd)', '6-311+G',
    '6-311+G*', '6-311+G**', '6-311+G(d)', '6-311+G(2d)', '6-311+G(2df)',
    '6-311+G(d,p)', '6-311+G(2d,p)', '6-311+G(2d,2p)', '6-311+G(2df,2p)',
    '6-311+G(2d,2pd)', '6-311+G(2df,2pd)', '6-311+G(2d,3p)', '6-311+G(2df,3p)',
    '6-311+G(2d,3pd)', '6-311+G(2df,3pd)', '6-311+G(3d)', '6-311+G(3df)',
    '6-311+G(3d,p)', '6-311+G(3d,2p)', '6-311+G(3d,3p)', '6-311+G(3df,3p)',
    '6-311+G(3d,3pd)', '6-311+G(3df,3pd)', '6-311++G', '6-311++G*', '6-311++G**',
    '6-311++G(d)', '6-311++G(2d)', '6-311++G(2df)', '6-311++G(d,p)', '6-311++G(2d,p)',
    '6-311++G(2d,2p)', '6-311++G(2df,2p)', '6-311++G(2d,2pd)', '6-311++G(2df,2pd)',
    '6-311++G(2d,3p)', '6-311++G(2df,3p)', '6-311++G(2d,3pd)', '6-311++G(2df,3pd)',
    '6-311++G(3d)', '6-311++G(3df)', '6-311++G(3d,p)', '6-311++G(3d,2p)', '6-311++G(3d,3p)',
    '6-311++G(3df,3p)', '6-311++G(3d,3pd)', '6-311++G(3df,3pd)', 'MC-311G',
    'D95', 'D95*', 'D95**', 'D95(d)', 'D95(2d)', 'D95(2df)', 'D95(d,p)', 'D95(2d,p)',
    'D95(2d,2p)', 'D95(2df,2p)', 'D95(2d,2pd)', 'D95(2df,2pd)', 'D95(3d)', 'D95(3df)',
    'D95(3d,3p)', 'D95(3df,3p)', 'D95(3d,3pd)', 'D95(3df,3pd)', 'D95V', 'D95V(d)', 'D95V(d,p)',
    'SHC', 'SHC*', 'SHC(d)', 'CEP-4G', 'CEP-4G(d)', 'CEP-4G*', 'CEP-31G', 'CEP-31G(d)', 'CEP-31G*',
    'CEP-121G', 'CEP-121G(d)', 'CEP-121G*', 'LanL2MB', 'LanL2DZ',
    'aug-cc-pVDZ', 'aug-cc-pVTZ', 'aug-cc-pVQZ', 'aug-cc-pV5Z', 'aug-cc-pV6Z',
    'spAug-cc-pVDZ', 'spAug-cc-pVTZ', 'spAug-cc-pVQZ', 'spAug-cc-pV5Z', 'spAug-cc-pV6Z',
    'dAug-cc-pVDZ', 'dAug-cc-pVTZ', 'dAug-cc-pVQZ', 'dAug-cc-pV5Z', 'dAug-cc-pV6Z',
    'jul-cc-pVDZ', 'jul-cc-pVTZ', 'jul-cc-pVQZ', 'jul-cc-pV5Z', 'jul-cc-pV6Z',
    'tjul-cc-pVDZ', 'tjul-cc-pVTZ', 'tjul-cc-pVQZ', 'tjul-cc-pV5Z', 'tjul-cc-pV6Z',
    'jun-cc-pVDZ', 'jun-cc-pVTZ', 'jun-cc-pVQZ', 'jun-cc-pV5Z', 'jun-cc-pV6Z',
    'tjun-cc-pVDZ', 'tjun-cc-pVTZ', 'tjun-cc-pVQZ', 'tjun-cc-pV5Z', 'tjun-cc-pV6Z',
    'may-cc-pVDZ', 'may-cc-pVTZ', 'may-cc-pVQZ', 'may-cc-pV5Z', 'may-cc-pV6Z',
    'tmay-cc-pVDZ', 'tmay-cc-pVTZ', 'tmay-cc-pVQZ', 'tmay-cc-pV5Z', 'tmay-cc-pV6Z',
    'apr-cc-pVDZ', 'apr-cc-pVTZ', 'apr-cc-pVQZ', 'apr-cc-pV5Z', 'apr-cc-pV6Z',
    'tapr-cc-pVDZ', 'tapr-cc-pVTZ', 'tapr-cc-pVQZ', 'tapr-cc-pV5Z', 'tapr-cc-pV6Z',
    'SV', 'SVP', 'def2SV', 'def2SVP', 'def2SVPP', 'TZV', 'TZVP', 'def2TZV', 'def2TZVP', 'def2TZVPP',
    'QZV', 'QZVP', 'QZVPP', 'def2QZV', 'def2QZVP', 'def2QZVPP', 'MidiX', 'EPR-II', 'EPR-III', 'UGBS',
    'UGBS1P', 'UGBS1V', 'UGBS1O', 'UGBS2P', 'UGBS2V', 'UGBS2O', 'UGBS3P', 'UGBS3V', 'UGBS3O', 'UGBS+',
    'UGBS1P+', 'UGBS1V+', 'UGBS1O+', 'UGBS2P+', 'UGBS2V+', 'UGBS2O+', 'UGBS3P+', 'UGBS3V+', 'UGBS3O+', 'UGBS++',
    'UGBS1P++', 'UGBS1V++', 'UGBS1O++', 'UGBS2P++', 'UGBS2V++', 'UGBS2O++', 'UGBS3P++', 'UGBS3V++', 'UGBS3O++', 'UGBS2+',
    'UGBS1P2+', 'UGBS1V2+', 'UGBS1O2+', 'UGBS2P2+', 'UGBS2V2+', 'UGBS2O2+', 'UGBS3P2+', 'UGBS3V2+', 'UGBS3O2+', 'UGBS2++',
    'UGBS1P2++', 'UGBS1V2++', 'UGBS1O2++', 'UGBS2P2++', 'UGBS2V2++', 'UGBS2O2++', 'UGBS3P2++', 'UGBS3V2++', 'UGBS3O2++',
    'MTSmall', 'DGDZVP', 'DGDZVP2', 'DGTZVP', 'CBSB7', 'CBSB7+', 'CBSB7++']


# In[26]:


valid_orca_basis = [
    '3-21G', 'STO-3G', '3-21GSP', '4-22GSP', '6-31G', 
    '6-31G*', '6-31G(d)', '6-31G**', '6-31G(d,p)', '6-31G(2d)', 
    '6-31G(2df)', '6-31G(2d,p)', '6-31G(2d,2p)', '6-31G(2df,2p)', '6-31G(2df,2pd)', 
    '6-31+G', '6-31+G*', '6-31+G(d)', '6-31+G**', '6-31+G(d,p)', 
    '6-31+G(2d)', '6-31+G(2df)', '6-31+G(2d,p)', '6-31+G(2d,2p)', '6-31+G(2df,2p)', 
    '6-31+G(2df,2pd)', '6-31++G', '6-31++G*', '6-31++G(d)', '6-31++G**', 
    '6-31++G(d,p)', '6-31++G(2d)', '6-31++G(2df)', '6-31++G(2d,p)', '6-31++G(2d,2p)', 
    '6-31++G(2df,2p)', '6-31++G(2df,2pd)', '6-311G', '6-311G*', '6-311G(d)', 
    '6-311G**', '6-311G(d,p)', '6-311G(2d)', '6-311G(2df)', '6-311G(2d,p)', 
    '6-311G(2d,2p)', '6-311G(2df,2p)', '6-311G(2df,2pd)', '6-311G(3df)', '6-311G(3df,3pd)', 
    '6-311+G', '6-311+G*', '6-311+G(d)', '6-311+G**', '6-311+G(d,p)', 
    '6-311+G(2d)', '6-311+G(2df)', '6-311+G(2d,p)', '6-311+G(2d,2p)', '6-311+G(2df,2p)', 
    '6-311+G(2df,2pd)', '6-311+G(3df)', '6-311+G(3df,3pd)', '6-311++G', '6-311++G*', 
    '6-311++G(d)', '6-311++G**', '6-311++G(d,p)', '6-311++G(2d)', '6-311++G(2df)', 
    '6-311++G(2d,p)', '6-311++G(2d,2p)', '6-311++G(2df,2p)', '6-311++G(2df,2pd)', '6-311++G(3df)', 
    '6-311++G(3df,3pd)', 'def2-SVP', 'def2-SVPD', 'def2-SV(P)', 'def2-TZVP', 
    'def2-TZVPD', 'def2-TZVP(-f)', 'def2-TZVPP', 'def2-TZVPPD', 'def2-QZVPP', 
    'def2-QZVPPD', 'SV(P)', 'old-SV(P)', 'SV', 'SVP', 
    'old-SV', 'old-SVP', 'TZV', 'old-TZV', 'TZV(P)', 
    'old-TZV(P)', 'TZV', 'TZVP', 'TZVPP', 'old-TZV', 
    'old-TZVP', 'old-TZVPP', 'QZVP', 'QZVPP', 'old-QZVP', 
    'old-QZVPP', 'ma-def2-SVP', 'ma-def2-SV(P)', 'ma-def2-TZVP', 'ma-def2-TZVP(-f)', 
    'ma-def2-TZVPP', 'ma-def2-QZVPP', 'DKH-SVP', 'ZORA-SVP', 'DKH-def2-SVP', 
    'ZORA-def2-SVP', 'ma-DKH-SVP', 'ma-ZORA-SVP', 'ma-DKH-def2-SVP', 'ma-ZORA-def2-SVP', 
    'ma-DKH-SV(P)', 'ma-ZORA-SV(P)', 'ma-DKH-def2-SV(P)', 'ma-ZORA-def2-SV(P)', 'ma-DKH-TZVP', 
    'ma-ZORA-TZVP', 'ma-DKH-def2-TZVP', 'ma-ZORA-def2-TZVP', 'ma-DKH-TZVP(-f)', 'ma-ZORA-TZVP(-f)', 
    'ma-DKH-def2-TZVP(-f)', 'ma-ZORA-def2-TZVP(-f)', 'SARC-DKH-SVP', 'SARC-ZORA-SVP', 'SARC-DKH-TZVP', 
    'SARC-DKH-TZVPP', 'SARC-ZORA-TZVP', 'SARC-ZORA-TZVPP', 'SARC-ZORA-TZVPP', 'SARC2-DKH-QZV', 
    'SARC2-DKH-QZVP', 'SARC2-ZORA-QZV', 'SARC2-ZORA-QZVP', 'pc-1', 'pc-2', 
    'pc-3', 'pc-4', 'aug-pc-1', 'aug-pc-2', 'aug-pc-3', 
    'aug-pc-4', 'pcseg-1', 'pcseg-2', 'pcseg-3', 'pcseg-4', 
    'aug-pcseg-1', 'aug-pcseg-2', 'aug-pcseg-3', 'aug-pcseg-4', 'pcSseg-1', 
    'pcSseg-2', 'pcSseg-3', 'pcSseg-4', 'aug-pcSseg-1', 'aug-pcSseg-2', 
    'aug-pcSseg-3', 'aug-pcSseg-4', 'pcJ-1', 'pcJ-2', 'pcJ-3', 
    'pcJ-4', 'aug-pcJ-1', 'aug-pcJ-2', 'aug-pcJ-3', 'aug-pcJ-4', 
    'Sapporo-DZP-2012', 'Sapporo-TZP-2012', 'Sapporo-QZP-2012', 'Sapporo-DKH3-DZP-2012', 'Sapporo-DKH3-TZP-2012', 
    'Sapporo-DKH3-QZP-2012', 'cc-pVDZ', 'cc-pVTZ', 'cc-pVQZ', 'cc-pV5Z', 
    'cc-pV6Z', 'cc-pCVDZ', 'cc-pCVTZ', 'cc-pCVQZ', 'cc-pCV5Z', 
    'cc-pCV6Z', 'cc-pwVDZ', 'cc-pwVTZ', 'cc-pwVQZ', 'cc-pwV5Z', 
    'cc-pwCVDZ', 'cc-pwCVTZ', 'cc-pwCVQZ', 'cc-pwCV5Z', 'cc-pVD(+d)Z', 
    'cc-pVT(+d)Z', 'cc-pVQ(+d)Z', 'cc-pV5(+d)Z', 'aug-cc-pVDZ', 'aug-cc-pVTZ', 
    'aug-cc-pVQZ', 'aug-cc-pV5Z', 'aug-cc-pV6Z', 'aug-cc-pCVDZ', 'aug-cc-pCVTZ', 
    'aug-cc-pCVQZ', 'aug-cc-pCV5Z', 'aug-cc-pCV6Z', 'aug-cc-pwVDZ', 'aug-cc-pwVTZ', 
    'aug-cc-pwVQZ', 'aug-cc-pwV5Z', 'aug-cc-pwCVDZ', 'aug-cc-pwCVTZ', 'aug-cc-pwCVQZ', 
    'aug-cc-pwCV5Z', 'cc-pVDZ-DK', 'cc-pVTZ-DK', 'cc-pVQZ-DK', 'cc-pV5Z-DK', 
    'cc-pwCVDZ-DK', 'cc-pwCVTZ-DK', 'cc-pwCVQZ-DK', 'cc-pwCV5Z-DK', 'aug-cc-pVDZ-DK', 
    'aug-cc-pVTZ-DK', 'aug-cc-pVQZ-DK', 'aug-cc-pV5Z-DK', 'aug-cc-pwCVDZ-DK', 'aug-cc-pwCVTZ-DK', 
    'aug-cc-pwCVQZ-DK', 'aug-cc-pwCV5Z-DK', 'cc-pVDZ-PP', 'cc-pVTZ-PP', 'cc-pVQZ-PP', 
    'cc-pV5Z-PP', 'cc-pwCVDZ-PP', 'cc-pwCVTZ-PP', 'cc-pwCVQZ-PP', 'cc-pwCV5Z-PP', 
    'aug-cc-pVDZ-PP', 'aug-cc-pVTZ-PP', 'aug-cc-pVQZ-PP', 'aug-cc-pV5Z-PP', 'aug-cc-pwCVDZ-PP', 
    'aug-cc-pwCVTZ-PP', 'aug-cc-pwCVQZ-PP', 'aug-cc-pwCV5Z-PP', 'cc-pVDZ-F12-OptRI', 'cc-pVTZ-F12-OptRI', 
    'cc-pVQZ-F12-OptRI', 'cc-pVDZ-PP-F12-OptRI', 'cc-pVTZ-PP-F12-OptRI', 'cc-pVQZ-PP-F12-OptRI', 'cc-pCVDZ-F12-OptRI', 
    'cc-pCVTZ-F12-OptRI', 'cc-pCVQZ-F12-OptRI', 'cc-pCVDZ-PP-F12-OptRI', 'cc-pCVTZ-PP-F12-OptRI', 'cc-pCVQZ-PP-F12-OptRI', 
    'cc-pVDZ-F12-CABS', 'cc-pVTZ-F12-CABS', 'cc-pVQZ-F12-CABS', 'aug-cc-pVDZ-F12-OptRI', 'aug-cc-pVTZ-F12-OptRI', 
    'aug-cc-pVQZ-F12-OptRI', 'aug-cc-pV5Z-F12-OptRI', 'aug-cc-pVDZ-PP-F12-OptRI', 'aug-cc-pVTZ-PP-F12-OptRI', 'aug-cc-pVQZ-PP-F12-OptRI', 
    'aug-cc-pV5Z-PP-F12-OptRI', 'aug-cc-pwCVDZ-F12-OptRI', 'aug-cc-pwCVTZ-F12-OptRI', 'aug-cc-pwCVQZ-F12-OptRI', 'aug-cc-pwCV5Z-F12-OptRI', 
    'aug-cc-pwCVDZ-PP-F12-OptRI', 'aug-cc-pwCVTZ-PP-F12-OptRI', 'aug-cc-pwCVQZ-PP-F12-OptRI', 'aug-cc-pwCV5Z-PP-F12-OptRI', 'ano-pVDZ', 
    'ano-pVTZ', 'ano-pVQZ', 'ano-pV5Z', 'aug-ano-pVDZ', 'aug-ano-pVTZ', 
    'aug-ano-pVQZ', 'aug-ano-pV5Z', 'saug-ano-pVDZ', 'saug-ano-pVTZ', 'saug-ano-pVQZ', 
    'saug-ano-pV5Z', 'ANO-RCC-DZP', 'ANO-RCC-TZP', 'ANO-RCC-QZP', 'ANO-RCC-FULL', 
    'D95', 'D95p', 'MINI', 'MINIS', 'MIDI', 
    'MINIX', 'Wachters+f', 'Partidge-1', 'Partidge-2', 'Partidge-3', 
    'Partidge-4', 'LANL2DZ', 'LANL2TZ', 'LANL2TZ(f)', 'LANL08', 
    'LANL08(f)', 'EPR-II', 'EPR-III', 'IGLO-II', 'IGLO-III', 
    'aug-cc-pVTZ-J', 'Def2/J', 'SARC/J', 'Def2/JK', 'Def2/JKsmall', 
    'cc-pVDZ/JK', 'cc-pVTZ/JK', 'cc-pVQZ/JK', 'cc-pV5Z/JK', 'aug-cc-pVDZ/JK', 
    'aug-cc-pVTZ/JK', 'aug-cc-pVQZ/JK', 'aug-cc-pV5Z/JK', 'def2-SVP/C', 'def2-TZVP/C', 
    'def2-TZVPP/C', 'def2-QZVPP/C', 'cc-pVDZ/C', 'cc-pVTZ/C', 'cc-pVQZ/C', 
    'cc-pV5Z/C', 'cc-pV6Z/C', 'aug-cc-pVDZ/C', 'aug-cc-pVTZ/C', 'aug-cc-pVQZ/C', 
    'aug-cc-pV5Z/C', 'aug-cc-pV6Z', 'aug-cc-pVDZ/C', 'aug-cc-pVTZ/C', 'aug-cc-pVQZ/C', 'aug-cc-pV5Z/C', 
   'aug-cc-pV6Z/C', 'cc-pwCVDZ/C', 'cc-pwCVTZ/C', 'cc-pwCVQZ/C', 
   'cc-pwCV5Z/C', 'aug-cc-pwCVDZ/C', 'aug-cc-pwCVTZ/C', 'aug-cc-pwCVQZ/C', 
   'aug-cc-pwCV5Z/C', 'cc-pVDZ-PP/C', 'cc-pVTZ-PP/C', 'cc-pVQZ-PP/C', 
   'aug-cc-pVDZ-PP/C', 'aug-cc-pVTZ-PP/C', 'aug-cc-pVQZ-PP/C', 'cc-pwCVDZ-PP/C', 
   'cc-pwCVTZ-PP/C', 'cc-pwCVQZ-PP/C', 'aug-cc-pwCVDZ-PP/C', 'aug-cc-pwCVTZ-PP/C', 
   'aug-cc-pwCVQZ-PP/C', 'cc-pVDZ-F12-MP2fit', 'cc-pVTZ-F12-MP2fit', 'cc-pVQZ-F12-MP2fit', 
   'cc-pCVDZ-F12-MP2fit', 'cc-pCVTZ-F12-MP2fit', 'cc-pCVQZ-F12-MP2fit', 'cc-pVDZ-PP-F12-MP2fit', 
   'cc-pVTZ-PP-F12-MP2fit', 'cc-pVQZ-PP-F12-MP2fit', 'apr-cc-pV(Q+d)Z', 'may-cc-pV(T+d)Z', 
   'may-cc-pV(Q+d)Z', 'jun-cc-pv(D+d)Z', 'jun-cc-pv(T+d)Z', 'jun-cc-pv(Q+d)Z', 
   'jul-cc-pv(D+d)Z', 'jul-cc-pv(T+d)Z', 'jul-cc-pv(Q+d)Z', 'maug-cc-pv(D+d)Z', 
   'maug-cc-pv(T+d)Z', 'maug-cc-pv(Q+d)Z'
]


# In[29]:


# Define a function 
def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate input files from XYZ files.')
    parser.add_argument('--program', required=True, help='Specify ORCA or Gaussian')
    parser.add_argument('--memory', required=True, help='Number of gigabytes of memory to use (e.g., 32GB, 64GB)')
    parser.add_argument('--proc', required=True, help='Number of processors to use (e.g., 16, 32)')
    parser.add_argument('--charge_mult', required=True, help='Charge and multiplicity (e.g., 0, 1)')
    parser.add_argument('--title', required=True, help='Title for the calculation')
    parser.add_argument('--func', required=True, help='Electronic structure method (e.g., DFT functional like PBE0)')
    parser.add_argument('--basis', required=True, help='Basis set (e.g., def2-TZVP or 6-311+G(d,p))')
    parser.add_argument('--solvent', default='', help='Solvent model (e.g., scrf=(smd), cpcm)')
    parser.add_argument('--keys', default='', help='Additional keywords (e.g., opt, FREQ, D3)')
    return parser.parse_args()


# In[30]:


def parse_xyz_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    atoms = []
    for line in lines[2:]:  # Skip the first two lines (number of atoms and comment)
        parts = line.strip().split()
        if len(parts) == 4:  # Ensure we have an atom symbol and 3 coordinates
            atom_symbol = parts[0]
            coordinates = [coord.strip() for coord in parts[1:]]
            formatted_line = f"{atom_symbol:<2} {coordinates[0]:>14} {coordinates[1]:>14} {coordinates[2]:>14}\n"
            atoms.append(formatted_line)

    print("Atoms collected: ")
    print(''.join(atoms))  # Print all atoms together

    return atoms


# In[1]:


def gen_inp(atoms, args, file):
    
    # Use the values from the args object
    orca_gaussian = args.program.upper()
    memory = args.memory
    proc = args.proc
    title = args.title
    charge_mult = args.charge_mult
    func = args.func
    basis = args.basis
    solvent = args.solvent
    keys = args.keys
    
    # prompt the user to specify whether he/she is using Gaussian
    if orca_gaussian == "GAUSSIAN":
    
        # check that the functional has proper syntax
        if func.upper() in [f.upper() for f in valid_gaussian_functionals]:
            print(f"Using {func} as the electronic structure method.")
            # Proceed with the rest of your code

            # Combine the contents of user inputs to create Gaussian input                    
            combined_content = f"%mem={memory}\n" + f"%nprocshared={proc}\n" + f"# {func}/{basis} " + f"{solvent} " + f"{keys}\n" + f"{title}\n" + f"{charge_mult}" + "".join(atoms) + "\n\n"
            # Create the output file name
            base_name = os.path.splitext(file)[0]
            output_file = base_name + ".inp"

            # Write the combined content to the output file
            with open(output_file, "w") as f:
                f.writelines(combined_content)

            print(f"Gaussian input file {output_file} created successfully.")

        else:
            print(f"Invalid input: {func}. Please enter a valid electronic structure method for Gaussian.")
            # Handle the invalid input case

    elif orca_gaussian.upper() == "ORCA":
        # Code to handle ORCA input

        # check that the functional has proper syntax
        if func.upper() in [f.upper() for f in valid_orca_functionals]:
            print(f"Using {func} as the electronic structure method.")
            # Proceed with the rest of your code

            # Combine the contents of user inputs to create ORCA input                    
            combined_content = f"!{func} {basis} " + f"{solvent} " + f"{keys}\n" + f"%maxcore {memory}\n\n" + f"%pal\n nprocs {proc}\nend\n\n" + f"*xyz {charge_mult}\n" + "\n".join(atoms) + "\n*\n"
            # Create the output file name
            base_name = os.path.splitext(file)[0]
            output_file = base_name + ".inp"

            # Write the combined content to the output file
            with open(output_file, "w") as f:
                f.writelines(combined_content)

            print(f"ORCA input file {output_file} created successfully. Allocating {memory} memory per core.")

    else:
        print(f"Invalid input: {func}. Please enter a valid electronic structure method for ORCA.")
        # Handle the invalid input case


# In[32]:


def main():
    args = parse_arguments()

    xyz_files = glob.glob('*.xyz')
    for xyz_file in xyz_files:
        atoms = parse_xyz_file(xyz_file)
        gen_inp(atoms, args, xyz_file)

if __name__ == '__main__':
    main()

