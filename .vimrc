set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()

    " alternatively, pass a path where Vundle should install plugins
    "call vundle#begin('~/some/path/here')

    " let Vundle manage Vundle, required
    Plugin 'gmarik/Vundle.vim'

    " Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)
    "
    "git
    Plugin 'tpope/vim-fugitive'
    "powerline
    Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
    "filesystem
    Plugin 'scrooloose/nerdtree'
    Plugin 'jistr/vim-nerdtree-tabs'
    "html
    "  isnowfy only compatible with python not python3
    Plugin 'isnowfy/python-vim-instant-markdown'
    Plugin 'jtratner/vim-flavored-markdown'
    Plugin 'suan/vim-instant-markdown'
    Plugin 'nelstrom/vim-markdown-preview'
    "python
    Plugin 'nvie/vim-flake8'
    "Plugin 'vim-scripts/Pydiction'
    Plugin 'scrooloose/syntastic'
    Plugin 'vim-scripts/indentpython.vim'
    "autocomplete
    Plugin 'Valloric/YouCompleteMe'
    Plugin 'kien/ctrlp.vim'
    Plugin 'Raimondi/delimitMate'
    "code folding
    Plugin 'tmhedberg/SimpylFold'
    "Colors!!
    Plugin 'jnurmine/Zenburn'
    Plugin 'altercation/vim-colors-solarized'
    "navigation
    Plugin 'majutsushi/tagbar'
    "buffer managing"
    Plugin 'vim-airline/vim-airline'
    Plugin 'vim-airline/vim-airline-themes'
    Plugin 'jeetsukumaran/vim-buffergator'
    "comments
    Plugin 'scrooloose/nerdcommenter'

    " All of your Plugins must be added before the following line
    call vundle#end()            " required
    filetype plugin indent on    " required

    " Use System Clipboard
    set clipboard=unnamed

    " Powerline
    set rtp+=$HOME/.local/lib/python2.7/site-packages/powerline/bindings/vim/

    " Always show statusline
    set laststatus=2

    " Use 256 colours (Use this setting only if your terminal supports 256 colours)
    set t_Co=256

    " select scheme
    "if has('gui_running')
    "  set background=dark
    "  colorscheme solarized
    "else
    "  colorscheme zenburn
    "endif

    " Toggle shemes
    "call togglebg#map("<F5>")
if !has('python')
    echo "Error: Required vim compiled with +python"
    finish
endif
let g:pythonworkon = "System"
" Virtualenv
"python with virtualenv support
py << EOF
import os
import sys
import vim
import os.path
if 'VIRTUAL_ENV' in os.environ:
  project_base_dir = os.environ['VIRTUAL_ENV']
  activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
  execfile(activate_this, dict(__file__=activate_this))
  # Save virtual environment name to VIM variable
  vim.command("let g:pythonworkon = '%s'" % os.path.basename(project_base_dir))
EOF

    " tabs navigation
    nnoremap <C-J> <C-W><C-J>
    nnoremap <C-K> <C-W><C-K>
    nnoremap <C-L> <C-W><C-L>
    nnoremap <C-H> <C-W><C-H>

    " Defaults
    if g:pythonworkon == "cv2"
        nnoremap <F5> :w !python2<cr>
        inoremap <F5> <esc> :w !python2<cr>
        nnoremap <silent> <S-F5> :!clear;python2 %<CR>
    else
        nnoremap <buffer> <F5> :w !python3<cr>
        inoremap <buffer> <F5> <esc> :w !python3<cr>
        nnoremap <silent> <S-F5> :!clear;python3 %<CR>
    endif

    " jj exits insert mode
    inoremap jj <esc>
    inoremap ññ <esc>A
    inoremap kk <C-O>a
    " sudo save
    cmap w!! w !sudo tee % >/dev/null
    noremap H ^
    noremap L $
    nmap <F8> :TagbarToggle<CR>
    nnoremap <F7> :call QuickfixToggle()<cr>
    nnoremap <leader>g ggVG= :w<cr>
nnoremap <F9> :NERDTreeToggle<CR>
"comment python
"vnoremap <silent> i :s/^/# /<cr>:noh<cr>
"vnoremap <silent> u :s/^# //<cr>:noh<cr>
"nnoremap <leader>i 0i#<Esc><cr>:noh<cr>
"nnoremap <leader>u :s/^#//<cr>:noh<cr>

