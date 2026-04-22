import re

path = r"c:\Users\aanaf\Downloads\rasid-smart.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Inject Phosphor Icons script
if "phosphor-icons" not in content:
    content = content.replace("</head>", '  <script src="https://unpkg.com/@phosphor-icons/web"></script>\n</head>')

# 2. Text Replacements (Formalization)
replacements = {
    "صوّر وامش — الذكاء الاصطناعي يكمّل الشغل": "منصة رصد متطورة — والذكاء الاصطناعي يتولى المعالجة",
    "بدل ما نكون فريق ينزل ينظف فقط — نقدم نظاماً ذكياً متكاملاً يعمل بالكاميرا والذكاء الاصطناعي لمعالجة كل أنواع المشاكل البيئية.": "نظام مؤسسي ذكي ومتكامل، يعتمد على تقنيات الرؤية الحاسوبية والذكاء الاصطناعي لرصد ومعالجة كافة التحديات البيئية لحظياً.",
    "يلقط النفايات العادية في الحدائق والشوارع ويصنفها تلقائياً حسب النوع والخطورة والحجم المقدّر.": "يرصد النفايات في المرافق العامة، ويصنفها تلقائياً بدقة متناهية حسب نوعها ودرجة خطورتها وحجمها المقدر.",
    "يلقط مخلفات الهدم والبناء والأهم إنه يُقدّر حجمها بدقة عشان تحدد للبلدية نوع الشاحنة المطلوبة.": "يرصد مخلفات الهدم والبناء ويقدر حجمها بدقة ثلاثية الأبعاد، لتوجيه المعدات المناسبة تلقائياً وبأعلى كفاءة.",
    "يكتشف تسربات المياه من المواسير والخزانات في المرافق العامة ويرفعها كـ \"بلاغ طارئ\" لفرق الصيانة.": "يكتشف تسربات المياه والهدر المائي في المرافق العامة ويرفعها كبلاغ طارئ للجهات المختصة فوراً للتعامل معها.",
    "صوّر وامش — الباقي علينا": "أتمتة كاملة — من الرصد إلى الإغلاق",
    "المتطوع يوجه الكاميرا": "المستفيد يوثق الحالة",
    "الداشبور": "لوحة المؤشرات",
    "ارفع بلاغك البيئي الآن": "تسجيل بلاغ بيئي جديد",
    "صورة البلاغ": "المرفقات المرئية للرصد",
    "التقط صورة": "إرفاق صورة",
    "جاهز تبدأ الرصد<br><span>الذكي معنا؟</span>": "كن جزءاً من مستقبل<br><span>الرصد البيئي الذكي</span>",
    "انضم لمنصة الراصد الذكي وساهم في تحسين البيئة بمنطقة جازان": "ساهم في تحقيق استدامة بيئية ذكية تواكب تطلعات الرؤية الوطنية.",
    "ابدأ الآن": "بدء الاستخدام",
    "تواصل مع الفريق": "طلب عرض توضيحي (Demo)",
    "كيف يعمل": "آلية العمل",
    "فريق غيث التطوعي": "مبادرة الراصد الذكي البيئية",
    "مبادرة فريق غيث التطوعي · أمانة منطقة جازان": "مشروع وطني متكامل · بالشراكة مع القطاعات المختصة",
    "مبادرة تطوعية بيئية متخصصة تعمل في منطقة جازان، تجمع بين الشغف البيئي والتقنية الحديثة لخدمة المجتمع. الراصد الذكي هو إسهامنا التقني لأمانة منطقة جازان.": "منصة رائدة تم تصميمها لدعم متخذي القرار في وزارة البيئة والمياه والزراعة، ووزارة الشؤون البلدية والقروية، من خلال حلول الذكاء الاصطناعي لتحقيق الاستدامة وحماية البيئة.",
    "مبادرة فريق غيث التطوعي": "مشروع الراصد الذكي"
}

for old, new in replacements.items():
    content = content.replace(old, new)

