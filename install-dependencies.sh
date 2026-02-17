#!/usr/bin/env bash 

print_green() {
    BOLD_GREEN=$(tput bold ; tput setaf 2)
    NORMAL=$(tput sgr0)
    echo "${BOLD_GREEN}$1${NORMAL}"
}

print_yellow() {
    BOLD_YELLOW=$(tput bold ; tput setaf 3)
    NORMAL=$(tput sgr0)
    echo "${BOLD_YELLOW}$1${NORMAL}"
}

print_red() {
    BOLD_YELLOW=$(tput bold ; tput setaf 1)
    NORMAL=$(tput sgr0)
    echo "${BOLD_YELLOW}$1${NORMAL}"
}

print_blue() {
    BOLD_YELLOW=$(tput bold ; tput setaf 4)
    NORMAL=$(tput sgr0)
    echo "${BOLD_YELLOW}$1${NORMAL}"
}

print_delimiter() {
    echo
    echo "-------------------------------------------------------------------------------"
    echo
}

echo
echo
print_blue "=============================="
print_blue " Jok3r - Dependencies Install "
print_blue "=============================="
echo
echo
print_blue "This script will install Jok3r and all the required dependencies"

# Make sure we are root !
if [ "$EUID" -ne 0 ]; then 
    print_red "[!] Must be run as root"
    exit 1
fi

# Make sure we are on Arch-based OS
OS=`(lsb_release -sd || grep NAME /etc/*-release) 2> /dev/null`
print_blue "[~] Detected OS:"
echo $OS
if [[ `echo $OS | egrep -i '(arch|blackarch)'` ]]; then
    print_green "[+] Arch-based Linux OS detected !"
else
    print_red "[!] No Arch-based Linux OS detected (Arch/BlackArch). Will not be able to continue !"
    exit 1
fi
echo
echo

# -----------------------------------------------------------------------------
# Initialize BlackArch repository if not already configured

if [[ ! $(grep "\[blackarch\]" /etc/pacman.conf 2>/dev/null) ]]; then
    print_blue "[~] Add BlackArch repository (not found in /etc/pacman.conf)"
    cd /tmp/
    curl -O https://blackarch.org/strap.sh
    chmod +x strap.sh
    ./strap.sh
    rm -f strap.sh
    if [ $? -eq 0 ]; then
        print_green "[+] BlackArch repository added with success"
    else
        print_red "[!] Error occured while adding BlackArch repository"
        exit 1
    fi
else
    print_green "[+] BlackArch repository already configured"
fi
print_blue "[~] Updating repositories..."
pacman -Syu --noconfirm
if [ $? -eq 0 ]; then
    print_green "[+] Repositories updated with success"
else
    print_red "[!] Error occured while updating repositories"
    exit 1
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install Git

if ! [ -x "$(command -v git)" ]; then
    print_blue "[~] Install git ..."
    pacman -S --noconfirm git
    if [ -x "$(command -v git)" ]; then
        print_green "[+] Git installed successfully"
    else
        print_red "[!] An error occured during Git install"
        exit 1
    fi
else
    print_green "[+] Git is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install various required packages 

print_blue "[~] Install various required packages (if missing)"

PACKAGES="
automake
bc
base-devel
curl
bind-tools
gawk
gcc
gnupg
iputils
libffi
gmp
xz
postgresql-libs
openssl
perl-libwww
libxml2
libxslt
mlocate
make
net-tools
patch
postgresql
procps-ng
smbclient
sudo
unixodbc
unzip
wget
zlib
"
for package in $PACKAGES; do    
    if [[ ! $(pacman -Q $package 2>/dev/null) ]]; then
        echo
        print_blue "[~] Install ${package} ..."
        pacman -S --noconfirm $package 
    fi
done
print_delimiter

# -----------------------------------------------------------------------------
# Install Metasploit-framework

if ! [ -x "$(command -v msfconsole)" ]; then
    print_blue "[~] Install Metasploit ..."
    pacman -S --noconfirm metasploit 
    if [ -x "$(command -v msfconsole)" ]; then
        print_green "[+] Metasploit installed successfully"
    else
        print_red "[!] An error occured during Metasploit install"
        exit 1
    fi        
else
    print_green "[+] Metasploit is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install Nmap 

if ! [ -x "$(command -v nmap)" ]; then
    print_blue "[~] Install Nmap ..."
    pacman -S --noconfirm nmap 
    if [ -x "$(command -v nmap)" ]; then
        print_green "[+] Nmap installed successfully"
    else
        print_red "[!] An error occured during Nmap install"
        exit 1
    fi   
