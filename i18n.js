/* Interface labels in Kannada and Hindi (beta), the same way LitFest Guide does it. English is the source text; this only swaps
   fixed labels (menus, tabs, headings, captions, calendar statuses), never film titles, names, descriptions or other data.
   The translations are new and need review by native speakers: corrections are welcome through the project's GitHub issues.
   Choose a language on the home page or in About; the choice is kept in this browser. */
(function(){
var D={
kn:{'Search':'ಹುಡುಕಿ','Explore':'ಅನ್ವೇಷಿಸಿ','About':'ಬಗ್ಗೆ','All':'ಎಲ್ಲಾ','Close':'ಮುಚ್ಚಿ','Region':'ಪ್ರದೇಶ',
'Film festivals, films and people':'ಚಲನಚಿತ್ರೋತ್ಸವಗಳು, ಚಿತ್ರಗಳು ಮತ್ತು ಜನರು','What screens at film festivals, starting with India':'ಚಲನಚಿತ್ರೋತ್ಸವಗಳಲ್ಲಿ ಏನು ಪ್ರದರ್ಶನವಾಗುತ್ತದೆ: ಭಾರತದಿಂದ ಆರಂಭ',
'film festivals worldwide':'ವಿಶ್ವದಾದ್ಯಂತ ಚಲನಚಿತ್ರೋತ್ಸವಗಳು','countries with a festival':'ಉತ್ಸವ ನಡೆಯುವ ದೇಶಗಳು','people credited':'ಶ್ರೇಯ ಪಡೆದ ಜನರು','awards and honours':'ಪ್ರಶಸ್ತಿಗಳು ಮತ್ತು ಗೌರವಗಳು',
'Happening now':'ಈಗ ನಡೆಯುತ್ತಿದೆ','Full calendar ›':'ಪೂರ್ಣ ಕ್ಯಾಲೆಂಡರ್ ›','Next up':'ಮುಂದಿನವು','Work in progress':'ಕೆಲಸ ನಡೆಯುತ್ತಿದೆ','In the guide':'ಮಾರ್ಗದರ್ಶಿಯಲ್ಲಿ',
'World map of films and people ›':'ಚಿತ್ರಗಳು ಮತ್ತು ಜನರ ವಿಶ್ವ ನಕ್ಷೆ ›','Festival calendar: on now and next ›':'ಉತ್ಸವ ಕ್ಯಾಲೆಂಡರ್: ಈಗ ಮತ್ತು ಮುಂದೆ ›','Languages ›':'ಭಾಷೆಗಳು ›',
'Roles: directors, writers, actors, crew ›':'ಪಾತ್ರಗಳು: ನಿರ್ದೇಶಕರು, ಬರಹಗಾರರು, ನಟರು, ತಂತ್ರಜ್ಞರು ›','Award impact: what winning led to ›':'ಪ್ರಶಸ್ತಿಯ ಪರಿಣಾಮ: ಗೆಲುವಿನ ನಂತರ ಏನಾಯಿತು ›',
'Across festivals ›':'ಉತ್ಸವಗಳಾದ್ಯಂತ ›','World festivals, work in progress ›':'ವಿಶ್ವ ಉತ್ಸವಗಳು, ಕೆಲಸ ನಡೆಯುತ್ತಿದೆ ›','Also this month:':'ಈ ತಿಂಗಳು ಇವೂ:',
'Founded by decade':'ದಶಕವಾರು ಸ್ಥಾಪನೆ','Notable festivals worldwide':'ವಿಶ್ವದ ಪ್ರಮುಖ ಉತ್ಸವಗಳು','Award-winning films':'ಪ್ರಶಸ್ತಿ ವಿಜೇತ ಚಿತ್ರಗಳು','Data freshness':'ಮಾಹಿತಿ ಎಷ್ಟು ಹೊಸದು',
'Discover':'ಅನ್ವೇಷಣೆ','Films':'ಚಿತ್ರಗಳು','People':'ಜನರು','Awards':'ಪ್ರಶಸ್ತಿಗಳು','Map':'ನಕ್ಷೆ','Past years':'ಹಿಂದಿನ ವರ್ಷಗಳು','Festivals':'ಉತ್ಸವಗಳು','Numbers':'ಅಂಕಿಅಂಶಗಳು','Overview':'ಅವಲೋಕನ','Notable festivals':'ಪ್ರಮುಖ ಉತ್ಸವಗಳು','Winners':'ವಿಜೇತ ಚಿತ್ರಗಳು','Data':'ಮಾಹಿತಿ',
'Calendar':'ಕ್ಯಾಲೆಂಡರ್','Languages':'ಭಾಷೆಗಳು','Roles':'ಪಾತ್ರಗಳು','Award impact':'ಪ್ರಶಸ್ತಿಯ ಪರಿಣಾಮ','Across festivals':'ಉತ್ಸವಗಳಾದ್ಯಂತ','World festivals':'ವಿಶ್ವ ಉತ್ಸವಗಳು',
'Festival calendar':'ಉತ್ಸವ ಕ್ಯಾಲೆಂಡರ್','Coming next':'ಮುಂಬರುವವು','Just finished':'ಈಗಷ್ಟೇ ಮುಗಿದವು','likely on now':'ಬಹುಶಃ ಈಗ ನಡೆಯುತ್ತಿದೆ','Likely on now':'ಬಹುಶಃ ಈಗ ನಡೆಯುತ್ತಿದೆ',
'On now':'ಈಗ ನಡೆಯುತ್ತಿದೆ','Over':'ಮುಗಿದಿದೆ','dates TBC':'ದಿನಾಂಕ ಖಚಿತವಾಗಿಲ್ಲ','No festivals on record.':'ದಾಖಲೆಯಲ್ಲಿ ಉತ್ಸವಗಳಿಲ್ಲ.',
'Nothing on record for today.':'ಇಂದಿಗೆ ದಾಖಲೆಯಲ್ಲಿ ಏನೂ ಇಲ್ಲ.','Nothing on record yet.':'ಇನ್ನೂ ದಾಖಲೆಯಲ್ಲಿ ಏನೂ ಇಲ್ಲ.','Nothing in the last six weeks.':'ಕಳೆದ ಆರು ವಾರಗಳಲ್ಲಿ ಏನೂ ಇಲ್ಲ.',
'Director':'ನಿರ್ದೇಶಕ','Writer':'ಬರಹಗಾರ','Actor':'ನಟ','Producer':'ನಿರ್ಮಾಪಕ','Cinematographer':'ಛಾಯಾಗ್ರಾಹಕ','Editor':'ಸಂಕಲನಕಾರ','Composer':'ಸಂಗೀತ ನಿರ್ದೇಶಕ','Sound':'ಧ್ವನಿ',
'Most awarded':'ಹೆಚ್ಚು ಪ್ರಶಸ್ತಿ ಪಡೆದವರು','Shown at the most festivals':'ಹೆಚ್ಚು ಉತ್ಸವಗಳಲ್ಲಿ ಪ್ರದರ್ಶಿತ','What winners won next':'ವಿಜೇತರು ಮುಂದೆ ಗೆದ್ದದ್ದು','By festival':'ಉತ್ಸವವಾರು',
'Did winning directors return?':'ವಿಜೇತ ನಿರ್ದೇಶಕರು ಮತ್ತೆ ಬಂದರೇ?','Major awards reached after a festival win':'ಉತ್ಸವ ಗೆಲುವಿನ ನಂತರ ಸಿಕ್ಕ ಪ್ರಮುಖ ಪ್ರಶಸ್ತಿಗಳು','Awards festival winners won next':'ಉತ್ಸವ ವಿಜೇತರು ಮುಂದೆ ಗೆದ್ದ ಪ್ರಶಸ್ತಿಗಳು',
'Films on record per edition':'ಪ್ರತಿ ಆವೃತ್ತಿಯ ದಾಖಲಿತ ಚಿತ್ರಗಳು','Start here':'ಇಲ್ಲಿಂದ ಆರಂಭಿಸಿ','No films on record yet':'ಇನ್ನೂ ದಾಖಲೆಯಲ್ಲಿ ಚಿತ್ರಗಳಿಲ್ಲ','films across all editions':'ಎಲ್ಲಾ ಆವೃತ್ತಿಗಳ ಚಿತ್ರಗಳು',
'All editions':'ಎಲ್ಲಾ ಆವೃತ್ತಿಗಳು','Clear':'ತೆರವುಗೊಳಿಸಿ','‹ Prev':'‹ ಹಿಂದೆ','Next ›':'ಮುಂದೆ ›','0 results':'ಫಲಿತಾಂಶಗಳಿಲ್ಲ','Archive documents':'ಆರ್ಕೈವ್ ದಾಖಲೆಗಳು','Documents':'ದಾಖಲೆಗಳು','Browse these films':'ಈ ಚಿತ್ರಗಳನ್ನು ನೋಡಿ',
'About FilmFest Guide':'FilmFest Guide ಬಗ್ಗೆ','Where the information comes from':'ಮಾಹಿತಿ ಎಲ್ಲಿಂದ ಬರುತ್ತದೆ','What to keep in mind':'ಗಮನದಲ್ಲಿಡಬೇಕಾದದ್ದು','How festival types are worked out':'ಉತ್ಸವದ ಪ್ರಕಾರಗಳನ್ನು ಹೇಗೆ ನಿರ್ಧರಿಸಲಾಗುತ್ತದೆ',
'Open data':'ಮುಕ್ತ ಮಾಹಿತಿ','Stills, posters, portraits and logos':'ಸ್ಥಿರಚಿತ್ರಗಳು, ಪೋಸ್ಟರ್‌ಗಳು, ಭಾವಚಿತ್ರಗಳು ಮತ್ತು ಲಾಂಛನಗಳು','Your privacy':'ನಿಮ್ಮ ಖಾಸಗಿತನ','Use it as an app':'ಆ್ಯಪ್ ಆಗಿ ಬಳಸಿ',
'Corrections, removal and contact':'ತಿದ್ದುಪಡಿ, ತೆಗೆದುಹಾಕುವಿಕೆ ಮತ್ತು ಸಂಪರ್ಕ','Language (beta)':'ಭಾಷೆ (ಬೀಟಾ)',
'Menus, headings and buttons can be shown in Kannada or Hindi. Film titles, names, descriptions and festival data stay as published. These translations are new, so corrections from native speakers are welcome on GitHub.':'ಮೆನು, ಶೀರ್ಷಿಕೆಗಳು ಮತ್ತು ಬಟನ್‌ಗಳನ್ನು ಕನ್ನಡ ಅಥವಾ ಹಿಂದಿಯಲ್ಲಿ ತೋರಿಸಬಹುದು. ಚಿತ್ರಗಳ ಹೆಸರು, ವ್ಯಕ್ತಿಗಳ ಹೆಸರು, ವಿವರಣೆಗಳು ಮತ್ತು ಉತ್ಸವದ ಮಾಹಿತಿ ಪ್ರಕಟವಾದಂತೆಯೇ ಇರುತ್ತವೆ. ಈ ಅನುವಾದಗಳು ಹೊಸವು; ಕನ್ನಡ ಮತ್ತು ಹಿಂದಿ ಬಲ್ಲವರ ತಿದ್ದುಪಡಿಗಳನ್ನು GitHub‌ನಲ್ಲಿ ಸ್ವಾಗತಿಸುತ್ತೇವೆ.',
mon:['ಜನವರಿ','ಫೆಬ್ರವರಿ','ಮಾರ್ಚ್','ಏಪ್ರಿಲ್','ಮೇ','ಜೂನ್','ಜುಲೈ','ಆಗಸ್ಟ್','ಸೆಪ್ಟೆಂಬರ್','ಅಕ್ಟೋಬರ್','ನವೆಂಬರ್','ಡಿಸೆಂಬರ್'],
pat:[[/^films on record from the (\d+) festivals in the guide$/,'ಮಾರ್ಗದರ್ಶಿಯ $1 ಉತ್ಸವಗಳ ದಾಖಲಿತ ಚಿತ್ರಗಳು'],[/^festival editions, (\d+) to (\d+)$/,'ಉತ್ಸವ ಆವೃತ್ತಿಗಳು, $1 ರಿಂದ $2'],
[/^films from the ([^·]+) edition$/,'$1 ಆವೃತ್ತಿಯ ಚಿತ್ರಗಳು'],[/^Page (\d+) of (\d+)$/,'ಪುಟ $1 / $2'],[/^(\d+) editions?$/,'$1 ಆವೃತ್ತಿಗಳು'],[/^and (\S+) more$/,'ಮತ್ತು ಇನ್ನೂ $1'],
[/^until ([^·]+)$/,'$1ರವರೆಗೆ'],[/^Next: ([^·]+)$/,'ಮುಂದೆ: $1'],[/^ended ([^·]+)$/,'$1ರಂದು ಮುಗಿದಿದೆ'],[/^last ([^·]+)$/,'ಹಿಂದಿನದು $1'],
[/^[Uu]sually in ([^·]+)$/,'ಸಾಮಾನ್ಯವಾಗಿ $1 ತಿಂಗಳಲ್ಲಿ'],[/^(\d{4}) dates not confirmed$/,'$1ರ ದಿನಾಂಕ ಖಚಿತವಾಗಿಲ್ಲ'],[/^Likely over for (\d{4})$/,'$1ಕ್ಕೆ ಬಹುಶಃ ಮುಗಿದಿದೆ'],
[/^((?:Jan|Febr)uary|March|April|May|June|July|August|(?:Septem|Octo|Novem|Decem)ber) (\d{4})$/,'$1 $2']]},
hi:{'Search':'खोजें','Explore':'खोजबीन','About':'परिचय','All':'सभी','Close':'बंद करें','Region':'क्षेत्र',
'Film festivals, films and people':'फ़िल्म उत्सव, फ़िल्में और लोग','What screens at film festivals, starting with India':'फ़िल्म उत्सवों में क्या दिखाया जाता है: भारत से शुरुआत',
'film festivals worldwide':'दुनिया भर के फ़िल्म उत्सव','countries with a festival':'उत्सव वाले देश','people credited':'श्रेय पाने वाले लोग','awards and honours':'पुरस्कार और सम्मान',
'Happening now':'अभी जारी','Full calendar ›':'पूरा कैलेंडर ›','Next up':'आगे','Work in progress':'काम जारी है','In the guide':'गाइड में',
'World map of films and people ›':'फ़िल्मों और लोगों का विश्व नक्शा ›','Festival calendar: on now and next ›':'उत्सव कैलेंडर: अभी और आगे ›','Languages ›':'भाषाएँ ›',
'Roles: directors, writers, actors, crew ›':'भूमिकाएँ: निर्देशक, लेखक, अभिनेता, तकनीकी दल ›','Award impact: what winning led to ›':'पुरस्कार का असर: जीत के बाद क्या हुआ ›',
'Across festivals ›':'सभी उत्सवों में ›','World festivals, work in progress ›':'विश्व उत्सव, काम जारी है ›','Also this month:':'इस महीने ये भी:',
'Founded by decade':'दशक के अनुसार स्थापना','Notable festivals worldwide':'दुनिया के प्रमुख उत्सव','Award-winning films':'पुरस्कृत फ़िल्में','Data freshness':'डेटा कितना ताज़ा है',
'Discover':'खोज','Films':'फ़िल्में','People':'लोग','Awards':'पुरस्कार','Map':'नक्शा','Past years':'पिछले वर्ष','Festivals':'उत्सव','Numbers':'आँकड़े','Overview':'सारांश','Notable festivals':'प्रमुख उत्सव','Winners':'विजेता फ़िल्में','Data':'डेटा',
'Calendar':'कैलेंडर','Languages':'भाषाएँ','Roles':'भूमिकाएँ','Award impact':'पुरस्कार का असर','Across festivals':'सभी उत्सवों में','World festivals':'विश्व उत्सव',
'Festival calendar':'उत्सव कैलेंडर','Coming next':'आगामी','Just finished':'अभी समाप्त','likely on now':'शायद अभी जारी','Likely on now':'शायद अभी जारी',
'On now':'अभी जारी','Over':'समाप्त','dates TBC':'तारीखें तय नहीं','No festivals on record.':'रिकॉर्ड में कोई उत्सव नहीं।',
'Nothing on record for today.':'आज के लिए रिकॉर्ड में कुछ नहीं।','Nothing on record yet.':'अभी रिकॉर्ड में कुछ नहीं।','Nothing in the last six weeks.':'पिछले छह हफ़्तों में कुछ नहीं।',
'Director':'निर्देशक','Writer':'लेखक','Actor':'अभिनेता','Producer':'निर्माता','Cinematographer':'छायाकार','Editor':'संपादक','Composer':'संगीतकार','Sound':'ध्वनि',
'Most awarded':'सबसे ज़्यादा पुरस्कृत','Shown at the most festivals':'सबसे ज़्यादा उत्सवों में दिखाई गई','What winners won next':'विजेताओं ने आगे क्या जीता','By festival':'उत्सव के अनुसार',
'Did winning directors return?':'क्या विजेता निर्देशक लौटे?','Major awards reached after a festival win':'उत्सव में जीत के बाद मिले बड़े पुरस्कार','Awards festival winners won next':'उत्सव विजेताओं ने आगे जो पुरस्कार जीते',
'Films on record per edition':'हर संस्करण की दर्ज फ़िल्में','Start here':'यहाँ से शुरू करें','No films on record yet':'अभी कोई फ़िल्म दर्ज नहीं','films across all editions':'सभी संस्करणों की फ़िल्में',
'All editions':'सभी संस्करण','Clear':'साफ़ करें','‹ Prev':'‹ पिछला','Next ›':'अगला ›','0 results':'कोई परिणाम नहीं','Archive documents':'संग्रह दस्तावेज़','Documents':'दस्तावेज़','Browse these films':'ये फ़िल्में देखें',
'About FilmFest Guide':'FilmFest Guide के बारे में','Where the information comes from':'जानकारी कहाँ से आती है','What to keep in mind':'ध्यान रखने योग्य बातें','How festival types are worked out':'उत्सवों के प्रकार कैसे तय होते हैं',
'Open data':'खुला डेटा','Stills, posters, portraits and logos':'स्टिल, पोस्टर, चित्र और लोगो','Your privacy':'आपकी निजता','Use it as an app':'ऐप की तरह इस्तेमाल करें',
'Corrections, removal and contact':'सुधार, हटाना और संपर्क','Language (beta)':'भाषा (बीटा)',
'Menus, headings and buttons can be shown in Kannada or Hindi. Film titles, names, descriptions and festival data stay as published. These translations are new, so corrections from native speakers are welcome on GitHub.':'मेनू, शीर्षक और बटन कन्नड़ या हिन्दी में दिखाए जा सकते हैं। फ़िल्मों के नाम, लोगों के नाम, विवरण और उत्सवों का डेटा जैसा प्रकाशित हुआ वैसा ही रहता है। ये अनुवाद नए हैं, इसलिए हिन्दी और कन्नड़ जानने वालों के सुधारों का GitHub पर स्वागत है।',
mon:['जनवरी','फ़रवरी','मार्च','अप्रैल','मई','जून','जुलाई','अगस्त','सितंबर','अक्टूबर','नवंबर','दिसंबर'],
pat:[[/^films on record from the (\d+) festivals in the guide$/,'गाइड के $1 उत्सवों की दर्ज फ़िल्में'],[/^festival editions, (\d+) to (\d+)$/,'उत्सव संस्करण, $1 से $2'],
[/^films from the ([^·]+) edition$/,'$1 संस्करण की फ़िल्में'],[/^Page (\d+) of (\d+)$/,'पृष्ठ $1 / $2'],[/^(\d+) editions?$/,'$1 संस्करण'],[/^and (\S+) more$/,'और $1'],
[/^until ([^·]+)$/,'$1 तक'],[/^Next: ([^·]+)$/,'अगला: $1'],[/^ended ([^·]+)$/,'$1 को समाप्त'],[/^last ([^·]+)$/,'पिछली बार $1'],
[/^[Uu]sually in ([^·]+)$/,'आम तौर पर $1 में'],[/^(\d{4}) dates not confirmed$/,'$1 की तारीखें तय नहीं'],[/^Likely over for (\d{4})$/,'$1 के लिए शायद समाप्त'],
[/^((?:Jan|Febr)uary|March|April|May|June|July|August|(?:Septem|Octo|Novem|Decem)ber) (\d{4})$/,'$1 $2']]}
};
var EN=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
var lang='en',orig=new WeakMap(),busy=false,queued=false;
try{lang=localStorage.getItem('filmfest_lang')||'en'}catch(e){}
if(!D[lang])lang='en';
// Month names are only swapped inside strings a pattern matched, i.e. our own date and status text, never in data.
function months(s,d){return s.replace(/\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\b/g,function(m,k){return d.mon[EN.indexOf(k)]})}
function one(t,d){if(Object.prototype.hasOwnProperty.call(d,t)&&typeof d[t]==='string')return d[t];
for(var i=0;i<d.pat.length;i++)if(d.pat[i][0].test(t))return months(t.replace(d.pat[i][0],d.pat[i][1]),d);return null}
// "Likely on now · usually in November" and "Calendar month · 12": translate each ' · ' part, if any part is ours.
function tr(s){var d=D[lang];if(!d)return null;var t=s.trim();if(!t)return null;var r=one(t,d);
if(r===null&&t.indexOf(' · ')>0){var hit=false,parts=t.split(' · ').map(function(p){var x=one(p,d);if(x!==null){hit=true;return x}return p});if(hit)r=months(parts.join(' · '),d)}
return r===null?null:s.replace(t,r)}
function walk(root){busy=true;var w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:function(n){var p=n.parentNode&&n.parentNode.nodeName;return p==='SCRIPT'||p==='STYLE'?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT}}),n,list=[];while((n=w.nextNode()))list.push(n);
list.forEach(function(n){var o=orig.get(n);if(o===undefined){if(lang==='en')return;o=n.nodeValue;orig.set(n,o)}
var v=lang==='en'?o:(tr(o)||o);if(n.nodeValue!==v)n.nodeValue=v});
document.documentElement.lang=lang;busy=false}
function mark(){[].forEach.call(document.querySelectorAll('[data-lang]'),function(x){x.classList.toggle('on',x.dataset.lang===lang);x.setAttribute('aria-pressed',x.dataset.lang===lang)})}
function schedule(){if(queued)return;queued=true;requestAnimationFrame(function(){queued=false;walk(document.body);mark()})}
function setLang(l){lang=D[l]?l:'en';try{localStorage.setItem('filmfest_lang',lang)}catch(e){}walk(document.body);mark()}
new MutationObserver(function(){if(busy)return;if(lang!=='en')schedule();else mark()}).observe(document.documentElement,{childList:true,subtree:true,characterData:true});
document.documentElement.lang=lang;
window.FFI18N={set:setLang,get:function(){return lang},tr:function(s,l){var k=lang;lang=l;var r=tr(s);lang=k;return r}};
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-lang]');if(b)setLang(b.dataset.lang)});
window.addEventListener('load',function(){if(lang!=='en')walk(document.body);mark()});
})();
