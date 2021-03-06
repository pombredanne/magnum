# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import yaml

from magnum.i18n import _LE

if hasattr(yaml, 'CSafeDumper'):
    yaml_dumper = yaml.CSafeDumper
else:
    yaml_dumper = yaml.SafeDumper


def load(s):
    try:
        yml_dict = yaml.safe_load(s)
    except yaml.YAMLError as exc:
        msg = _LE('An error occurred during YAML parsing.')
        if hasattr(exc, 'problem_mark'):
            msg += _LE(' Error position: '
                       '(%(l)s:%(c)s)') % {'l': exc.problem_mark.line + 1,
                                           'c': exc.problem_mark.column + 1}
        raise ValueError(msg)
    if not isinstance(yml_dict, dict) and not isinstance(yml_dict, list):
        raise ValueError(_LE('The source is not a YAML mapping or list.'))
    if isinstance(yml_dict, dict) and len(yml_dict) < 1:
        raise ValueError(_LE('Could not find any element in your YAML '
                             'mapping.'))
    return yml_dict


def dump(s):
    return yaml.dump(s, Dumper=yaml_dumper)
