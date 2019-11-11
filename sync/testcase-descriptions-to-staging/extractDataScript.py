import json

BASE_PATH = '../../driver/config/'
MAP_FILE = '%smap.json'%BASE_PATH
TAGS_FILE = '%stags.json'%BASE_PATH
TESTCASES_FILE = '%stestcases.json'%BASE_PATH

with open(MAP_FILE) as jsonMapFile, open(TAGS_FILE) as jsonTagsFile, open(TESTCASES_FILE) as jsonTestcasesFile:
  jsonMap = json.load(jsonMapFile)
  jsonTags = json.load(jsonTagsFile)
  jsonTestcases = json.load(jsonTestcasesFile)

  # For each test case in map.json that is set to "isLive": true, the corresponding test case content from testcases.json is synced to the staging database
  testcases = []
  for testNumber in jsonMap:
    if jsonMap[testNumber]['isLive']:
      if testNumber in jsonTestcases:
        print('Extract testcase number %s' % testNumber)
        testcases.append(jsonTestcases[testNumber])
      else:
        print('There is no description for testcase number %s' % testNumber)

  # Write tags to json array file
  with open('testcases.db.json', 'w') as testcasesOutFile:
    json.dump(testcases, testcasesOutFile)

  # All tags in tags.json are synced to the staging database
  tags = []
  for tagNumber in jsonTags:
    print('Extract tag number %s' % tagNumber)
    tags.append(jsonTags[tagNumber])

  # Write tags to json array file
  with open('tags.db.json', 'w') as tagsOutFile:
    json.dump(tags, tagsOutFile)