# 3. Emoji Replacements
emoji_map = {
    "🗑️": '<i class="ph ph-trash"></i>',
    "🏗️": '<i class="ph ph-crane"></i>',
    "💧": '<i class="ph ph-drop"></i>',
    "🤖": '<i class="ph ph-robot"></i>',
    "✅": '<i class="ph ph-check-circle"></i>',
    "📊": '<i class="ph ph-chart-bar"></i>',
    "📋": '<i class="ph ph-clipboard-text"></i>',
    "🗺️": '<i class="ph ph-map-trifold"></i>',
    "🏢": '<i class="ph ph-buildings"></i>',
    "👁️‍🗨️": '<i class="ph ph-eye"></i>',
    "👁️": '<i class="ph ph-eye"></i>',
    "⚙️": '<i class="ph ph-gear"></i>',
    "⭐": '<i class="ph ph-star"></i>',
    "🔔": '<i class="ph ph-bell"></i>',
    "⚡": '<i class="ph ph-lightning"></i>',
    "👤": '<i class="ph ph-user"></i>',
    "📷": '<i class="ph ph-camera"></i>',
    "📤": '<i class="ph ph-upload-simple"></i>',
    "🎯": '<i class="ph ph-target"></i>',
    "🛠️": '<i class="ph ph-wrench"></i>',
    "🧠": '<i class="ph ph-brain"></i>',
    "📍": '<i class="ph ph-map-pin"></i>',
    "🔄": '<i class="ph ph-arrows-clockwise"></i>',
    "⚠": '<i class="ph ph-warning"></i>',
    "👑": '<i class="ph ph-crown"></i>',
    "🌧️": '<i class="ph ph-cloud-rain"></i>',
    "🌿": '<i class="ph ph-plant"></i>',
    "🏛️": '<i class="ph ph-bank"></i>',
    "💚": '<i class="ph ph-heart"></i>',
    "⏳": '<i class="ph ph-hourglass"></i>',
    "🚛": '<i class="ph ph-truck"></i>'
}

for emoji, icon in emoji_map.items():
    content = content.replace(emoji, icon)

# Add Partners Section if it doesn't exist
partners_html = """
<!-- ═══════════════ PARTNERS ═══════════════ -->
<section class="partners" style="padding: 40px 60px; background: rgba(0,0,0,0.4); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); text-align: center;">
  <p style="font-size: 0.85rem; color: var(--muted); margin-bottom: 24px; letter-spacing: 1px; font-weight: 700;">منصة موحدة ومصممة لدعم قطاعات</p>
  <div style="display: flex; justify-content: center; align-items: center; gap: 60px; flex-wrap: wrap; opacity: 0.7;">
    <div style="display: flex; align-items: center; gap: 12px; font-weight: 700; font-size: 1.1rem; color: var(--text);">
      <i class="ph ph-plant" style="font-size: 2.2rem; color: var(--green);"></i>
      وزارة البيئة والمياه والزراعة
    </div>
    <div style="display: flex; align-items: center; gap: 12px; font-weight: 700; font-size: 1.1rem; color: var(--text);">
      <i class="ph ph-buildings" style="font-size: 2.2rem; color: var(--blue);"></i>
      وزارة البلديات والإسكان
    </div>
    <div style="display: flex; align-items: center; gap: 12px; font-weight: 700; font-size: 1.1rem; color: var(--text);">
      <i class="ph ph-map-pin" style="font-size: 2.2rem; color: var(--amber);"></i>
      أمانات المناطق
    </div>
  </div>
</section>
"""

if "<!-- ═══════════════ PARTNERS ═══════════════ -->" not in content:
    content = content.replace("<!-- ═══════════════ NUMBERS ═══════════════ -->", partners_html + "\n<!-- ═══════════════ NUMBERS ═══════════════ -->")


# Custom aesthetic tweaks
# Adjusting hero title to look more "Ministry" level
content = content.replace("font-size:clamp(2.8rem,5.5vw,5rem);", "font-size:clamp(2.4rem,4.5vw,4.2rem);")
content = content.replace("المنصة الموحدة<br>\n            <span>للرصد البيئي الذكي</span>", "المنظومة الوطنية<br>\n            <span>للرصد البيئي الذكي</span>")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated successfully")
