#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.smartmodules.matchstrings.MatchStrings import creds_match


creds_match['http'] = {

    'changeme': {
        r'\[\+\] Found Apache Tomcat( Host Manager)? default cred (?P<m1>\S*):(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'tomcat',
        },
        r'\[\+\] Found Oracle Glassfish default cred (?P<m1>\S*):(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'glassfish',
        },
        r'\[\+\] Found JBoss AS.*? default cred (?P<m1>\S*):(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'jboss',
        },
        r'\[\+\] Found (?P<m1>.*?) default cred (?P<m2>\S*):(?P<m3>\S*)': {
            'meth': 'finditer',
            'user': '$2',
            'pass': '$3',
            'type': '$1',
        },
    },
    'clusterd': {
        # -a axis2 --ax-lfi
        r'--ax-lfi[\s\S]*?Found credentials: (?P<m1>\S+):(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'axis2',
        },
        # -a tomcat --tc-ofetch
        r'--tc-ofetch[\s\S]*?Found credentials:(\s*(?P<m1>\S+):(?P<m2>\S+)\s*\n)+': {
            'meth': 'search',
            'user': '$1',
            'pass': '$2',
            'type': 'tomcat',
        },
        # -a railo --deploy (default creds check) (railo does not have username)
        r'-a railo --deploy[\s\S]*?Successfully authenticated with \'(?P<m1>\S+)\'': {
            'meth': 'finditer',
            'user': '',
            'pass': '$1',
            'type': 'railo',
        },
        # -a <appserver> --deploy (default creds check)
        r'-a (?P<m1>\S+) --deploy[\s\S]*?Successfully authenticated with (?P<m2>\S+):(?P<m3>\S*)': {
            'meth': 'finditer',
            'user': '$2',
            'pass': '$3',
            'type': '$1',
        },
        # -a railo --wordlist --deploy (bruteforce with wordlist)(railo does not have username)
        r'-a railo .*?--wordlist[\s\S]*?Brute forcing password[\s\S]*?Successful login with (?P<m1>\S+)': {
            'meth': 'finditer',
            'user': '',
            'pass': '$1',
            'type': 'railo',
        },
        # -a <appserver> --wordlist --deploy (bruteforce with wordlist)
        r'-a (?P<m1>\S+) .*?--wordlist[\s\S]*?Brute forcing[\s\S]*?Successful login (?P<m2>\S+):(?P<m3>\S*)': {
            'meth': 'finditer',
            'user': '$2',
            'pass': '$3',
            'type': '$1',
        },
    },
    'cmseek': {
        r'"wp_users":\s*r"((?P<m1>\S+?),)+"': {
            'meth': 'search',
            'user': '$1',
            'type': 'wordpress',
        },
    },
    'cmsmap': {
        r'CMS Detection:\s*WordPress\s*?\n[\s\S]*?(\[H\] Valid Credentials(!|:) (Username:)?\s*(?P<m1>\S+)\s*(Password:)?\s*(?P<m2>\S+)\s*?\n(Trying Credentials:.*\n)*)+': {
            'meth': 'search',
            'user': '$1',
            'pass': '$2',
            'type': 'wordpress',
        },
        r'CMS Detection:\s*Joomla\s*?\n[\s\S]*?(\[H\] Valid Credentials(!|:) (Username:)?\s*(?P<m1>\S+)\s*(Password:)?\s*(?P<m2>\S+)\s*?\n(Trying Credentials:.*\n)*)+': {
            'meth': 'search',
            'user': '$1',
            'pass': '$2',
            'type': 'joomla',
        },
        r'CMS Detection:\s*Drupal\s*?\n[\s\S]*?(\[H\] Valid Credentials(!|:) (Username:)?\s*(?P<m1>\S+)\s*(Password:)?\s*(?P<m2>\S+)\s*?\n(Trying Credentials:.*\n)*)+': {
            'meth': 'search',
            'user': '$1',
            'pass': '$2',
            'type': 'drupal',
        },
        r'CMS Detection:\s*WordPress[\s\S]*?WordPress usernames identified:\s*?\n(\[M\]\s*(?P<m1>\S+)\s*?\n)+': {
            'meth': 'search',
            'user': '$1',
            'type': 'wordpress',
        },
    },
    'domiowned': {
        r'(?P<m1>\S+)\s+(?P<m2>\S+)\s+(Admin|User)\s*?\n': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'domino',
        },
    },
    'hydra': {
        r'\[http-get\] host: \S+\s+login:\s+(?P<m1>\S+)\s+password: (?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'htaccess',
        },
    },
    'metasploit': {
        # auxiliary/scanner/http/jenkins_login
        r'jenkins_login[\s\S]*- Login Successful:\s*(?P<m1>\S+):(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'jenkins',
        },
        # auxiliary/scanner/http/tomcat_enum
        r'tomcat_enum[\s\S]*- Apache Tomcat (?P<m1>\S+) found': {
            'meth': 'finditer',
            'user': '$1',
            'type': 'tomcat',
        },
        # auxiliary/scanner/http/tomcat_mgr_login
        r'tomcat_mgr_login[\s\S]*Login Successful:\s*(?P<m1>\S+):(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'tomcat',
        },
        r'jboss_vulnscan[\s\S]*Authenticated using\s*(?P<m1>\S+):(?P<m2>\S*) at ': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'jboss',
        }
    },
    'web-brutator': {
        r'Found (?P<m1>\S+) creds: (?P<m2>\S*):(?P<m3>\S*)': {
            'meth': 'finditer',
            'user': '$2',
            'pass': '$3',
            'type': '$1',
        },
    },
    'wpscan': {
        # [i] User(s) Identified:

        # [+] user1
        #  | Detected By: Wp Json Api (Aggressive Detection)
        #  |  - https://miniwick.com/wp-json/wp/v2/users/?per_page=100&page=1
        #  | Confirmed By: Login Error Messages (Aggressive Detection)

        # [+] user2
        #  | Detected By: Rss Generator (Aggressive Detection)

        r'\[i\] User\(s\) Identified:\s*?(\[\+\]\s*(?P<m1>\S+)\s*?\n(\s*\|.*(\n)+)*)+': {
            'meth': 'search',
            'user': '$1',
            'type': 'wordpress',
        },
        r'\|\s+[0-9]+\s+\|\s+(?!None\s+)(?P<m1>\S+)\s+\|.*\|': { # deprecated
            'meth': 'finditer',
            'user': '$1',
            'type': 'wordpress',
        },
    },
    'wpseku': {
        r'\|\s+[0-9]+\s+\|.*\|\s+(?!None\s+)(?P<m1>\S+)\s+\|': {
            'meth': 'finditer',
            'user': '$1',
            'type': 'wordpress',
        },
    },
    'xbruteforcer': {
        r'wp-login\.php\s+.*User:\s*(?P<m1>\S+)\s*Pass:\s*(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'wordpress',
        },
        r'administrator/index\.php\s+.*User:\s*(?P<m1>\S+)\s*Pass:\s*(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'joomla',
        },
        r'user/login\s+.*User:\s*(?P<m1>\S+)\s*Pass:\s*(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'drupal',
        },
        r'admin/index\.php\s+.*User:\s*(?P<m1>\S+)\s*Pass:\s*(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'opencart',
        },
        r'admin/index\.php\s+.*User:\s*(?P<m1>\S+)\s*Pass:\s*(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'opencart',
        },
        r'/admin\s+.*User:\s*(?P<m1>\S+)\s*Pass:\s*(?P<m2>\S*)': {
            'meth': 'finditer',
            'user': '$1',
            'pass': '$2',
            'type': 'magento',
        },
    }


}