else
    print_green "[+] Nmap is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install Tcpdump

if ! [ -x "$(command -v tcpdump)" ]; then
    print_blue "[~] Install tcpdump ..."
    pacman -S --noconfirm tcpdump
    if [ -x "$(command -v tcpdump)" ]; then
        print_green "[+] tcpdump installed successfully"
    else
        print_red "[!] An error occured during tcpdump install"
        exit 1
    fi   
else
    print_green "[+] tcpdump is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------

# if ! [ -x "$(command -v npm)" ]; then
#     print_green "[~] Install NodeJS ..."
#     pacman -S --noconfirm nodejs npm
# else
#     print_green "[+] NodeJS is already installed"
# fi
# print_delimiter   

# -----------------------------------------------------------------------------
# Install Python and related packages
print_blue "[~] Install Python 3 and useful related packages (if missing)"

PACKAGES="
python
python-pip
python-setuptools
python-pymysql
python-psycopg2
"

for package in $PACKAGES; do    
    if [[ ! $(pacman -Q $package 2>/dev/null) ]]; then
        echo
        print_blue "[~] Install ${package} ..."
        pacman -S --noconfirm $package 
    fi
done

pip3 install --upgrade pip
pip3 install shodan
if [ -x "$(command -v python3)" ]; then
    print_green "[+] Python3 installed successfully"
else
    print_red "[!] An error occured during Python3 install"
    exit 1
fi 
if [ -x "$(command -v pip3)" ]; then
    print_green "[+] pip3 installed successfully"
else
    print_red "[!] An error occured during pip3 install"
    exit 1
fi 
print_delimiter

# -----------------------------------------------------------------------------
# Install Python virtualenv

if ! [ -x "$(command -v virtualenv)" ]; then
    print_blue "[~] Install python virtual environment packages"
    pip3 install virtualenv
    if [ -x "$(command -v virtualenv)" ]; then
        print_green "[+] virtualenv installed successfully"
    else
        print_red "[!] An error occured during virtualenv install"
        exit 1
    fi
else
    print_green "[+] Python virtualenv is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install common Python libraries
# We decide to add system-wide install of common Python libraries even if
# most of Python tools are then installed inside virtualenv, because it appears
# that a lot of projects/tools do not embed correct requirements.txt or
# setup.py. Then virtualenv for Python projects are created with 
# --system-site-package option which allows to access those libraries.

print_blue "[~] Install common Python 3 libraries..."

LIBPY3="aiohttp
ansi2html
asn1crypto
async-timeout
asyncio
attrs
Babel
bcrypt
beautifulsoup4
blessed
bs4
cement
Cerberus
certifi
cffi
chardet
cmd2
colorama
colored
colorlog
cryptography
dnspython
docutils
enlighten
entrypoints
Flask
future
html5lib
humanfriendly
idna
imagesize
inflect
ipparser
itsdangerous
keyring
keyrings.alt
ldap3
ldapdomaindump
logutils
lxml
MarkupSafe
multidict
netaddr
ntlm-auth
packaging
paramiko
pbr
Pillow
pluginbase
ply
pockets
prettytable
prompt-toolkit
psycopg2
psycopg2-binary
pyasn1
pycparser
pycrypto
pycryptodomex
pycurl
Pygments
PyGObject
pymongo
PyMySQL
PyNaCl
pyodbc
pyOpenSSL
pyparsing
pyperclip
pysmi
pysnmp
PySocks
python-libnmap
python-memcached
pytz
pyxdg
PyYAML
redis
regex
requests
requests-ntlm
requests-toolbelt
SecretStorage
selenium
shodan
six
snowballstemmer
soupsieve
Sphinx
sphinx-better-theme
sphinxcontrib-napoleon
sphinxcontrib-websupport
SQLAlchemy
SQLAlchemy-Utils
stem
stevedore
tabulate
termcolor
tld
tqdm
urllib3
veryprettytable
virtualenv
virtualenv-clone
virtualenvwrapper
wcwidth
webencodings
Werkzeug
yarl
"

PIP3FREEZE=$(pip3 freeze)
for lib in $LIBPY3; do    
    if [[ ! $(echo $PIP3FREEZE | grep -i $lib) ]]; then
        echo
        print_blue "[~] Install Python library ${lib} (py3)"
        pip3 install $lib
    fi
done

print_delimiter

# -----------------------------------------------------------------------------
# Install Jython

if ! [ -x "$(command -v jython)" ]; then
    print_blue "[~] Install Jython"
    pacman -S --noconfirm jython
    if [ -x "$(command -v jython)" ]; then
        print_green "[+] Jython installed successfully"
    else
        print_red "[!] An error occured during Jython install"
        exit 1
    fi   
