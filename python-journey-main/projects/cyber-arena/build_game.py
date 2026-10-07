# Generator script
import pathlib

HTML = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>CYBER ARENA - Neon Fighter v2</title>
<meta name="description" content="Game doi khang anime cyberpunk 5 nhan vat voi chieu thuc dac biet!"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@400;600;700&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--c:#00f5ff;--p:#ff2d78;--v:#8b00ff;--g:#ffd700;--d:#040810;--gr:#00ff7f;--o:#ff8c00}
html,body{width:100%;height:100%;overflow:hidden}
body{background:var(--d);font-family:'Rajdhani',sans-serif;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center}
body::after{content:'';position:fixed;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,.12) 2px,rgba(0,0,0,.12) 4px);pointer-events:none;z-index:9999}
.screen{display:none;flex-direction:column;align-items:center;justify-content:center;width:100%;height:100%;position:absolute;inset:0}
.screen.active{display:flex}
.bg-glow{position:absolute;inset:0;pointer-events:none;background:radial-gradient(circle at 20% 80%,rgba(0,245,255,.07),transparent 50%),radial-gradient(circle at 80% 20%,rgba(255,45,120,.07),transparent 50%),radial-gradient(circle at 50% 50%,rgba(139,0,255,.04),transparent 60%);animation:bgP 4s ease-in-out infinite alternate}
@keyframes bgP{from{opacity:.5}to{opacity:1}}
.logo{font-family:'Orbitron',monospace;font-weight:900;font-size:clamp(2rem,6vw,4rem);letter-spacing:.12em;background:linear-gradient(135deg,var(--c),var(--v),var(--p));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;filter:drop-shadow(0 0 16px rgba(0,245,255,.5));animation:lf 3s ease-in-out infinite;z-index:1;text-align:center}
@keyframes lf{0%,100%{filter:drop-shadow(0 0 16px rgba(0,245,255,.5))}50%{filter:drop-shadow(0 0 32px rgba(255,45,120,.7)) drop-shadow(0 0 60px rgba(139,0,255,.4))}}
.sub{font-family:'Orbitron',monospace;font-size:.8rem;letter-spacing:.4em;color:var(--c);opacity:.6;margin:.3rem 0 0;z-index:1}
.btn{font-family:'Orbitron',monospace;font-size:.85rem;font-weight:700;letter-spacing:.1em;padding:.8rem 2rem;border:2px solid;cursor:pointer;position:relative;overflow:hidden;transition:all .25s;background:transparent;text-transform:uppercase}
.btn::before{content:'';position:absolute;inset:0;background:currentColor;opacity:0;transition:opacity .25s}
.btn:hover::before{opacity:.15}
.btn:hover{transform:translateY(-3px);box-shadow:0 0 25px currentColor}
.btn:active{transform:translateY(0)}
.bc{border-color:var(--c);color:var(--c)}
.bp{border-color:var(--p);color:var(--p)}
.bg2{border-color:var(--g);color:var(--g)}
.bgrp{display:flex;gap:1rem;flex-wrap:wrap;justify-content:center;z-index:1}

/* TUTORIAL */
#tut{background:radial-gradient(ellipse at 50% 60%,#080020,var(--d) 70%);gap:0;overflow-y:auto;padding:1.5rem 1rem}
.tgrid{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;max-width:820px;width:100%;z-index:1;margin:1.2rem 0}
.tc{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);padding:1.1rem;position:relative;overflow:hidden}
.tc::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--tg,linear-gradient(90deg,var(--c),var(--v)))}
.tc h3{font-family:'Orbitron',monospace;font-size:.75rem;letter-spacing:.12em;color:var(--c);margin-bottom:.7rem}
.kr{display:flex;align-items:center;gap:.5rem;margin:.3rem 0;font-size:.85rem}
.k{display:inline-flex;align-items:center;justify-content:center;min-width:1.8rem;height:1.8rem;padding:0 .35rem;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.25);font-family:'Orbitron',monospace;font-size:.65rem;font-weight:700;border-radius:3px;color:#fff;flex-shrink:0}
.kd{opacity:.72;font-size:.82rem}
.db{display:inline-block;padding:.04rem .35rem;border-radius:2px;font-family:'Orbitron',monospace;font-size:.62rem;font-weight:700;margin-left:.3rem}
.tip{font-size:.76rem;opacity:.52;margin-top:.7rem;border-top:1px solid rgba(255,255,255,.08);padding-top:.55rem;line-height:1.5}
@media(max-width:600px){.tgrid{grid-template-columns:1fr}}

/* CHAR SEL */
#csel{background:radial-gradient(ellipse at 50% 40%,#0a0020,var(--d) 70%);gap:.8rem}
.csl{display:flex;flex-direction:column;align-items:center;gap:.7rem;z-index:1;flex:1}
.csly{display:flex;align-items:flex-start;gap:1.2rem;z-index:1;width:100%;max-width:920px}
.cl{display:flex;flex-direction:column;gap:.4rem;min-width:110px}
.cbtn{font-family:'Orbitron',monospace;font-size:.62rem;letter-spacing:.07em;padding:.45rem .75rem;border:1px solid rgba(255,255,255,.15);background:rgba(255,255,255,.03);cursor:pointer;color:#fff;transition:all .2s;text-align:left}
.cbtn:hover,.cbtn.sel{background:rgba(255,255,255,.1);border-color:var(--sc,var(--c));box-shadow:0 0 10px var(--sc,var(--c));color:var(--sc,var(--c))}
.cpb{flex:1;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);display:flex;flex-direction:column;align-items:center;padding:1rem;gap:.7rem;min-height:250px;position:relative;overflow:hidden}
.cpname{font-family:'Orbitron',monospace;font-size:1rem;font-weight:900;letter-spacing:.12em}
.cptit{font-size:.76rem;opacity:.5;letter-spacing:.15em}
.cstats{width:100%;display:flex;flex-direction:column;gap:.3rem;margin-top:.2rem}
.sr{display:flex;align-items:center;gap:.45rem;font-size:.72rem}
.sl{font-family:'Orbitron',monospace;font-size:.58rem;letter-spacing:.07em;opacity:.55;min-width:2.2rem}
.st{flex:1;height:4px;background:rgba(255,255,255,.08)}
.sf{height:100%;transition:width .4s}
.cspl{width:100%;display:flex;flex-direction:column;gap:.25rem;border-top:1px solid rgba(255,255,255,.07);padding-top:.5rem;margin-top:.2rem}
.spi{display:flex;align-items:center;gap:.45rem;font-size:.72rem}
.spk{font-family:'Orbitron',monospace;font-size:.58rem;padding:.1rem .3rem;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.05);flex-shrink:0}
.vsd{font-family:'Orbitron',monospace;font-size:1.6rem;font-weight:900;color:var(--v);text-shadow:0 0 18px var(--v);align-self:center;flex-shrink:0}
.pl{font-family:'Orbitron',monospace;font-size:.65rem;letter-spacing:.18em;opacity:.55}
.srow{display:flex;gap:.35rem;align-items:center;margin-top:.8rem;z-index:1}
.srow label{font-family:'Orbitron',monospace;font-size:.62rem;letter-spacing:.1em;color:var(--g)}
.sb{font-family:'Orbitron',monospace;font-size:.58rem;padding:.22rem .6rem;border:1px solid rgba(255,215,0,.3);color:var(--g);background:transparent;cursor:pointer;transition:all .2s}
.sb.act,.sb:hover{background:rgba(255,215,0,.1);box-shadow:0 0 8px rgba(255,215,0,.3)}
/* STAGE SELECT */
#stsel{background:radial-gradient(ellipse at 50% 50%,#0d0028,var(--d) 70%);gap:.6rem}
.sgrid{display:grid;grid-template-columns:repeat(5,1fr);gap:.6rem;max-width:950px;width:100%;z-index:1;padding:0 .5rem}
.scard{position:relative;cursor:pointer;border:2px solid rgba(255,255,255,.12);overflow:hidden;transition:all .25s;aspect-ratio:16/9;background:#111;flex-shrink:0}
.scard img{width:100%;height:100%;object-fit:cover;transition:transform .3s;display:block}
.scard:hover img,.scard.sel img{transform:scale(1.07)}
.scard.sel{border-color:var(--g);box-shadow:0 0 18px var(--g),0 0 36px rgba(255,215,0,.28)}
.scard::after{content:'';position:absolute;inset:0;background:rgba(0,0,0,.32);transition:background .25s;pointer-events:none}
.scard:hover::after,.scard.sel::after{background:rgba(0,0,0,.08)}
.slabel{position:absolute;bottom:0;left:0;right:0;z-index:3;padding:.3rem .4rem;font-family:'Orbitron',monospace;font-size:.55rem;letter-spacing:.07em;font-weight:700;text-align:center;text-transform:uppercase;background:linear-gradient(to top,rgba(0,0,0,.85),transparent);color:#fff}
.scard.sel .slabel{color:var(--g);text-shadow:0 0 8px var(--g)}
.sprev{position:relative;max-width:580px;width:100%;z-index:1;border:1px solid rgba(255,255,255,.12);overflow:hidden}
.sprev img{width:100%;display:block;max-height:160px;object-fit:cover;object-position:center 30%}
.sprev-ov{position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.75) 0%,transparent 55%);display:flex;align-items:flex-end;padding:.7rem .9rem}
.sprev-name{font-family:'Orbitron',monospace;font-size:1rem;font-weight:900;letter-spacing:.12em}
.sprev-desc{font-size:.72rem;opacity:.6;margin-top:.15rem}


/* GAME */
#game{flex-direction:column;background:var(--d)}
#hud{width:100%;display:flex;align-items:center;padding:.4rem .7rem;background:rgba(0,0,0,.7);backdrop-filter:blur(6px);border-bottom:1px solid rgba(0,245,255,.13);flex-shrink:0;gap:.4rem}
.hs{flex:1;display:flex;flex-direction:column;gap:.22rem}
.hs.r{align-items:flex-end}
.fn{font-family:'Orbitron',monospace;font-size:.75rem;font-weight:700;letter-spacing:.06em}
.hbw{width:100%;max-width:330px;height:15px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);overflow:hidden;position:relative}
.hbf{height:100%;transition:width .12s ease-out;position:relative;overflow:hidden}
.hbf::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.25),transparent);animation:sh 2s linear infinite}
@keyframes sh{from{transform:translateX(-100%)}to{transform:translateX(100%)}}
.sbw{width:100%;max-width:330px;height:4px;background:rgba(255,215,0,.08);border:1px solid rgba(255,215,0,.13)}
.sbf{height:100%;transition:width .17s}
.hns{font-size:.68rem;opacity:.58;font-family:'Orbitron',monospace;display:flex;justify-content:space-between;max-width:330px;width:100%}
.wd{display:flex;gap:.3rem}
.wdt{width:8px;height:8px;border-radius:50%;border:1px solid currentColor;transition:background .3s}
.wdt.f{background:currentColor;box-shadow:0 0 6px currentColor}
.ch{display:flex;flex-direction:column;align-items:center;gap:.12rem;flex-shrink:0;padding:0 .7rem}
#rd{font-family:'Orbitron',monospace;font-size:.58rem;letter-spacing:.18em;color:var(--g);opacity:.72}
#td{font-family:'Orbitron',monospace;font-size:1.7rem;font-weight:900;line-height:1;text-shadow:0 0 14px rgba(255,255,255,.35);min-width:2ch;text-align:center}
#td.u{color:var(--p);animation:pu .5s infinite}
@keyframes pu{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}
#cw{position:relative;flex:1;width:100%;overflow:hidden}
#gc{display:block;width:100%;height:100%}
#ann{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;pointer-events:none}
#at{font-family:'Orbitron',monospace;font-size:clamp(2.5rem,8vw,6rem);font-weight:900;letter-spacing:.1em;text-transform:uppercase;text-align:center;opacity:0;transform:scale(2);transition:all .3s}
#at.show{opacity:1;transform:scale(1)}
#cd{position:absolute;bottom:9%;left:50%;transform:translateX(-50%);font-family:'Orbitron',monospace;font-size:1.05rem;font-weight:700;color:var(--g);text-shadow:0 0 16px var(--g);opacity:0;transition:opacity .25s;text-align:center;pointer-events:none}
#sd{position:absolute;top:11%;left:50%;transform:translateX(-50%);font-family:'Orbitron',monospace;font-size:.95rem;font-weight:700;opacity:0;transition:opacity .25s;text-align:center;pointer-events:none;white-space:nowrap}
#mb{position:absolute;bottom:.4rem;left:50%;transform:translateX(-50%);font-family:'Orbitron',monospace;font-size:.52rem;letter-spacing:.1em;padding:.15rem .55rem;border:1px solid rgba(0,245,255,.18);color:var(--c);opacity:.5;pointer-events:none}

