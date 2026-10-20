// Point the toolbar's print button at the typeset PDF (print.py) instead of print.html
const pdf = document.getElementById("print-button").closest("a");
pdf.href = path_to_root + "polish-club.pdf";
pdf.title = "Download as PDF";
