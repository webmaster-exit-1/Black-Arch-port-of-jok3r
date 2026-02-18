#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.smartmodules.matchstrings.MatchStrings import products_match

WIG_REGEXP = r'{}\s*[VERSION]\s*Platform' 
WIG_REGEXP2 = r'- Found platform {}(\s*[VERSION])?'


products_match['http']['web-language'] = {
    'Microsoft/ASP.NET': {
        'wappalyzer': 'Microsoft ASP.NET',
        'wig': [
            WIG_REGEXP.format(r'ASP\.NET'),
            WIG_REGEXP2.format(r'ASP\.NET'),
        ],
    },
    'CFML': {
        'wappalyzer': 'CFML',
    },
    'Go': {
        'wappalyzer': 'Go',
    },
    'Java': {
        'wappalyzer': 'Java',
    },
    'Lua': {
        'wappalyzer': 'Lua',
    },
    'Node.js': {
        'wappalyzer': 'Node.js',
    },
    'Perl': {
        'wappalyzer': 'Perl',
    },
    'PHP': {
        'wappalyzer': 'PHP',
        'wig': [
            WIG_REGEXP.format('PHP'),
            WIG_REGEXP2.format('PHP'),
        ],
    },
    'Python': {
        'wappalyzer': 'Python',
    },
    'Ruby': {
        'wappalyzer': 'Ruby',
    },
}
