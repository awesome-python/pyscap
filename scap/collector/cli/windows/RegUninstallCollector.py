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

from scap.collector.cli.WindowsCollector import WindowsCollector
import logging
import re
from scap.model.cpe_2_3.CPE import CPE

logger = logging.getLogger(__name__)
class RegUninstallCollector(WindowsCollector):
    VALUE_MAP = {
        '(Default)': 'default',
        'AuthorizedCDFPrefix': 'authorized_cd_prefix',
        'Comments': 'comments',
        'Contact': 'contact',
        'DisplayVersion': 'display_version',
        'HelpLink': 'help_link',
        'HelpTelephone': 'help_telephone',
        'InstallDate': 'install_date',
        'InstallLocation': 'install_location',
        'InstallSource': 'install_source',
        'ModifyPath': 'modify_path',
        'Publisher': 'publisher',
        'Readme': 'readme',
        'Size': 'size',
        'EstimatedSize': 'estimated_size',
        'UninstallString': 'uninstall_string',
        'URLInfoAbout': 'url_info_about',
        'URLUpdateInfo': 'url_update_info',
        'VersionMajor': 'version_major',
        'VersionMinor': 'version_minor',
        'WindowsInstaller': 'windows_installer',
        'Version': 'version',
        'Language': 'language',
        'DisplayName': 'display_name',
        'NoModify': 'no_modify',
        'NoRepair': 'no_repair',
        'NoRemove': 'no_remove',
        'NoElevateOnModify': 'no_elevate_on_modifiy',
        'SystemComponent': 'system_component',
        'ParentKeyName': 'parent_key_name',
        'ParentDisplayName': 'parent_display_name',
        'MoreInfoURL': 'more_info_url',
        'IsMinorUpgrade': 'is_minor_upgrade',
        'Installed': 'installed',
        'Resume': 'resume',
        'QuietUninstallString': 'quiet_uninstall_string',
        'DisplayIcon': 'display_icon',
        'EngineVersion': 'engine_version',
        'BundleUpgradePath': 'bundle_upgrade_path',
        'BundleProviderKey': 'bundle_provider_key',
        'BundleDetectCode': 'bundle_detect_code',
        'BundlePatchCode': 'bundle_patch_code',
        'BundleCachePath': 'bundle_cache_path',
        'BundleUpgradeCache': 'bundle_upgrade_cache',
        'BundleAddonCode': 'bundle_addon_code',
        'BundleVersion': 'bundle_version',
        'BundleTag': 'bundle_tag',
        'BundleUpgradeCode': 'bundle_upgrade_code',
        'RegistryLocation': 'registry_location',
        'ReleaseType': 'release_type',
        'Inno': 'inno',
        'MajorVersion': 'version_major',
        'MinorVersion': 'version_minor',
        'CacheLocation': 'cache_location',
        'PackageRefs': 'package_refs',
        'ProductCodes': 'product_codes',
        'SkuComponents': 'sku_components',
        'ProductID': 'product_id',
        'ReleaseTrain': 'release_train',
        'UninstallPath': 'uninstall_path',
        'SQLProductFamilyCode': 'sql_product_family_code',
        'ShellUITransformLanguage': 'shell_ui_transform_language',
        'SPPSkuId': 'spp_sku_id',
    }
    def collect(self):
        if 'registry' not in self.host.facts:
            self.host.facts['registry'] = {}

        if 'uninstall' in self.host.facts['registry']:
            return

        self.host.facts['registry']['uninstall'] = []
        entry = None
        last_name = None
        for line in self.host.exec_command('reg query HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall /s'):
            # skip blank lines
            if re.match(r'^\s*$', line):
                continue

            # header line
            if line.startswith('HKEY_LOCAL_MACHINE'):
                if entry is not None:
                    self.host.facts['registry']['uninstall'].append(entry)
                entry = {'location': line}
                continue

            m = re.match(r'^\s+(\S+)\s+(\S+)\s*$', line)
            if m:
                name = m.group(1)
                last_name = name
                if name in self.VALUE_MAP:
                    name = self.VALUE_MAP[name]
                    entry[name] = ''
                elif name.startswith('Memento'):
                    pass
                else:
                    logger.warning('Unknown uninstall registry subkey: ' + name)

            m = re.match(r'^\s+(\S+)\s+(\S+)\s+(.+)\s*$', line)
            if m:
                name = m.group(1)
                last_name = name
                type_ = m.group(2)
                value = m.group(3)
                if name in self.VALUE_MAP:
                    name = self.VALUE_MAP[name]
                    entry[name] = value
                elif name.startswith('Memento'):
                    pass
                else:
                    logger.warning('Unknown uninstall registry subkey: ' + name)
            else:
                #logger.warning('Line with unknown format: ' + line)
                entry[name] += line

        for entry in self.host.facts['registry']['uninstall']:
            #logger.debug(str(entry))
            cpe = CPE(part='a')

            if 'publisher' not in entry:
                logger.warn('Uninstall entry with no publisher: ' + entry['location'])
                continue
            cpe.set_value('vendor', entry['publisher'])
            if 'display_name' not in entry:
                logger.warn('Uninstall entry with no display_name: ' + entry['location'])
                continue
            cpe.set_value('product', entry['display_name'])
            if 'display_version' in entry:
                cpe.set_value('version', entry['display_version'])

            if cpe not in self.host.facts['cpe']:
                self.host.facts['cpe'].append(cpe)
