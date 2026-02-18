#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.smartmodules.matchstrings.MatchStrings import products_match

# Most common FTP servers from Shodan

products_match['ftp']['ftp-server'] = {

    'Microsoft/ftpd': {
        'banner': r'Microsoft ftpd(\s+[VERSION])?',
    },
    'GNU/Inetutils': {
        'banner': r'GNU Inetutils FTPd(\s+[VERSION])?',
    },
    'Proftpd': {
        'banner': r'ProFTPD(\s+[VERSION])?',
    },
    'Pureftpd': {
        'banner': r'Pure-FTPd(\s+[VERSION])?',
    },
    'Serv-u': {
        'banner': r'Serv-U ftpd(\s+[VERSION])?',
    },
    'Vsftpd': {
        'banner': r'vsftpd(\s+[VERSION])?',
    },


}
