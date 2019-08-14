# tests.py
import pytest
import sys
sys.path.append('../')
from pymed import PubMed
from pymed import version
import xml.etree.ElementTree as xml
# create an empty PubMed instance using the default tool and email values
tester = PubMed()
# replace with other path for different scenario, default path assume using a file stored in test/
filepath = 'pubmed_result-10.xml'
test_article = tester.fromXMLFile(path=filepath)

#open the test file store the contents in test_str then close the file
testfile = open('pubmed_result-10.xml', 'r')
test_str = testfile.read()
testfile.close()

# convert test_str to an xml element
test_element = xml.fromstring(test_str)


def test_version():
    assert version.__version__ == '0.8.10'


def test_pubMedType():
    assert test_article._returnPubMedType() == 'PubmedArticle'


def test_extractPubMedId():
    assert test_article._extractPubMedId(test_element) == '17342225'


def test_extractTitle():
    assert test_article._extractTitle(test_element) == 'Premorbid IQ varies across different definitions of schizophrenia.'
