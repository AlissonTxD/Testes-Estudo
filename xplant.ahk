;primeiro slot
slot1x := 322
slot1y := 289
;transfer all
tallx := 408
tally := 197

r::
Send, f 
Sleep, 500
MouseClick, Left, %slot1x%, %slot1y%
Sleep, 50
Send, t
Sleep, 50
MouseClick, Left, %tallx%, %tally%
Sleep, 50
Send, {Esc}
return

f10::
Reload