#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.smartmodules.matchstrings.MatchStrings import products_match

# Match wafw00f 1.0.0
WAFW00F_REGEXP = r'The site http.* is behind {} WAF\.'

products_match['http']['web-application-firewall'] = {
    'aeSecure/aeSecure': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'aeSecure \(aeSecure\)'),
        ],
    },
    'Phion/Ergon/Airlock': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Airlock \(Phion/Ergon\)'),
        ],
    },
    'Alert Logic/Alert Logic': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Alert Logic \(Alert Logic\)'),
        ],
    },
    'Alibaba Cloud Computing/AliYunDun': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'AliYunDun \(Alibaba Cloud Computing\)'),
        ],
    },
    'Anquanbao/Anquanbao': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Anquanbao \(Anquanbao\)'),
        ],
    },
    'AnYu Technologies/AnYu': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'AnYu \(AnYu Technologies\)'),
        ],
    },
    'Approach/Approach': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Approach \(Approach\)'),
        ],
    },
    'Armor/Armor Defense': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Armor Defense \(Armor\)'),
        ],
    },
    'Microsoft/ASP.NET Generic Protection': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'ASP.NET Generic Protection \(Microsoft\)'),
        ],
    },
    'Czar Securities/Astra Web Protection': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Astra Web Protection \(Czar Securities\)'),
        ],
    },
    'Amazon/AWS Elastic Load Balancer': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'AWS Elastic Load Balancer \(Amazon\)'),
        ],
    },
    'Baidu Cloud Computing/Yunjiasu': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Yunjiasu \(Baidu Cloud Computing\)'),
        ],
    },
    'Ethic Ninja/Barikode': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Barikode \(Ethic Ninja\)'),
        ],
    },
    'Barracuda Networks/Barracuda Application Firewall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Barracuda Application Firewall \(Barracuda Networks\)'),
        ],
    },
    'Faydata Technologies Inc./Bekchy': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Bekchy \(Faydata Technologies Inc\.\)'),
        ],
    },
    'BinarySec/BinarySec': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'BinarySec \(BinarySec\)'),
        ],
    },
    'BitNinja/BitNinja': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'BitNinja \(BitNinja\)'),
        ],
    },
    'BlockDoS/BlockDoS': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'BlockDoS \(BlockDoS\)'),
        ],
    },
    'Bluedon IST/Bluedon': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Bluedon \(Bluedon IST\)'),
        ],
    },
    'Varnish/CacheWall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'CacheWall \(Varnish\)'),
        ],
    },
    'CdnNs/WdidcNet/CdnNS Application Gateway': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'CdnNS Application Gateway \(CdnNs/WdidcNet\)'),
        ],
    },
    'Cerber Tech/WP Cerber Security': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'WP Cerber Security \(Cerber Tech\)'),
        ],
    },
    'ChinaCache/ChinaCache CDN Load Balancer': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'ChinaCache CDN Load Balancer \(ChinaCache\)'),
        ],
    },
    'Yunaq/Chuang Yu Shield': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Chuang Yu Shield \(Yunaq\)'),
        ],
    },
    'Cisco/ACE XML Gateway': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'ACE XML Gateway \(Cisco\)'),
        ],
    },
    'Penta Security/Cloudbric': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Cloudbric \(Penta Security\)'),
        ],
    },
    'Cloudflare Inc./Cloudflare': {
        'wappalyzer': 'CloudFlare',
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Cloudflare \(Cloudflare Inc\.\)'),
        ],
    },
    'Amazon/Cloudfront': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Cloudfront \(Amazon\)'),
        ],
    },
    'Comodo CyberSecurity/Comodo cWatch': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Comodo cWatch \(Comodo CyberSecurity\)'),
        ],
    },
    'Jean-Denis Brun/CrawlProtect': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'CrawlProtect \(Jean-Denis Brun\)'),
        ],
    },
    'Rohde & Schwarz CyberSecurity/DenyALL': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'DenyALL \(Rohde & Schwarz CyberSecurity\)'),
        ],
    },
    'Distil Networks/Distil': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Distil \(Distil Networks\)'),
        ],
    },
    'DOSarrest Internet Security/DOSarrest': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'DOSarrest \(DOSarrest Internet Security\)'),
        ],
    },
    'Applicure Technologies/DotDefender': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'DotDefender \(Applicure Technologies\)'),
        ],
    },
    'DynamicWeb/DynamicWeb Injection Check': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'DynamicWeb Injection Check \(DynamicWeb\)'),
        ],
    },
    'Verizon Digital Media/Edgecast': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Edgecast \(Verizon Digital Media\)'),
        ],
    },
    'EllisLab/Expression Engine': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Expression Engine \(EllisLab\)'),
        ],
    },
    'F5 Networks/BIG-IP Access Policy Manager': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'BIG-IP Access Policy Manager \(F5 Networks\)'),
        ],
    },
    'F5 Networks/BIG-IP Application Security Manager': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'BIG-IP Application Security Manager \(F5 Networks\)'),
        ],
    },
    'F5 Networks/BIG-IP Local Traffic Manager': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'BIG-IP Local Traffic Manager \(F5 Networks\)'),
        ],
    },
    'F5 Networks/FirePass': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'FirePass \(F5 Networks\)'),
        ],
    },
    'F5 Networks/Trafficshield': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Trafficshield \(F5 Networks\)'),
        ],
    },
    'Fortinet/FortiWeb': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'FortiWeb \(Fortinet\)'),
        ],
    },
    'GoDaddy/GoDaddy Website Protection': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'GoDaddy Website Protection \(GoDaddy\)'),
        ],
    },
    'Grey Wizard/Greywizard': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Greywizard \(Grey Wizard\)'),
        ],
    },
    'Art of Defense/HyperGuard': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'HyperGuard \(Art of Defense\)'),
        ],
    },
    'IBM/DataPower': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'DataPower \(IBM\)'),
        ],
    },
    'CloudLinux/Imunify360': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Imunify360 \(CloudLinux\)'),
        ],
    },
    'Imperva Inc./Incapsula': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Incapsula \(Imperva Inc\.\)'),
        ],
    },
    'Instart Logic/Instart DX': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Instart DX \(Instart Logic\)'),
        ],
    },
    'Microsoft/ISA Server': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'ISA Server \(Microsoft\)'),
        ],
    },
    'Janusec/Janusec Application Gateway': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Janusec Application Gateway \(Janusec\)'),
        ],
    },
    'Jiasule/Jiasule': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Jiasule \(Jiasule\)'),
        ],
    },
    'KnownSec/KS-WAF': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'KS-WAF \(KnownSec\)'),
        ],
    },
    'Akamai/Kona Site Defender': {
        'wappalyzer': 'AkamaiGHost extrainfo: Akamai\'s HTTP',
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Kona Site Defender \(Akamai\)'),
        ],
    },
    'LiteSpeed Technologies/LiteSpeed Firewall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'LiteSpeed Firewall \(LiteSpeed Technologies\)'),
        ],
    },
    'Inactiv/Malcare': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Malcare \(Inactiv\)'),
        ],
    },
    'Mission Control/Mission Control Application Shield': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Mission Control Application Shield \(Mission Control\)'),
        ],
    },
    'SpiderLabs/ModSecurity': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'ModSecurity \(SpiderLabs\)'),
        ],
    },
    'NBS Systems/NAXSI': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'NAXSI \(NBS Systems\)'),
        ],
    },
    'PentestIt/Nemesida': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Nemesida \(PentestIt\)'),
        ],
    },
    'Barracuda Networks/NetContinuum': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'NetContinuum \(Barracuda Networks\)'),
        ],
    },
    'Citrix Systems/NetScaler AppFirewall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'NetScaler AppFirewall \(Citrix Systems\)'),
        ],
    },
    'AdNovum/NevisProxy': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'NevisProxy \(AdNovum\)'),
        ],
    },
    'NewDefend/Newdefend': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Newdefend \(NewDefend\)'),
        ],
    },
    'NexusGuard/NexusGuard Firewall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'NexusGuard Firewall \(NexusGuard\)'),
        ],
    },
    'NinTechNet/NinjaFirewall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'NinjaFirewall \(NinTechNet\)'),
        ],
    },
    'NSFocus Global Inc./NSFocus': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'NSFocus \(NSFocus Global Inc.\)'),
        ],
    },
    'BlackBaud/OnMessage Shield': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'OnMessage Shield \(BlackBaud\)'),
        ],
    },
    'Palo Alto Networks/Palo Alto Next Gen Firewall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Palo Alto Next Gen Firewall \(Palo Alto Networks\)'),
        ],
    },
    'PerimeterX/PerimeterX': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'PerimeterX \(PerimeterX\)'),
        ],
    },
    'PowerCDN/PowerCDN': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'PowerCDN \(PowerCDN\)'),
        ],
    },
    'ArmorLogic/Profense': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Profense \(ArmorLogic\)'),
        ],
    },
    'Radware/AppWall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'AppWall \(Radware\)'),
        ],
    },
    'Reblaze/Reblaze': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Reblaze \(Reblaze\)'),
        ],
    },
    'RSJoomla!/RSFirewall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'RSFirewall \(RSJoomla\!\)'),
        ],
    },
    'Microsoft/ASP.NET RequestValidationMode': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'ASP.NET RequestValidationMode \(Microsoft\)'),
        ],
    },
    'Sabre/Sabre Firewall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Sabre Firewall \(Sabre\)'),
        ],
    },
    'Safe3/Safe3 Web Firewall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Safe3 Web Firewall \(Safe3\)'),
        ],
    },
    'SafeDog/Safedog': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Safedog \(SafeDog\)'),
        ],
    },
    'Chaitin Tech./Safeline': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Safeline \(Chaitin Tech.\)'),
        ],
    },
    'SecuPress/SecuPress WordPress Security': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'SecuPress WordPress Security \(SecuPress\)'),
        ],
    },
    'United Security Providers/Secure Entry': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Secure Entry \(United Security Providers\)'),
        ],
    },
    'BeyondTrust/eEye SecureIIS': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'eEye SecureIIS \(BeyondTrust\)'),
        ],
    },
    'Imperva Inc./SecureSphere': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'SecureSphere \(Imperva Inc\.\)'),
        ],
    },
    'Neusoft/SEnginx': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'SEnginx \(Neusoft\)'),
        ],
    },
    'One Dollar Plugin/Shield Security': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Shield Security \(One Dollar Plugin\)'),
        ],
    },
    'SiteGround/SiteGround': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'SiteGround \(SiteGround\)'),
        ],
    },
    'Sakura Inc./SiteGuard': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'SiteGuard \(Sakura Inc\.\)'),
        ],
    },
    'TrueShield/Sitelock': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Sitelock \(TrueShield\)'),
        ],
    },
    'Dell/SonicWall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'SonicWall \(Dell\)'),
        ],
    },
    'Sophos/UTM Web Protection': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'UTM Web Protection \(Sophos\)'),
        ],
    },
    'Squarespace/Squarespace': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Squarespace \(Squarespace\)'),
        ],
    },
    'StackPath/StackPath': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'StackPath \(StackPath\)'),
        ],
    },
    'Sucuri Inc./Sucuri CloudProxy': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Sucuri CloudProxy \(Sucuri Inc\.\)'),
        ],
    },
    'Tencent Technologies/Tencent Cloud Firewall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Tencent Cloud Firewall \(Tencent Technologies\)'),
        ],
    },
    'Citrix Systems/Teros': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Teros \(Citrix Systems\)'),
        ],
    },
    'TransIP/TransIP Web Firewall': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'TransIP Web Firewall \(TransIP\)'),
        ],
    },
    'iFinity/DotNetNuke/URLMaster SecurityCheck': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'URLMaster SecurityCheck \(iFinity/DotNetNuke\)'),
        ],
    },
    'Microsoft/URLScan': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'URLScan \(Microsoft\)'),
        ],
    },
    'OWASP/Varnish': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Varnish \(OWASP\)'),
        ],
    },
    'VirusDie LLC/VirusDie': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'VirusDie \(VirusDie LLC\)'),
        ],
    },
    'Wallarm Inc./Wallarm': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Wallarm \(Wallarm Inc\.\)'),
        ],
    },
    'WatchGuard Technologies/WatchGuard': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'WatchGuard \(WatchGuard Technologies\)'),
        ],
    },
    'WebARX Security Solutions/WebARX': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'WebARX \(WebARX Security Solutions\)'),
        ],
    },
    'AQTRONIX/WebKnight': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'WebKnight \(AQTRONIX\)'),
        ],
    },
    'IBM/WebSEAL': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'WebSEAL \(IBM\)'),
        ],
    },
    'WebTotem/WebTotem': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'WebTotem \(WebTotem\)'),
        ],
    },
    'Feedjit/Wordfence': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Wordfence \(Feedjit\)'),
        ],
    },
    'WTS/WTS-WAF': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'WTS-WAF \(WTS\)'),
        ],
    },
    '360 Technologies/360WangZhanBao': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'360WangZhanBao \(360 Technologies\)'),
        ],
    },
    'XLabs/XLabs Security WAF': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'XLabs Security WAF \(XLabs\)'),
        ],
    },
    'Yundun/Yundun': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Yundun \(Yundun\)'),
        ],
    },
    'Yunsuo/Yunsuo': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Yunsuo \(Yunsuo\)'),
        ],
    },
    'Zenedge/Zenedge': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'Zenedge \(Zenedge\)'),
        ],
    },
    'Accenture/ZScaler': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'ZScaler \(Accenture\)'),
        ],
    },
    'Accenture/ZScaler': {
        'wafw00f': [
            WAFW00F_REGEXP.format(r'ZScaler \(Accenture\)'),
        ],
    },
    'West263 Content Delivery Network': {
        'wafw00f': [
            WAFW00F_REGEXP.format('West263 Content Delivery Network'),
        ],
    },
    'pkSecurity Intrusion Detection System': {
        'wafw00f': [
            WAFW00F_REGEXP.format('pkSecurity Intrusion Detection System'),
        ],
    },   
    'Xuanwudun': {
        'wafw00f': [
            WAFW00F_REGEXP.format('Xuanwudun'),
        ],
    },   
    'Open-Resty Lua Nginx WAF': {
        'wafw00f': [
            WAFW00F_REGEXP.format('Open-Resty Lua Nginx WAF'),
        ],
    },
}