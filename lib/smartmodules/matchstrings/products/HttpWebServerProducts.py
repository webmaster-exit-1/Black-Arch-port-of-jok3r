#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.smartmodules.matchstrings.MatchStrings import products_match

# List of most common web servers: https://en.wikipedia.org/wiki/Comparison_of_web_server_software

# Examples:
# product: Microsoft IIS httpd version: 6.0 ostype: Windows 
# product: Apache httpd version: 2.2.4 extrainfo: (Unix) DAV/2
# product: Apache httpd version: 2.0.63 extrainfo: DAV/2 hostname

WIG_REGEXP = r'{}\s*[VERSION]\s*Platform'
WIG_REGEXP2 = r'- Found platform {}(\s*[VERSION])?' 

products_match['http']['web-server'] = {

    'Apache': {
        'wappalyzer': 'Apache',
        'banner': r'Apache httpd(\s*[VERSION])?',
        'wig': [
            WIG_REGEXP.format('Apache'),
            WIG_REGEXP2.format('Apache'),
        ],
    },
    'Hiawatha': {
        'wappalyzer': 'Hiawatha',
        'banner': r'Hiawatha(\s*httpd)?(\s*[VERSION])?',
    },
    'IBM/HTTP Server': {
        'wappalyzer': 'IBM HTTP Server',
        'banner': r'IBM(\s*(HTTP Server|httpd))?(\s*[VERSION])?',
    },
    'Lighttpd': {
        'wappalyzer': 'lighttpd',
        'banner': r'lighttpd(\s*[VERSION])?',
    },
    'LiteSpeed Web Server': {
        'wappalyzer': 'LiteSpeed',
        'banner': r'LiteSpeed httpd(\s+[VERSION])?',
    },
    'Microsoft/IIS': {
        'wappalyzer': 'IIS',
        'banner': r'Microsoft IIS (httpd|WebDAV)(\s*[VERSION])?',
        'wig': [
            WIG_REGEXP.format('IIS'),
            WIG_REGEXP2.format('IIS'),
        ],
    },
    'Mongoose': {
        'banner': r'Mongoose httpd(\s*[VERSION])?',
    },
    'Monkey Http Daemon': {
        'wappalyzer': 'Monkey HTTP Server',
        'banner': r'Monkey httpd(\s*[VERSION])?',
    },
    'Nginx': {
        'wappalyzer': 'Nginx',
        'banner': r'nginx(\s*[VERSION])?',
        'wig': [
            WIG_REGEXP.format('nginx'),
            WIG_REGEXP2.format('nginx'),
        ],
    },
    'Oracle/Http Server': {
        'wappalyzer': 'Oracle HTTP Server',
        'banner': r'Oracle HTTP Server(\s*(9iAS httpd|Powered by Apache))?(.+\(version [VERSION]\))?',
    },
    'Rejetto/Http File Server': {
        'banner': r'HttpFileServer httpd(\s*[VERSION])?',
    },
    'Thttpd': {
        'wappalyzer': 'thttpd',
        'banner': r'thttpd(\s*[VERSION])?',
    },
    'Yaws': {
        'wappalyzer': 'Yaws',
        'banner': r'Yaws httpd(\s*[VERSION])?',
    },
    'Zeus Web Server': {
        'banner': r'Zeus httpd(\s*Admin Server)?(\s*[VERSION])?',
    },
}
