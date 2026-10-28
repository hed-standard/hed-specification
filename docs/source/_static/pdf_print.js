// Fit code blocks to the printed page; loaded only in the PDF build (sphinx-build -t pdf, see conf.py).
//
// Mediawiki, TSV and similar examples must read as one line per source line, so long lines are not
// wrapped freely. Each code block's font shrinks until its longest line fits the printed content
// width (Letter 816 px - 2 x 18 mm = 680 px), down to FLOOR_PX (6.5 pt). A line still too long at
// the floor is split at the width limit and each continuation starts with a gray "    > ".
document.addEventListener("DOMContentLoaded", function () {
    const PAGE_PX = 680;
    const FLOOR_PX = 6.5 / 0.75;
    const SAFETY = 0.97;
    const CONT = "    > ";

    // Horizontal padding, borders and margins between the code text and the page content box
    function insets(el) {
        let w = 0;
        for (let e = el; e && e.tagName !== "ARTICLE"; e = e.parentElement) {
            const cs = getComputedStyle(e);
            for (const k of ["paddingLeft", "paddingRight", "borderLeftWidth", "borderRightWidth"]) {
                w += parseFloat(cs[k]) || 0;
            }
            if (e !== el) {
                for (const k of ["marginLeft", "marginRight"]) w += Math.max(0, parseFloat(cs[k]) || 0);
            }
        }
        return w;
    }

    function charWidth(pre) {
        const s = document.createElement("span");
        s.textContent = "M".repeat(200);
        pre.appendChild(s);
        const w = s.getBoundingClientRect().width / 200;
        s.remove();
        return w;
    }

    function nextColumn(col, ch) {
        return ch === "\t" ? (Math.floor(col / 8) + 1) * 8 : col + 1;
    }

    function columns(line) {
        let c = 0;
        for (const ch of line) c = nextColumn(c, ch);
        return c;
    }

    // Split text nodes in place so the highlighting spans survive
    function wrap(pre, cap) {
        const walker = document.createTreeWalker(pre, NodeFilter.SHOW_TEXT);
        const nodes = [];
        while (walker.nextNode()) nodes.push(walker.currentNode);
        let col = 0;
        for (let node of nodes) {
            let i = 0;
            while (i < node.data.length) {
                const ch = node.data[i];
                if (ch === "\n") {
                    col = 0;
                    i++;
                    continue;
                }
                const next = nextColumn(col, ch);
                if (next > cap) {
                    const rest = node.splitText(i);
                    const marker = document.createElement("span");
                    marker.className = "pdf-cont";
                    marker.textContent = "\n" + CONT;
                    rest.parentNode.insertBefore(marker, rest);
                    node = rest;
                    i = 0;
                    col = CONT.length;
                    continue;
                }
                col = next;
                i++;
            }
        }
    }

    for (const pre of document.querySelectorAll("div.highlight pre")) {
        const maxCols = Math.max(...pre.textContent.split("\n").map(columns));
        const avail = (PAGE_PX - insets(pre)) * SAFETY;
        const base = parseFloat(getComputedStyle(pre).fontSize);
        const cw = charWidth(pre);
        if (maxCols * cw <= avail) continue;
        const size = Math.max(FLOOR_PX, (base * avail) / (maxCols * cw));
        pre.style.fontSize = size + "px";
        if (size === FLOOR_PX) wrap(pre, Math.floor(avail / ((cw * size) / base)));
    }
});