/* RESULT */
#res{background:radial-gradient(ellipse at 50% 50%,#0a0020,var(--d) 70%)}
#rt{font-family:'Orbitron',monospace;font-size:clamp(1.8rem,5.5vw,3.5rem);font-weight:900;letter-spacing:.15em;z-index:1;animation:lf 2s infinite}
#rs{font-family:'Orbitron',monospace;font-size:.95rem;letter-spacing:.15em;margin:.7rem 0 2rem;z-index:1;opacity:.68}
::-webkit-scrollbar{width:4px}
::-webkit-scrollbar-thumb{background:rgba(0,245,255,.3);border-radius:2px}
</style>
</head>
<body>

<!-- TUTORIAL -->
<div id="tut" class="screen active">
  <div class="bg-glow"></div>
  <div class="logo">&#9889; CYBER ARENA</div>
  <p class="sub">HUONG DAN DIEU KHIEN</p>
  <div class="tgrid">
    <div class="tc" style="--tg:linear-gradient(90deg,#00f5ff,#8b00ff)">
      <h3>&#127918; NGUOI CHOI 1 (WASD + JKL UIO) - PHONG CACH SHADOW FIGHT</h3>
      <div class="kr"><span class="k">A</span><span class="k">D</span><span class="kd">Di chuyen / <b>Nhap dup A/D hoac Shift</b> de Luot nhanh (Shadow Dash)</span></div>
      <div class="kr"><span class="k">W</span><span class="kd">Nhay cao | <b>W + D</b>: Nhào lộn trước (Front Flip) | <b>W + A</b>: Lộn ngược (Backflip)</span></div>
      <div class="kr"><span class="k">S</span><span class="kd">Ngoi ne don &amp; Do don (Giam 80% sat thuong, ne don tam cao va dan)</span></div>
      <div class="kr"><span class="k">J</span><span class="kd">Don nhanh: <b>Combo 3 don</b> (nhap J lien tuc) | <b>D+J</b>: Luot dam | <b>A+J</b>: Cho phan | <b>W+J / Tren khong</b>: <b>Phi than da (Flying Kick)</b></span></div>
      <div class="kr"><span class="k">K</span><span class="kd">Don nang: Da xoay uy luc | <b>D+K</b>: Song phi | <b>S+K</b>: <b>Quet chan nga (Dragon Sweep)</b> | <b>W+K</b>: <b>Da rong thang thien</b></span></div>
      <div class="kr"><span class="k">L</span><span class="kd">Tuyet ky nhao lon: <b>Shadow Vault / Acrobatic Strike</b> vuot qua doi thu</span></div>
      <div class="kr"><span class="k">U</span><span class="kd">Chieu dac biet 1 &#128256;</span></div>
      <div class="kr"><span class="k">I</span><span class="kd">Chieu dac biet 2 &#9889;</span></div>
      <div class="kr"><span class="k">O</span><span class="kd">SUPER &#10024; (Can day SP vang - Bat kha xam pham)</span></div>
      <div class="tip">&#128161; <b>Bi kip:</b> Dung nhap dup A/D de luot ne don! Quet chan S+K lam doi thu nga ngup. Tren khong bam J de tung cu Phi than da cuc hiem!</div>
    </div>
    <div class="tc" style="--tg:linear-gradient(90deg,#ff2d78,#8b00ff)">
      <h3>&#128214; HE THONG CHIEN DAU</h3>
      <div class="kr">&#10084; <span class="kd"><b>HP Bar</b> &mdash; thanh mau (500 HP)</span></div>
      <div class="kr">&#9889; <span class="kd"><b>SP Bar</b> (vang) &mdash; tich khi danh / nhan don</span></div>
      <div class="kr">&#128293; <span class="kd"><b>Combo</b> &mdash; danh lien tiep hien thi combo</span></div>
      <div class="kr">&#128737; <span class="kd"><b>Block</b> &mdash; giam 80% DMG, khong chan SUPER</span></div>
      <div class="kr">&#10024; <span class="kd"><b>SUPER</b> &mdash; bat kha xam pham + 55-70 DMG</span></div>
      <div class="kr">&#127942; <span class="kd"><b>Best of 3</b> &mdash; thang 2 round = thang tran</span></div>
      <div class="kr">&#8987; <span class="kd"><b>100 giay</b> &mdash; het gio so HP ai cao hon thang</span></div>
      <div class="tip">&#128161; Moi nhan vat co 2 chieu dac biet va 1 SUPER khac nhau.<br>Bot AI se su dung chieu thuc dua tren tinh trang chien dau!</div>
    </div>
    <div class="tc" style="--tg:linear-gradient(90deg,#00ff7f,#00f5ff);grid-column:1/-1">
      <h3>&#9876; 5 NHAN VAT (FIGHTERS)</h3>
      <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:.5rem;text-align:center;margin-top:.3rem">
        <div style="padding:.45rem;border:1px solid rgba(0,245,255,.2)"><div style="color:#00f5ff;font-family:'Orbitron',monospace;font-size:.68rem;font-weight:700">CYBER-X</div><div style="font-size:.6rem;opacity:.52;margin-top:.2rem">&#9876; Kiem nang luong<br>&#128256; Loc Xoay<br>&#10024; Bao Kiem</div></div>
        <div style="padding:.45rem;border:1px solid rgba(255,45,120,.2)"><div style="color:#ff2d78;font-family:'Orbitron',monospace;font-size:.68rem;font-weight:700">NOVA-K</div><div style="font-size:.6rem;opacity:.52;margin-top:.2rem">&#128165; Plasma Burst<br>&#128293; Vu Dieu Lua<br>&#10024; Plasma Storm</div></div>
        <div style="padding:.45rem;border:1px solid rgba(0,255,127,.2)"><div style="color:#00ff7f;font-family:'Orbitron',monospace;font-size:.68rem;font-weight:700">SHADOW</div><div style="font-size:.6rem;opacity:.52;margin-top:.2rem">&#129399; Ninja Slash<br>&#11088; Shuriken x3<br>&#10024; Man Dem</div></div>
        <div style="padding:.45rem;border:1px solid rgba(255,140,0,.2)"><div style="color:#ff8c00;font-family:'Orbitron',monospace;font-size:.68rem;font-weight:700">TITAN</div><div style="font-size:.6rem;opacity:.52;margin-top:.2rem">&#128170; Dam Sam<br>&#127755; Dia Chan<br>&#10024; Rage Mode</div></div>
        <div style="padding:.45rem;border:1px solid rgba(218,112,214,.2)"><div style="color:#da70d6;font-family:'Orbitron',monospace;font-size:.68rem;font-weight:700">PHANTOM</div><div style="font-size:.6rem;opacity:.52;margin-top:.2rem">&#128123; Void Blink<br>&#128302; Void Beam<br>&#10024; Bao Linh Hon</div></div>
      </div>
    </div>
  </div>
  <div class="bgrp"><button class="btn bg2" onclick="showCsel()">CHON NHAN VAT &#8594;</button></div>
</div>

<!-- CHAR SEL -->
<div id="csel" class="screen">
  <div class="bg-glow"></div>
  <div class="logo" style="font-size:clamp(1.4rem,3.5vw,2.2rem);margin-bottom:.2rem">CHON NHAN VAT</div>
  <div class="csly">
    <div class="csl">
      <div class="pl" style="color:#00f5ff">[ P1 - NGUOI CHOI / BOT ]</div>
      <div style="display:flex;gap:.7rem;width:100%;max-width:370px">
        <div class="cl" id="p1cl"></div>
        <div class="cpb" id="p1pb">
          <canvas id="p1pc" width="120" height="140" style="width:110px;height:130px"></canvas>
          <div class="cpname" id="p1pn" style="color:#00f5ff">CYBER-X</div>
          <div class="cptit" id="p1pt">Cyber Blade Fighter</div>
          <div class="cstats" id="p1ps"></div>
          <div class="cspl" id="p1sp"></div>
        </div>
      </div>
    </div>
    <div class="vsd">VS</div>
    <div class="csl">
      <div class="pl" style="color:#ff2d78">[ P2 - BOT ]</div>
      <div style="display:flex;gap:.7rem;width:100%;max-width:370px">
        <div class="cpb" id="p2pb">
          <canvas id="p2pc" width="120" height="140" style="width:110px;height:130px"></canvas>
          <div class="cpname" id="p2pn" style="color:#ff2d78">NOVA-K</div>
          <div class="cptit" id="p2pt">Plasma Striker</div>
          <div class="cstats" id="p2ps"></div>
          <div class="cspl" id="p2sp"></div>
        </div>
        <div class="cl" id="p2cl"></div>
      </div>
    </div>
  </div>
  <div class="srow">
    <label>BOT SPEED:</label>
    <button class="sb" onclick="setSp('slow')">SLOW</button>
    <button class="sb act" onclick="setSp('normal')">NORMAL</button>
    <button class="sb" onclick="setSp('fast')">FAST</button>
    <button class="sb" onclick="setSp('god')">&#9889; GOD</button>
  </div>
  <div class="bgrp" style="margin-top:.8rem">
    <button class="btn bg2" onclick="showStsel()">TIEP THEO &#8594; CHON CHIEN TRUONG</button>
    <button class="btn" style="border-color:rgba(255,255,255,.2);color:rgba(255,255,255,.45)" onclick="showTut()">&#9664; HUONG DAN</button>
  </div>
</div>


<!-- STAGE SELECT -->
<div id="stsel" class="screen">
  <div class="bg-glow"></div>
  <div class="logo" style="font-size:clamp(1.2rem,2.8vw,1.9rem);margin-bottom:.1rem">CHON KHU VUC CHIEN DAU</div>
  <p class="sub" style="margin-bottom:.5rem;font-size:.65rem">SELECT YOUR BATTLEGROUND</p>
  <div class="sgrid" id="sgrid"></div>
  <div class="sprev" id="sprev" style="margin-top:.5rem">
    <img id="sprev-img" src="stages/nether.jpg" alt="stage preview"/>
    <div class="sprev-ov">
      <div>
        <div class="sprev-name" id="sprev-name" style="color:#ff8c00">NETHER REALM</div>
        <div class="sprev-desc" id="sprev-desc">Chien truong dia nguc - cong dich chuyen huyen bi</div>
      </div>
    </div>
  </div>
  <div class="bgrp" style="margin-top:.6rem">
    <button class="btn bc" id="st-pvb" onclick="startGameFromStage('pvb')">&#127918; PLAYER vs BOT</button>
    <button class="btn bp" id="st-bvb" onclick="startGameFromStage('bvb')">&#129302; BOT vs BOT</button>
    <button class="btn" style="border-color:rgba(255,255,255,.2);color:rgba(255,255,255,.45)" onclick="showCsel()">&#9664; NHAN VAT</button>
  </div>
