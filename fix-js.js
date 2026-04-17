const fs = require('fs');
const files = ['index.html', 'services.html', 'about.html', 'portfolio.html', 'academy.html', 'contact.html'];
for (const file of files) {
  if (!fs.existsSync(file)) continue;
  let html = fs.readFileSync(file, 'utf8');
  
  // FIX 1: contactForm listener causing null error
  html = html.replace(
    /document\.getElementById\('contactForm'\)\.addEventListener\('submit',\s*async\s*function\(e\)\s*\{/g,
    "const cf = document.getElementById('contactForm');\nif (cf) cf.addEventListener('submit', async function(e) {"
  );
  
  fs.writeFileSync(file, html);
}
console.log('Fixed JS errors in all files');
