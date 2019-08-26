# tests.py
import pytest
import sys
sys.path.append('../')
from pymed import PubMed
from pymed import version
import xml.etree.ElementTree as xml
from datetime import date
# create an empty PubMed instance using the default tool and email values
tester = PubMed()
# replace with other path for different scenario, default path assume using a file stored in test/
filepath = 'pubmed_result-7.xml'
test_article = tester.fromXMLFile(path=filepath)

# open the test file store the contents in test_str then close the file
testfile = open('pubmed_result-7.xml', 'r')
test_str = testfile.read()
testfile.close()

# convert test_str to an xml element
test_element = xml.fromstring(test_str)


def test_version():
    assert version.__version__ == '0.8.10'


def test_pubMedType():
    assert test_article._returnPubMedType() == 'PubmedArticle'


def test_extractPubMedId():
    assert test_article._extractPubMedId(test_element) == '29346085'


def test_extractTitle():
    assert test_article._extractTitle(test_element) == 'Performance of the BioPlex 2200 HIV Ag-Ab assay for identifying acute HIV infection.'


def test_extractKeywords():
    assert test_article._extractKeywords(test_element) == ['Acute', 'Ag/Ab assay', 'BioPlex', 'HIV']

def test_extractMeshHeadings():
    assert test_article._extractMeshHeadings(test_element) == [{'Acute Retroviral Syndrome': 'N'}, {'Africa, Southern': 'N'}, {'HIV': 'N'}, {'HIV Antibodies': 'N'}, {'HIV Antigens': 'N'}, {'Humans': 'N'}, {'Immunoenzyme Techniques': 'N'}, {'Limit of Detection': 'N'},{'RNA, Viral': 'N'}, {'Reagent Kits, Diagnostic': 'N'}, {'Retrospective Studies': 'N'}, {'United States': 'N'}, {'Viral Load': 'N'}]


def test_extractJournal():
    assert test_article._extractJournal(test_element) == 'Journal of clinical virology : the official publication of the Pan American Society for Clinical Virology'


def test_extractJournalShortname():
    assert test_article._extractJournalShortname(test_element) == 'J Clin Virol'

def test_extractPages():
    assert test_article._extractPages(test_element) == '67-70'

def test_extractAbstract():
    assert test_article._extractAbstract(test_element) == 'Assays that detect HIV antigen (Ag) and antibody (Ab) can be used to screen for HIV infection.\nTo compare the performance of the BioPlex 2200 HIV Ag-Ab assay and two other Ag/Ab combination assays for detection of acute HIV infection.\nSamples were obtained from 24 individuals (18 from the US, 6 from South Africa); these individuals were classified as having acute infection based on the following criteria: positive qualitative RNA assay; two negative rapid tests; negative discriminatory test. The samples were tested with the BioPlex assay, the ARCHITECT HIV Ag/Ab Combo test, the Bio-Rad GS HIV Combo Ag-Ab EIA test, and a viral load assay.\nTwelve (50.0%) of 24 samples had RNA detected only (\u202f>\u202f40 to 13,476 copies/mL). Ten (43.5%) samples had reactive results with all three Ag/Ab assays, one sample was reactive with the ARCHITECT and Bio-Rad assays, and one sample was reactive with the Bio-Rad and BioPlex assays. The 11 samples that were reactive with the BioPlex assay had viral loads from 83,010 to >750,000 copies/mL; 9/11 samples were classified as Ag positive/Ab negative by the BioPlex assay.\nDetection of acute HIV infection was similar for the BioPlex assay and two other Ag/Ab assays. All three tests were less sensitive than a qualitative RNA assay and only detected HIV Ag when the viral load was high. The BioPlex assay detected acute infection in about half of the cases, and identified most of those infections as Ag positive/Ab negative.'

# def test_extractAbstractList():
#    test_article._extractAbstractList(test_element) ==

def test_extractConclusions():
    assert test_article._extractConclusions(test_element) == None

def test_extractMethods():
    assert test_article._extractMethods(test_element) == None


def test_extractResults():
    assert test_article._extractResults(test_element) == 'Twelve (50.0%) of 24 samples had RNA detected only (\u202f>\u202f40 to 13,476 copies/mL). Ten (43.5%) samples had reactive results with all three Ag/Ab assays, one sample was reactive with the ARCHITECT and Bio-Rad assays, and one sample was reactive with the Bio-Rad and BioPlex assays. The 11 samples that were reactive with the BioPlex assay had viral loads from 83,010 to >750,000 copies/mL; 9/11 samples were classified as Ag positive/Ab negative by the BioPlex assay.'


def test_extractCopyrights():
    assert test_article._extractCopyrights(test_element) == 'Copyright © 2018 Elsevier B.V. All rights reserved.'


def test_extractDoi():
    assert test_article._extractDoi(test_element) == '10.1016/j.jcv.2018.01.003'


def test_extractNlmUniqueID():
    assert test_article._extractNlmUniqueID(test_element) == '9815671'