" buffers as tabs----------------------------------
set hidden
"nmap <leader>T :enew<cr>
nmap <leader>l :bnext<CR>
nmap <leader>h :bprevious<CR>
"nmap <leader>bq :bp <BAR> bd #<CR>
nmap <leader>q :ls<CR>
let g:airline_theme='powerlineish'
let g:airline_right_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_left_alt_sep= ''
let g:airline_left_sep = ''
" Enable list of buffers
let g:airline#extensions#tabline#enabled = 1
" Show just the filename
let g:airline#extensions#tabline#fnamemod = ':t'

" Setup some default ignores
let g:ctrlp_custom_ignore = {
  \ 'dir':  '\v[\/](\.(git|hg|svn)|\_site)$',
  \ 'file': '\v\.(exe|so|dll|class|png|jpg|jpeg)$',
\}

" Use the nearest .git directory as the cwd
let g:ctrlp_working_path_mode = 'r'

" Use a leader instead of the actual named binding
nmap <leader>p :CtrlP<cr>

" Easy bindings for its various modes
nmap <leader>bb :CtrlPBuffer<cr>
nmap <leader>bm :CtrlPMixed<cr>
nmap <leader>bs :CtrlPMRU<cr>

" Buffergator

" Use the right side of the screen
let g:buffergator_viewport_split_policy = 'R'

" I want my own keymappings...
let g:buffergator_suppress_keymaps = 1

" Looper buffers
"let g:buffergator_mru_cycle_loop = 1

" Go to the previous buffer open
nmap <leader>jj :BuffergatorMruCyclePrev<cr>

" Go to the next buffer open
nmap <leader>kk :BuffergatorMruCycleNext<cr>

" View the entire list of buffers open
nmap <leader>bl :BuffergatorOpen<cr>

" Shared bindings from Solution #1 from earlier
nmap <leader>T :enew<cr>
nmap <leader>bq :w! bp <BAR> bd #<cr>

"--------------------------------------------------
set number
set relativenumber		"See numbers in lines
set encoding=utf-8
set incsearch " incremental search aka search as you type
set hlsearch " highlight search matches
set ignorecase " ignore case
set smartcase " but when the query starts with upper character be case sensitive

set laststatus=2 " always show the status line
set lazyredraw " do not redraw while running macros
set linespace=0 " don't insert any extra pixel lines between rows
set list " show traling listchars
set listchars=tab:▸\ ,trail:¬,extends:❯,precedes:❮,nbsp:~
set nostartofline " don't move the cursor to first non-blank character after some commands (:25 e.g.)
set novisualbell " don't blink
set report=0 " tell us when anything is changed
set ruler " Always show current positions along the bottom
set shortmess=atToOI " shortens messages to avoid 'press a key' prompt
set showcmd " show the command being typed
set showmode " show current mode
set showmatch " show matching brackets
set scrolloff=5 " Keep 10 lines (top/bottom) for scope
set sidescrolloff=10 " Keep 5 lines at the size
set cursorline " visually mark current line
set showbreak=↪  " indicate wrapped line

set wildmenu " turn on command line completion wild style
" ignore these list file extensions
set wildignore=*.dll,*.o,*.obj,*.bak,*.exe,*.pyc,
                    \*.jpg,*.gif,*.png
set wildmode=full
set ttyfast " I have a fast terminal
set undofile " make undo possible after the file is closed and reopened
set gdefault " global substitutions are default s/a/b/g
set ttimeoutlen=50  " Make Esc work faster

let delimitMate_expand_cr=1
let g:quickfix_is_open = 1
" Syntastic error window toggle {{{
function! QuickfixToggle()
    if g:quickfix_is_open
        let g:syntastic_auto_loc_list = 2
        let g:quickfix_is_open = 0
    else
        let g:syntastic_auto_loc_list = 1
        let g:quickfix_is_open = 1
    endif
endfunction
" }}}

"Leader Mappings
let mapleader=" "

" this key combination gets rid of the search highlights
nmap <leader><space> :noh<cr>

" strip all trailing whitespace in the current file
nnoremap <leader>W :%s/\s\+$//<cr>:let @/=''<CR>

" edit .vimrc
nnoremap <leader>ev <C-w><C-v><C-l>:e $MYVIMRC<cr>

" source .vimrc
nnoremap <leader>sv :source $MYVIMRC<cr>

" open vertical split and switch to it
nnoremap <leader>w <C-w>v<C-w>l

" reformat whole file
nnoremap <leader>= ggVG=



