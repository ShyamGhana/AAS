const canvas = document.getElementById('mapCanvas');
const ctx = canvas.getContext('2d');

let W, H;
function resizeCanvas() {
  const wrap = canvas.parentElement;
  W = wrap.clientWidth;
  H = Math.max(420, Math.round(W * 0.58));
  canvas.width = W;
  canvas.height = H;
}
resizeCanvas();
window.addEventListener('resize', () => { resizeCanvas(); drawAll(); });

let rooms = [], landmarks = [], walls = [];

function buildISSMap() {
  const s = Math.min(W, H);
  const u = s / 22;
  rooms = [
    { x: 2*u, y: 4*u, w: 5*u, h: 4*u, label: 'Zarya',      color: '#0a2040' },
    { x: 7*u, y: 4*u, w: 5*u, h: 4*u, label: 'Zvezda',     color: '#091830' },
    { x:12*u, y: 4*u, w: 4*u, h: 4*u, label: 'Unity',      color: '#0a1e38' },
    { x:12*u, y: 8*u, w: 4*u, h: 3*u, label: 'Harmony',    color: '#071828' },
    { x: 7*u, y: 8*u, w: 5*u, h: 3*u, label: 'Destiny',    color: '#091a30' },
    { x: 2*u, y: 8*u, w: 5*u, h: 3*u, label: 'Columbus',   color: '#081520' },
    { x:16*u, y: 5*u, w: 3*u, h: 5*u, label: 'Kibo',       color: '#081a2e' },
    { x:16*u, y:10*u, w: 3*u, h: 4*u, label: 'Tranquility',color: '#07121e' },
    { x: 8*u, y:0.5*u,w: 3*u, h:3.5*u,label: 'Cupola',     color: '#050e1a' },
    { x:0.5*u,y:5.5*u,w:1.5*u,h: 1*u, label: '',           color: '#060f1c' },
  ];
  landmarks = [
    { x: 4.5*u, y: 6*u,   label: 'L1', type: 'camera' },
    { x: 9.5*u, y: 6*u,   label: 'L2', type: 'sensor' },
    { x:  14*u, y: 6*u,   label: 'L3', type: 'camera' },
    { x:17.5*u, y: 7.5*u, label: 'L4', type: 'sensor' },
    { x: 9.5*u, y: 9.5*u, label: 'L5', type: 'camera' },
    { x:  14*u, y: 9.5*u, label: 'L6', type: 'sensor' },
    { x:17.5*u, y:  12*u, label: 'L7', type: 'camera' },
    { x: 9.5*u, y:   2*u, label: 'L8', type: 'sensor' },
  ];
  walls = [];
  rooms.forEach(r => {
    walls.push({ x1: r.x,     y1: r.y,     x2: r.x+r.w, y2: r.y     });
    walls.push({ x1: r.x+r.w, y1: r.y,     x2: r.x+r.w, y2: r.y+r.h });
    walls.push({ x1: r.x+r.w, y1: r.y+r.h, x2: r.x,     y2: r.y+r.h });
    walls.push({ x1: r.x,     y1: r.y+r.h, x2: r.x,     y2: r.y     });
  });
}

let particles = [], robot = { x:0, y:0, theta:0 }, estimate = { x:0, y:0, theta:0 };
let iter = 0, running = false, autoTimer = null;
let lastFrameTime = performance.now(), fpsSmooth = 0, posErrors = [];
let wSlow = 0, wFast = 0;

const params = () => ({
  N:           parseInt(document.getElementById('numParticles').value),
  motionTrans: parseFloat(document.getElementById('motionTransNoise').value),
  motionRot:   parseFloat(document.getElementById('motionRotNoise').value) * Math.PI / 180,
  sensorRange: parseFloat(document.getElementById('sensorRangeNoise').value),
  sensorBear:  parseFloat(document.getElementById('sensorBearNoise').value) * Math.PI / 180,
  alphaSlow:   parseFloat(document.getElementById('alphaSlow').value) * 0.001,
  alphaFast:   parseFloat(document.getElementById('alphaFast').value) * 0.01,
  stepSize:    parseFloat(document.getElementById('stepSize').value),
});

function randn() {
  let u = 0, v = 0;
  while (!u) u = Math.random();
  while (!v) v = Math.random();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}

function inBounds(x, y) {
  return rooms.some(r => x >= r.x && x <= r.x+r.w && y >= r.y && y <= r.y+r.h);
}
function clampToMap(x, y) {
  if (inBounds(x, y)) return { x, y };
  let best = rooms[0], bd = Infinity;
  rooms.forEach(r => {
    const d = (r.x+r.w/2-x)**2 + (r.y+r.h/2-y)**2;
    if (d < bd) { bd = d; best = r; }
  });
  return { x: best.x + best.w/2, y: best.y + best.h/2 };
}
function randomMapPoint() {
  for (let i = 0; i < 200; i++) {
    const rx = Math.random()*W, ry = Math.random()*H;
    if (inBounds(rx, ry)) return { x: rx, y: ry };
  }
  const r = rooms[Math.floor(Math.random()*rooms.length)];
  return { x: r.x + Math.random()*r.w, y: r.y + Math.random()*r.h };
}

