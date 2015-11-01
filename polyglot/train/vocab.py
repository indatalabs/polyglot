from __future__ import division
from collections import Counter
from math import log

from .wiki import ArticlesReader
from ..mapping.base import IDFVocabulary

def build_idf_vocab_from_wiki_text(wikipedia_text_file, processing=None):
    """
    Builds IDFVocabulary from parsed Wikipedia text.
    :param wikipedia_text_file: path to parsed Wikipedia text file
    :param processing: callable, that will be applied to tokens of each article. Default is None.
    :return: IDFVocabulary
    """
    total_articles = 0
    document_frequency = Counter()

    reader = ArticlesReader(wikipedia_text_file)
    for article_tokens in reader:
        if processing is not None:
            article_tokens = processing(article_tokens)

        unique_tokens = set(article_tokens)
        document_frequency.update(unique_tokens)

        total_articles += 1

    word_idf_mapping = {}
    for word, df in document_frequency.iteritems():
        word_idf_mapping[word] = log(total_articles / df)

    return IDFVocabulary(word_idf_map=word_idf_mapping)
