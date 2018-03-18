from neuralcoref import Coref

coref = Coref()
clusters = coref.continuous_coref(utterances=u"John wanted to marry Mary. He was a doctor and she was a nurse. She went to the market one day when Henry met her and proposed her. He was a local don.")
print(clusters)

mentions = coref.get_mentions()
#print(mentions)

utterances = coref.get_utterances()
print(utterances)

resolved_utterance_text = coref.get_resolved_utterances()
print(resolved_utterance_text)

print(coref.get_scores())