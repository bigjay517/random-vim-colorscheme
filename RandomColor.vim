command! RANDOMCOLOR : call s:GetRandomColor()

function! s:GetRandomColor()
  let randclr = system("python $VIMHOME/getcolor.py")
  exe "color ".randclr
endfu

