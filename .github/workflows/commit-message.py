import os
import json
import nltk

def check_imperative(paragraph):
    try:
        # for _word in paragraph.split(" "):
        words = nltk.word_tokenize(nltk.sent_tokenize(paragraph)[0])
        # VBZ : Verb, 3rd person singular present, like 'adds', 'writes' etc
        # VBD : Verb, Past tense , like 'added', 'wrote' etc
        # VBG : Verb, Present participle, like 'adding', 'writing'
        word, tag = nltk.pos_tag(['I'] + words)[1:2][0]
        if(tag.startswith('VBZ') or tag.startswith('VBD') or
            tag.startswith('VBG') or
            word.lower()=="adds" or  # Handle special case for VBZ
            word.endswith('ing')):  # Handle special case for VBG
                return word
        else:
            return None
    except LookupError as error:  # pragma: no cover
        print("NLTK data missing, install by running following commands "
                    "`python -m nltk.downloader punkt"
                    " maxent_treebank_pos_tagger averaged_perceptron_tagger`")
        return


if __name__ == "__main__":
    commits = os.getenv("GIT_COMMITS", "").split("\n")
    offending_commits = []
    for commit in commits:
        offending_words = check_imperative(commit)
        if offending_words:
            offending_commits.append(commit)
    formatted_response = ""
    for commit in offending_commits:
        formatted_response += f"  - {commit}\n"
    print(formatted_response)