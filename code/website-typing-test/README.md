# README

## ChatGPT prompts to build this website:

----

Create a website with provided text prominently displayed in black color with a highly visible and legible font. The visitor to the website must type the provided text, but is not permitted to hit the backspace, return, tab, or arrow keys or correct any mistakes -- the visitor can only keep typing. As the visitor types each character (corresponding to a letter, number, space, symbol, or punctuation mark) in the provided text, the character on the screen changes color. If the visitor types the correct key, the character changes color to green. If the visitor types an incorrect key, the character changes color to red. The website logs the timing of each keystroke with millisecond precision. The website displays the following information as a table below the text, formatted as follows. Each row corresponds to a character and the following are filled in for the columns: (1) character from the provided text, (2) character the visitor typed, (3) the number 1 if these two match each other and 0 if they don't, (4) a time stamp when the key is pressed, (5) a time stamp when the key is released. Please create the necessary documents for such a website with as few dependencies and in the simplest way possible.

The resulting website displays the text and the column headers for the table, but when I start typing, it searches the page rather than change the colors of the text. Also, the text is legible, but the table text is too bold and prominent.

At the top of the page display the text "Please touch type the following text as you would usually type -- at your usual typing speed on a keyboard of your choice. Each correctly typed character will turn green and each incorrectly typed character will turn red. You will not be able to go back or correct any mistakes. Just keep typing until you have finished."

----

## Input text for website visitor

At an average typing speed of 40 words per minute where a word is on average 5 characters, a person can type approximately 1,000 characters in 5 minutes.

ChatGPT prompt: "Generate a random text string containing 1,000 characters with only lowercase letters and the following punctuation marks  , . / ; ' and include a space after every 5 characters."

Resulting code is in generate_string.py

Resulting random string:

p'uco wnqum i/min crj'i gt;pl pwvd. pxlxm 'smdq g[cgo ivat; jh[ud vdizb bskts nnotb dw';, u,ko. ocm/z hld.p h/cur cenvd vj/sn h/,y. gz;an mlrgm dt,.n wajf/ /r'xi /h'pp qiwvt hcb/u 'gcg[ 'yqra khbdq tfdf; sojp, zm[wj ;sj[y pczzo ktji; iegid xjkk/ ;vm.i l''n/ h'cyx sk.'f iutza 'ydf, gtqga fvuie gyqy. v[h,; ebj[/ mkzwt icw[x txliv px.c[ wurbg ./krh o.hli a;cqv nntp; rix[. wrxhq 'lmni hwhza urg[' fs[v/ qeldu eol'f ugqgu y'hbk wuqr; gd'xf c,'im l.;hs [qyt' c/yhf w'lj/ tttbg '[qp. vkvb/ .qspv .nfg' mohw. t[ntx c.qlf /o'qb b;ygs defu. y;gnv ghiz' yly.. z;mm[ cgj/w qkei, xo;uf qqjmk zqp;k cgko; .dkbn rpihv pb;[s wbiem u,lsz vabzy ,obqm tmtoj p/;[u rz;[o c/k,[ ;/;vy qsxmr c.xrd ybtm[ e'[/h amfq/ [yxnc z'prc mox'a thvnn gofxr e.tfm i.pyb xrauq kv,vs nnyed sd[hs miwfp cknsf jvxxm qeba, dquls myprm ;'qpc ;;c,. .a.[p r/qvc jo'mg ahhet ,jk'u wo.c. qtzlr ;'i., hjp/n ztpkc j;qxw l;vl, tc;lr ;qwx. utq,' rlack ddcwu i;u/j jaskd ixeye r;[s' bhpdv pulbw qcyp/ pahls yirfi xl[oz ss;xx ,gt'u ,avqm pemkd rpdk