</div>
<!-- GAME -->
<div id="game" class="screen">
  <div id="hud">
    <div class="hs">
      <div class="fn" id="p1fn" style="color:#00f5ff">CYBER-X</div>
      <div class="hbw"><div class="hbf" id="p1hf" style="width:100%;background:linear-gradient(90deg,#0088ff,#00f5ff)"></div></div>
      <div class="hns"><span id="p1hn">500</span><div class="sbw" style="max-width:160px;flex:1;margin:0 .4rem"><div class="sbf" id="p1sf" style="background:linear-gradient(90deg,#ffd700,#ffaa00)"></div></div><span style="font-size:.58rem;color:var(--g);font-family:'Orbitron',monospace">SP</span></div>
      <div class="wd" id="p1wd" style="color:#00f5ff"><div class="wdt"></div><div class="wdt"></div><div class="wdt"></div></div>
    </div>
    <div class="ch">
      <div id="rd">ROUND 1</div>
      <div id="td">100</div>
    </div>
    <div class="hs r">
      <div class="fn" id="p2fn" style="color:#ff2d78">NOVA-K</div>
      <div class="hbw"><div class="hbf" id="p2hf" style="width:100%;background:linear-gradient(270deg,#ff2d78,#ff6b9d);float:right"></div></div>
      <div class="hns" style="flex-direction:row-reverse"><span id="p2hn">500</span><div class="sbw" style="max-width:160px;flex:1;margin:0 .4rem"><div class="sbf" id="p2sf" style="background:linear-gradient(270deg,#ffd700,#ffaa00);float:right"></div></div><span style="font-size:.58rem;color:var(--g);font-family:'Orbitron',monospace">SP</span></div>
      <div class="wd" id="p2wd" style="color:#ff2d78;flex-direction:row-reverse;display:flex"><div class="wdt"></div><div class="wdt"></div><div class="wdt"></div></div>
    </div>
  </div>
  <div id="cw">
    <canvas id="gc"></canvas>
    <div id="ann"><div id="at"></div></div>
    <div id="cd"></div>
    <div id="sd"></div>
    <div id="mb">BOT vs BOT</div>
  </div>
</div>

<!-- RESULT -->
<div id="res" class="screen">
  <div class="bg-glow"></div>
  <div id="rt">GAME OVER</div>
  <div id="rs">MATCH COMPLETE</div>
  <div class="bgrp">
    <button class="btn bc" onclick="showCsel()">&#9664; NHAN VAT</button>
    <button class="btn bp" onclick="rematch()">&#8635; REMATCH</button>
    <button class="btn bg2" onclick="showTut()">&#128214; HUONG DAN</button>
  </div>
</div>

<script>
const canvas=document.getElementById('gc'),ctx=canvas.getContext('2d');
let W=0,H=0;
function resize(){const w=document.getElementById('cw');W=canvas.width=w.clientWidth||innerWidth;H=canvas.height=w.clientHeight||(innerHeight-62);}
window.addEventListener('resize',()=>{resize();if(gameRunning){p1F.applyLayout();p2F.applyLayout();}});

// ── CHARS ──
const CHARS=[
  {id:'cx',name:'CYBER-X',title:'Cyber Blade Fighter',c:'#00f5ff',c2:'#0088ff',c3:'#00ffcc',
   stats:{ATK:80,DEF:75,SPD:70},
   sp1:{key:'U',name:'Kiem Nang Luong',desc:'Luot ve phia truoc 20-28 DMG',type:'dash',dmg:[20,28],col:'#00f5ff'},
   sp2:{key:'I',name:'Loc Xoay',desc:'Xoay tai cho multi-hit 5x6',type:'spin',dmg:[6,6],col:'#00ffcc'},
   sup:{key:'O',name:'Bao Kiem',desc:'Kiem khong lo 55-65 DMG',dmg:[55,65]}},
  {id:'nk',name:'NOVA-K',title:'Plasma Striker',c:'#ff2d78',c2:'#ff6b9d',c3:'#ff00cc',
   stats:{ATK:85,DEF:65,SPD:85},
   sp1:{key:'U',name:'Plasma Burst',desc:'Ban cau lua 18-25 DMG',type:'proj',dmg:[18,25],col:'#ff2d78'},
   sp2:{key:'I',name:'Vu Dieu Lua',desc:'Cap da lua tu tren khong 22-30 DMG',type:'dive',dmg:[22,30],col:'#ff6b00'},
   sup:{key:'O',name:'Plasma Storm',desc:'Bung no plasma 60-70 DMG',dmg:[60,70]}},
  {id:'sh',name:'SHADOW',title:'Dark Ninja',c:'#00ff7f',c2:'#00cc55',c3:'#aaff00',
   stats:{ATK:90,DEF:55,SPD:95},
   sp1:{key:'U',name:'Ninja Slash',desc:'Bien mat roi xuat hien danh 25-32 DMG',type:'tele',dmg:[25,32],col:'#00ff7f'},
   sp2:{key:'I',name:'Shuriken x3',desc:'Nem 3 phi tieu 8x3 DMG',type:'triple',dmg:[8,8],col:'#aaff00'},
   sup:{key:'O',name:'Man Dem',desc:'Tan cong tu bong toi 55-68 DMG',dmg:[55,68]}},
  {id:'tt',name:'TITAN',title:'Iron Berserker',c:'#ff8c00',c2:'#ff4500',c3:'#ffd700',
   stats:{ATK:95,DEF:90,SPD:50},
   sp1:{key:'U',name:'Dam Sam',desc:'Soc song lan 28-38 DMG',type:'slam',dmg:[28,38],col:'#ff8c00'},
   sp2:{key:'I',name:'Dia Chan',desc:'Song chan knockback 20-28 DMG',type:'quake',dmg:[20,28],col:'#ff4500'},
   sup:{key:'O',name:'Rage Mode',desc:'Dien cuong 4 cu dam 65-75 DMG',dmg:[65,75]}},
  {id:'ph',name:'PHANTOM',title:'Void Mage',c:'#da70d6',c2:'#9b30ff',c3:'#ff88ff',
   stats:{ATK:88,DEF:60,SPD:78},
   sp1:{key:'U',name:'Void Blink',desc:'Dich chuyen sau lung 16-22 DMG',type:'blink',dmg:[16,22],col:'#da70d6'},
   sp2:{key:'I',name:'Void Beam',desc:'Tia xuyen suot 20-28 DMG',type:'beam',dmg:[20,28],col:'#9b30ff'},
   sup:{key:'O',name:'Bao Linh Hon',desc:'Linh hon bao quanh 60-70 DMG',dmg:[60,70]}},
];


const STAGES=[
  {id:'nether',name:'NETHER REALM',desc:'Chien truong dia nguc - cong dich chuyen huyen bi',img:'stages/nether.jpg',fog:'rgba(60,0,0,.28)',floorCol:'rgba(255,140,0,.7)',accent:'#ff8c00'},
  {id:'konoha',name:'LANG LA AN',desc:'San thuong lang la an - nui Hokage nhin xuong',img:'stages/konoha.jpg',fog:'rgba(135,206,235,.06)',floorCol:'rgba(80,200,80,.6)',accent:'#00cc55'},
  {id:'akatsuki',name:'CAN CU AKATSUKI',desc:'Chua toi - bao to do - khong co duong thoat',img:'stages/akatsuki.jpg',fog:'rgba(60,0,60,.3)',floorCol:'rgba(200,0,50,.7)',accent:'#ff2d78'},
  {id:'space',name:'KHONG GIAN DBZ',desc:'San dau noi vu tru - cac titan tung giao tranh',img:'stages/space.jpg',fog:'rgba(0,0,30,.35)',floorCol:'rgba(0,200,255,.65)',accent:'#00f5ff'},
  {id:'top',name:'GIAI VO DICH',desc:'Tournament of Power - san dau quyen nang nhat',img:'stages/top.jpg',fog:'rgba(20,0,50,.3)',floorCol:'rgba(160,80,255,.65)',accent:'#da70d6'},
];
let stageIdx = 0;
let _stImgs = {};
let gameMode = 'bvb', botSpd = 'normal', gameRunning = false, roundActive = false;
let roundTimer = 100, timerInt = null, p1W = 0, p2W = 0, curRound = 1, lastMode = 'bvb';
let aF = null, parts = [], projs = [], flash = 0, p1ci = 0, p2ci = 1, p1F, p2F;
const BR = { slow: .28, normal: .55, fast: .88, god: 1.5 };

function rnd(a,b){return a+Math.floor(Math.random()*(b-a+1));}

// ── SHADOW FIGHT 2 CLEAN ENGINE ──
let camShake = 0, hitstop = 0;

// Clean crisp martial arts sparks (no messy smoke clouds)
function sp(x, y, col, n = 8, big = false) {
  for (let i = 0; i < n; i++) {
    const a = Math.random() * Math.PI * 2;
    const s = (big ? 5.5 : 2.5) + Math.random() * 3.5;
    parts.push({
      x, y,
      vx: Math.cos(a) * s,
      vy: Math.sin(a) * s - (big ? 2.5 : 1),
      l: 1,
      d: 0.065 + Math.random() * 0.035, // rapidly dissolves in ~0.25s
      col,
      sz: (big ? 2.8 : 1.6) + Math.random() * 1.2
    });
  }
}

class Fighter {
  constructor(id, cd) {
    this.id = id; this.cd = cd; this.name = cd.name;
    this.c = cd.c; this.c2 = cd.c2; this.c3 = cd.c3;
    this.maxHp = 500; this.hp = 500; this.sp = 0;
    this.x = 0; this.y = 0; this.w = 0; this.h = 0;
    this.vx = 0; this.vy = 0; this.gr = true; this.fr = (id === 1);
    this.st = 'idle'; this.stT = 0; this.aType = ''; this.hbA = false;
    this.inv = 0; this.bl = false; this._hr = false; this._sup = false;
    this.combo = 0; this.sHits = 0; this.at = 0; this.bT = 0; this.pCd = 0;
    this.flipRot = 0; this.comboBuffer = null;
    this.slashArc = 0; // weapon slash arc progress
  }
  get fl() { return H * 0.82; }
  get cx() { return this.x + this.w / 2; }
  get cy() { return this.y + this.h / 2; }
  applyLayout() {
    this.h = H * 0.23;
    this.w = this.h * 0.52;
    if (this.gr) this.y = this.fl - this.h;
  }
  reset(xf) {
    this.hp = this.maxHp || 500; this.sp = 0;
    this.x = W * xf - this.w / 2; this.y = this.fl - this.h;
    this.vx = 0; this.vy = 0; this.st = 'idle'; this.stT = 0;
    this.hbA = false; this.inv = 0; this.bl = false; this.combo = 0;
    this.gr = true; this.fr = (this.id === 1); this.sHits = 0; this.pCd = 0;
    this.flipRot = 0; this.comboBuffer = null;
    this._hr = false; this._sup = false; this.slashArc = 0;
  }

  // Double tap dash & evasive dodge
  doDash(dir) {
    if (['hurt', 'knockdown', 'super'].includes(this.st)) return;
    const isFwd = (dir > 0 && this.fr) || (dir < 0 && !this.fr);
    if (isFwd) {
      this.st = 'dash'; this.stT = 14; this.vx = dir * 13;
      this.inv = 10; this.bl = false;
      sp(this.cx, this.fl - 4, this.c, 6, false);
    } else {
      this.st = 'dash_bwd'; this.stT = 12; this.vx = dir * 10.5; this.vy = -3;
      this.inv = 8; this.bl = false;
      sp(this.cx, this.fl - 4, this.c2, 5, false);
    }
  }

  // Acrobatic Jumps & Flips
  doJump(dir = 0) {
    if (!this.gr || ['hurt', 'knockdown', 'super', 'attack'].includes(this.st)) return;
    this.gr = false;
    if (dir === 0) {
      this.vy = -H * 0.023; this.st = 'jump'; this.flipRot = 0;
    } else {
      const isFwd = (dir > 0 && this.fr) || (dir < 0 && !this.fr);
      this.vy = -H * 0.0225;
      this.vx = dir * (isFwd ? 6.5 : 5.5) * (this.cd.stats.SPD / 70);
      this.st = isFwd ? 'flip_fwd' : 'flip_bwd';
      this.flipRot = 0;
    }
    sp(this.cx, this.fl - 2, this.c, 4, false);
  }

