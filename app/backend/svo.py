import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, SemanticRolesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='username',
  password='password',
  version=2017-02-27)

response = natural_language_understanding.analyze(
  text='IBM has one of the largest workforces in the world',
  features=Features(
    semantic_roles=SemanticRolesOptions()))

print(json.dumps(response, indent=2))