def test_extractArticleIDs():
    assert test_article._extractArticleIDs(test_element) == {'pubmed': '24153130', 'pii': 'S1386-6532(18)30003-9', 'doi': '10.1016/j.jcv.2018.01.003', 'pmc': 'PMC5807223', 'mid': 'NIHMS934711'}


def test_extractPublicationType():
    assert test_article._extractPublicationType(test_element) == 'Evaluation Studies\nJournal Article\nResearch Support, N.I.H., Extramural'


def test_extractPublicationStatus():
    assert test_article._extractPublicationStatus(test_element) == 'ppublish'


def test_extractOwner():
    assert test_article._extractOwner(test_element) == 'NLM'


def test_extractIssueNumber():
    assert test_article._extractIssueNumber(test_element) is None


def test_extractPubDate():
    assert test_article._extractPubDate(test_element) == '2018 Feb - Mar'


def test_extractPublicationDate():
    assert test_article._extractPublicationDate(test_element) == date(2018, 1, 19)


def test_extractAuthors():
    assert test_article._extractAuthors(test_element) == [{'lastname': 'Eshleman', 'firstname': 'Susan H', 'initials': 'SH', 'affiliation': 'Department of Pathology, Johns Hopkins University School of Medicine, Baltimore, MD, United States. Electronic address: seshlem@jhmi.edu.', 'Identifier': None}, {'lastname': 'Piwowar-Manning', 'firstname': 'Estelle', 'initials': 'E', 'affiliation': 'Department of Pathology, Johns Hopkins University School of Medicine, Baltimore, MD, United States. Electronic address: epiwowa@jhmi.edu.', 'Identifier': None}, {'lastname': 'Sivay', 'firstname': 'Mariya V', 'initials': 'MV', 'affiliation': 'Department of Pathology, Johns Hopkins University School of Medicine, Baltimore, MD, United States. Electronic address: msivay1@jhmi.edu.', 'Identifier': None}, {'lastname': 'Debevec', 'firstname': 'Barbara', 'initials': 'B', 'affiliation': 'Department of Pathology, Johns Hopkins University School of Medicine, Baltimore, MD, United States. Electronic address: Bdebeve1@jhmi.edu.', 'Identifier': None}, {'lastname': 'Veater', 'firstname': 'Stephanie', 'initials': 'S', 'affiliation': 'Department of Pathology, Johns Hopkins University School of Medicine, Baltimore, MD, United States. Electronic address: sveater1@jhmi.edu.', 'Identifier': None}, {'lastname': 'McKinstry', 'firstname': 'Laura', 'initials': 'L', 'affiliation': 'Statistical Center for AIDS Research and Prevention, Fred Hutchinson Cancer Research Center, Seattle, WA, United States. Electronic address: lamckins@scharp.org.', 'Identifier': None}, {'lastname': 'Bekker','firstname': 'Linda-Gail', 'initials': 'LG', 'affiliation': 'The Desmond Tutu HIV Centre, University of Cape Town, South Africa. Electronic address: linda-gail.bekker@hiv-research.org.za.', 'Identifier': None}, {'lastname': 'Mannheimer', 'firstname': 'Sharon', 'initials': 'S', 'affiliation': 'Department of Medicine, Harlem Hospital, Columbia University, Mailman School of Public Health, New York, NY, United States. Electronic address: Sbm20@cumc.columbia.edu.', 'Identifier': None}, {'lastname': 'Grant', 'firstname': 'Robert M', 'initials': 'RM', 'affiliation': 'University of California, San Francisco Gladstone Institutes, San Francisco, CA, United States. Electronic address: rgrant@gladstone.ucsf.edu.', 'Identifier': None}, {'lastname': 'Chesney', 'firstname': 'Margaret A', 'initials': 'MA', 'affiliation': 'Department of Medicine, School of Medicine, Univers ity of California, San Francisco, CA, United States. Electronic address: Margaret.Chesney@ucsf.edu.', 'Identifier': None}, {'lastname': 'Coates', 'firstname': 'Thomas J', 'initials': 'TJ', 'affiliation': 'Center for World Health, David Geffen School of Medicine, Los Angeles, CA, United States. Electronic address: tcoates@mednet.ucla.edu.', 'Identifier': None}, {'lastname': 'Koblin', 'firstname': 'Beryl A', 'initials': 'BA', 'affiliation': 'Laboratory of Infectious Disease Prevention, New York Blood Center, New York, NY, United States. Electronic address: bkoblin@nybc.org.', 'Identifier': None}, {'lastname': 'Fogel', 'firstname': 'Jessica M', 'initials': 'JM', 'affiliation': 'Department of Pathology, Johns Hopkins University School of Medicine, Baltimore, MD, United States. Electronic address: jfogel@jhmi.edu.', 'Identifier': None}]


def test_extractISSNs():
    assert test_article._extractISSNs(test_element) == {'eISSN': '1873-5967', 'ISSN': None, 'ISSNLinking': '1386-6532'}