function initParticles(N) {
  particles = Array.from({ length: N }, () => {
    const p = randomMapPoint();
    return { x: p.x, y: p.y, theta: Math.random()*2*Math.PI, w: 1/N };
  });
}
function initRobot() {
  const r = rooms[Math.floor(Math.random()*rooms.length)];
  robot = {
    x: r.x + r.w*0.3 + Math.random()*r.w*0.4,
    y: r.y + r.h*0.3 + Math.random()*r.h*0.4,
    theta: Math.random()*2*Math.PI
  };
}

function applyMotion(p, dx, dy, dtheta, p_) {
  const nx = p.x + dx + randn()*p_.motionTrans;
  const ny = p.y + dy + randn()*p_.motionTrans;
  const c = clampToMap(nx, ny);
  return { x: c.x, y: c.y, theta: (p.theta + dtheta + randn()*p_.motionRot) % (2*Math.PI), w: p.w };
}

function sensorWeight(px, py, ptheta, obs, p_) {
  let logW = 0;
  landmarks.forEach((lm, i) => {
    const trueR = Math.hypot(lm.x-px, lm.y-py);
    const trueB = Math.atan2(lm.y-py, lm.x-px) - ptheta;
    const errR = obs[i].r - trueR;
    const errB = ((obs[i].b - trueB + Math.PI) % (2*Math.PI)) - Math.PI;
    logW += -0.5*(errR**2)/(p_.sensorRange**2) - 0.5*(errB**2)/(p_.sensorBear**2);
  });
  return Math.exp(logW);
}

function getObservations(rx, ry, rtheta, p_) {
  return landmarks.map(lm => ({
    r: Math.hypot(lm.x-rx, lm.y-ry) + randn()*p_.sensorRange,
    b: Math.atan2(lm.y-ry, lm.x-rx) - rtheta + randn()*p_.sensorBear
  }));
}

function lowVarianceResample(parts, N) {
  const wsum = parts.reduce((a, b) => a + b.w, 0);
  if (!wsum) return parts;
  const step = wsum / N, out = [];
  let r = Math.random()*step, cum = parts[0].w, i = 0;
  for (let k = 0; k < N; k++) {
    while (cum < r && i < parts.length-1) { i++; cum += parts[i].w; }
    out.push({ ...parts[i], w: 1/N });
    r += step;
  }
  return out;
}

function computeEstimate() {
  let sx=0, sy=0, sc=0, ss=0, sw=0;
  particles.forEach(p => { sx+=p.x*p.w; sy+=p.y*p.w; sc+=Math.cos(p.theta)*p.w; ss+=Math.sin(p.theta)*p.w; sw+=p.w; });
  if (sw) estimate = { x: sx/sw, y: sy/sw, theta: Math.atan2(ss/sw, sc/sw) };
}
function computeNEff() {
  const sw2 = particles.reduce((a, p) => a + p.w*p.w, 0);
  return sw2 ? 1/sw2 : 0;
}
function computeEntropy() {
  return particles.reduce((h, p) => p.w > 0 ? h - p.w*Math.log(p.w+1e-300) : h, 0);
}

function mclStep() {
  const p_ = params();
  const newTheta = robot.theta + (Math.random()-0.5)*0.6;
  const c = clampToMap(robot.x + Math.cos(newTheta)*p_.stepSize, robot.y + Math.sin(newTheta)*p_.stepSize);
  const dx = c.x - robot.x, dy = c.y - robot.y, dtheta = newTheta - robot.theta;
  robot.x = c.x; robot.y = c.y; robot.theta = newTheta;

  const obs = getObservations(robot.x, robot.y, robot.theta, p_);
  let wSum = 0;
  particles = particles.map(p => {
    const m = applyMotion(p, dx, dy, dtheta, p_);
    m.w = sensorWeight(m.x, m.y, m.theta, obs, p_) + 1e-300;
    wSum += m.w;
    return m;
  });
  particles.forEach(p => p.w /= wSum);

  const wAvg = 1 / particles.length;
  wSlow += p_.alphaSlow * (wAvg - wSlow);
  wFast += p_.alphaFast * (wAvg - wFast);
  const pRand = Math.max(0, 1 - wFast/(wSlow+1e-300));

  let resampled = lowVarianceResample(particles, Math.round(p_.N*(1-pRand)));
  const nRandom = p_.N - resampled.length;
  for (let i = 0; i < nRandom; i++) {
    const rp = randomMapPoint();
    resampled.push({ x: rp.x, y: rp.y, theta: Math.random()*2*Math.PI, w: 1/p_.N });
  }
  particles = resampled;

  computeEstimate();
  iter++;
  const err = Math.hypot(estimate.x-robot.x, estimate.y-robot.y);
  posErrors.push(err);
  if (posErrors.length > 60) posErrors.shift();
  updateStats(err, computeNEff(), computeEntropy());
  log(`Step ${iter}: err=${err.toFixed(1)}px, N_eff=${computeNEff().toFixed(0)}, rand=${(pRand*100).toFixed(1)}%`,
    err < 30 ? 'good' : err < 70 ? 'info' : 'warn');
}

