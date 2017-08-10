# For git
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# For command line
PS1="\[\e[0;31m\]\u@\[\e[m\e[0;35m\]\h\[\e[m \e[0;32m\]\w\$(parse_git_branch)\n\$\[\e[m\]"

export CLICOLOR=true
export LSCOLORS="gxfxcxdxcxegedabagacad"

# alias
alias ll='ls -al'
alias gogit='cd ~/git'
alias goJenkins='ssh test@10.33.130.156'
alias goAlan='ssh devin@10.33.130.23'
alias cleardata='python ~/git/101_work/bin/py/clearApp.py'
alias getdevice='adb devices'
alias doinstallApk='adb install -r'
alias ainput='adb shell input text'
alias getTrueDate='date -r'

# export
export JAVA_HOME=$(/usr/libexec/java_home)
export ANDROID_HOME='/Users/devinchen/Library/Android/sdk'
export PATH="${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools:${JAVA_HOME}/bin:/usr/local/bin"


# PG
export PGPKG='com.roidapp.photogrid'
alias clearSticker='adb shell rm -rf /sdcard/Photo Grid/ /sdcard/roidapp/'
alias getcharlesSSL='adb shell input text chls.pro/ssl'

# Git Autocomplete
[ -f ~/.git-bash-completion.sh ] && . ~/.git-bash-completion.sh
