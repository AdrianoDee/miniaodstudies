Last login: Thu Apr 22 08:20:14 on ttys002
ssh 
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) MBP-di-Adriano:~ adrianodif$ ssh lxplus
Warning: Permanently added the ECDSA host key for IP address '137.138.31.64' to the list of known hosts.
Password: 
* ********************************************************************
* Welcome to lxplus734.cern.ch, CentOS, 7.9.2009
* Archive of news is available in /etc/motd-archive
* Reminder: you have agreed to the CERN
*   computing rules, in particular OC5. CERN implements
*   the measures necessary to ensure compliance.
*   https://cern.ch/ComputingRules
* Puppet environment: production, Roger state: production
* Foreman hostgroup: lxplus/nodes/login
* Availability zone: cern-geneva-b
* LXPLUS Public Login Service - http://lxplusdoc.web.cern.ch/
* A C8 based lxplus8.cern.ch is now available
* Please read LXPLUS Privacy Notice in http://cern.ch/go/TpV7
* Users of "screen" on lxplus be aware of http://cern.ch/go/6F6j
* lxplus-cloud closing 31st Mar 2021 - http://cern.ch/go/GN8g
* ********************************************************************
[adiflori@lxplus734 adiflori]$ eos
# ---------------------------------------------------------------------------
# EOS  Copyright (C) 2011-2020 CERN/Switzerland
# This program comes with ABSOLUTELY NO WARRANTY; for details type `license'.
# This is free software, and you are welcome to redistribute it 
# under certain conditions; type `license' for details.
# ---------------------------------------------------------------------------
EOS_INSTANCE=eoscms
EOS_SERVER_VERSION=4.8.39 EOS_SERVER_RELEASE=1
EOS_CLIENT_VERSION=4.8.28 EOS_CLIENT_RELEASE=1
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/bu/> cd ..
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/> mkdir xi
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/> cd xi^C
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/> ls -tlrh
drwxr-xr-+   1 adiflori zh           561.21 G Apr 20 13:46 bu
drwxr-xr-+   1 adiflori zh                  0 Apr 22 08:35 xi
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/> cd xi/
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/xi/> ls -tlrh
drwxr-sr-+   1 adiflori zh           196.42 M Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200229
drwxr-sr-+   1 adiflori zh           147.47 M Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200526
drwxr-sr-+   1 adiflori zh                  0 Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200733
drwxr-sr-+   1 adiflori zh           109.76 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200902
drwxr-sr-+   1 adiflori zh            71.98 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_201023
drwxr-sr-+   1 adiflori zh            20.19 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_204351
drwxr-sr-+   1 adiflori zh           103.63 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133146
drwxr-sr-+   1 adiflori zh            42.23 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133157
drwxr-sr-+   1 adiflori zh            57.67 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133213
drwxr-sr-+   1 adiflori zh            15.86 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152952
drwxr-sr-+   1 adiflori zh             4.19 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152956
drwxr-sr-+   1 adiflori zh            40.01 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213105
drwxr-sr-+   1 adiflori zh                  0 Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213252
drwxr-sr-+   1 adiflori zh            69.19 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213257
drwxr-sr-+   1 adiflori zh            47.76 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213302
drwxr-sr-+   1 adiflori zh                  0 Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213307
drwxr-sr-+   1 adiflori zh            25.09 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075433
drwxr-sr-+   1 adiflori zh             8.08 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075434
drwxr-sr-+   1 adiflori zh            71.61 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075444
drwxr-sr-+   1 adiflori zh            48.63 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125941
drwxr-sr-+   1 adiflori zh            26.79 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125946
drwxr-sr-+   1 adiflori zh            48.78 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125951
drwxr-sr-+   1 adiflori zh            18.71 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125956
drwxr-sr-+   1 adiflori zh                  0 Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130003
drwxr-sr-+   1 adiflori zh            86.16 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130008
drwxr-sr-+   1 adiflori zh            79.70 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225359
drwxr-sr-+   1 adiflori zh            65.06 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225403
drwxr-sr-+   1 adiflori zh            72.76 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225408
drwxr-sr-+   1 adiflori zh            54.03 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225412
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/xi/> ls -tlrh
drwxr-sr-+   1 adiflori zh           284.83 M Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200229
drwxr-sr-+   1 adiflori zh           314.48 M Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200526
drwxr-sr-+   1 adiflori zh           102.61 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200733
drwxr-sr-+   1 adiflori zh           156.60 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200902
drwxr-sr-+   1 adiflori zh           171.58 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_201023
drwxr-sr-+   1 adiflori zh            45.90 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_204351
drwxr-sr-+   1 adiflori zh           225.90 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133146
drwxr-sr-+   1 adiflori zh            96.95 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133157
drwxr-sr-+   1 adiflori zh           145.92 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133213
drwxr-sr-+   1 adiflori zh            59.50 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152952
drwxr-sr-+   1 adiflori zh            92.33 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152956
drwxr-sr-+   1 adiflori zh            81.58 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213105
drwxr-sr-+   1 adiflori zh            16.54 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213252
drwxr-sr-+   1 adiflori zh           127.60 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213257
drwxr-sr-+   1 adiflori zh           115.51 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213302
drwxr-sr-+   1 adiflori zh             4.08 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213307
drwxr-sr-+   1 adiflori zh            39.31 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075433
drwxr-sr-+   1 adiflori zh            73.12 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075434
drwxr-sr-+   1 adiflori zh            79.57 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075444
drwxr-sr-+   1 adiflori zh           147.05 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125941
drwxr-sr-+   1 adiflori zh           124.13 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125946
drwxr-sr-+   1 adiflori zh            82.87 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125951
drwxr-sr-+   1 adiflori zh            51.51 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125956
drwxr-sr-+   1 adiflori zh            68.95 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130003
drwxr-sr-+   1 adiflori zh           133.40 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130008
drwxr-sr-+   1 adiflori zh            95.82 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225359
drwxr-sr-+   1 adiflori zh            97.44 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225403
drwxr-sr-+   1 adiflori zh           191.92 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225408
drwxr-sr-+   1 adiflori zh            74.76 M Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225412
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/xi/> ls -tlrh
drwxr-sr-+   1 adiflori zh             4.02 G Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200229
drwxr-sr-+   1 adiflori zh             3.03 G Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200526
drwxr-sr-+   1 adiflori zh             2.19 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200733
drwxr-sr-+   1 adiflori zh             3.31 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200902
drwxr-sr-+   1 adiflori zh             2.95 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_201023
drwxr-sr-+   1 adiflori zh             1.16 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_204351
drwxr-sr-+   1 adiflori zh             2.65 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133146
drwxr-sr-+   1 adiflori zh             2.26 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133157
drwxr-sr-+   1 adiflori zh             2.82 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133213
drwxr-sr-+   1 adiflori zh             1.38 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152952
drwxr-sr-+   1 adiflori zh             1.31 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152956
drwxr-sr-+   1 adiflori zh             1.69 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213105
drwxr-sr-+   1 adiflori zh             1.43 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213252
drwxr-sr-+   1 adiflori zh             1.49 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213257
drwxr-sr-+   1 adiflori zh             1.38 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213302
drwxr-sr-+   1 adiflori zh             1.20 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213307
drwxr-sr-+   1 adiflori zh             1.34 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075433
drwxr-sr-+   1 adiflori zh             1.33 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075434
drwxr-sr-+   1 adiflori zh             1.44 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075444
drwxr-sr-+   1 adiflori zh             1.50 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125941
drwxr-sr-+   1 adiflori zh             1.64 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125946
drwxr-sr-+   1 adiflori zh             1.31 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125951
drwxr-sr-+   1 adiflori zh             1.40 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125956
drwxr-sr-+   1 adiflori zh             1.61 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130003
drwxr-sr-+   1 adiflori zh             1.50 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130008
drwxr-sr-+   1 adiflori zh             1.40 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225359
drwxr-sr-+   1 adiflori zh             1.33 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225403
drwxr-sr-+   1 adiflori zh             1.32 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225408
drwxr-sr-+   1 adiflori zh             1.43 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225412
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/xi/> ls -tlrh
drwxr-sr-+   1 adiflori zh             4.06 G Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200229
drwxr-sr-+   1 adiflori zh             3.04 G Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200526
drwxr-sr-+   1 adiflori zh             2.20 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200733
drwxr-sr-+   1 adiflori zh             3.31 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200902
drwxr-sr-+   1 adiflori zh             2.98 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_201023
drwxr-sr-+   1 adiflori zh             1.18 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_204351
drwxr-sr-+   1 adiflori zh             2.67 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133146
drwxr-sr-+   1 adiflori zh             2.27 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133157
drwxr-sr-+   1 adiflori zh             2.82 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133213
drwxr-sr-+   1 adiflori zh             1.41 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152952
drwxr-sr-+   1 adiflori zh             1.31 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152956
drwxr-sr-+   1 adiflori zh             1.69 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213105
drwxr-sr-+   1 adiflori zh             1.45 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213252
drwxr-sr-+   1 adiflori zh             1.51 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213257
drwxr-sr-+   1 adiflori zh             1.38 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213302
drwxr-sr-+   1 adiflori zh             1.22 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213307
drwxr-sr-+   1 adiflori zh             1.35 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075433
drwxr-sr-+   1 adiflori zh             1.33 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075434
drwxr-sr-+   1 adiflori zh             1.44 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075444
drwxr-sr-+   1 adiflori zh             1.51 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125941
drwxr-sr-+   1 adiflori zh             1.65 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125946
drwxr-sr-+   1 adiflori zh             1.32 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125951
drwxr-sr-+   1 adiflori zh             1.40 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125956
drwxr-sr-+   1 adiflori zh             1.63 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130003
drwxr-sr-+   1 adiflori zh             1.52 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130008
drwxr-sr-+   1 adiflori zh             1.42 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225359
drwxr-sr-+   1 adiflori zh             1.34 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225403
drwxr-sr-+   1 adiflori zh             1.34 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225408
drwxr-sr-+   1 adiflori zh             1.45 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225412
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/xi/> ls -tlrh
drwxr-sr-+   1 adiflori zh             4.06 G Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200229
drwxr-sr-+   1 adiflori zh             3.04 G Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200526
drwxr-sr-+   1 adiflori zh             2.20 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200733
drwxr-sr-+   1 adiflori zh             3.31 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200902
drwxr-sr-+   1 adiflori zh             2.98 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_201023
drwxr-sr-+   1 adiflori zh             1.18 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_204351
drwxr-sr-+   1 adiflori zh             2.67 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133146
drwxr-sr-+   1 adiflori zh             2.27 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133157
drwxr-sr-+   1 adiflori zh             2.82 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133213
drwxr-sr-+   1 adiflori zh             1.41 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152952
drwxr-sr-+   1 adiflori zh             1.31 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152956
drwxr-sr-+   1 adiflori zh             1.69 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213105
drwxr-sr-+   1 adiflori zh             1.45 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213252
drwxr-sr-+   1 adiflori zh             1.51 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213257
drwxr-sr-+   1 adiflori zh             1.38 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213302
drwxr-sr-+   1 adiflori zh             1.22 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213307
drwxr-sr-+   1 adiflori zh             1.35 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075433
drwxr-sr-+   1 adiflori zh             1.33 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075434
drwxr-sr-+   1 adiflori zh             1.44 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075444
drwxr-sr-+   1 adiflori zh             1.51 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125941
drwxr-sr-+   1 adiflori zh             1.65 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125946
drwxr-sr-+   1 adiflori zh             1.32 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125951
drwxr-sr-+   1 adiflori zh             1.40 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125956
drwxr-sr-+   1 adiflori zh             1.63 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130003
drwxr-sr-+   1 adiflori zh             1.52 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130008
drwxr-sr-+   1 adiflori zh             1.42 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225359
drwxr-sr-+   1 adiflori zh             1.34 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225403
drwxr-sr-+   1 adiflori zh             1.34 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225408
drwxr-sr-+   1 adiflori zh             1.45 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225412
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/xi/> ls -tlrh
drwxr-sr-+   1 adiflori zh             9.30 G Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200229
drwxr-sr-+   1 adiflori zh             6.75 G Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200526
drwxr-sr-+   1 adiflori zh             4.56 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200733
drwxr-sr-+   1 adiflori zh             6.87 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200902
drwxr-sr-+   1 adiflori zh             6.73 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_201023
drwxr-sr-+   1 adiflori zh             2.51 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_204351
drwxr-sr-+   1 adiflori zh             5.66 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133146
drwxr-sr-+   1 adiflori zh             5.52 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133157
drwxr-sr-+   1 adiflori zh             6.33 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133213
drwxr-sr-+   1 adiflori zh             2.96 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152952
drwxr-sr-+   1 adiflori zh             2.72 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152956
drwxr-sr-+   1 adiflori zh             3.26 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213105
drwxr-sr-+   1 adiflori zh             2.85 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213252
drwxr-sr-+   1 adiflori zh             3.02 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213257
drwxr-sr-+   1 adiflori zh             2.89 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213302
drwxr-sr-+   1 adiflori zh             2.92 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213307
drwxr-sr-+   1 adiflori zh             2.62 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075433
drwxr-sr-+   1 adiflori zh             2.86 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075434
drwxr-sr-+   1 adiflori zh             2.88 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075444
drwxr-sr-+   1 adiflori zh             2.64 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125941
drwxr-sr-+   1 adiflori zh             3.01 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125946
drwxr-sr-+   1 adiflori zh             2.82 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125951
drwxr-sr-+   1 adiflori zh             2.82 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125956
drwxr-sr-+   1 adiflori zh             3.26 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130003
drwxr-sr-+   1 adiflori zh             3.00 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130008
drwxr-sr-+   1 adiflori zh             2.90 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225359
drwxr-sr-+   1 adiflori zh             2.77 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225403
drwxr-sr-+   1 adiflori zh             3.27 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225408
drwxr-sr-+   1 adiflori zh             2.87 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225412
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/xi/> ls -tlrh
drwxr-sr-+   1 adiflori zh             9.30 G Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200229
drwxr-sr-+   1 adiflori zh             6.75 G Apr 22 08:51 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200526
drwxr-sr-+   1 adiflori zh             4.56 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200733
drwxr-sr-+   1 adiflori zh             6.87 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200902
drwxr-sr-+   1 adiflori zh             6.73 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_201023
drwxr-sr-+   1 adiflori zh             2.51 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_204351
drwxr-sr-+   1 adiflori zh             5.66 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133146
drwxr-sr-+   1 adiflori zh             5.52 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133157
drwxr-sr-+   1 adiflori zh             6.33 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210412_133213
drwxr-sr-+   1 adiflori zh             2.96 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152952
drwxr-sr-+   1 adiflori zh             2.72 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_152956
drwxr-sr-+   1 adiflori zh             3.26 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213105
drwxr-sr-+   1 adiflori zh             2.85 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213252
drwxr-sr-+   1 adiflori zh             3.02 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213257
drwxr-sr-+   1 adiflori zh             2.89 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213302
drwxr-sr-+   1 adiflori zh             2.92 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210414_213307
drwxr-sr-+   1 adiflori zh             2.62 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075433
drwxr-sr-+   1 adiflori zh             2.86 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075434
drwxr-sr-+   1 adiflori zh             2.88 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210415_075444
drwxr-sr-+   1 adiflori zh             2.64 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125941
drwxr-sr-+   1 adiflori zh             3.01 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125946
drwxr-sr-+   1 adiflori zh             2.82 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125951
drwxr-sr-+   1 adiflori zh             2.82 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_125956
drwxr-sr-+   1 adiflori zh             3.26 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130003
drwxr-sr-+   1 adiflori zh             3.00 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210416_130008
drwxr-sr-+   1 adiflori zh             2.90 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225359
drwxr-sr-+   1 adiflori zh             2.77 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225403
drwxr-sr-+   1 adiflori zh             3.27 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225408
drwxr-sr-+   1 adiflori zh             2.87 G Apr 22 08:52 0000_good_crab_xi_PUFlat55To75_run3_failures_20210418_225412
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/xi/> ls -tlrhls ^C
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/xi/> ls 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200229
good
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/xi/> ls 0000_good_crab_xi_PUFlat55To75_run3_failures_20210411_200229/good
miniaod_v3_2021_align_112.root
miniaod_v3_2021_align_116.root
miniaod_v3_2021_align_14.root
miniaod_v3_2021_align_32.root
miniaod_v3_2021_align_33.root
miniaod_v3_2021_align_34.root
miniaod_v3_2021_align_41.root
miniaod_v3_2021_align_49.root
miniaod_v3_2021_align_52.root
miniaod_v3_2021_align_55.root
miniaod_v3_2021_align_56.root
miniaod_v3_2021_align_62.root
miniaod_v3_2021_align_64.root
miniaod_v3_2021_align_65.root
miniaod_v3_2021_align_66.root
miniaod_v3_2021_align_71.root
miniaod_v3_2021_align_84.root
miniaod_v3_2021_align_97.root
miniaod_v3_2021_baseline_110.root
miniaod_v3_2021_baseline_112.root
miniaod_v3_2021_baseline_116.root
miniaod_v3_2021_baseline_117.root
miniaod_v3_2021_baseline_14.root
miniaod_v3_2021_baseline_17.root
miniaod_v3_2021_baseline_25.root
miniaod_v3_2021_baseline_32.root
miniaod_v3_2021_baseline_33.root
miniaod_v3_2021_baseline_41.root
miniaod_v3_2021_baseline_49.root
miniaod_v3_2021_baseline_52.root
miniaod_v3_2021_baseline_55.root
miniaod_v3_2021_baseline_56.root
miniaod_v3_2021_baseline_62.root
miniaod_v3_2021_baseline_63.root
miniaod_v3_2021_baseline_66.root
miniaod_v3_2021_baseline_71.root
miniaod_v3_2021_baseline_77.root
miniaod_v3_2021_baseline_94.root
miniaod_v3_2021_baseline_97.root
miniaod_v3_2021_d_110.root
miniaod_v3_2021_d_112.root
miniaod_v3_2021_d_117.root
miniaod_v3_2021_d_17.root
miniaod_v3_2021_d_32.root
miniaod_v3_2021_d_33.root
miniaod_v3_2021_d_34.root
miniaod_v3_2021_d_38.root
miniaod_v3_2021_d_49.root
miniaod_v3_2021_d_55.root
miniaod_v3_2021_d_56.root
miniaod_v3_2021_d_62.root
miniaod_v3_2021_d_64.root
miniaod_v3_2021_d_65.root
miniaod_v3_2021_d_66.root
miniaod_v3_2021_d_71.root
miniaod_v3_2021_d_77.root
miniaod_v3_2021_d_84.root
miniaod_v3_2021_d_94.root
miniaod_v3_2021_d_97.root
miniaod_v3_2024_baseline_110.root
miniaod_v3_2024_baseline_112.root
miniaod_v3_2024_baseline_116.root
miniaod_v3_2024_baseline_117.root
miniaod_v3_2024_baseline_32.root
miniaod_v3_2024_baseline_33.root
miniaod_v3_2024_baseline_34.root
miniaod_v3_2024_baseline_41.root
miniaod_v3_2024_baseline_49.root
miniaod_v3_2024_baseline_52.root
miniaod_v3_2024_baseline_62.root
miniaod_v3_2024_baseline_63.root
miniaod_v3_2024_baseline_64.root
miniaod_v3_2024_baseline_66.root
miniaod_v3_2024_baseline_77.root
miniaod_v3_2024_baseline_94.root
miniaod_v3_2024_baseline_97.root
miniaod_v3_2024_d_117.root
miniaod_v3_2024_d_14.root
miniaod_v3_2024_d_17.root
miniaod_v3_2024_d_33.root
miniaod_v3_2024_d_34.root
miniaod_v3_2024_d_38.root
miniaod_v3_2024_d_41.root
miniaod_v3_2024_d_49.root
miniaod_v3_2024_d_52.root
miniaod_v3_2024_d_56.root
miniaod_v3_2024_d_62.root
miniaod_v3_2024_d_63.root
miniaod_v3_2024_d_65.root
miniaod_v3_2024_d_66.root
miniaod_v3_2024_d_71.root
miniaod_v3_2024_d_77.root
miniaod_v3_2024_d_84.root
miniaod_v3_2024_d_97.root
miniaod_v4_2021_align_110.root
miniaod_v4_2021_align_112.root
miniaod_v4_2021_align_117.root
miniaod_v4_2021_align_17.root
miniaod_v4_2021_align_32.root
miniaod_v4_2021_align_34.root
miniaod_v4_2021_align_38.root
miniaod_v4_2021_align_41.root
miniaod_v4_2021_align_49.root
miniaod_v4_2021_align_63.root
miniaod_v4_2021_align_64.root
miniaod_v4_2021_align_65.root
miniaod_v4_2021_align_71.root
miniaod_v4_2021_align_77.root
miniaod_v4_2021_align_84.root
miniaod_v4_2021_baseline_110.root
miniaod_v4_2021_baseline_116.root
miniaod_v4_2021_baseline_117.root
miniaod_v4_2021_baseline_14.root
miniaod_v4_2021_baseline_41.root
miniaod_v4_2021_baseline_49.root
miniaod_v4_2021_baseline_55.root
miniaod_v4_2021_baseline_56.root
miniaod_v4_2021_baseline_64.root
miniaod_v4_2021_baseline_65.root
miniaod_v4_2021_baseline_66.root
miniaod_v4_2021_baseline_77.root
miniaod_v4_2021_baseline_84.root
miniaod_v4_2021_baseline_94.root
miniaod_v4_2021_baseline_97.root
miniaod_v4_2021_d_110.root
miniaod_v4_2021_d_112.root
miniaod_v4_2021_d_116.root
miniaod_v4_2021_d_25.root
miniaod_v4_2021_d_33.root
miniaod_v4_2021_d_41.root
miniaod_v4_2021_d_49.root
miniaod_v4_2021_d_52.root
miniaod_v4_2021_d_55.root
miniaod_v4_2021_d_56.root
miniaod_v4_2021_d_62.root
miniaod_v4_2021_d_65.root
miniaod_v4_2021_d_66.root
miniaod_v4_2021_d_71.root
miniaod_v4_2021_d_84.root
miniaod_v4_2024_baseline_110.root
miniaod_v4_2024_baseline_112.root
miniaod_v4_2024_baseline_117.root
miniaod_v4_2024_baseline_17.root
miniaod_v4_2024_baseline_32.root
miniaod_v4_2024_baseline_33.root
miniaod_v4_2024_baseline_34.root
miniaod_v4_2024_baseline_38.root
miniaod_v4_2024_baseline_41.root
miniaod_v4_2024_baseline_55.root
miniaod_v4_2024_baseline_56.root
miniaod_v4_2024_baseline_64.root
miniaod_v4_2024_baseline_71.root
miniaod_v4_2024_baseline_77.root
miniaod_v4_2024_baseline_84.root
miniaod_v4_2024_baseline_94.root
miniaod_v4_2024_baseline_97.root
miniaod_v4_2024_d_116.root
miniaod_v4_2024_d_117.root
miniaod_v4_2024_d_14.root
miniaod_v4_2024_d_32.root
miniaod_v4_2024_d_33.root
miniaod_v4_2024_d_38.root
miniaod_v4_2024_d_49.root
miniaod_v4_2024_d_52.root
miniaod_v4_2024_d_62.root
miniaod_v4_2024_d_63.root
miniaod_v4_2024_d_64.root
miniaod_v4_2024_d_65.root
miniaod_v4_2024_d_66.root
miniaod_v4_2024_d_71.root
miniaod_v4_2024_d_77.root
miniaod_v4_2024_d_94.root
miniaod_v4_2024_d_97.root
miniaod_vOriginal_2021_align_112.root
miniaod_vOriginal_2021_align_116.root
miniaod_vOriginal_2021_align_117.root
miniaod_vOriginal_2021_align_14.root
miniaod_vOriginal_2021_align_17.root
miniaod_vOriginal_2021_align_32.root
miniaod_vOriginal_2021_align_33.root
miniaod_vOriginal_2021_align_34.root
miniaod_vOriginal_2021_align_38.root
miniaod_vOriginal_2021_align_41.root
miniaod_vOriginal_2021_align_52.root
miniaod_vOriginal_2021_align_55.root
miniaod_vOriginal_2021_align_56.root
miniaod_vOriginal_2021_align_63.root
miniaod_vOriginal_2021_align_64.root
miniaod_vOriginal_2021_align_65.root
miniaod_vOriginal_2021_align_66.root
miniaod_vOriginal_2021_align_71.root
miniaod_vOriginal_2021_align_77.root
miniaod_vOriginal_2021_align_84.root
miniaod_vOriginal_2021_align_97.root
miniaod_vOriginal_2021_baseline_110.root
miniaod_vOriginal_2021_baseline_112.root
miniaod_vOriginal_2021_baseline_117.root
miniaod_vOriginal_2021_baseline_14.root
miniaod_vOriginal_2021_baseline_17.root
miniaod_vOriginal_2021_baseline_32.root
miniaod_vOriginal_2021_baseline_33.root
miniaod_vOriginal_2021_baseline_41.root
miniaod_vOriginal_2021_baseline_52.root
miniaod_vOriginal_2021_baseline_56.root
miniaod_vOriginal_2021_baseline_62.root
miniaod_vOriginal_2021_baseline_64.root
miniaod_vOriginal_2021_baseline_65.root
miniaod_vOriginal_2021_baseline_66.root
miniaod_vOriginal_2021_baseline_77.root
miniaod_vOriginal_2021_baseline_84.root
miniaod_vOriginal_2021_baseline_97.root
miniaod_vOriginal_2021_d_110.root
miniaod_vOriginal_2021_d_112.root
miniaod_vOriginal_2021_d_116.root
miniaod_vOriginal_2021_d_117.root
miniaod_vOriginal_2021_d_14.root
miniaod_vOriginal_2021_d_25.root
miniaod_vOriginal_2021_d_32.root
miniaod_vOriginal_2021_d_34.root
miniaod_vOriginal_2021_d_38.root
miniaod_vOriginal_2021_d_41.root
miniaod_vOriginal_2021_d_55.root
miniaod_vOriginal_2021_d_62.root
miniaod_vOriginal_2021_d_63.root
miniaod_vOriginal_2021_d_64.root
miniaod_vOriginal_2021_d_65.root
miniaod_vOriginal_2021_d_66.root
miniaod_vOriginal_2021_d_71.root
miniaod_vOriginal_2021_d_77.root
miniaod_vOriginal_2021_d_84.root
miniaod_vOriginal_2021_d_94.root
miniaod_vOriginal_2021_d_97.root
miniaod_vOriginal_2024_baseline_112.root
miniaod_vOriginal_2024_baseline_117.root
miniaod_vOriginal_2024_baseline_14.root
miniaod_vOriginal_2024_baseline_17.root
miniaod_vOriginal_2024_baseline_25.root
miniaod_vOriginal_2024_baseline_32.root
miniaod_vOriginal_2024_baseline_33.root
miniaod_vOriginal_2024_baseline_34.root
miniaod_vOriginal_2024_baseline_38.root
miniaod_vOriginal_2024_baseline_41.root
miniaod_vOriginal_2024_baseline_49.root
miniaod_vOriginal_2024_baseline_52.root
miniaod_vOriginal_2024_baseline_55.root
miniaod_vOriginal_2024_baseline_56.root
miniaod_vOriginal_2024_baseline_62.root
miniaod_vOriginal_2024_baseline_63.root
miniaod_vOriginal_2024_baseline_64.root
miniaod_vOriginal_2024_baseline_65.root
miniaod_vOriginal_2024_baseline_66.root
miniaod_vOriginal_2024_baseline_71.root
miniaod_vOriginal_2024_baseline_77.root
miniaod_vOriginal_2024_baseline_84.root
miniaod_vOriginal_2024_baseline_94.root
miniaod_vOriginal_2024_baseline_97.root
miniaod_vOriginal_2024_d_110.root
miniaod_vOriginal_2024_d_116.root
miniaod_vOriginal_2024_d_117.root
miniaod_vOriginal_2024_d_14.root
miniaod_vOriginal_2024_d_25.root
miniaod_vOriginal_2024_d_32.root
miniaod_vOriginal_2024_d_33.root
miniaod_vOriginal_2024_d_41.root
miniaod_vOriginal_2024_d_52.root
miniaod_vOriginal_2024_d_55.root
miniaod_vOriginal_2024_d_56.root
miniaod_vOriginal_2024_d_62.root
miniaod_vOriginal_2024_d_64.root
miniaod_vOriginal_2024_d_65.root
miniaod_vOriginal_2024_d_71.root
miniaod_vOriginal_2024_d_77.root
miniaod_vOriginal_2024_d_84.root
miniaod_vOriginal_2024_d_94.root
step1_110.root
step1_112.root
step1_116.root
step1_117.root
step1_14.root
step1_17.root
step1_25.root
step1_32.root
step1_33.root
step1_34.root
step1_38.root
step1_41.root
step1_49.root
step1_55.root
step1_63.root
step1_64.root
step1_65.root
step1_66.root
step1_71.root
step1_94.root
step1_97.root
step3_2021_align_aod_112.root
step3_2021_align_aod_117.root
step3_2021_align_aod_14.root
step3_2021_align_aod_17.root
step3_2021_align_aod_25.root
step3_2021_align_aod_33.root
step3_2021_align_aod_34.root
step3_2021_align_aod_38.root
step3_2021_align_aod_41.root
step3_2021_align_aod_52.root
step3_2021_align_aod_55.root
step3_2021_align_aod_56.root
step3_2021_align_aod_62.root
step3_2021_align_aod_63.root
step3_2021_align_aod_65.root
step3_2021_align_aod_94.root
step3_2021_align_aod_97.root
step3_2021_baseline_aod_116.root
step3_2021_baseline_aod_117.root
step3_2021_baseline_aod_14.root
step3_2021_baseline_aod_25.root
step3_2021_baseline_aod_32.root
step3_2021_baseline_aod_34.root
step3_2021_baseline_aod_38.root
step3_2021_baseline_aod_49.root
step3_2021_baseline_aod_52.root
step3_2021_baseline_aod_55.root
step3_2021_baseline_aod_56.root
step3_2021_baseline_aod_62.root
step3_2021_baseline_aod_63.root
step3_2021_baseline_aod_64.root
step3_2021_baseline_aod_65.root
step3_2021_baseline_aod_66.root
step3_2021_baseline_aod_71.root
step3_2021_baseline_aod_77.root
step3_2021_baseline_aod_97.root
step3_2021_d_aod_112.root
step3_2021_d_aod_14.root
step3_2021_d_aod_17.root
step3_2021_d_aod_33.root
step3_2021_d_aod_34.root
step3_2021_d_aod_41.root
step3_2021_d_aod_49.root
step3_2021_d_aod_52.root
step3_2021_d_aod_55.root
step3_2021_d_aod_56.root
step3_2021_d_aod_62.root
step3_2021_d_aod_64.root
step3_2021_d_aod_65.root
step3_2021_d_aod_66.root
step3_2021_d_aod_71.root
step3_2021_d_aod_84.root
step3_2021_d_aod_94.root
step3_2024_baseline_aod_112.root
step3_2024_baseline_aod_116.root
step3_2024_baseline_aod_117.root
step3_2024_baseline_aod_14.root
step3_2024_baseline_aod_33.root
step3_2024_baseline_aod_34.root
step3_2024_baseline_aod_41.root
step3_2024_baseline_aod_52.root
step3_2024_baseline_aod_55.root
step3_2024_baseline_aod_97.root
step3_2024_d_aod_110.root
step3_2024_d_aod_112.root
step3_2024_d_aod_117.root
step3_2024_d_aod_14.root
step3_2024_d_aod_17.root
step3_2024_d_aod_32.root
step3_2024_d_aod_34.root
step3_2024_d_aod_41.root
step3_2024_d_aod_49.root
step3_2024_d_aod_52.root
step3_2024_d_aod_55.root
step3_2024_d_aod_56.root
step3_2024_d_aod_63.root
step3_2024_d_aod_64.root
step3_2024_d_aod_65.root
step3_2024_d_aod_66.root
step3_2024_d_aod_71.root
step3_2024_d_aod_77.root
step3_2024_d_aod_84.root
step3_2024_d_aod_94.root
step3_2024_d_aod_97.root
EOS Console [root://eoscms.cern.ch] |/eos/cms/store/group/phys_tracking/run3_miniaod_new/xi/> packet_write_wait: Connection to 137.138.31.64 port 22: Broken pipe
(base) MBP-di-Adriano:~ adrianodif$ ssh 
  [Ripristinato: 25 apr 2021, 23:15:59]
Last login: Thu Apr 22 18:57:18 on console

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) MacBook-Pro-di-Adriano:~ adrianodif$ 
  [Ripristinato: 27 apr 2021, 13:15:41]
