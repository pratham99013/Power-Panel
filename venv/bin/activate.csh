# This file must be used with "source bin/activate.csh" *from csh*.
# You cannot run it directly.
<<<<<<< HEAD

# Created by Davide Di Blasi <davidedb@gmail.com>.
# Ported to Python 3.3 venv by Andrew Svetlov <andrew.svetlov@gmail.com>

alias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PATH" && unset _OLD_VIRTUAL_PATH; rehash; test $?_OLD_VIRTUAL_PROMPT != 0 && set prompt="$_OLD_VIRTUAL_PROMPT" && unset _OLD_VIRTUAL_PROMPT; unsetenv VIRTUAL_ENV; unsetenv VIRTUAL_ENV_PROMPT; test "\!:*" != "nondestructive" && unalias deactivate'
=======
# Created by Davide Di Blasi <davidedb@gmail.com>.

set newline='\
'

alias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PATH:q" && unset _OLD_VIRTUAL_PATH; rehash; test $?_OLD_VIRTUAL_PROMPT != 0 && set prompt="$_OLD_VIRTUAL_PROMPT:q" && unset _OLD_VIRTUAL_PROMPT; unsetenv VIRTUAL_ENV; unsetenv VIRTUAL_ENV_PROMPT; test "\!:*" != "nondestructive" && unalias deactivate && unalias pydoc'
>>>>>>> origin/main

# Unset irrelevant variables.
deactivate nondestructive

<<<<<<< HEAD
setenv VIRTUAL_ENV "/Users/prathammishra/Downloads/Power-Panel-main/venv"

set _OLD_VIRTUAL_PATH="$PATH"
setenv PATH "$VIRTUAL_ENV/bin:$PATH"


set _OLD_VIRTUAL_PROMPT="$prompt"

if (! "$?VIRTUAL_ENV_DISABLE_PROMPT") then
    set prompt = "(venv) $prompt"
    setenv VIRTUAL_ENV_PROMPT "(venv) "
endif

=======
setenv VIRTUAL_ENV '/Users/prathammishra/Desktop/Importtant projects/Thori/Thor/venv'

set _OLD_VIRTUAL_PATH="$PATH:q"
setenv PATH "$VIRTUAL_ENV:q/bin:$PATH:q"



if ('' != "") then
    setenv VIRTUAL_ENV_PROMPT ''
else
    setenv VIRTUAL_ENV_PROMPT "$VIRTUAL_ENV:t:q"
endif

if ( $?VIRTUAL_ENV_DISABLE_PROMPT ) then
    if ( $VIRTUAL_ENV_DISABLE_PROMPT == "" ) then
        set do_prompt = "1"
    else
        set do_prompt = "0"
    endif
else
    set do_prompt = "1"
endif

if ( $do_prompt == "1" ) then
    # Could be in a non-interactive environment,
    # in which case, $prompt is undefined and we wouldn't
    # care about the prompt anyway.
    if ( $?prompt ) then
        set _OLD_VIRTUAL_PROMPT="$prompt:q"
        if ( "$prompt:q" =~ *"$newline:q"* ) then
            :
        else
            set prompt = '('"$VIRTUAL_ENV_PROMPT:q"') '"$prompt:q"
        endif
    endif
endif

unset env_name
unset do_prompt

>>>>>>> origin/main
alias pydoc python -m pydoc

rehash