function drawAll() {
  ctx.clearRect(0, 0, W, H);
  ctx.strokeStyle = 'rgba(0,80,160,0.08)'; ctx.lineWidth = 1;
  for (let x = 0; x < W; x += 30) { ctx.beginPath(); ctx.moveTo(x,0); ctx.lineTo(x,H); ctx.stroke(); }
  for (let y = 0; y < H; y += 30) { ctx.beginPath(); ctx.moveTo(0,y); ctx.lineTo(W,y); ctx.stroke(); }

  rooms.forEach(r => {
    ctx.fillStyle = r.color || '#081520'; ctx.fillRect(r.x, r.y, r.w, r.h);
    ctx.strokeStyle = 'rgba(0,150,230,0.25)'; ctx.lineWidth = 1.5; ctx.strokeRect(r.x, r.y, r.w, r.h);
    if (r.label) {
      ctx.fillStyle = 'rgba(0,180,255,0.18)';
      ctx.font = `${Math.max(9, Math.min(13, r.w/6))}px "Exo 2"`;
      ctx.textAlign = 'center';
      ctx.fillText(r.label, r.x+r.w/2, r.y+r.h/2+4);
    }
  });

  const maxW = Math.max(...particles.map(p => p.w));
  particles.forEach(p => {
    const alpha = Math.min(1, p.w/maxW*0.9+0.05);
    ctx.globalAlpha = alpha;
    ctx.fillStyle = '#00d4ff';
    ctx.beginPath(); ctx.arc(p.x, p.y, 2.5, 0, 2*Math.PI); ctx.fill();
    ctx.strokeStyle = '#00d4ff'; ctx.lineWidth = 0.8;
    ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(p.x+Math.cos(p.theta)*5, p.y+Math.sin(p.theta)*5); ctx.stroke();
  });
  ctx.globalAlpha = 1;

  landmarks.forEach(lm => {
    ctx.save(); ctx.translate(lm.x, lm.y);
    ctx.strokeStyle = 'rgba(255,215,0,0.6)'; ctx.fillStyle = 'rgba(255,215,0,0.15)'; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(0, -8);
    for (let i = 1; i < 6; i++) {
      const a = (i*2*Math.PI/5) - Math.PI/2;
      ctx.lineTo(Math.cos(a)*(i%2===0?8:4), Math.sin(a)*(i%2===0?8:4));
    }
    ctx.closePath(); ctx.fill(); ctx.stroke();
    ctx.fillStyle = 'rgba(255,215,0,0.5)'; ctx.font = '8px "Share Tech Mono"'; ctx.textAlign = 'center';
    ctx.fillText(lm.label, 0, 16); ctx.restore();
  });

  ctx.save(); ctx.translate(estimate.x, estimate.y);
  ctx.strokeStyle = '#ff6b35'; ctx.lineWidth = 2.5; ctx.shadowColor = '#ff6b35'; ctx.shadowBlur = 10;
  ctx.beginPath(); ctx.moveTo(-10,0); ctx.lineTo(10,0); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(0,-10); ctx.lineTo(0,10); ctx.stroke();
  ctx.rotate(estimate.theta); ctx.strokeStyle = '#ff6b3580';
  ctx.beginPath(); ctx.moveTo(0,0); ctx.lineTo(14,0); ctx.stroke(); ctx.restore();

  ctx.save(); ctx.translate(robot.x, robot.y);
  ctx.strokeStyle = '#39ff14'; ctx.fillStyle = 'rgba(57,255,20,0.15)';
  ctx.lineWidth = 2; ctx.shadowColor = '#39ff14'; ctx.shadowBlur = 12;
  ctx.beginPath(); ctx.arc(0,0,9,0,2*Math.PI); ctx.fill(); ctx.stroke();
  ctx.rotate(robot.theta); ctx.lineWidth = 2;
  ctx.beginPath(); ctx.moveTo(0,0); ctx.lineTo(12,0); ctx.stroke(); ctx.restore();

  if (iter > 0) {
    ctx.strokeStyle = 'rgba(255,100,50,0.25)'; ctx.setLineDash([4,4]); ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(robot.x, robot.y); ctx.lineTo(estimate.x, estimate.y); ctx.stroke();
    ctx.setLineDash([]);
  }

  if (posErrors.length > 2) {
    const cw=120, ch=40, cx=W-cw-12, cy=H-ch-12;
    ctx.fillStyle = 'rgba(4,12,24,0.85)'; ctx.strokeStyle = 'rgba(0,100,160,0.4)'; ctx.lineWidth = 1;
    ctx.fillRect(cx,cy,cw,ch); ctx.strokeRect(cx,cy,cw,ch);
    ctx.fillStyle = 'rgba(0,180,255,0.4)'; ctx.font = '7px "Share Tech Mono"';
    ctx.fillText('POS ERROR', cx+4, cy+9);
    const maxE = Math.max(...posErrors, 60);
    ctx.strokeStyle = '#00d4ff'; ctx.lineWidth = 1.5; ctx.beginPath();
    posErrors.forEach((e, i) => {
      const px2 = cx + (i/(posErrors.length-1))*cw;
      const py2 = cy + ch - (e/maxE)*(ch-12) - 4;
      i === 0 ? ctx.moveTo(px2,py2) : ctx.lineTo(px2,py2);
    });
    ctx.stroke();
  }
}

