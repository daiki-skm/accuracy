import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
import re
from num2words import num2words
from autocorrect import Speller
spell_corrector = Speller(lang='en')


def getProcessedContentsByLineFromFiles(filep, filen):
    with open(filep, encoding="utf-8_sig") as fp:
        linesp = fp.readlines()
        lineContentsp = []
        for line in linesp:
            ## remove url
            url_pattern = r'https?://\S+|www\.\S+'
            without_urls = re.sub(pattern=url_pattern, repl=" ", string=line)

            ## convert number to words
            after_spliting = without_urls.split()
            for index in range(len(after_spliting)):
                # isdigit(): judge num or str
                if after_spliting[index].isdigit():
                    after_spliting[index] = num2words(after_spliting[index])
            numbers_to_words = " ".join(after_spliting)

            ## to ASCII
            # text = unidecode(numbers_to_words)

            sentencesp = sent_tokenize(numbers_to_words.lower())
            sep_sentencesp = []
            for sentence in sentencesp:
                tagged_token = word_tokenize(sentence)

                # ## fix spelling
                # correct_spell_words = []
                # for word in tagged_token:
                #     correct_word = spell_corrector(word)
                #     correct_spell_words.append(correct_word)

                tagged_words = nltk.pos_tag(tagged_token)
                sep_sentence = " ".join(w for (w, t) in tagged_words if t.startswith('JJ') or t.startswith('NN') or t.startswith('VB') or t.startswith('RB'))
                sep_sentencesp.append(sep_sentence)
            lineContentsp.append(" ".join(sep_sentencesp))
    fp.close()

    with open(filen, encoding="utf-8_sig") as fn:
        linesn = fn.readlines()
        lineContentsn = []
        for line in linesn:
            ## remove url
            url_pattern = r'https?://\S+|www\.\S+'
            without_urls = re.sub(pattern=url_pattern, repl=" ", string=line)

            ## convert number to words
            after_spliting = without_urls.split()
            for index in range(len(after_spliting)):
                # isdigit(): judge num or str
                if after_spliting[index].isdigit():
                    after_spliting[index] = num2words(after_spliting[index])
            numbers_to_words = " ".join(after_spliting)

            # # to ASCII
            # text = unidecode(numbers_to_words)

            sentencesn = sent_tokenize(numbers_to_words.lower())
            sep_sentencesn = []
            for sentence in sentencesn:
                tagged_token = word_tokenize(sentence)

                #  ## fix spelling
                # correct_spell_words = []
                # for word in tagged_token:
                #     correct_word = spell_corrector(word)
                #     correct_spell_words.append(correct_word)

                tagged_words = nltk.pos_tag(tagged_token)
                sep_sentence = " ".join(w for (w, t) in tagged_words if t.startswith('JJ') or t.startswith('NN') or t.startswith('VB') or t.startswith('RB'))
                sep_sentencesn.append(sep_sentence)
            lineContentsn.append(" ".join(sep_sentencesn))
    fn.close()

    input_documents = lineContentsp + lineContentsn

    return input_documents, lineContentsp, lineContentsn