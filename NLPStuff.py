
from flask import Flask, request, redirect, session, jsonify, render_template
import requests
from twilio import twiml
from textblob import TextBlob
from textblob import Word
from textblob.wordnet import NOUN

import mechanize
from bs4 import BeautifulSoup
import re
import datetime
import argparse
import sys
import ConfigParser
import time


class NLPStuff(object):
    def __init__(self,response, blob, message):
        self.blob = blob 
        self.response = response
        self.message = message

        blob = self.spellCorrector(blob)
        self.extractPOS(blob)
        self.AnalyzeSentiments(blob)
        self.wordnetStuff(blob)
        # self.AnlayzeMessage(blob)
        # self.presentMessage()

    def spellCorrector(self, blob):
        return blob.correct()

    def wordnetStuff(self,blob):
        if self.nouns:
            noun1 = self.nouns[0].decode("ascii", errors="ignore")
            print noun1
            noun = Word(noun1)
        else:
            noun = Word("bag")
        synsets = noun.synsets
        for synset in synsets:
            print synset.definition()
        print "Same meaning"
        print synsets[0].lemma_names()


    def extractPOS(self, blob):
        self.nouns = [tag[0] for tag in blob.tags if tag[1] == 'NNP']
        self.verbs = [tag[0] for tag in blob.tags if 'V' in tag[1]]
        
        self.nounphrases = blob.noun_phrases
        self.verbs = list() 

        for word, tag in blob.tags:
            if tag == "VB":
                self.verbs.append(word.lemmatize())

        print self.verbs, self.nounphrases

    def AnalyzeSentiments(self, blob):
        sentiment = blob.sentiment
        sentimentState = {'polarity': blob.polarity, 'subjectivity':blob.subjectivity}
        print sentimentState
        # if 'buy' == verb.lemma:
        # if "compare" in blob: 
        #     message+="Cool, I will compare the food prizes and get back to you"
        # elif "eat" in blob:
        #     message+="I see, where would you like to eat, now?"
        # else:
        #     message+="Is there something that I can do for you?"

        # if sentiment.polarity > 0 and sentiment.subjectivity > 0.7:
        #     message+=" Awesome! I'm stoked you're stoked."
        # elif sentiment.polarity < 0 and sentiment.subjectivity > 0.7:
        #     message+=" Railer.  I'm bummed you're bummed."
        # else:
        #     message+=" Meh."

    def AnlayzeMessage(self, blob):
        if verbs: 
            for verb in verbs:
                if "compare" == verb.lemma:
                    message+=" Awesome, I ll right away compare prices and dishes and tell you "
                elif "eat" == verb.lemma:
                    message+=" Is there a restaurant that you would like to eat? "
                elif "hotels" == verb.lemma:
                    message+=" Are you looking for a hotel, here? "
        else:
            message+=" I am sorry, I couldn understand, can you please repeat? "

    def presentMessage(self):
        return self.message

    def imageSearch(): 
        with self.resp.message(message+" \n") as m: 
            m.media("") 