function updateStats(err, neff, entropy) {
  document.getElementById('statErr').textContent = err.toFixed(1);
  document.getElementById('statIter').textContent = iter;
  document.getElementById('statNEff').textContent = neff.toFixed(0);
  document.getElementById('statEntropy').textContent = entropy.toFixed(2);
  const converged = err < 30;
  const el = document.getElementById('statConv');
  el.textContent = converged ? 'YES' : 'NO';
  el.style.color = converged ? '#39ff14' : '#ff6b35';
  const now = performance.now(), dt = now - lastFrameTime;
  lastFrameTime = now;
  fpsSmooth = fpsSmooth*0.8 + (1000/dt)*0.2;
  document.getElementById('statFPS').textContent = fpsSmooth.toFixed(1);
}

let logEntries = [];
function log(msg, type = 'info') {
  const ts = new Date().toLocaleTimeString('en',{hour12:false,hour:'2-digit',minute:'2-digit',second:'2-digit'});
  logEntries.push({ ts, msg, type });
  if (logEntries.length > 80) logEntries.shift();
  const body = document.getElementById('logBody');
  body.innerHTML = logEntries.slice(-20).map(e =>
    `<div class="log-entry"><span class="log-ts">[${e.ts}]</span><span class="log-msg ${e.type}">${e.msg}</span></div>`
  ).join('');
  body.scrollTop = body.scrollHeight;
}

document.querySelectorAll('input[type=range]').forEach(el => {
  const valEl = document.getElementById(el.id + 'Val');
  el.addEventListener('input', () => {
    let v = el.value;
    if (el.id === 'alphaSlow') v = (parseFloat(v)*0.001).toFixed(3);
    else if (el.id === 'alphaFast') v = (parseFloat(v)*0.01).toFixed(3);
    if (valEl) valEl.textContent = v;
  });
});

document.getElementById('btnStep').addEventListener('click', () => { mclStep(); drawAll(); });

document.getElementById('btnAuto').addEventListener('click', () => {
  running = !running;
  const btn = document.getElementById('btnAuto');
  if (running) { btn.textContent = '⏸ PAUSE'; btn.classList.add('primary'); autoLoop(); }
  else { btn.textContent = '▶ AUTO'; cancelAnimationFrame(autoTimer); }
});

function autoLoop() {
  if (!running) return;
  mclStep(); drawAll();
  autoTimer = requestAnimationFrame(autoLoop);
}

document.getElementById('btnReset').addEventListener('click', () => {
  const p_ = params();
  initParticles(p_.N);
  iter = 0; wSlow = 0; wFast = 0; posErrors = [];
  computeEstimate(); drawAll();
  log('Particles reinitialized — uniform distribution', 'warn');
});

document.getElementById('btnKidnap').addEventListener('click', () => {
  initRobot();
  log('⚠ ROBOT KIDNAPPED — belief mismatch introduced', 'warn');
  drawAll();
});

canvas.addEventListener('click', e => {
  const rect = canvas.getBoundingClientRect();
  const mx = (e.clientX - rect.left) * (W / rect.width);
  const my = (e.clientY - rect.top) * (H / rect.height);
  if (inBounds(mx, my)) {
    robot.x = mx; robot.y = my;
    log(`Robot moved to (${mx.toFixed(0)}, ${my.toFixed(0)})`, 'info');
    drawAll();
  }
});

buildISSMap();
initRobot();
initParticles(500);
computeEstimate();
drawAll();
log('MCL system initialized — 500 particles, ISS map loaded', 'good');
log('Click map to reposition robot. Press AUTO to begin localization.', 'info');
