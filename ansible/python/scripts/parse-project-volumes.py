import sys
import json
import parsers.compose_file

compose_cfg = json.loads(sys.stdin.read())
volumes     = []

if __name__ == '__main__':

  if 'volumes' not in compose_cfg.keys():
    sys.stdout.write('[]')
    sys.exit(0)

  for compose_vol_name, compose_vol_data in compose_cfg['volumes'].items():

    if not compose_vol_data:
      compose_vol_data = {}
    compose_vol = parsers.compose_file.ComposeFileVolume(compose_vol_name, compose_vol_data)

    vol = {
      'name'    : compose_vol.name,
      'imports' : compose_vol.get_imports(),
      'size'    : compose_vol.get_size(),
    }

    if vol['size']:
      volumes.append(vol)

  sys.stdout.write(json.dumps(volumes))
  sys.exit(0)