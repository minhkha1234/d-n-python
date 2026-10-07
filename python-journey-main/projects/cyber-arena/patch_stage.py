import pathlib, re

SRC = pathlib.Path(r'C:\Users\Admin\Downloads\python-journey-main\python-journey-main\projects\cyber-arena\index.html')
content = SRC.read_text(encoding='utf-8')

if 'let stageIdx' in content:
    print('Already patched! Skipping to avoid duplicate declarations.')
    exit(0)

# ── 1. STAGE CSS ──────────────────────────────────────────────
STAGE_CSS = """
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
"""
content = content.replace(
    '.sb.act,.sb:hover{background:rgba(255,215,0,.1);box-shadow:0 0 8px rgba(255,215,0,.3)}',
    '.sb.act,.sb:hover{background:rgba(255,215,0,.1);box-shadow:0 0 8px rgba(255,215,0,.3)}' + STAGE_CSS
)

# ── 2. STAGE SELECT HTML (insert before <!-- GAME -->) ────────
STAGE_HTML = """
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
"""
content = content.replace('<!-- GAME -->', STAGE_HTML + '<!-- GAME -->')

# ── 3. Update char-select buttons to go to stage select ──────
OLD_CSEL_BTNS = '<button class="btn bc" onclick="startGame(\'pvb\')">&#127918; PLAYER vs BOT</button>\n    <button class="btn bp" onclick="startGame(\'bvb\')">&#129302; BOT vs BOT</button>\n    <button class="btn" style="border-color:rgba(255,255,255,.2);color:rgba(255,255,255,.45)" onclick="showTut()">&#9664; HUONG DAN</button>'
NEW_CSEL_BTNS = '<button class="btn bg2" onclick="showStsel()">TIEP THEO &#8594; CHON CHIEN TRUONG</button>\n    <button class="btn" style="border-color:rgba(255,255,255,.2);color:rgba(255,255,255,.45)" onclick="showTut()">&#9664; HUONG DAN</button>'
content = content.replace(OLD_CSEL_BTNS, NEW_CSEL_BTNS)

# ── 4. STAGES data + stageIdx JS ────────────────────────────
STAGES_JS = """
const STAGES=[
  {id:'nether',name:'NETHER REALM',desc:'Chien truong dia nguc - cong dich chuyen huyen bi',img:'stages/nether.jpg',fog:'rgba(60,0,0,.28)',floorCol:'rgba(255,140,0,.7)',accent:'#ff8c00'},
  {id:'konoha',name:'LANG LA AN',desc:'San thuong lang la an - nui Hokage nhin xuong',img:'stages/konoha.jpg',fog:'rgba(135,206,235,.06)',floorCol:'rgba(80,200,80,.6)',accent:'#00cc55'},
  {id:'akatsuki',name:'CAN CU AKATSUKI',desc:'Chua toi - bao to do - khong co duong thoat',img:'stages/akatsuki.jpg',fog:'rgba(60,0,60,.3)',floorCol:'rgba(200,0,50,.7)',accent:'#ff2d78'},
  {id:'space',name:'KHONG GIAN DBZ',desc:'San dau noi vu tru - cac titan tung giao tranh',img:'stages/space.jpg',fog:'rgba(0,0,30,.35)',floorCol:'rgba(0,200,255,.65)',accent:'#00f5ff'},
  {id:'top',name:'GIAI VO DICH',desc:'Tournament of Power - san dau quyen nang nhat',img:'stages/top.jpg',fog:'rgba(20,0,50,.3)',floorCol:'rgba(160,80,255,.65)',accent:'#da70d6'},
];
let stageIdx=0;
let _stImgs={};
"""
content = content.replace('let gameMode=', STAGES_JS + 'let gameMode=')

# ── 5. Stage UI + preload functions ─────────────────────────
STAGE_FUNCS = """
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
"""
content = content.replace('function buildUI(){', STAGE_FUNCS + 'function buildUI(){')

# ── 6. Call preloadStages() at init ─────────────────────────
content = content.replace('buildUI();resize();', 'preloadStages();buildUI();resize();')

# ── 7. Modify drawBG to use stage image ─────────────────────
OLD_BG_START = """function drawBG(){
  const sky=ctx.createLinearGradient(0,0,0,H);
  sky.addColorStop(0,'#020010');sky.addColorStop(.55,'#080022');sky.addColorStop(1,'#0f0033');
  ctx.fillStyle=sky;ctx.fillRect(0,0,W,H);"""

NEW_BG_START = """function drawBG(){
  const _st=STAGES[stageIdx];
  const _si=_stImgs[_st.id];
  if(_si&&_si.complete&&_si.naturalWidth>0){
    ctx.drawImage(_si,0,0,W,H);
    ctx.fillStyle=_st.fog||'rgba(0,0,10,.25)';ctx.fillRect(0,0,W,H);
  } else {
    const sky=ctx.createLinearGradient(0,0,0,H);
    sky.addColorStop(0,'#020010');sky.addColorStop(.55,'#080022');sky.addColorStop(1,'#0f0033');
    ctx.fillStyle=sky;ctx.fillRect(0,0,W,H);
  }"""
content = content.replace(OLD_BG_START, NEW_BG_START)

# ── 8. Skip city buildings when stage image used ─────────────
OLD_CITY = """  const bw=W/18;ctx.fillStyle='#06001a';
  const bhs=[.54,.34,.47,.27,.41,.21,.37,.31,.49,.25,.43,.29,.45,.33,.27,.41,.35,.49];
  for(let i=0;i<bhs.length;i++)ctx.fillRect(i*bw,H*.82-bhs[i]*H*.58,bw-1,bhs[i]*H*.58);
  const now=Date.now();
  const wcs=['#00f5ff','#ff2d78','#8b00ff','#ffd700','#00ff7f','#da70d6'];
  for(let i=0;i<65;i++){
    const sx=i*173.7%W,sy=H*.27+(i*131.3%(H*.36));
    if(Math.sin(now*.002+i)>.6)continue;
    ctx.globalAlpha=.28+.18*Math.sin(now*.003+i*2);
    ctx.fillStyle=wcs[i%wcs.length];ctx.fillRect(sx,sy,3,5);
  }ctx.globalAlpha=1;"""
NEW_CITY = "  // Stage image is the background; skip procedural city"
content = content.replace(OLD_CITY, NEW_CITY)

# ── 9. Stage-colored floor line ──────────────────────────────
OLD_FLOOR = """  ctx.shadowColor='rgba(0,245,255,.45)';ctx.shadowBlur=15;ctx.strokeStyle='rgba(0,245,255,.42)';ctx.lineWidth=2;
  ctx.beginPath();ctx.moveTo(0,fy);ctx.lineTo(W,fy);ctx.stroke();ctx.shadowBlur=0;"""
NEW_FLOOR = """  const _fc=STAGES[stageIdx].floorCol||'rgba(0,245,255,.65)';
  ctx.shadowColor=_fc;ctx.shadowBlur=14;ctx.strokeStyle=_fc;ctx.lineWidth=2;
  ctx.beginPath();ctx.moveTo(0,fy);ctx.lineTo(W,fy);ctx.stroke();ctx.shadowBlur=0;"""
content = content.replace(OLD_FLOOR, NEW_FLOOR)

SRC.write_text(content, encoding='utf-8')
print('Done! Size:', len(content), 'bytes, Lines:', content.count('\n'))
