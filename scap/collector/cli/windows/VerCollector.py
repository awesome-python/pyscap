# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

from scap.Collector import Collector
import logging

logger = logging.getLogger(__name__)
class VerCollector(Collector):
    def collect(self):
        ver = self.host.line_from_command('ver', ())
        self.host.facts['ver'] = ver
        if not ver.startswith('Microsoft Windows'):
            raise NotImplementedError('Unknown windows ver output: ' + ver)

        version = ver.partition('[Version ')[2]
        version = version.strip(']').split('.')
        logger.debug('Split version into ' + str(version))
        self.host.facts['windows_version'] = 'Windows'
        if version[0] == '1':
            # Windows 1.0	1.04
            self.host.facts['windows_version'] = 'Windows 1.0'
        elif version[0] == '2':
            # Windows 2.0	2.11
            self.host.facts['windows_version'] = 'Windows 2.0'
        elif version[0] == '3':
            self.host.facts['windows_version'] = 'Windows NT'
            if version[1] == '10':
                # Windows NT 3.1	3.10.528
                self.host.facts['windows_version'] = 'Windows NT 3.1'
            elif version[1] == '11':
                # Windows for Workgroups 3.11	3.11
                self.host.facts['windows_version'] = 'Windows for Workgroups 3.11'
            elif version[1] == '50':
                # Windows NT 3.5	3.50.807
                self.host.facts['windows_version'] = 'Windows NT 3.5'
            elif version[1] == '51':
                # Windows NT 3.51	3.51.1057
                self.host.facts['windows_version'] = 'Windows NT 3.51'
            elif version[1] == '0':
                # Windows 3.0	3
                self.host.facts['windows_version'] = 'Windows 3.0'
            else:
                logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
        elif version[0] == '4':
            self.host.facts['windows_version'] = 'Windows 95 / 98 / ME'
            if version[1] == '00':
                self.host.facts['windows_version'] = 'Windows 95'
                if version[2] == '950':
                    # Windows 95	4.00.950
                    self.host.facts['windows_version'] = 'Windows 95'
                elif version[2] == '1111':
                    # Windows 95 OSR2	4.00.1111
                    self.host.facts['windows_version'] = 'Windows 95 OSR2'
                elif version[2] == '1381':
                    # Windows NT 4.0	4.00.1381
                    self.host.facts['windows_version'] = 'Windows NT 4.0'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
            elif version[1] == '03':
                self.host.facts['windows_version'] = 'Windows 95 OSR'
                build = int(version[2])
                if build >= 1212 and build < 1214:
                    # Windows 95 OSR2.1	4.03.1212-1214
                    self.host.facts['windows_version'] = 'Windows 95 OSR2.1'
                elif build == 1214:
                    # Windows 95 OSR2.5	4.03.1214
                    self.host.facts['windows_version'] = 'Windows 95 OSR2.5'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
            elif version[1] == '10':
                self.host.facts['windows_version'] = 'Windows 98'
                if version[2] == '1998':
                    # Windows 98	4.10.1998
                    self.host.facts['windows_version'] = 'Windows 98'
                elif version[2] == '2222':
                    # Windows 98 SE	4.10.2222
                    self.host.facts['windows_version'] = 'Windows 98 SE'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
            elif version[1] == '90':
                self.host.facts['windows_version'] = 'Windows ME'
                if version[2] == '2476':
                    # Windows ME Beta	4.90.2476
                    self.host.facts['windows_version'] = 'Windows ME Beta'
                elif version[2] == '2419':
                    # Windows ME Beta 2	4.90.2419
                    self.host.facts['windows_version'] = 'Windows ME Beta 2'
                elif version[2] == '3000':
                    # Windows ME	4.90.3000
                    self.host.facts['windows_version'] = 'Windows ME'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
            else:
                logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
        elif version[0] == '5':
            self.host.facts['windows_version'] = 'Windows 2000 / 200 Professional / XP / Server 2003'
            if version[1] == '00':
                self.host.facts['windows_version'] = 'Windows 2000'
                if version[2] == '1515':
                    # Windows NT 5.0 Beta 2	5.00.1515
                    self.host.facts['windows_version'] = 'Windows NT 5.0 Beta 2'
                elif version[2] == '2031':
                    # Windows 2000 Beta 3	5.00.2031
                    self.host.facts['windows_version'] = 'Windows 2000 Beta 3'
                elif version[2] == '2128':
                    # Windows 2000 Beta 3 RC2	5.00.2128
                    self.host.facts['windows_version'] = 'Windows 2000 Beta 3 RC2'
                elif version[2] == '2183':
                    # Windows 2000 Beta 3	5.00.2183
                    self.host.facts['windows_version'] = 'Windows 2000 Beta 3'
                elif version[2] == '2195':
                    # Windows 2000	5.00.2195
                    self.host.facts['windows_version'] = 'Windows 2000'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')

                from scap.collector.windows.SystemInfoCollector import SystemInfoCollector
                self.host.fact_collectors.append(SystemInfoCollector(self.host))
            elif version[1] == '0':
                self.host.facts['windows_version'] = 'Windows 2000 Professional'
                if version[2] == '2195':
                    # Windows 2000 Professional	5.0.2195
                    self.host.facts['windows_version'] = 'Windows 2000 Professional'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
            elif version[1] == '1':
                #TODO PowerShellCollector may be supported by earlier versions of XP
                self.host.facts['windows_version'] = 'Windows XP'
                if version[2] == '2505':
                    # Windows XP RC1	5.1.2505
                    self.host.facts['windows_version'] = 'Windows XP RC1'
                elif version[2] == '2600':
                    # Windows XP	5.1.2600
                    if len(version) >= 4:
                        release = int(version[3])
                        if release >= 1105 and release <= 1106:
                            # Windows XP SP1	5.1.2600.1105-1106
                            self.host.facts['windows_version'] = 'Windows XP SP1'
                        elif version[3] == '2180':
                            # Windows XP SP2	5.1.2600.2180
                            self.host.facts['windows_version'] = 'Windows XP SP2'

                            from scap.collector.windows.PowerShellCollector import PowerShellCollector
                            self.host.fact_collectors.append(PowerShellCollector(self.host))
                        else:
                            logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
                    else:
                        logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')

                from scap.collector.windows.SystemInfoCollector import SystemInfoCollector
                self.host.fact_collectors.append(SystemInfoCollector(self.host))
            elif version[1] == '2':
                self.host.facts['windows_version'] = 'Windows Server 2003'
                if version[2] == '3541':
                    # Windows .NET Server interim	5.2.3541
                    self.host.facts['windows_version'] = 'Windows .NET Server interim'
                elif version[2] == '3590':
                    # Windows .NET Server Beta 3	5.2.3590
                    self.host.facts['windows_version'] = 'Windows .NET Server Beta 3'
                elif version[2] == '3660':
                    # Windows .NET Server RC1	5.2.3660
                    self.host.facts['windows_version'] = 'Windows .NET Server RC1'
                elif version[2] == '3718':
                    # Windows .NET Server 2003 RC2	5.2.3718
                    self.host.facts['windows_version'] = 'Windows .NET Server 2003 RC2'
                elif version[2] == '3763':
                    # Windows Server 2003 Beta	5.2.3763
                    self.host.facts['windows_version'] = 'Windows Server 2003 Beta'
                elif version[2] == '3790':
                    # Windows Home Server	5.2.3790
                    self.host.facts['windows_version'] = 'Windows Home Server'
                elif version[2] == '3790':
                    if version[3] == '1180':
                        # Windows Server 2003 SP1	5.2.3790.1180
                        self.host.facts['windows_version'] = 'Windows Server 2003 SP1'
                    elif version[3] == '1218':
                        # Windows Server 2003	5.2.3790.1218
                        self.host.facts['windows_version'] = 'Windows Server 2003'
                    else:
                        logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')

                from scap.collector.windows.SystemInfoCollector import SystemInfoCollector
                self.host.fact_collectors.append(SystemInfoCollector(self.host))
                from scap.collector.windows.PowerShellCollector import PowerShellCollector
                self.host.fact_collectors.append(PowerShellCollector(self.host))
        elif version[0] == '6':
            self.host.facts['windows_version'] = 'Windows Vista / 7 / Server 2008 R2 / Home Server 2011 / 8 / 8.1 / Server 2012'
            if version[1] == '0':
                self.host.facts['windows_version'] = 'Windows Vista'
                if version[2] == '5048':
                    # Windows Longhorn	6.0.5048
                    self.host.facts['windows_version'] = 'Windows Longhorn'
                elif version[2] == '5112':
                    # Windows Vista Beta 1	6.0.5112
                    self.host.facts['windows_version'] = 'Windows Vista Beta 1'
                elif version[2] == '5219':
                    # Windows Vista CTP	6.0.5219
                    self.host.facts['windows_version'] = 'Windows Vista CTP'
                elif version[2] == '5259':
                    # Windows Vista TAP Preview	6.0.5259
                    self.host.facts['windows_version'] = 'Windows Vista TAP Preview'
                elif version[2] == '5270':
                    # Windows Vista CTP December	6.0.5270
                    self.host.facts['windows_version'] = 'Windows Vista CTP December'
                elif version[2] == '5308':
                    # Windows Vista CTP February	6.0.5308
                    self.host.facts['windows_version'] = 'Windows Vista CTP February'
                elif version[2] == '5342':
                    # Windows Vista CTP Refresh	6.0.5342
                    self.host.facts['windows_version'] = 'Windows Vista CTP Refresh'
                elif version[2] == '5365':
                    # Windows Vista April EWD	6.0.5365
                    self.host.facts['windows_version'] = 'Windows Vista April EWD'
                elif version[2] == '5381':
                    # Windows Vista Beta 2 Preview	6.0.5381
                    self.host.facts['windows_version'] = 'Windows Vista Beta 2 Preview'
                elif version[2] == '5384':
                    # Windows Vista Beta 2	6.0.5384
                    self.host.facts['windows_version'] = 'Windows Vista Beta 2'
                elif version[2] == '5456':
                    # Windows Vista, Pre-RC1	6.0.5456
                    self.host.facts['windows_version'] = 'Windows Vista, Pre-RC1'
                elif version[2] == '5472':
                    # Windows Vista Pre-RC1 Build 5472	6.0.5472
                    self.host.facts['windows_version'] = 'Windows Vista Pre-RC1 Build 5472'
                elif version[2] == '5536':
                    # Windows Vista Pre-RC1 Build 5536	6.0.5536
                    self.host.facts['windows_version'] = 'Windows Vista Pre-RC1 Build 5536'
                elif version[2] == '5600':
                    # Windows Vista RC1	6.0.5600.16384
                    self.host.facts['windows_version'] = 'Windows Vista RC1'
                elif version[2] == '5700':
                    # Windows Vista Pre-RC2	6.0.5700
                    self.host.facts['windows_version'] = 'Windows Vista Pre-RC2'
                elif version[2] == '5728':
                    # Windows Vista Pre-RC2 Build 5728	6.0.5728
                    self.host.facts['windows_version'] = 'Windows Vista Pre-RC2 Build 5728'
                elif version[2] == '5744':
                    # Windows Vista RC2	6.0.5744.16384
                    self.host.facts['windows_version'] = 'Windows Vista RC2'
                elif version[2] == '5808':
                    # Windows Vista Pre-RTM Build 5808	6.0.5808
                    self.host.facts['windows_version'] = 'Windows Vista Pre-RTM Build 5808'
                elif version[2] == '5824':
                    # Windows Vista Pre-RTM Build 5824	6.0.5824
                    self.host.facts['windows_version'] = 'Windows Vista Pre-RTM Build 5824'
                elif version[2] == '5840':
                    # Windows Vista Pre-RTM Build 5840	6.0.5840
                    self.host.facts['windows_version'] = 'Windows Vista Pre-RTM Build 5840'
                elif version[2] == '6000':
                    # Windows Vista	6.0.6000
                    self.host.facts['windows_version'] = 'Windows Vista'
                    if len(version) >= 4 and version[3] == '16386':
                        # Windows Vista RTM	6.0.6000.16386
                        self.host.facts['windows_version'] = 'Windows Vista RTM'
                    else:
                        logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
                elif version[2] == '6001':
                    # Windows Vista SP1 / Windows Server 2008 SP1	6.0.6001
                    self.host.facts['windows_version'] = 'Windows Vista'
                elif version[2] == '6001':
                    # Windows Vista SP2 / Windows Server 2008 SP2	6.0.6002
                    self.host.facts['windows_version'] = 'Windows Vista'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
            elif version[1] == '1':
                self.host.facts['windows_version'] = 'Windows 7 / Windows Server 2008 R2'
                if version[2] == '7600':
                    # Windows 7 / Windows Server 2008 R2	6.1.7600
                    self.host.facts['windows_version'] = 'Windows 7 / Windows Server 2008 R2'
                    if len(version) >= 4 and version[3] == '16385':
                        # Windows 7 / Windows Server 2008 R2 RTM	6.1.7600.16385
                        self.host.facts['windows_version'] = 'Windows 7 / Windows Server 2008 R2 RTM'
                    else:
                        logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
                elif version[2] == '7601':
                    # Windows 7 SP1 / Windows Server 2008 R2 SP1	6.1.7601
                    self.host.facts['windows_version'] = 'Windows 7 SP1 / Windows Server 2008 R2 SP1'
                elif version[2] == '8400':
                    # Windows Home Server 2011	6.1.8400
                    self.host.facts['windows_version'] = 'Windows Home Server 2011'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
            elif version[1] == '2':
                self.host.facts['windows_version'] = 'Windows 8 / Server 2012'
                if version[2] == '8102':
                    # Windows Server 2012 Developer Preview	6.2.8102
                    self.host.facts['windows_version'] = 'Windows Server 2012 Developer Preview'
                elif version[2] == '9200':
                    # Windows 8 / Windows Server 2012	6.2.9200
                    self.host.facts['windows_version'] = 'Windows 8 / Server 2012'
                    if len(version) >= 4 and version[3] == '16384':
                        # Windows 8 RTM	6.2.9200.16384
                        self.host.facts['windows_version'] = 'Windows 8 RTM'
                elif version[2] == '10211':
                    # Windows Phone 8	6.2.10211
                    self.host.facts['windows_version'] = 'Windows Phone 8'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
            elif version[1] == '3':
                self.host.facts['windows_version'] = 'Windows 8.1 / Windows Server 2012'
                if version[2] == '9200':
                    # Windows 8.1 / Windows Server 2012	6.3.9200
                    self.host.facts['windows_version'] = 'Windows 8.1 / Windows Server 2012'
                elif version[2] == '9600':
                    # Windows 8.1 Update 1 / Windows Server 2012 R2	6.3.9600
                    self.host.facts['windows_version'] = 'Windows 8.1 Update 1 / Windows Server 2012 R2'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
            elif version[1] == '4':
                self.host.facts['windows_version'] = 'Windows 10 Technical Preview'
                if version[2] == '9841':
                    # Windows 10 Technical Preview 1	6.4.9841
                    self.host.facts['windows_version'] = 'Windows 10 Technical Preview 1'
                elif version[2] == '9860':
                    # Windows 10 Technical Preview 2	6.4.9860
                    self.host.facts['windows_version'] = 'Windows 10 Technical Preview 2'
                elif version[2] == '9879':
                    # Windows 10 Technical Preview 3	6.4.9879
                    self.host.facts['windows_version'] = 'Windows 10 Technical Preview 3'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
            else:
                logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')

            from scap.collector.windows.SystemInfoCollector import SystemInfoCollector
            self.host.fact_collectors.append(SystemInfoCollector(self.host))
            from scap.collector.windows.PowerShellCollector import PowerShellCollector
            self.host.fact_collectors.append(PowerShellCollector(self.host))
        elif version[0] == '10':
            self.host.facts['windows_version'] = 'Windows 10'
            if version[1] == '0':
                self.host.facts['windows_version'] = 'Windows 10'
                if version[2] == '9926':
                    # Windows 10 Technical Preview 4	10.0.9926
                    self.host.facts['windows_version'] = 'Windows 10 Technical Preview 4'
                elif version[2] == '10041':
                    # Windows 10 Technical Preview 5	10.0.10041
                    self.host.facts['windows_version'] = 'Windows 10 Technical Preview 5'
                elif version[2] == '10049':
                    # Windows 10 Technical Preview 6	10.0.10049
                    self.host.facts['windows_version'] = 'Windows 10 Technical Preview 6'
                elif version[2] == '10166':
                    # Windows 10 Insider Preview	10.0.10166
                    self.host.facts['windows_version'] = 'Windows 10 Insider Preview'
                elif version[2] == '10240':
                    # Windows 10 Threshold 1	10.0.10240
                    self.host.facts['windows_version'] = 'Windows 10 Threshold 1'
                elif version[2] == '10525':
                    # Windows 10 Insider Preview	10.0.10525
                    self.host.facts['windows_version'] = 'Windows 10 Insider Preview'
                elif version[2] == '10565':
                    # Windows 10 Insider Preview	10.0.10565
                    self.host.facts['windows_version'] = 'Windows 10 Insider Preview'
                elif version[2] == '10586':
                    # Windows 10 Threshold 2	10.0.10586
                    self.host.facts['windows_version'] = 'Windows 10 Threshold 2'
                elif version[2] == '11082':
                    # Windows 10 Insider Preview	10.0.11082
                    self.host.facts['windows_version'] = 'Windows 10 Insider Preview'
                elif version[2] == '11099':
                    # Windows 10 Insider Preview	10.0.11099
                    self.host.facts['windows_version'] = 'Windows 10 Insider Preview'
                elif version[2] == '11102':
                    # Windows 10 Insider Preview	10.0.11102
                    self.host.facts['windows_version'] = 'Windows 10 Insider Preview'
                elif version[2] == '14251':
                    # Windows 10 Insider Preview	10.0.14251
                    self.host.facts['windows_version'] = 'Windows 10 Insider Preview'
                elif version[2] == '14257':
                    # Windows 10 Insider Preview	10.0.14257
                    self.host.facts['windows_version'] = 'Windows 10 Insider Preview'
                elif version[2] == '14267':
                    # Windows 10 Insider Preview	10.0.14267
                    self.host.facts['windows_version'] = 'Windows 10 Insider Preview'
                elif version[2] == '14393':
                    # Windows 10 Redstone 1	10.0.14393
                    self.host.facts['windows_version'] = 'Windows 10 Redstone 1'
                else:
                    logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
            else:
                logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')

            from scap.collector.windows.SystemInfoCollector import SystemInfoCollector
            self.host.fact_collectors.append(SystemInfoCollector(self.host))
            from scap.collector.windows.PowerShellCollector import PowerShellCollector
            self.host.fact_collectors.append(PowerShellCollector(self.host))
        else:
            logger.info('Host discovery incomplete; best guess "' + self.host.facts['windows_version'] + '" for "' + ver + '"')
