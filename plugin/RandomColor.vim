command! RANDOMCOLOR : call s:GetRandomColor()

function! s:GetRandomColor()
  let randclr = system("python $VIMHOME/plugin/random-vim-colorscheme/tools/getcolor.py")
  exe "color ".randclr
endfu