  // Crouch / Duck
  doCrouch() {
    if (!this.gr || ['attack', 'hurt', 'knockdown', 'super'].includes(this.st)) return;
    this.st = 'crouch'; this.bl = true;
  }

  // Light attacks
  doL(dir = 'neutral') {
    if (['hurt', 'knockdown', 'super'].includes(this.st)) return;
    if (!this.gr) { this.doAirKick(); return; }
    if (dir === 'fwd') { this._sa('lunge', rnd(12, 17), 20); return; }
    if (dir === 'bwd') { this._sa('counter', rnd(11, 16), 18); return; }
    if (dir === 'down') { this._sa('low', rnd(9, 14), 16); return; }
    if (this.st === 'attack' && ['jab_1', 'jab_2'].includes(this.aType)) {
      this.comboBuffer = this.aType === 'jab_1' ? 'jab_2' : 'jab_3';
      return;
    }
    this._sa('jab_1', rnd(9, 13), 15);
  }

  // Heavy attacks
  doH(dir = 'neutral') {
    if (['hurt', 'knockdown', 'super'].includes(this.st)) return;
    if (!this.gr) { this.doAirKick(true); return; }
    if (dir === 'down') { this._sa('sweep', rnd(12, 18), 26); return; } // Dragon Sweep
    if (dir === 'up') { this._sa('rising', rnd(16, 24), 25); return; } // Rising Dragon Upper
    if (dir === 'fwd') { this._sa('spin_kick', rnd(16, 23), 24); return; }
    this._sa('heavy', rnd(18, 25), 26);
  }

  // Acrobatic Strike (L)
  doS() {
    if (['hurt', 'knockdown', 'super'].includes(this.st)) return;
    this._sa('acrobatic', rnd(14, 20), 26);
    this.vx = (this.fr ? 1 : -1) * 7;
  }

  // Aerial Flying Jump Kick
  doAirKick(heavy = false) {
    if (['hurt', 'knockdown', 'super'].includes(this.st)) return;
    const d = this.fr ? 1 : -1;
    this._sa('air_kick', heavy ? rnd(17, 24) : rnd(13, 19), 24);
    this.vx = d * (heavy ? 9.0 : 7.8);
    this.vy = Math.min(this.vy, -1.2);
  }

  // Blocking
  doB(on) {
    if (!['attack', 'super', 'sp1', 'sp2', 'knockdown', 'hurt'].includes(this.st)) {
      this.bl = on;
      if (on && this.gr) this.st = 'block';
      else if (!on && this.st === 'block') this.st = 'idle';
    }
  }

  // Special 1 (lasts 1s = 60 frames)
  doSp1(en) {
    if (['attack', 'hurt', 'knockdown', 'super', 'sp1', 'sp2'].includes(this.st)) return;
    const s = this.cd.sp1;
    this.st = 'sp1'; this.stT = 60; this._spDur = 60;
    this._hr = false; this.hbA = false; this.bl = false; this.sHits = 0;
    ann2(s.name, this.c);
    if (s.type === 'dash') { const d = this.fr ? 1 : -1; this.vx = d * 13; }
    if (s.type === 'tele') {
      const d = this.fr ? 1 : -1; this.x = en.x - d * (this.w * 1.2);
      this.x = Math.max(0, Math.min(W - this.w, this.x));
      sp(this.cx, this.cy, this.c, 12, true);
    }
    if (s.type === 'blink') {
      const bx = this.fr ? en.x + en.w + 6 : en.x - this.w - 6;
      this.x = Math.max(0, Math.min(W - this.w, bx));
      sp(this.cx, this.cy, this.c, 12, true);
    }
    if (['proj', 'triple', 'beam'].includes(s.type)) { this.launch(s, en); }
    if (s.type === 'dive') { this.vy = -H * 0.019; this.vx = (this.fr ? 1 : -1) * 6.5; }
    sp(this.cx, this.cy, this.c, 10, true);
    camShake = 4;
  }

  // Special 2 (lasts 1s = 60 frames)
  doSp2(en) {
    if (['attack', 'hurt', 'knockdown', 'super', 'sp1', 'sp2'].includes(this.st)) return;
    const s = this.cd.sp2;
    this.st = 'sp2'; this.stT = 60; this._spDur = 60;
    this._hr = false; this.hbA = false; this.bl = false; this.sHits = 0;
    ann2(s.name, this.c);
    if (['proj', 'triple', 'beam'].includes(s.type)) { this.launch(s, en); }
    if (s.type === 'dive') { this.vy = -H * 0.019; this.vx = (this.fr ? 1 : -1) * 6.5; }
    sp(this.cx, this.cy, this.c3, 10, true);
    camShake = 4;
  }

  launch(s, en) {
    if (this.pCd > 0) return; this.pCd = 40;
    const d = this.fr ? 1 : -1, cnt = s.type === 'triple' ? 3 : 1;
    for (let i = 0; i < cnt; i++) {
      const spd = s.type === 'beam' ? 14 : 8.5, sy = (cnt === 3) ? (i - 1) * 5 : 0;
      projs.push({
        x: this.cx, y: this.cy - this.h * 0.3,
        vx: d * spd + sy * 0.3, vy: sy * 0.2,
        own: this.id, col: s.col || this.c,
        dmg: rnd(s.dmg[0], s.dmg[1]), l: 1.0, // 1 second lifetime
        w: s.type === 'beam' ? 24 : 11, h: s.type === 'beam' ? 8 : 11,
        tp: s.type, hit: false
      });
    }
    sp(this.cx, this.cy, this.c, 6, false);
  }

  // Super Mode (lasts 1s = 60 frames)
  doSuper(en) {
    if (this.sp < 100 || ['attack', 'hurt', 'knockdown', 'super', 'sp1', 'sp2'].includes(this.st)) return false;
    this.st = 'super'; this.stT = 60; this._spDur = 60; this.sp = 0; this.inv = 60; this._sup = false;
    ann2(this.cd.sup.name, this.c2);
    sp(this.cx, this.cy, this.c2, 16, true);
    camShake = 8;
    return true;
  }

  _sa(tp, d, dur) {
    if (['attack', 'hurt', 'knockdown', 'super', 'sp1', 'sp2'].includes(this.st) && this.st !== 'attack') return;
    this.st = 'attack'; this.aType = tp; this.stT = dur; this._durMax = dur;
    this._d = d; this._hr = false; this.hbA = false; this.bl = false; this.slashArc = 0;
  }

  hbox() {
    if (!this.hbA) return null;
    let r = this.w * 0.72, hy = this.y + this.h * 0.12, hh = this.h * 0.55;
    if (this.aType === 'sweep') {
      r = this.w * 0.92; hy = this.y + this.h * 0.65; hh = this.h * 0.32;
    } else if (this.aType === 'lunge') {
      r = this.w * 1.1;
    } else if (this.aType === 'air_kick') {
      r = this.w * 0.85; hy = this.y + this.h * 0.35; hh = this.h * 0.55;
    } else if (this.aType === 'rising') {
      r = this.w * 0.78; hy = this.y - this.h * 0.15; hh = this.h * 0.7;
    }
    return { x: this.fr ? this.cx : this.cx - r, y: hy, w: r, h: hh };
  }

  hits(e) {
    const b = this.hbox();
    if (!b) return false;
    let eh = e.h, ey = e.y;
    if (e.st === 'crouch') { eh = e.h * 0.45; ey = e.fl - eh; }
    return b.x < e.x + e.w && b.x + b.w > e.x && b.y < ey + eh && b.y + b.h > ey;
  }

  takeDmg(d, type = 'n') {
    if (this.inv > 0 || this.st === 'super') return 0;
    if (this.bl && type !== 'super') d = Math.ceil(d * 0.18);
    this.hp = Math.max(0, this.hp - d);
    this.sp = Math.min(100, this.sp + d * 0.44);

    if (!this.bl) {
      if (type === 'sweep') {
        this.st = 'knockdown'; this.stT = 30; this.inv = 24;
        this.vy = -H * 0.013; this.vx = (this.fr ? -1 : 1) * 6;
        this.gr = false;
        camShake = 6;
      } else if (type === 'heavy' || type === 'super' || type === 'quake') {
        this.st = 'hurt'; this.stT = 14; this.inv = 10;
        this.vy = -H * 0.01; this.vx = (this.fr ? -1 : 1) * 4;
        camShake = 4;
      } else {
        this.st = 'hurt'; this.stT = 10; this.inv = 7;
        this.vx = (this.fr ? -1 : 1) * 2.2;
      }
      hitstop = 3;
    }
    return d;
  }

  update(en) {
    this.at += 0.016;
    if (this.inv > 0) this.inv--;
    if (this.pCd > 0) this.pCd--;

    const fl = this.fl;
    this.vy += 0.58;
    this.y += this.vy;
    this.x += this.vx;
    this.vx *= 0.82;

    if (this.y + this.h >= fl) {
      this.y = fl - this.h;
      this.vy = 0;
      this.gr = true;
      if (['jump', 'flip_fwd', 'flip_bwd', 'air_kick'].includes(this.st)) {
        this.st = 'idle';
        this.flipRot = 0;
        sp(this.cx, fl - 2, this.c, 4, false);
      }
    } else {
      this.gr = false;
    }

    this.x = Math.max(0, Math.min(W - this.w, this.x));

    if (!['attack', 'super', 'sp1', 'sp2', 'dash', 'dash_bwd', 'flip_fwd', 'flip_bwd', 'knockdown'].includes(this.st)) {
      this.fr = en.cx > this.cx;
    }

    let hd = 0;

    switch (this.st) {
      case 'idle':
      case 'walk':
        this.hbA = false;
        this.st = Math.abs(this.vx) > 0.4 ? 'walk' : 'idle';
        break;
      case 'crouch':
      case 'block':
      case 'jump':
        this.hbA = false;
        break;
      case 'dash':
      case 'dash_bwd':
        this.hbA = false;
        if (--this.stT <= 0) this.st = 'idle';
        break;
      case 'flip_fwd':
        this.flipRot += 0.22;
        break;
      case 'flip_bwd':
        this.flipRot -= 0.22;
        break;
      case 'hurt':
        this.hbA = false;
        if (--this.stT <= 0) this.st = 'idle';
        break;
      case 'knockdown':
        this.hbA = false;
        this.flipRot += (this.fr ? -0.15 : 0.15);
        if (--this.stT <= 0) {
          this.st = 'idle'; this.flipRot = 0;
          sp(this.cx, fl - 4, this.c, 6, false);
        }
        break;
      case 'attack': {
        const dur = this._durMax || 20;
        const tt = dur - this.stT;
        this.hbA = tt >= Math.floor(dur * 0.3) && tt <= Math.floor(dur * 0.75);
        this.slashArc = this.hbA ? (tt / dur) : 0;

        if (this.hbA && !this._hr && this.hits(en)) {
          this._hr = true;
          hd = en.takeDmg(this._d, this.aType);
          this.sp = Math.min(100, this.sp + 8);
          this.combo++;
          sp(en.cx, en.cy, en.c, 10, this.aType === 'heavy' || this.aType === 'sweep');
        }

        if (--this.stT <= 0) {
          if (this.comboBuffer) {
            const next = this.comboBuffer; this.comboBuffer = null;
            this._sa(next, rnd(12, 18), next === 'jab_3' ? 22 : 16);
          } else {
            this.st = 'idle'; this.hbA = false; this.slashArc = 0;
          }
        }
        break;
      }
      case 'sp1':
      case 'sp2': {
        const si = this.st === 'sp1' ? 0 : 1;
        const s = si === 0 ? this.cd.sp1 : this.cd.sp2;
        this.stT--;
        this.hbA = this.stT >= 10 && this.stT <= 52;

        if (s.type === 'spin' && this.hbA && this.sHits < 6) {
          if (this.hits(en) && this.stT % 8 === 0) {
            const d = rnd(s.dmg[0], s.dmg[1]);
            hd += en.takeDmg(d, 'spin');
            this.sHits++;
            sp(en.cx, en.cy, this.c, 6, false);
          }
        } else if ((s.type === 'slam' || s.type === 'quake') && !this._hr && this.stT < 48) {
          this._hr = true;
          const d = rnd(s.dmg[0], s.dmg[1]);
          hd = en.takeDmg(d, s.type);
          sp(this.cx, this.fl - 4, this.c, 16, true);
          camShake = 6;
        } else if (['dash', 'tele', 'blink', 'dive'].includes(s.type) && this.hbA && !this._hr && this.hits(en)) {
          this._hr = true;
          const d = rnd(s.dmg[0], s.dmg[1]);
          hd = en.takeDmg(d, 'sp');
          sp(en.cx, en.cy, this.c2, 12, true);
          camShake = 5;
        }
        if (this.stT <= 0) { this.st = 'idle'; this.hbA = false; }
        break;
      }
      case 'super': {
        this.stT--;
        this.hbA = this.stT >= 10;
        if (!this._sup && this.stT < 48 && this.hits(en)) {
          this._sup = true;
          const sd = this.cd.sup.dmg, d = rnd(sd[0], sd[1]);
          hd = en.takeDmg(d, 'super');
          sp(en.cx, en.cy, this.c2, 22, true);
          sp(this.cx, this.cy, this.c, 14, true);
          camShake = 10;
        }
        if (this.stT <= 0) { this.st = 'idle'; this.hbA = false; }
        break;
      }
    }
    return hd;
  }

