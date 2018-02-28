from nltk.stem.wordnet import WordNetLemmatizer
import spacy

SUBJECT_TOKENS = ["nsubj", "nsubjpass", "csubj", "csubjpass", "agent", "expl"]
OBJECT_TOKENS = ["dobj", "dative", "attr", "oprd"]

def get_subjects_from_conj(sbj_tok):
    subject_words = []
    for sub in sbj_tok:
        # right_children is a generator
        right_children = list(sub.right_children)
        right_deps = {tok.lower_ for tok in right_children}
        if "and" in right_deps:
            subject_words.extend([tok for tok in right_children if tok.dep_ in SUBJECT_TOKENS or tok.pos_ == "NOUN"])
            if len(subject_words) > 0:
                subject_words.extend(get_subjects_from_conj(subject_words))
    return subject_words

def get_objects_from_conj(objs):
    objects_words = []
    for obj in objs:
        # right_children is a generator
        right_children = list(obj.right_children)
        right_deps = {tok.lower_ for tok in right_children}
        if "and" in right_deps:
            objects_words.extend([tok for tok in right_children if tok.dep_ in OBJECT_TOKENS or tok.pos_ == "NOUN"])
            if len(objects_words) > 0:
                objects_words.extend(get_objects_from_conj(objects_words))
    return objects_words

def get_verbs_from_conj(verbs):
    verb_words = []
    for verb in verbs:
        right_deps = {tok.lower_ for tok in verb.right_children}
        if "and" in right_deps:
            verb_words.extend([tok for tok in verb.right_children if tok.pos_ == "VERB"])
            if len(verb_words) > 0:
                verb_words.extend(get_verbs_from_conj(verb_words))
    return verb_words

def find_subjects(tok):
    head = tok.head
    while head.pos_ != "VERB" and head.pos_ != "NOUN" and head.head != head:
        head = head.head
    if head.pos_ == "VERB":
        sbj_tok = [tok for tok in head.left_children if tok.dep_ == "SUB"]
        if len(sbj_tok) > 0:
            negative_verb = is_negative(head)
            sbj_tok.extend(get_subjects_from_conj(sbj_tok))
            return sbj_tok, negative_verb
        elif head.head != head:
            return find_subjects(head)
    elif head.pos_ == "NOUN":
        return [head], is_negative(tok)
    return [], False

def is_negative(tok):
    negations = {"no", "not", "n't", "never", "none"}
    for dep in list(tok.left_children) + list(tok.right_children):
        if dep.lower_ in negations:
            return True
    return False

def get_objects_from_preps(deps):
    objs = []
    for dep in deps:
        if dep.pos_ == "ADP" and dep.dep_ == "prep":
            objs.extend([tok for tok in dep.right_children if tok.dep_  in OBJECT_TOKENS or (tok.pos_ == "PRON" and tok.lower_ == "me")])
    return objs

def get_objects_from_xcomp(deps):
    for dep in deps:
        if dep.pos_ == "VERB" and dep.dep_ == "xcomp":
            v = dep
            right_children = list(v.right_children)
            objs = [tok for tok in right_children if tok.dep_ in OBJECT_TOKENS]
            objs.extend(get_objects_from_preps(right_children))
            if len(objs) > 0:
                return v, objs
    return None, None

def get_all_subjects(v):
    negative_verb = is_negative(v)
    sbj_tok = [tok for tok in v.left_children if tok.dep_ in SUBJECT_TOKENS and tok.pos_ != "DET"]
    if len(sbj_tok) > 0:
        sbj_tok.extend(get_subjects_from_conj(sbj_tok))
    else:
        foundSubs, negative_verb = find_subjects(v)
        sbj_tok.extend(foundSubs)
    return sbj_tok, negative_verb

def get_objects(v):
    # right_children is a generator
    right_children = list(v.right_children)
    objs = [tok for tok in right_children if tok.dep_ in OBJECT_TOKENS]
    objs.extend(get_objects_from_preps(right_children))

    new_verb, new_object = get_objects_from_xcomp(right_children)
    if new_verb is not None and new_object is not None and len(new_object) > 0:
        objs.extend(new_object)
        v = new_verb
    if len(objs) > 0:
        objs.extend(get_objects_from_conj(objs))
    return v, objs

def find_triplets(tokens):
    svos = []
    verbs = [tok for tok in tokens if tok.pos_ == "VERB" and tok.dep_ != "aux"]
    for v in verbs:
        sbj_tok, negative_verb = get_all_subjects(v)
        # hopefully there are sbj_tok, if not, don't examine this verb any longer
        if len(sbj_tok) > 0:
            v, objs = get_objects(v)
            for sub in sbj_tok:
                for obj in objs:
                    objNegated = is_negative(obj)
                    svos.append((sub.lower_, "!" + v.lower_ if negative_verb or objNegated else v.lower_, obj.lower_))
    return svos



# def printDeps(toks):
#     for tok in toks:
#         print(tok.orth_, tok.dep_, tok.pos_, tok.head.orth_, [t.orth_ for t in tok.left_children], [t.orth_ for t in tok.right_children])

def extract_triplets(sentence):
    nlp = spacy.load('en')

    tok = nlp(sentence)
    svos = find_triplets(tok)
    
    return svos


def test():
    extract_triplets("I am a scientist")

if __name__ == "__main__":
    test()