Last login: Sun Apr 25 23:20:49 on ttys006
Restored session: Mar 27 Apr 2021 10:40:47 CEST

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) MBP-di-Adriano:~ adrianodif$ ssh tesla
Last login: Mon Apr 26 17:47:06 2021 from ui03.recas.ba.infn.it
Identity added: /lustre/home/adrianodif/.ssh/id_tesla (/lustre/home/adrianodif/.ssh/id_tesla)
[adrianodif@tesla04 ~]$ screen -S jupy
[detached from 152266.jupy]
[adrianodif@tesla04 ~]$ screen -r jupy
[remote power detached from 152266.jupy]
Screen session of adrianodif 
ended.
Connection to tesla04 closed.
(base) MBP-di-Adriano:~ adrianodif$ 
  [Ripristinato: 29 apr 2021, 16:01:24]
Last login: Thu Apr 29 16:01:24 on ttys001

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) MacBook-Pro-di-Adriano:~ adrianodif$ 
  [Ripristinato: 3 mag 2021, 16:54:29]
Last login: Mon May  3 16:54:29 on ttys001

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) dhcp191:~ adrianodif$ ssh tesla
Last login: Mon May  3 17:53:33 2021 from ui03.recas.ba.infn.it
screenIdentity added: /lustre/home/adrianodif/.ssh/id_tesla (/lustre/home/adrianodif/.ssh/id_tesla)
[adrianodif@tesla04 ~]$ screen -r 285^C
[adrianodif@tesla04 ~]$ exit
logout
Connection to tesla04 closed.
(base) dhcp191:~ adrianodif$ ssh recas
Last login: Tue May  4 09:34:19 2021 from dhcp191.ba.infn.it
Identity added: /lustre/home/adrianodif/.ssh/id_tesla (/lustre/home/adrianodif/.ssh/id_tesla)
[adrianodif@ui03 ~]$ screen -r three
[detached from 17619.three]
[adrianodif@ui03 ~]$ screen -r three

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *



generator = cms.EDFilter("Pythia8GeneratorFilter",
                         crossSection = cms.untracked.double(71.39e+09),
                         maxEventsToPrint = cms.untracked.int32(0),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'SoftQCD:inelastic = on'),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
                         )

XiFilter = cms.EDFilter("PythiaFilter",
    MinPt = cms.untracked.double(1.0),
    ParticleID = cms.untracked.int32(3312),
    MaxEta = cms.untracked.double(2.6),
    MinEta = cms.untracked.double(-2.6)
)

ProductionFilterSequence = cms.Sequence(generator*XiFilter)