" Text Formatting/Layout {{{
    set expandtab " no real tabs please!
    " set wrap "wrap text
    " set textwidth=79 " to 79 characters
    "set colorcolumn=85 " and warn me if my line gets over 85 characters
    set formatoptions=cqt " see :help fo-table
    set infercase " case inferred by default
    set shiftround " round the indent to shiftwidth (when at 3 spaces, and I hit > go to 4, not 5)
    set shiftwidth=4 " auto-indent amount when using >> <<
    set softtabstop=4 " when hitting tab or backspace, how many spaces should a tab be (see expandtab)
    set tabstop=4 " real tabs should be 4, and they will show with set list on
    set autoindent
    match ErrorMsg '^\(<\|=\|>\)\{7\}\([^=].\+\)\?$' " Highlight VCS conflict markers"
" }}}


"Colapse methods and classes
"let g:SimpylFold_docstring_preview=1
"set foldmethod=indent			"Collapse methods and classes
"set foldlevel=99
noremap mm za 			" Enable folding with mm
" noremap mM :call UnrolMe3()<CR>

" let $unrol=0
"function UnrolMe3()
"if $unrol==0
"    :exe "normal zR"
""    let $unrol=1
"else
"    :exe "normal zM"
""    let $unrol=0
"endif
"endfunction

" Folding {{{
set foldenable " Turn on folding
set foldmethod=indent " Fold on the marker
" set foldlevel=100 " Don't autofold anything (but I can still fold manually)
set foldopen=block,hor,mark,percent,quickfix,tag " what movements open folds

function! MyFoldText() " {{{
  let line = getline(v:foldstart)

  let nucolwidth = &fdc + &number * &numberwidth
  let windowwidth = winwidth(0) - nucolwidth - 3
  let foldedlinecount = v:foldend - v:foldstart

  " expand tabs into spaces
  let onetab = strpart('          ', 0, &tabstop)
  let line = substitute(line, '\t', onetab, 'g')

  let line = strpart(line, 0, windowwidth - 2 -len(foldedlinecount))
  let fillcharcount = windowwidth - len(line) - len(foldedlinecount) - 6
  return line . '  …' . repeat(" ",fillcharcount) . foldedlinecount . '…' . ' '
endfunction " }}}

set foldtext=MyFoldText()
" }}}

" Paste Mode
nnoremap <F3> :set nopaste!<CR>

" PEP8 indentation
au BufNewFile,BufRead *.py
    \ set tabstop=4
"    \ set softtabstop=4
    \ set shiftwidth=4
    \ set textwidth=79
    \ set expandtab
    \ set autoindent
    \ set fileformat=unix

au BufNewFile,BufRead *.js, *.html, *.css
    \ set tabstop=2
    \ set softtabstop=2
    \ set shiftwidth=2

" Flagg unnecesary whitespace
"au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

" YouCompleteMe
let g:ycm_autoclose_preview_window_after_completion=1
map <F12>  :YcmCompleter GoToDefinitionElseDeclaration<CR>

" Python higligth
let python_highlight_all=1
syntax on
let g:syntastic_auto_loc_list=2
let g:syntastic_enable_signs=1
let g:synastic_quiet_warnings=1
let g:syntastic_python_checkers=['flake8']

" Fugitive {{{
      nnoremap <leader>gs :Gstatus<cr>
      nnoremap <leader>gc :Gcommit<cr>
      nnoremap <leader>gd :Gdiff<cr>
    " }}}
" Ignore .pyc files on NERDTree
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree

" make backspaces more powerfull
set backspace=indent,eol,start

" backup, swap and undo files
set backup " make backup files
set backupdir=~/.vim/tmp/backup " where to put backup files
set directory=~/.vim/tmp/swap " directory to place swap files in
set undodir=~/.vim/tmp/undo " directory to place undo files in

" Use the below highlight group when displaying bad whitespace is desired.
highlight BadWhitespace ctermbg=red guibg=red

" Display tabs at the beginning of a line in Python mode as bad.
au BufRead,BufNewFile *.py,*.pyw match BadWhitespace /^\t\+/
" Make trailing whitespace be flagged as bad.
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

" Wrap text after a certain number of characters
au BufRead,BufNewFile *.py,*.pyw, set textwidth=100

autocmd VimEnter * source $MYVIMRC
autocmd VimEnter * :normal zR

" NERDCommenter
" Add spaces after comment delimiters by default
let g:NERDSpaceDelims = 1

" Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1

" Align line-wise comment delimiters flush left instead of following code indentation
let g:NERDDefaultAlign = 'left'

" Set a language to use its alternate delimiters by default
let g:NERDAltDelims_python = 1

" Add your own custom formats or override the defaults
"let g:NERDCustomDelimiters = { 'python': { 'left': '/*','right': '*/' } }

" Allow commenting and inverting empty lines (useful when commenting a region)
let g:NERDCommentEmptyLines = 1

" Enable trimming of trailing whitespace when uncommenting
let g:NERDTrimTrailingWhitespace = 1
