const $ = (s,r=document)=>r.querySelector(s);

// ===== Dark Mode: โหลดค่าจากระบบ/ที่บันทึกไว้ + toggle =====
(function initTheme() {
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const saved = localStorage.getItem('theme');
  const dark = saved ? saved === 'dark' : prefersDark;

  const apply = (isDark) => {
    document.body.classList.toggle('dark-mode', isDark);
  };

  const run = () => {
    const toggle = document.getElementById('toggle-dark');
    apply(dark);
    if (toggle) {
      toggle.checked = dark;
      toggle.addEventListener('change', function () {
        apply(this.checked);
        localStorage.setItem('theme', this.checked ? 'dark' : 'light');
      });
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();

const form = $('#form');
const genderEl = $('#gender');
const ageEl = $('#age');
const weightEl = $('#weight');
const heightEl = $('#height');
const actEl = $('#activity');

const bmiEl = $('#bmi');
const bmiLabelEl = $('#bmiLabel');
const tdeeEl = $('#tdee');
const bmrNoteEl = $('#bmrNote');

const targetsBox = $('#targets');
const cutEl = $('#cut');
const maintainEl = $('#maintain');
const bulkEl = $('#bulk');

const adviceEl = $('#advice');

$('#reset').addEventListener('click', ()=>{
  form.reset();
  [bmiEl, tdeeEl].forEach(n=>n.textContent='—');
  bmiLabelEl.textContent='—'; bmiLabelEl.className='tag';
  bmrNoteEl.textContent='—';
  adviceEl.textContent='—';
  targetsBox.hidden = true;
});

form.addEventListener('submit', e=>{
  e.preventDefault();

  const gender = genderEl.value;
  const age = +ageEl.value;
  const weight = +weightEl.value;  // kg
  const height = +heightEl.value;  // cm
  const activity = +actEl.value;

  if(!age || !weight || !height) return;

  // ===== BMI
  const hM = height/100;
  const bmi = weight/(hM*hM);
  bmiEl.textContent = bmi.toFixed(1);

  // BMI label (Asian)
  let label='—', cls='tag';
  if(bmi < 18.5){ label='น้ำหนักน้อย'; }
  else if(bmi < 23){ label='ปกติ'; cls+=' tag--ok'; }
  else if(bmi < 25){ label='ท้วม/เสี่ยง'; cls+=' tag--warn'; }
  else if(bmi < 30){ label='อ้วนระดับ 1'; cls+=' tag--warn'; }
  else { label='อ้วนระดับ 2'; cls+=' tag--danger'; }
  bmiLabelEl.textContent = label;
  bmiLabelEl.className = cls;

  // ===== BMR (Mifflin–St Jeor)
  const BMR = 10*weight + 6.25*height - 5*age + (gender==='male' ? 5 : -161);

  // ===== TDEE
  const TDEE = BMR * activity;
  tdeeEl.textContent = Math.round(TDEE).toLocaleString('th-TH');
  bmrNoteEl.textContent = `BMR ≈ ${Math.round(BMR).toLocaleString('th-TH')} kcal/วัน (Mifflin–St Jeor)`;

  // ===== Targets (แนะนำแคลอรี่เป้าหมาย)
  const cut = Math.round(TDEE*0.85);
  const maintain = Math.round(TDEE);
  const bulk = Math.round(TDEE*1.10);
  cutEl.textContent = cut.toLocaleString('th-TH') + ' kcal/วัน';
  maintainEl.textContent = maintain.toLocaleString('th-TH') + ' kcal/วัน';
  bulkEl.textContent = bulk.toLocaleString('th-TH') + ' kcal/วัน';
  targetsBox.hidden = false;

  // ===== Personal Advice by BMI
  let advice = '—';
  if(bmi < 18.5){
    advice = 'น้ำหนักน้อย: ตั้งเป้า +10–15% จาก TDEE เพื่อเพิ่มน้ำหนักอย่างค่อยเป็นค่อยไป, โปรตีน 1.6–2.2 g/กก./วัน, เวท 3 วัน/สัปดาห์ (ท่าหลัก: Squat/Bench/Row/Deadlift), นอน 7–9 ชม.';
  } else if(bmi < 23){
    advice = 'ปกติ: คงพลังงานใกล้ TDEE (±5–10%), เวท 2–3 วัน + คาร์ดิโอ 1–2 วัน, โฟกัสอาหารไม่แปรรูป ผัก-ผลไม้ น้ำเพียงพอ';
  } else if(bmi < 25){
    advice = 'ท้วม/เสี่ยง: ลดพลังงาน ~10–15% จาก TDEE, โปรตีน 1.6–2.0 g/กก./วัน ช่วยอิ่มและรักษามวลกล้าม, เดินเยอะขึ้น (NEAT), เวท 2–3 วัน';
  } else if(bmi < 30){
    advice = 'อ้วนระดับ 1: ลดพลังงาน ~15%, เวท 3 วัน + คาร์ดิโอ 2 วัน, เน้นอาหารไม่แปรรูป ลดน้ำตาล/น้ำหวาน, ตั้งเป้าก้าว/วัน ≥ 8,000';
  } else {
    advice = 'อ้วนระดับ 2: ลดพลังงาน 15–20% อย่างปลอดภัย, เริ่มคาร์ดิโอแรงกระแทกต่ำ (เดินเร็ว/จักรยาน) + เวทพื้นฐาน, พิจารณาปรึกษาผู้เชี่ยวชาญหากมีโรคร่วม';
  }
  adviceEl.textContent = advice;
});