else
    print_green "[+] Jython is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install Ruby

if ! [ -x "$(command -v ruby)" ]; then
    print_blue "[~] Install Ruby"
    pacman -S --noconfirm ruby
    if [ -x "$(command -v ruby)" ]; then
        print_green "[+] Ruby installed successfully"
    else
        print_red "[!] An error occured during Ruby install"
        exit 1
    fi   
else
    print_green "[+] Ruby is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install rbenv (Ruby Version Manager)

if ! [ -x "$(command -v rbenv)" ]; then
    print_blue "[~] Install rbenv and ruby-build"
    pacman -S --noconfirm rbenv ruby-build
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc
    export PATH="$HOME/.rbenv/bin:$PATH"
    eval "$(rbenv init -)"
    if [ -n "$(command -v rbenv)" ]; then
        print_green "[+] rbenv installed successfully"
    else
        print_red "[!] An error occurred during rbenv install"
        exit 1
    fi
else
    print_green "[+] rbenv is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install Ruby 3.2 via rbenv

if [[ ! $(rbenv versions | grep 3.2) ]]; then
    print_blue "[~] Install Ruby 3.2 via rbenv"
    rbenv install 3.2.0
    rbenv global 3.2.0
    if [[ $(rbenv versions | grep 3.2) ]]; then
        print_green "[+] Ruby 3.2 has been successfully installed with rbenv"
    else
        print_red "[!] Ruby 3.2 has not been installed correctly with rbenv"
        exit 1
    fi
else
    print_green "[+] Ruby 3.2 is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------

print_blue "[~] Update Ruby bundler"
gem install bundler
print_delimiter

# -----------------------------------------------------------------------------
# Install Perl

if ! [ -x "$(command -v perl)" ]; then
    print_blue "[~] Install Perl"
    pacman -S --noconfirm perl 
    if [ -x "$(command -v perl)" ]; then
        print_green "[+] Perl installed successfully"
    else
        print_red "[!] An error occured during Perl install"
        exit 1
    fi   
else
    print_green "[+] Perl is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install PHP

if ! [ -x "$(command -v php)" ]; then
    print_blue "[~] Install PHP"
    pacman -S --noconfirm php
    if [ -x "$(command -v php)" ]; then
        print_green "[+] PHP installed successfully"
    else
        print_red "[!] An error occured during PHP install"
        exit 1
    fi   
else
    print_green "[+] PHP is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install Java

if ! [ -x "$(command -v java)" ]; then
    print_blue "[~] Install Java"
    pacman -S --noconfirm jdk-openjdk
    if [ -x "$(command -v java)" ]; then
        print_green "[+] Java installed successfully"
    else
        print_red "[!] An error occured during Java install"
        exit 1
    fi   
else
    print_green "[+] Java is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install Firefox

if ! [ -x "$(command -v firefox)" ]; then
    print_blue "[~] Install Firefox (for HTML reports and web screenshots)"
    pacman -S --noconfirm firefox
    if [ -x "$(command -v firefox)" ]; then
        print_green "[+] Firefox installed successfully"
    else
        print_red "[!] An error occured during Firefox install"
        exit 1
    fi   
else
    print_green "[+] Firefox is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------
# Install Geckodriver

if ! [ -x "$(command -v geckodriver)" ]; then
    print_blue "[~] Install Geckodriver (for web screenshots)"
    pacman -S --noconfirm geckodriver
    if [ -x "$(command -v geckodriver)" ]; then
        print_green "[+] Geckodriver installed successfully"
    else
        print_red "[!] An error occured during Geckodriver install"
        exit 1
    fi   
else
    print_green "[+] Geckodriver is already installed"
fi
print_delimiter

# -----------------------------------------------------------------------------

print_blue "[~] Install Python3 libraries required by Jok3r (if missing)"
pip3 install -r requirements.txt
pip3 install --upgrade requests
print_delimiter

# -----------------------------------------------------------------------------

print_blue "[~] Disable UserWarning related to psycopg2"
pip3 uninstall psycopg2-binary -y
pip3 uninstall psycopg2 -y
pip3 install psycopg2-binary
print_delimiter

# -----------------------------------------------------------------------------

print_blue "[~] Cleaning pacman cache..."
pacman -Scc --noconfirm
print_delimiter

# -----------------------------------------------------------------------------

print_green "[~] Dependencies installation finished."
print_green "[~] IMPORTANT: Make sure to check if any error has been raised"
echo
