from mwmbl.indexer.index_batches import clean_unicode


def test_clean_unicode():
    result = clean_unicode('Bad extract text \ud83c')
    assert result == 'Bad extract text '
