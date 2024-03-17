document.addEventListener('DOMContentLoaded', () => {
    const textToType = "p'uco wnqum i/min crj'i gt;pl pwvd. pxlxm 'smdq g[cgo ivat; jh[ud vdizb bskts nnotb dw';, u,ko. ocm/z hld.p h/cur cenvd vj/sn h/,y. gz;an mlrgm dt,.n wajf/ /r'xi /h'pp qiwvt hcb/u 'gcg[ 'yqra khbdq tfdf; sojp, zm[wj ;sj[y pczzo ktji; iegid xjkk/ ;vm.i l''n/ h'cyx sk.'f iutza 'ydf, gtqga fvuie gyqy. v[h,; ebj[/ mkzwt icw[x txliv px.c[ wurbg ./krh o.hli a;cqv nntp; rix[. wrxhq 'lmni hwhza urg[' fs[v/ qeldu eol'f ugqgu y'hbk wuqr; gd'xf c,'im l.;hs [qyt' c/yhf w'lj/ tttbg '[qp. vkvb/ .qspv .nfg' mohw. t[ntx c.qlf /o'qb b;ygs defu. y;gnv ghiz' yly.. z;mm[ cgj/w qkei, xo;uf qqjmk zqp;k cgko; .dkbn rpihv pb;[s wbiem u,lsz vabzy ,obqm tmtoj p/;[u rz;[o c/k,[ ;/;vy qsxmr c.xrd ybtm[ e'[/h amfq/ [yxnc z'prc mox'a thvnn gofxr e.tfm i.pyb xrauq kv,vs nnyed sd[hs miwfp cknsf jvxxm qeba, dquls myprm ;'qpc ;;c,. .a.[p r/qvc jo'mg ahhet ,jk'u wo.c. qtzlr ;'i., hjp/n ztpkc j;qxw l;vl, tc;lr ;qwx. utq,' rlack ddcwu i;u/j jaskd ixeye r;[s' bhpdv pulbw qcyp/ pahls yirfi xl[oz ss;xx ,gt'u ,avqm pemkd rpdk"; // Replace with your text
    const container = document.getElementById('text-container');
    container.innerHTML = textToType.split('').map(char => `<span>${char}</span>`).join('');

    let currentIndex = 0;
    const keystrokeData = [];

    document.addEventListener('keydown', (e) => {
        e.preventDefault(); // Prevent default browser actions
        if (['Backspace', 'Tab', 'ArrowLeft', 'ArrowRight', 'Enter'].includes(e.key)) {
            return; // Still prevent the use of these keys
        }

        const keyPressTime = new Date().getTime();
        const currentChar = textToType[currentIndex];
        const span = container.getElementsByTagName('span')[currentIndex];
        const isCorrect = e.key === currentChar;

        span.className = isCorrect ? 'correct' : 'incorrect';

        keystrokeData.push({
            expected: currentChar,
            typed: e.key,
            match: isCorrect ? 1 : 0,
            pressTime: keyPressTime,
            releaseTime: null // This will be filled on keyup
        });

        currentIndex++;
        updateTable();
    });

    document.addEventListener('keyup', (e) => {
        const keyReleaseTime = new Date().getTime();
        if (keystrokeData[currentIndex - 1]) {
            keystrokeData[currentIndex - 1].releaseTime = keyReleaseTime;
            updateTable();
        }
    });

    function updateTable() {
        const tbody = document.getElementById('keystroke-data').getElementsByTagName('tbody')[0];
        tbody.innerHTML = '';
        keystrokeData.forEach(data => {
            const row = tbody.insertRow();
            Object.values(data).forEach(text => {
                const cell = row.insertCell();
                cell.appendChild(document.createTextNode(text));
            });
        });
    }
});
