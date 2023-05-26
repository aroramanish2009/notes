import yaml
import sys
datafile = sys.argv[1]
with open(datafile, "r") as stream:
    try:
       print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
       print(exc)
#print (yaml.dump(yaml.safe_load(datafile)))
