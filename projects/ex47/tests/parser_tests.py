from nose.tools import *
from ex47 import parser

# 一个一个函数的测试
def test_Sentence():
    item = parser.Sentence(('noun','bear'),
                           ('verb','go'),
                           ('direction','down'))
    assert_equal(item.subject,'bear')
    assert_equal(item.verb, 'go')
    assert_equal(item.object, 'down')

def test_peek():
    assert_equal(parser.peek([('verb','go')]),'verb')
    assert_equal(parser.peek([]),None)

def test_match():
    assert_equal(parser.match([('verb','go')],'verb'),('verb','go'))
    assert_equal(parser.match([('verb', 'go')], 'noun'), None)
    assert_equal(parser.match([], 'verb'), None)

def test_parse_verb():
    assert_equal(parser.parse_verb([('verb', 'go')]), ('verb', 'go'))
    assert_equal(parser.parse_verb([('stop','the'),('verb', 'go')]), ('verb', 'go'))
    assert_raises(parser.ParseError,parser.parse_verb,[('stop','the'),('number', 123)])

def test_parse_object():
    assert_equal(parser.parse_object([('noun', 'bear')]), ('noun', 'bear'))
    assert_equal(parser.parse_object([('stop','the'),('direction', 'east')]), ('direction', 'east'))
    assert_raises(parser.ParseError,parser.parse_object,[('stop','the'),('verb', 'go')])

def test_parse_subject():
    sen1 = parser.parse_subject([('verb', 'go'),('direction', 'east')],('noun', 'bear'))
    assert_equal(sen1.subject, 'bear')
    assert_equal(sen1.verb, 'go')
    assert_equal(sen1.object, 'east')

    sen2 = parser.parse_subject([('verb', 'go'), ('stop','the'),('direction', 'east')], ('noun', 'bear'))
    assert_equal(sen2.subject, 'bear')
    assert_equal(sen2.verb, 'go')
    assert_equal(sen2.object, 'east')

def test_parse_sentence():
    sen1 = parser.parse_sentence([('verb', 'go'), ('direction', 'east')])
    assert_equal(sen1.subject, 'player')
    assert_equal(sen1.verb, 'go')
    assert_equal(sen1.object, 'east')

    sen2 = parser.parse_sentence([('noun', 'bear'),('verb', 'go'),('stop', 'the'), ('direction', 'east')])
    assert_equal(sen2.subject, 'bear')
    assert_equal(sen2.verb, 'go')
    assert_equal(sen2.object, 'east')

    assert_raises(parser.ParseError, parser.parse_sentence, [('stop', 'the'), ('number', 123)])
