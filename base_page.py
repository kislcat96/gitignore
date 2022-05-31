from os import link
from tkinter import BROWSE
from webbrowser import get
from selenium import webdriver
import pytest


class BasePage(object):
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open(self):
        self.browser.get(self.link)
