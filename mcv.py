#!/usr/bin/env python
# mcv - a utility for reading the Minecraft launcher version manifest
# Copyright 2016 Devin Ryan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import urllib, json, argparse

def get_json(url):
    response = urllib.urlopen(url)
    return json.loads(response.read())

def get_version_manifest(staging):
    return get_json('https://launchermeta.mojang.com/mc' + ('-staging' if staging else '') + '/game/version_manifest.json')

def get_latest(release_type):
    manifest = get_version_manifest(args.staging)
    return manifest['latest'][release_type]

def get_meta(target_version, target_side, target_data):
    manifest = get_version_manifest(args.staging)

    if target_version == 'latest-release':
        target_version = manifest['latest']['release']
    elif target_version == 'latest-snapshot':
        target_version = manifest['latest']['snapshot']

    for version in manifest['versions']:
        if version['id'] == target_version:
            version_data = get_json(version['url'])
            break

    try:
        return version_data['downloads'][target_side][target_data]
    except NameError:
        raise Exception('version not found in version manifest: ' + target_version)

parser = argparse.ArgumentParser(description='A utility for reading the Minecraft launcher version manifest.')
subparsers = parser.add_subparsers(dest='action', help='the action to take. Specify --help with one of these options to show more help.')
parser.add_argument('--staging', action='store_true', help='uses the Minecraft staging manifest instead of release')

latest_parser = subparsers.add_parser('latest', description='Gets the latest release/snapshot version identifier.')
latest_parser.add_argument('type', choices=['release', 'snapshot'], help='the release type')

version_parser = subparsers.add_parser('meta', description='Gets metadata for a specific version.')
version_parser.add_argument('version', help='the target version id')
version_parser.add_argument('side', choices=['client', 'server'], help='whether to retrieve metadata targeting the client jar or server jar')
version_parser.add_argument('target', choices=['sha1', 'size', 'url'], help='the target metadata entry to retrieve')

args = parser.parse_args()
if args.action == 'latest':
    print get_latest(args.type)
elif args.action == 'meta':
    print get_meta(args.version, args.side, args.target)
