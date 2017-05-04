Assuming Linux, place the files getcolor.py and favorite\_colors.txt (edit the latter to contain the
names of colorschemes you like) in the directory $HOME/.vim and the file RandomColor.vim in the directory
$HOME/.vim/plugin

Now add the following lines to your .vimrc:

let $VIMHOME = $HOME."/.vim"
autocmd BufEnter,BufRead * :RANDOMCOLOR



