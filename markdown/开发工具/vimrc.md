### 基本设置
```
#!vim
set hlsearch
set incsearch
set autoindent
set tabstop=4 expandtab
set fileencodings=utf-8,gbk
set fileencoding=utf-8
set termencoding=utf-8
set t_Co=256
set mouse=n
set ttymouse=xterm2
set diffopt=iwhite,vertical
set ruler
filetype plugin on
syntax on

"切换标签的快捷键
map <C-H> :tabprevious<CR>
map <C-L> :tabnext<CR>

"状态栏
set laststatus=2
set statusline=%<%f\ %h%m%r%=%{\"[\".(&fenc==\"\"?&enc:&fenc).((exists(\"+bomb\")\ &&\ &bomb)?\",B\":\"\").\"]\ \"}%k\ %-14.(%l,%c%V%)\ %P

"配色
colorscheme desert
```

### 代码折叠
```
#!vim
"C++代码折叠
function SetCppOptions()
  syn region IfFoldContainer
    \ start="^\s*#\s*if\(n\?def\)\?\>"
    \ end="#\s*endif\>"
    \ transparent
    \ keepend extend
    \ containedin=NONE
    \ contains=ZhouzmFoldIf
  syn region ZhouzmFoldIf start="^\s*#if" end="^\s*#endif" contained contains=TOP fold transparent
  set foldmethod=syntax
  set foldcolumn=3
endfunction
au FileType h,c,cpp call SetCppOptions()

"js代码折叠
function SetJsFolding()
    set foldmarker={,}
    set foldmethod=marker
    set foldlevel=0
    set foldcolumn=3
endfunction
au FileType js,html call SetJsFolding()

"Python代码折叠
function SetPythonOptions()
  set foldmethod=indent
  set foldcolumn=3
  set shiftwidth=2
endfunction
au FileType python call SetPythonOptions()

"代码折叠选项
set foldlevel=1
set foldminlines=5
set foldnestmax=2



```