  // Draw clean, crisp Shadow Fight 2 silhouette
  draw() {
    const t = this.at, sw = this.w, sh = this.h;
    const u = sh / 100;
    const fl = this.fl;

    // 1. Neat Ground Shadow directly under feet (no giant horizontal bars)
    const distToGround = Math.max(0, fl - (this.y + sh));
    const shadowScale = Math.max(0.3, 1 - distToGround / (H * 0.3));
    ctx.save();
    ctx.globalAlpha = 0.4 * shadowScale;
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.ellipse(this.cx, fl, 26 * shadowScale, 5 * shadowScale, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();

    ctx.save();
    ctx.translate(this.cx, this.y + sh);
    if (!this.fr) ctx.scale(-1, 1);
    if (this.flipRot !== 0) {
      ctx.translate(0, -sh * 0.5);
      ctx.rotate(this.flipRot);
      ctx.translate(0, sh * 0.5);
    }

    const hf = this.st === 'hurt' && Math.floor(t * 12) % 2 === 0;
    const silCol = hf ? '#ffffff' : '#08090d';
    const edgeCol = this.c;

    // Poses calculation
    let hipY = -48 * u, hipX = 0;
    let spineRot = 0.05;
    let kneeL = { x: -8 * u, y: -24 * u }, footL = { x: -12 * u, y: 0 };
    let kneeR = { x: 10 * u, y: -24 * u }, footR = { x: 14 * u, y: 0 };
    let elL = { x: -10 * u, y: -64 * u }, handL = { x: -6 * u, y: -54 * u };
    let elR = { x: 14 * u, y: -66 * u }, handR = { x: 18 * u, y: -72 * u };

    if (this.st === 'idle') {
      const breath = Math.sin(t * 3.5) * 1.5 * u;
      hipY += breath;
      kneeL = { x: -9 * u, y: -24 * u + breath * 0.5 }; footL = { x: -13 * u, y: 0 };
      kneeR = { x: 11 * u, y: -24 * u + breath * 0.5 }; footR = { x: 14 * u, y: 0 };
      elL = { x: -11 * u, y: -66 * u + breath }; handL = { x: -4 * u, y: -58 * u + breath };
      elR = { x: 12 * u, y: -68 * u + breath }; handR = { x: 17 * u, y: -75 * u + breath };
    } else if (this.st === 'walk') {
      const legA = Math.sin(t * 13);
      hipY += Math.abs(legA) * 2 * u;
      kneeL = { x: -legA * 14 * u, y: -25 * u }; footL = { x: -legA * 18 * u, y: 0 };
      kneeR = { x: legA * 14 * u, y: -25 * u }; footR = { x: legA * 18 * u, y: 0 };
      elL = { x: legA * 10 * u - 8 * u, y: -66 * u }; handL = { x: legA * 12 * u, y: -58 * u };
      elR = { x: -legA * 10 * u + 12 * u, y: -68 * u }; handR = { x: -legA * 12 * u + 18 * u, y: -74 * u };
    } else if (this.st === 'crouch') {
      hipY = -24 * u; spineRot = 0.28;
      kneeL = { x: -18 * u, y: -14 * u }; footL = { x: -16 * u, y: 0 };
      kneeR = { x: 14 * u, y: -12 * u }; footR = { x: 20 * u, y: 0 };
      elL = { x: -8 * u, y: -40 * u }; handL = { x: 2 * u, y: -36 * u };
      elR = { x: 14 * u, y: -42 * u }; handR = { x: 18 * u, y: -46 * u };
    } else if (this.st === 'dash' || this.st === 'dash_bwd') {
      hipY = -34 * u; spineRot = this.st === 'dash' ? 0.38 : -0.22;
      kneeL = { x: -22 * u, y: -16 * u }; footL = { x: -26 * u, y: -6 * u };
      kneeR = { x: 18 * u, y: -14 * u }; footR = { x: 26 * u, y: 0 };
      elL = { x: -22 * u, y: -52 * u }; handL = { x: -30 * u, y: -44 * u };
      elR = { x: -12 * u, y: -54 * u }; handR = { x: -24 * u, y: -46 * u };
    } else if (this.st === 'jump' || this.st === 'flip_fwd' || this.st === 'flip_bwd') {
      hipY = -52 * u;
      kneeL = { x: -14 * u, y: -42 * u }; footL = { x: -8 * u, y: -28 * u };
      kneeR = { x: 12 * u, y: -44 * u }; footR = { x: 6 * u, y: -30 * u };
      elL = { x: -18 * u, y: -72 * u }; handL = { x: -12 * u, y: -82 * u };
      elR = { x: 18 * u, y: -72 * u }; handR = { x: 12 * u, y: -82 * u };
    } else if (this.st === 'attack') {
      const reach = Math.sin(((this._durMax - this.stT) / this._durMax) * Math.PI);
      if (['jab_1', 'jab_2', 'jab_3'].includes(this.aType)) {
        spineRot = 0.12;
        elR = { x: 16 * u + reach * 18 * u, y: -68 * u };
        handR = { x: 24 * u + reach * 28 * u, y: -72 * u };
      } else if (this.aType === 'lunge') {
        spineRot = 0.35; hipX = reach * 10 * u;
        elR = { x: 22 * u + reach * 26 * u, y: -64 * u };
        handR = { x: 30 * u + reach * 38 * u, y: -66 * u };
        kneeR = { x: 18 * u, y: -22 * u }; footR = { x: 28 * u, y: 0 };
      } else if (this.aType === 'sweep') {
        hipY = -22 * u; spineRot = 0.45;
        kneeL = { x: -14 * u, y: -10 * u }; footL = { x: -8 * u, y: 0 };
        kneeR = { x: 24 * u + reach * 20 * u, y: -8 * u };
        footR = { x: 36 * u + reach * 24 * u, y: -2 * u };
        handL = { x: -6 * u, y: -8 * u }; handR = { x: 6 * u, y: -8 * u };
      } else if (this.aType === 'rising') {
        spineRot = -0.15;
        kneeR = { x: 14 * u, y: -58 * u }; footR = { x: 20 * u, y: -82 * u };
        elR = { x: 16 * u, y: -78 * u }; handR = { x: 18 * u, y: -94 * u };
      } else if (this.aType === 'air_kick') {
        spineRot = -0.22;
        kneeR = { x: 24 * u, y: -38 * u }; footR = { x: 42 * u, y: -24 * u };
        kneeL = { x: -12 * u, y: -42 * u }; footL = { x: -6 * u, y: -28 * u };
        elR = { x: -14 * u, y: -64 * u }; handR = { x: -22 * u, y: -58 * u };
      } else if (this.aType === 'heavy' || this.aType === 'spin_kick') {
        spineRot = 0.18;
        kneeR = { x: 18 * u + reach * 14 * u, y: -42 * u };
        footR = { x: 28 * u + reach * 24 * u, y: -52 * u };
        elR = { x: 16 * u + reach * 16 * u, y: -70 * u };
        handR = { x: 24 * u + reach * 24 * u, y: -76 * u };
      } else if (this.aType === 'acrobatic') {
        spineRot = 0.4;
        kneeR = { x: 22 * u, y: -48 * u }; footR = { x: 34 * u, y: -62 * u };
        elR = { x: 18 * u, y: -72 * u }; handR = { x: 28 * u, y: -80 * u };
      }
    } else if (this.st === 'knockdown') {
      hipY = -12 * u; spineRot = -0.55;
      kneeL = { x: -16 * u, y: -24 * u }; footL = { x: -24 * u, y: -36 * u };
      kneeR = { x: 8 * u, y: -26 * u }; footR = { x: 14 * u, y: -38 * u };
      elL = { x: -14 * u, y: -32 * u }; handL = { x: -22 * u, y: -42 * u };
      elR = { x: 10 * u, y: -34 * u }; handR = { x: 16 * u, y: -44 * u };
    } else if (this.st === 'block') {
      spineRot = -0.06;
      elL = { x: 8 * u, y: -68 * u }; handL = { x: 14 * u, y: -76 * u };
      elR = { x: 12 * u, y: -66 * u }; handR = { x: 16 * u, y: -74 * u };
    }

    // Chest & Head
    const chestX = hipX + Math.sin(spineRot) * 22 * u;
    const chestY = hipY - Math.cos(spineRot) * 22 * u;
    const neckX = chestX + Math.sin(spineRot) * 11 * u;
    const neckY = chestY - Math.cos(spineRot) * 11 * u;
    const headX2 = neckX + Math.sin(spineRot) * 9 * u;
    const headY2 = neckY - Math.cos(spineRot) * 9 * u;

    // 1. BACK LEG
    this.drawLimb(hipX - 5 * u, hipY, kneeL.x, kneeL.y, footL.x, footL.y, 8.5 * u, 7.5 * u, silCol);
    // 2. BACK ARM + WEAPON
    this.drawLimb(chestX - 6 * u, chestY - 2 * u, elL.x, elL.y, handL.x, handL.y, 7 * u, 6 * u, silCol);
    this.drawWeapon(handL.x, handL.y, elL.x, elL.y, this.cd.id, false);

    // 3. TORSO
    ctx.fillStyle = silCol;
    ctx.beginPath();
    ctx.moveTo(chestX - 9 * u, chestY - 5 * u);
    ctx.lineTo(chestX + 10 * u, chestY - 3 * u);
    ctx.lineTo(hipX + 6.5 * u, hipY + 4 * u);
    ctx.lineTo(hipX - 6.5 * u, hipY + 4 * u);
    ctx.closePath();
    ctx.fill();

    // Belt Obi & Hanging ribbon
    ctx.fillStyle = silCol;
    ctx.fillRect(hipX - 7 * u, hipY, 14 * u, 4.5 * u);
    ctx.fillStyle = edgeCol;
    ctx.fillRect(hipX + 2 * u, hipY + 1 * u, 3 * u, 3 * u);
    ctx.strokeStyle = edgeCol; ctx.lineWidth = 2 * u;
    ctx.beginPath();
    ctx.moveTo(hipX + 2 * u, hipY + 4 * u);
    ctx.lineTo(hipX + 4 * u, hipY + 12 * u);
    ctx.stroke();

    // 4. FRONT LEG
    this.drawLimb(hipX + 4 * u, hipY, kneeR.x, kneeR.y, footR.x, footR.y, 9.5 * u, 8 * u, silCol);

    // 5. HEAD & NINJA MASK
    ctx.fillStyle = silCol;
    ctx.beginPath();
    ctx.ellipse(headX2, headY2, 7.5 * u, 8.5 * u, spineRot, 0, Math.PI * 2);
    ctx.fill();

    // Cowl / Horns
    if (this.cd.id === 'tt') {
      ctx.fillStyle = silCol;
      ctx.beginPath();
      ctx.moveTo(headX2 - 4 * u, headY2 - 6 * u);
      ctx.lineTo(headX2 - 12 * u, headY2 - 18 * u);
      ctx.lineTo(headX2 - 1 * u, headY2 - 8 * u);
      ctx.closePath(); ctx.fill();
      ctx.beginPath();
      ctx.moveTo(headX2 + 3 * u, headY2 - 6 * u);
      ctx.lineTo(headX2 + 11 * u, headY2 - 18 * u);
      ctx.lineTo(headX2 + 5 * u, headY2 - 8 * u);
      ctx.closePath(); ctx.fill();
    } else if (this.cd.id === 'ph') {
      ctx.beginPath();
      ctx.arc(headX2, headY2 - 2 * u, 9.5 * u, Math.PI * 0.8, Math.PI * 2.2);
      ctx.fill();
    }

    // ELEGANT HEADBAND RIBBONS (Clean quadratic curve, 100% stable, no physics explosion)
    const ribSway = Math.sin(t * 7) * 3 * u;
    const ribVx = (this.vx * 1.5);
    ctx.save();
    ctx.strokeStyle = edgeCol; ctx.lineWidth = 2.4; ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(headX2 - 5 * u, headY2 - 1 * u);
    ctx.quadraticCurveTo(headX2 - 14 * u, headY2 - 4 * u + ribSway, headX2 - 22 * u - ribVx, headY2 - 2 * u + ribSway);
    ctx.stroke();
    ctx.strokeStyle = '#08090d'; ctx.lineWidth = 1.8;
    ctx.beginPath();
    ctx.moveTo(headX2 - 5 * u, headY2 + 1 * u);
    ctx.quadraticCurveTo(headX2 - 12 * u, headY2 + 2 * u + ribSway, headX2 - 18 * u - ribVx, headY2 + 4 * u + ribSway);
    ctx.stroke();
    ctx.restore();

    // PIERCING GLOWING EYES
    const eyeX = headX2 + 2.5 * u, eyeY = headY2 - 1.2 * u;
    ctx.save();
    ctx.fillStyle = edgeCol; ctx.shadowColor = edgeCol; ctx.shadowBlur = 8;
    ctx.beginPath();
    ctx.ellipse(eyeX, eyeY, 3.6 * u, 1.3 * u, 0.22, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.ellipse(eyeX + 0.6 * u, eyeY, 1.4 * u, 0.7 * u, 0.22, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();

    // 6. FRONT ARM + MAIN WEAPON
    this.drawLimb(chestX + 6 * u, chestY - 2 * u, elR.x, elR.y, handR.x, handR.y, 8 * u, 6.8 * u, silCol);
    this.drawWeapon(handR.x, handR.y, elR.x, elR.y, this.cd.id, true);

    // Dynamic clean weapon slash arc (crescent trail, not giant circles)
    if (this.hbA && this.st === 'attack') {
      ctx.save();
      ctx.strokeStyle = edgeCol; ctx.lineWidth = 3.5;
      ctx.shadowColor = edgeCol; ctx.shadowBlur = 10;
      ctx.globalAlpha = 0.8;
      ctx.beginPath();
      ctx.arc(handR.x + 12 * u, handR.y - 4 * u, 22 * u, -Math.PI * 0.38, Math.PI * 0.38);
      ctx.stroke();
      ctx.restore();
    }

    // Blocking Ward
    if (this.bl) {
      ctx.save();
      ctx.strokeStyle = edgeCol; ctx.lineWidth = 2.5;
      ctx.shadowColor = edgeCol; ctx.shadowBlur = 10;
      ctx.globalAlpha = 0.6;
      ctx.beginPath();
      ctx.arc(20 * u, -52 * u, 24 * u, -Math.PI * 0.4, Math.PI * 0.4);
      ctx.stroke();
      ctx.restore();
    }

    // Localized Aura Ring during Super (lasts 1s, clean and compact)
    if (this.st === 'super') {
      const prog = (60 - this.stT) / 60;
      ctx.save();
      ctx.strokeStyle = this.c2; ctx.lineWidth = 3;
      ctx.shadowColor = this.c2; ctx.shadowBlur = 14;
      ctx.globalAlpha = 0.65 * (1 - prog * 0.3);
      ctx.beginPath();
      ctx.arc(0, -sh * 0.48, sw * (0.55 + 0.25 * Math.sin(prog * Math.PI)), 0, Math.PI * 2);
      ctx.stroke();
      ctx.restore();
    }

    // Localized Aura during Special 1 & 2 (lasts 1s)
    if (this.st === 'sp1' || this.st === 'sp2') {
      const prog = (60 - this.stT) / 60;
      ctx.save();
      ctx.strokeStyle = this.st === 'sp1' ? this.c : this.c3;
      ctx.lineWidth = 2.5; ctx.shadowColor = this.c; ctx.shadowBlur = 12;
      ctx.globalAlpha = 0.6 * (1 - prog * 0.25);
      ctx.beginPath();
      ctx.arc(0, -sh * 0.48, sw * (0.48 + 0.2 * Math.sin(prog * Math.PI)), 0, Math.PI * 2);
      ctx.stroke();
      ctx.restore();
    }

    ctx.restore();
  }

  drawLimb(x1, y1, x2, y2, x3, y3, th1, th2, col) {
    ctx.save();
    ctx.strokeStyle = col;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.lineWidth = th1;
    ctx.beginPath();
    ctx.moveTo(x1, y1); ctx.lineTo(x2, y2);
    ctx.stroke();
    ctx.lineWidth = th2;
    ctx.beginPath();
    ctx.moveTo(x2, y2); ctx.lineTo(x3, y3);
    ctx.stroke();
    ctx.restore();
  }

  drawWeapon(hx, hy, ex, ey, charId, isFront) {
    const dx = hx - ex, dy = hy - ey;
    const angle = Math.atan2(dy, dx);
    const u = this.h / 100;
    ctx.save();
    ctx.translate(hx, hy);
    ctx.rotate(angle);

    const edgeCol = this.c;
    ctx.shadowColor = edgeCol;
    ctx.shadowBlur = 6;

    if (charId === 'cx') {
      const len = isFront ? 36 * u : 24 * u;
      ctx.fillStyle = '#111218';
      ctx.fillRect(-5 * u, -1.8 * u, 7 * u, 3.6 * u);
      ctx.fillStyle = edgeCol;
      ctx.fillRect(2 * u, -4 * u, 2 * u, 8 * u);
      ctx.fillStyle = '#08090d';
      ctx.beginPath();
      ctx.moveTo(4 * u, -1.8 * u);
      ctx.lineTo(len - 4 * u, -1.2 * u);
      ctx.lineTo(len, 0);
      ctx.lineTo(len - 4 * u, 2 * u);
      ctx.lineTo(4 * u, 1.8 * u);
      ctx.closePath(); ctx.fill();
      ctx.strokeStyle = edgeCol; ctx.lineWidth = 1.5 * u;
      ctx.beginPath();
      ctx.moveTo(4 * u, -1.8 * u);
      ctx.lineTo(len - 4 * u, -1.2 * u);
      ctx.lineTo(len, 0);
      ctx.stroke();
    } else if (charId === 'nk') {
      const len = 25 * u;
      ctx.fillStyle = '#08090d';
      ctx.fillRect(-6 * u, -1.8 * u, 10 * u, 3.6 * u);
      ctx.strokeStyle = edgeCol; ctx.lineWidth = 2 * u;
      ctx.beginPath();
      ctx.moveTo(0, -2.5 * u); ctx.lineTo(len, -1.8 * u);
      ctx.moveTo(0, 2.5 * u); ctx.lineTo(len * 0.7, 2.5 * u);
      ctx.stroke();
    } else if (charId === 'sh') {
      if (isFront) {
        const len = 32 * u;
        ctx.fillStyle = '#08090d';
        ctx.fillRect(-5 * u, -1.8 * u, 7 * u, 3.6 * u);
        ctx.fillRect(2 * u, -1.8 * u, len - 2 * u, 3.6 * u);
        ctx.strokeStyle = edgeCol; ctx.lineWidth = 1.8 * u;
        ctx.beginPath();
        ctx.moveTo(2 * u, -1.8 * u); ctx.lineTo(len, -1.8 * u);
        ctx.stroke();
      } else {
        ctx.fillStyle = '#08090d';
        ctx.fillRect(-4 * u, -1.5 * u, 12 * u, 3 * u);
        ctx.strokeStyle = edgeCol; ctx.lineWidth = 2 * u;
        ctx.beginPath();
        ctx.arc(6 * u, 5 * u, 8 * u, -Math.PI * 0.4, Math.PI * 0.4);
        ctx.stroke();
      }
    } else if (charId === 'tt') {
      const len = isFront ? 42 * u : 30 * u;
      ctx.fillStyle = '#08090d';
      ctx.fillRect(-7 * u, -2.5 * u, 10 * u, 5 * u);
      ctx.fillRect(3 * u, -4 * u, len - 3 * u, 8 * u);
      ctx.strokeStyle = edgeCol; ctx.lineWidth = 2 * u;
      ctx.strokeRect(3 * u, -4 * u, len - 3 * u, 8 * u);
    } else if (charId === 'ph') {
      const len = 38 * u;
      ctx.fillStyle = '#08090d';
      ctx.fillRect(-8 * u, -1.5 * u, len + 8 * u, 3 * u);
      ctx.strokeStyle = edgeCol; ctx.lineWidth = 2.5 * u;
      ctx.beginPath();
      ctx.arc(len - 4 * u, 10 * u, 14 * u, -Math.PI * 0.8, -Math.PI * 0.1);
      ctx.stroke();
    }
    ctx.restore();
  }
}

// ── INPUT HANDLING ──
const keys = {};
let pk = {};
let lastKeyA = 0, lastKeyD = 0;

window.addEventListener('keydown', e => {
  keys[e.code] = true;
  if (['Space', 'ArrowUp', 'ArrowDown'].includes(e.code)) e.preventDefault();

  if (roundActive && gameMode === 'pvb' && p1F) {
    const now = Date.now();
    if (e.code === 'KeyA') {
      if (now - lastKeyA < 260) { p1F.doDash(-1); }
      lastKeyA = now;
    } else if (e.code === 'KeyD') {
      if (now - lastKeyD < 260) { p1F.doDash(1); }
      lastKeyD = now;
    } else if (e.code === 'ShiftLeft' || e.code === 'ShiftRight') {
      const d = keys['KeyA'] ? -1 : (keys['KeyD'] ? 1 : (p1F.fr ? 1 : -1));
      p1F.doDash(d);
    }
  }
}, { passive: false });

window.addEventListener('keyup', e => {
  keys[e.code] = false;
  if (e.code === 'KeyS' && p1F && p1F.st === 'crouch') {
    p1F.st = 'idle'; p1F.bl = false;
  }
});

function jp(c) { return keys[c] && !pk[c]; }

function handleInput() {
  if (!roundActive || gameMode !== 'pvb') return;
  const f = p1F;
  if (['hurt', 'knockdown', 'super'].includes(f.st)) { pk = { ...keys }; return; }

  const spd = 4.8 * (f.cd.stats.SPD / 70);
  if (keys['KeyA']) f.vx = -spd;
  if (keys['KeyD']) f.vx = spd;

  if (jp('KeyW')) {
    if (keys['KeyD']) f.doJump(1);
    else if (keys['KeyA']) f.doJump(-1);
    else f.doJump(0);
  }

  if (keys['KeyS'] && !keys['KeyJ'] && !keys['KeyK'] && !keys['KeyL'] && !keys['KeyU'] && !keys['KeyI'] && !keys['KeyO']) {
    f.doCrouch();
  } else if (!keys['KeyS'] && f.st === 'crouch') {
    f.st = 'idle'; f.bl = false;
  }

  if (jp('KeyJ')) {
    if (!f.gr || keys['KeyW']) f.doAirKick(false);
    else if (keys['KeyS']) f.doL('down');
    else if (keys['KeyD']) f.doL('fwd');
    else if (keys['KeyA']) f.doL('bwd');
    else f.doL('neutral');
  }

  if (jp('KeyK')) {
    if (!f.gr) f.doAirKick(true);
    else if (keys['KeyS']) f.doH('down');
    else if (keys['KeyW']) f.doH('up');
    else if (keys['KeyD']) f.doH('fwd');
    else f.doH('neutral');
  }

  if (jp('KeyL')) f.doS();
  if (jp('KeyU')) f.doSp1(p2F);
  if (jp('KeyI')) f.doSp2(p2F);
  if (jp('KeyO')) { f.doSuper(p2F); }

  pk = { ...keys };
}

// ── BOT AI ──
function botAI(bot, en) {
  if (!roundActive || ['hurt', 'knockdown', 'super'].includes(bot.st)) return;
  const r = BR[botSpd];
  bot.bT -= r;
  if (bot.bT > 0) return;
  bot.bT = 7 + Math.random() * 18 / r;

  const dist = Math.abs(bot.cx - en.cx);
  const opt = bot.w * 1.35;
  const hpP = bot.hp / (bot.maxHp || 500), spP = bot.sp / 100;

  if (spP >= 1 && en.st !== 'super' && Math.random() < 0.65) {
    if (bot.doSuper(en)) return;
  }

  if (en.hbA && en.st === 'attack') {
    const rv = Math.random();
    if (rv < 0.35) { bot.doCrouch(); return; }
    if (rv < 0.6) { bot.doDash(en.cx > bot.cx ? -1 : 1); return; }
    if (rv < 0.8) { bot.doJump(en.cx > bot.cx ? -1 : 1); return; }
    bot.doB(true); return;
  }
  bot.doB(false);

  if (!bot.gr && Math.random() < 0.75) {
    bot.doAirKick(Math.random() < 0.5);
    return;
  }

  if (dist < opt * 2.5 && Math.random() < 0.28 * r) {
    if (Math.random() < 0.5 && bot.pCd === 0) { bot.doSp1(en); return; }
    if (Math.random() < 0.45) { bot.doSp2(en); return; }
  }

  if (dist > opt * 2.8) {
    if (Math.random() < 0.35 * r) {
      bot.doDash(en.cx > bot.cx ? 1 : -1);
    } else {
      en.cx > bot.cx ? bot.vx = 4.5 * (bot.cd.stats.SPD / 70) : bot.vx = -4.5 * (bot.cd.stats.SPD / 70);
    }
  } else if (dist > opt * 1.5) {
    if (Math.random() < 0.28) {
      bot.doJump(en.cx > bot.cx ? 1 : -1);
    } else {
      en.cx > bot.cx ? bot.vx = 3.6 * (bot.cd.stats.SPD / 70) : bot.vx = -3.6 * (bot.cd.stats.SPD / 70);
    }
  } else {
    const rv = Math.random();
    if (rv < 0.28) bot.doL('neutral');
    else if (rv < 0.46) bot.doH('down');
    else if (rv < 0.64) bot.doH('neutral');
    else if (rv < 0.76) bot.doS();
    else if (rv < 0.88) bot.doL('fwd');
    else { bot.doDash(en.cx > bot.cx ? -1 : 1); }
  }
}

function updProjs(){
  for(let i=projs.length-1;i>=0;i--){
    const p=projs[i];p.x+=p.vx;p.y+=p.vy;p.l-=.025; // dissolves cleanly in ~0.6s
    const tgt=p.own===1?p2F:p1F;
    if(!p.hit&&p.x<tgt.x+tgt.w&&p.x+p.w>tgt.x&&p.y<tgt.y+tgt.h&&p.y+p.h>tgt.y){
      p.hit=true;tgt.takeDmg(p.dmg,'proj');sp(p.x,p.y,p.col,8,false);
      projs.splice(i,1);continue;
    }
    if(p.l<=0||p.x<-40||p.x>W+40){projs.splice(i,1);continue;}
    ctx.globalAlpha=Math.max(0,Math.min(1,p.l*2.5));
    ctx.fillStyle=p.col;ctx.shadowColor=p.col;ctx.shadowBlur=8;
    if(p.tp==='beam')ctx.fillRect(p.x-p.w/2,p.y-p.h/2,p.w,p.h);
    else{ctx.beginPath();ctx.arc(p.x,p.y,p.w/2,0,Math.PI*2);ctx.fill();}
    ctx.shadowBlur=0;ctx.globalAlpha=1;
  }
}

// Background
function drawBG(){
  const _st=STAGES[stageIdx];
  const _si=_stImgs[_st.id];
  if(_si&&_si.complete&&_si.naturalWidth>0){
    ctx.drawImage(_si,0,0,W,H);
    ctx.fillStyle=_st.fog||'rgba(0,0,10,.25)';ctx.fillRect(0,0,W,H);
  } else {
    const sky=ctx.createLinearGradient(0,0,0,H);
    sky.addColorStop(0,'#020010');sky.addColorStop(.55,'#080022');sky.addColorStop(1,'#0f0033');
    ctx.fillStyle=sky;ctx.fillRect(0,0,W,H);
  }
  // Stage image is the background; skip procedural city
  const fy=H*.82;
  const fg=ctx.createLinearGradient(0,fy,0,H);
  fg.addColorStop(0,'rgba(0,245,255,.11)');fg.addColorStop(1,'rgba(0,245,255,.01)');
  ctx.fillStyle=fg;ctx.fillRect(0,fy,W,H-fy);
  ctx.strokeStyle='rgba(0,245,255,.09)';ctx.lineWidth=.5;
  for(let i=0;i<=20;i++){const x=(i/20)*W;ctx.beginPath();ctx.moveTo(x,fy);ctx.lineTo(W/2+(x-W/2)*.07,H);ctx.stroke();}
  for(let j=1;j<=7;j++){const y=fy+(H-fy)*(j/7);ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();}
  const _fc=STAGES[stageIdx].floorCol||'rgba(0,245,255,.65)';
  ctx.shadowColor=_fc;ctx.shadowBlur=14;ctx.strokeStyle=_fc;ctx.lineWidth=2;
  ctx.beginPath();ctx.moveTo(0,fy);ctx.lineTo(W,fy);ctx.stroke();ctx.shadowBlur=0;
  // White flash disabled
  flash = 0;
}

function drawParts(){
  parts=parts.filter(p=>p.l>0);
  for(const p of parts){
    p.x+=p.vx;p.y+=p.vy;p.vy+=.14;p.l-=p.d;
    ctx.globalAlpha=Math.max(0,p.l);ctx.fillStyle=p.col;ctx.shadowColor=p.col;ctx.shadowBlur=7;
    ctx.beginPath();ctx.arc(p.x,p.y,p.sz*p.l,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
  }ctx.globalAlpha=1;
}

function updHUD(){
  const m1=p1F.maxHp||500,m2=p2F.maxHp||500;
  document.getElementById('p1hf').style.width=Math.max(0,(p1F.hp/m1*100))+'%';
  document.getElementById('p2hf').style.width=Math.max(0,(p2F.hp/m2*100))+'%';
  document.getElementById('p1hn').textContent=Math.max(0,Math.round(p1F.hp));
  document.getElementById('p2hn').textContent=Math.max(0,Math.round(p2F.hp));
  document.getElementById('p1sf').style.width=p1F.sp+'%';
  document.getElementById('p2sf').style.width=p2F.sp+'%';
  const td=document.getElementById('td');td.textContent=Math.ceil(roundTimer);td.classList.toggle('u',roundTimer<=10);
}
function updWD(){
  document.querySelectorAll('#p1wd .wdt').forEach((d,i)=>d.classList.toggle('f',i<p1W));
  document.querySelectorAll('#p2wd .wdt').forEach((d,i)=>d.classList.toggle('f',i<p2W));
}

function announce(txt,col='#fff',dur=1400){
  const el=document.getElementById('at');
  el.textContent=txt;el.style.color=col;el.style.textShadow=`0 0 38px ${col},0 0 75px ${col}`;
  el.classList.add('show');
  return new Promise(r=>setTimeout(()=>{el.classList.remove('show');setTimeout(r,280);},dur));
}
let _at=null;
function ann2(n,col){
  const el=document.getElementById('sd');
  if(!el)return;
  el.textContent=n;el.style.color=col;el.style.textShadow=`0 0 20px ${col}, 0 0 40px ${col}`;
  el.style.opacity='1';
  clearTimeout(_at);
  _at=setTimeout(()=>{el.style.opacity='0';},800);
}
let _ct=null;
function showCombo(who,n){
  const el=document.getElementById('cd');if(n<2){el.style.opacity='0';return;}
  el.textContent=n+' HIT COMBO!';el.style.color=who===1?p1F.c:p2F.c;el.style.opacity='1';
  clearTimeout(_ct);_ct=setTimeout(()=>el.style.opacity='0',850);
}

let isTransitioningRound = false;

function gameLoop(){
  if(!gameRunning) return;
  aF = requestAnimationFrame(gameLoop);
  p1F.applyLayout(); p2F.applyLayout();

  // Screen shake calculation
  let camX = 0, camY = 0;
  if(camShake > 0){
    camX = (Math.random() - 0.5) * camShake;
    camY = (Math.random() - 0.5) * camShake;
    camShake *= 0.84;
    if(camShake < 0.5) camShake = 0;
  }

  // Hitstop pause
  if(hitstop > 0){
    hitstop--;
  } else {
    if(roundActive){
      handleInput();
      botAI(p2F, p1F);
      if(gameMode === 'bvb') botAI(p1F, p2F);
      const d2 = p1F.update(p2F), d1 = p2F.update(p1F);
      if(d2 > 0) showCombo(1, p1F.combo);
      if(d1 > 0) showCombo(2, p2F.combo);
      if(!['attack','sp1','sp2','super'].includes(p1F.st)) p1F.combo = 0;
      if(!['attack','sp1','sp2','super'].includes(p2F.st)) p2F.combo = 0;
    } else {
      // Keep fighters firmly placed on floor during round announcements
      p1F.vx = 0; p1F.vy = 0;
      p2F.vx = 0; p2F.vy = 0;
      p1F.y = p1F.fl - p1F.h;
      p2F.y = p2F.fl - p2F.h;
      p1F.st = 'idle'; p2F.st = 'idle';
      p1F.update(p2F);
      p2F.update(p1F);
    }
  }

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.save();
  if(camX !== 0 || camY !== 0) ctx.translate(camX, camY);
  drawBG();
  p1F.draw();
  p2F.draw();
  updProjs();
  drawParts();
  ctx.restore();

  updHUD();
  if(roundActive && (p1F.hp <= 0 || p2F.hp <= 0)) {
    endRound('ko');
  }
}

async function startRound(){
  roundActive = false;
  clearInterval(timerInt);
  timerInt = null;

  // Fully restore both fighters to 100% HP and initial fighting stance
  p1F.reset(0.27);
  p2F.reset(0.73);
  p1F.applyLayout();
  p2F.applyLayout();
  p1F.hp = p1F.maxHp || 500;
  p2F.hp = p2F.maxHp || 500;
  p1F.sp = 0;
  p2F.sp = 0;
  p1F.st = 'idle';
  p2F.st = 'idle';
  p1F.inv = 0;
  p2F.inv = 0;
  p1F.combo = 0;
  p2F.combo = 0;
  p1F.slashTrails = [];
  p2F.slashTrails = [];

  // Clear all residual projectiles, particles, and ghosts
  parts = []; projs = []; ghosts = [];
  hitstop = 0; camShake = 0; flash = 0;

  // Reset timer & display
  roundTimer = 100;
  document.getElementById('rd').textContent = 'ROUND ' + curRound;
  updHUD();
  updWD();

  // Hide any lingering banners
  const sd = document.getElementById('sd'); if(sd) sd.style.opacity = '0';
  const cd = document.getElementById('cd'); if(cd) cd.style.opacity = '0';

  // Announce new round
  await announce('ROUND ' + curRound, '#ffd700', 950);
  await announce('FIGHT!', p1F.c, 650);

  // Guarantee positions and start combat
  p1F.reset(0.27);
  p2F.reset(0.73);
  p1F.applyLayout();
  p2F.applyLayout();
  updHUD();

  roundActive = true;
  timerInt = setInterval(() => {
    if(!roundActive) return;
    roundTimer--;
    if(roundTimer <= 0){
      roundTimer = 0;
      endRound('time');
    }
    const td = document.getElementById('td');
    if(td){
      td.textContent = Math.ceil(roundTimer);
      td.classList.toggle('u', roundTimer <= 10);
    }
  }, 1000);
}

async function endRound(reason){
  if(isTransitioningRound || !roundActive) return;
  isTransitioningRound = true;
  roundActive = false;
  clearInterval(timerInt);
  timerInt = null;

  let w = 0;
  if(reason === 'time') w = p1F.hp > p2F.hp ? 1 : (p2F.hp > p1F.hp ? 2 : 0);
  else w = p1F.hp <= 0 ? 2 : 1;

  if(w === 1) p1W++;
  else if(w === 2) p2W++;
  updWD();

  const col = w === 1 ? p1F.c : (w === 2 ? p2F.c : '#ffd700');
  if(w === 0) await announce('DRAW!', '#ffd700', 1200);
  else await announce('K.O.!', col, 1000);

  if(p1W >= 2 || p2W >= 2) {
    await endMatch();
  } else {
    curRound++;
    await new Promise(r => setTimeout(r, 400));
    await startRound(); // Properly restores the next round!
  }
  isTransitioningRound = false;
}

async function endMatch(){
  gameRunning=false;const wf=p1W>p2W?p1F:p2F;
  await announce(wf.name+' WINS!',wf.c,1900);
  cancelAnimationFrame(aF);
  const rt=document.getElementById('rt');
  rt.textContent=wf.name+' WINS!';
  rt.style.background=`linear-gradient(135deg,${wf.c},${wf.c2})`;
  rt.style['-webkit-background-clip']='text';rt.style['-webkit-text-fill-color']='transparent';rt.style['background-clip']='text';
  document.getElementById('rs').textContent=`${p1W} - ${p2W} | MATCH COMPLETE`;
  showScr('res');
}

function showScr(id){document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));document.getElementById(id).classList.add('active');}
function showTut(){cancelAnimationFrame(aF);clearInterval(timerInt);gameRunning=false;showScr('tut');}
function showCsel(){showScr('csel');}
function setSp(s){botSpd=s;document.querySelectorAll('.sb').forEach(b=>{const t=b.textContent.trim().toLowerCase();b.classList.toggle('act',t===s||(s==='god'&&t.includes('god')));});}

function startGame(mode){
  gameMode=mode;lastMode=mode;p1W=0;p2W=0;curRound=1;parts=[];projs=[];flash = 0;
  showScr('game');resize();
  const c1=CHARS[p1ci],c2=CHARS[p2ci];
  p1F=new Fighter(1,c1);p2F=new Fighter(2,c2);p1F.applyLayout();p2F.applyLayout();
  document.getElementById('p1fn').textContent=c1.name;document.getElementById('p1fn').style.color=c1.c;
  document.getElementById('p1hf').style.background=`linear-gradient(90deg,${c1.c2},${c1.c})`;
  document.getElementById('p1wd').style.color=c1.c;
  document.getElementById('p2fn').textContent=c2.name;document.getElementById('p2fn').style.color=c2.c;
  document.getElementById('p2hf').style.background=`linear-gradient(270deg,${c2.c2},${c2.c})`;
  document.getElementById('p2wd').style.color=c2.c;
  document.getElementById('mb').textContent=mode==='pvb'?`PLAYER(${c1.name}) vs BOT(${c2.name})`:`BOT(${c1.name}) vs BOT(${c2.name})`;
  gameRunning=true;aF=requestAnimationFrame(gameLoop);startRound();
}

function rematch(){startGame(lastMode);}

// Char select UI

function preloadStages(){STAGES.forEach(s=>{const i=new Image();i.src=s.img;_stImgs[s.id]=i;});}
function buildStageUI(){
  const g=document.getElementById('sgrid');g.innerHTML='';
  STAGES.forEach((s,i)=>{
    const c=document.createElement('div');c.className='scard'+(i===stageIdx?' sel':'');
    const img=document.createElement('img');img.src=s.img;img.alt=s.name;
    const lbl=document.createElement('div');lbl.className='slabel';lbl.textContent=s.name;
    c.appendChild(img);c.appendChild(lbl);
    c.onclick=()=>{
      stageIdx=i;
      document.querySelectorAll('.scard').forEach((x,j)=>x.classList.toggle('sel',j===i));
      document.getElementById('sprev-img').src=s.img;
      document.getElementById('sprev-name').textContent=s.name;
      document.getElementById('sprev-name').style.color=s.accent;
      document.getElementById('sprev-desc').textContent=s.desc;
    };
    g.appendChild(c);
  });
}
function showStsel(){buildStageUI();showScr('stsel');}
function startGameFromStage(mode){startGame(mode);}
function buildUI(){
  const p1cl=document.getElementById('p1cl'),p2cl=document.getElementById('p2cl');
  CHARS.forEach((c,i)=>{
    const b1=document.createElement('button');b1.className='cbtn';b1.textContent=c.name;
    b1.style.setProperty('--sc',c.c);if(i===p1ci)b1.classList.add('sel');
    b1.onclick=()=>{p1ci=i;updPrev(1,i);document.querySelectorAll('#p1cl .cbtn').forEach((x,j)=>x.classList.toggle('sel',j===i));};
    p1cl.appendChild(b1);
    const b2=document.createElement('button');b2.className='cbtn';b2.textContent=c.name;
    b2.style.setProperty('--sc',c.c);if(i===p2ci)b2.classList.add('sel');
    b2.onclick=()=>{p2ci=i;updPrev(2,i);document.querySelectorAll('#p2cl .cbtn').forEach((x,j)=>x.classList.toggle('sel',j===i));};
    p2cl.appendChild(b2);
  });
  updPrev(1,p1ci);updPrev(2,p2ci);
}

function updPrev(pid,ci){
  const c=CHARS[ci],sx=pid===1?'p1':'p2';
  document.getElementById(sx+'pn').textContent=c.name;document.getElementById(sx+'pn').style.color=c.c;
  document.getElementById(sx+'pt').textContent=c.title;
  const se=document.getElementById(sx+'ps');se.innerHTML='';
  Object.entries(c.stats).forEach(([k,v])=>{
    se.innerHTML+=`<div class="sr"><span class="sl">${k}</span><div class="st"><div class="sf" style="width:${v}%;background:${c.c}"></div></div><span style="font-size:.68rem;font-family:'Orbitron',monospace;color:${c.c}">${v}</span></div>`;
  });
  const spe=document.getElementById(sx+'sp');spe.innerHTML='';
  [c.sp1,c.sp2].forEach(s=>{spe.innerHTML+=`<div class="spi"><span class="spk">${s.key}</span><span>${s.name} <span style="opacity:.5">${s.desc}</span></span></div>`;});
  spe.innerHTML+=`<div class="spi"><span class="spk" style="color:${c.c}">O</span><span style="color:${c.c}">${c.sup.name} <span style="opacity:.5">${c.sup.desc}</span></span></div>`;
  drawMini(document.getElementById(sx+'pc'),c);
}

function drawMini(cv,c){
  const cx=cv.getContext('2d');
  cx.clearRect(0,0,120,140);
  const ox=56,oy=124,sh=96,sw=sh*0.48;
  const u=sh/100;

  // Ground shadow
  cx.fillStyle='rgba(0,0,0,0.35)';
  cx.beginPath();
  cx.ellipse(ox,oy,sw*0.65,sh*0.06,0,0,Math.PI*2);
  cx.fill();

  // Silhouette aura
  cx.globalAlpha=0.18;cx.fillStyle=c.c;
  cx.beginPath();cx.ellipse(ox,oy-sh*0.48,sw*0.75,sh*0.5,0,0,Math.PI*2);cx.fill();
  cx.globalAlpha=1;

  // Shadow Figure
  const sil='#08090d';
  cx.strokeStyle=sil;cx.lineCap='round';cx.lineJoin='round';

  // Back leg
  cx.lineWidth=7*u;
  cx.beginPath();cx.moveTo(ox-5*u,oy-48*u);cx.lineTo(ox-11*u,oy-24*u);cx.lineTo(ox-14*u,oy);cx.stroke();
  // Front leg
  cx.lineWidth=8*u;
  cx.beginPath();cx.moveTo(ox+4*u,oy-48*u);cx.lineTo(ox+11*u,oy-24*u);cx.lineTo(ox+14*u,oy);cx.stroke();

  // Torso
  cx.fillStyle=sil;
  cx.beginPath();
  cx.moveTo(ox-8*u,oy-75*u);cx.lineTo(ox+9*u,oy-73*u);
  cx.lineTo(ox+6*u,oy-46*u);cx.lineTo(ox-6*u,oy-46*u);
  cx.closePath();cx.fill();

  // Belt sash
  cx.strokeStyle=c.c;cx.lineWidth=2.2*u;
  cx.beginPath();cx.moveTo(ox+2*u,oy-46*u);cx.lineTo(ox+5*u,oy-34*u);cx.stroke();

  // Back arm
  cx.lineWidth=6*u;
  cx.beginPath();cx.moveTo(ox-6*u,oy-73*u);cx.lineTo(ox-14*u,oy-64*u);cx.lineTo(ox-6*u,oy-56*u);cx.stroke();
  // Front arm & weapon
  cx.lineWidth=6.8*u;
  cx.beginPath();cx.moveTo(ox+6*u,oy-73*u);cx.lineTo(ox+14*u,oy-66*u);cx.lineTo(ox+18*u,oy-74*u);cx.stroke();

  // Weapon
  cx.strokeStyle=c.c;cx.lineWidth=2*u;cx.shadowColor=c.c;cx.shadowBlur=7;
  cx.beginPath();cx.moveTo(ox+18*u,oy-74*u);cx.lineTo(ox+34*u,oy-96*u);cx.stroke();
  cx.shadowBlur=0;

  // Head
  cx.fillStyle=sil;
  cx.beginPath();cx.ellipse(ox+2*u,oy-84*u,7.5*u,8.5*u,0.06,0,Math.PI*2);cx.fill();

  // Headband ribbon
  cx.strokeStyle=c.c;cx.lineWidth=2.5;cx.shadowColor=c.c;cx.shadowBlur=6;
  cx.beginPath();
  cx.moveTo(ox-4*u,oy-84*u);
  cx.quadraticCurveTo(ox-14*u,oy-88*u,ox-22*u,oy-82*u);
  cx.stroke();
  cx.shadowBlur=0;

  // Piercing glowing eye
  cx.fillStyle=c.c;cx.shadowColor=c.c;cx.shadowBlur=10;
  cx.beginPath();cx.ellipse(ox+5*u,oy-85*u,3.6*u,1.4*u,0.2,0,Math.PI*2);cx.fill();
  cx.shadowBlur=0;

  cx.font="bold 8.5px 'Orbitron',monospace";cx.fillStyle=c.c;cx.textAlign='center';
  cx.shadowColor=c.c;cx.shadowBlur=7;cx.fillText(c.name,60,135);cx.shadowBlur=0;
}

preloadStages();buildUI();resize();
</script>
</body>
</html>"""

if __name__ == '__main__':
    pathlib.Path("index.html").write_text(HTML, encoding="utf-8")
    print("Regenerated index.html")
