// Force a number between 0 and 1
function clamp01(val) {
    return Math.min(1, Math.max(0, val));
}

// Force a hex value to have 2 characters
function pad2(c) { return c.length == 1 ? '0' + c : '' + c }

// Assumes: r, g, and b are contained in [0, 255]
// Returns: { h, s, l } in [0,1]
function rgbToHsl(r, g, b){
    r /= 255, g /= 255, b /= 255;
    var max = Math.max(r, g, b), min = Math.min(r, g, b);
    var h, s, l = (max + min) / 2;

    if(max == min){
        h = s = 0; // achromatic
    }else{
        var d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch(max){
            case r: h = (g - b) / d + (g < b ? 6 : 0); break;
            case g: h = (b - r) / d + 2; break;
            case b: h = (r - g) / d + 4; break;
        }
        h /= 6;
    }

    return { h: h, s: s, l: l };
}

// Assumes: h, s, and l are contained in the set [0, 1]
// Returns: { r, g, b } in the set [0, 1]
function hslToRgb(h, s, l){
    var r, g, b;

    if(s == 0){
        r = g = b = l; // achromatic
    }else{
        var hue2rgb = function hue2rgb(p, q, t){
            if(t < 0) t += 1;
            if(t > 1) t -= 1;
            if(t < 1/6) return p + (q - p) * 6 * t;
            if(t < 1/2) return q;
            if(t < 2/3) return p + (q - p) * (2/3 - t) * 6;
            return p;
        }

        var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
        var p = 2 * l - q;
        r = hue2rgb(p, q, h + 1/3);
        g = hue2rgb(p, q, h);
        b = hue2rgb(p, q, h - 1/3);
    }

    return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
}

// Assumes r, g, and b are contained in the set [0, 255]
// Returns a 3 or 6 character hex
function rgbToHex(r, g, b) {
    var hex = [ pad2(Math.round(r).toString(16)),pad2(Math.round(g).toString(16)),pad2(Math.round(b).toString(16)) ];
    return hex.join("");
}

// Assumes hex is a string of six alphanumeric characters. It can have a hashtag at the start as well
// Returns: { r, g, b } in the set [0, 255]
function hexToRgb(hex) {
    if (hex[0]=="#") { hex=hex.slice(1) }
    const r = parseInt(hex.slice(0, 2), 16);
    const g = parseInt(hex.slice(2, 4), 16);
    const b = parseInt(hex.slice(4, 6), 16);
    return { r: r, g: g, b: b };
}

// Assumes color is in a { h, s, l } format. Amount is a percentage for how much you decrease it from it's current value
function desaturate(color, amount) {
    amount = (amount === 0) ? 0 : (amount || 10);
    color.s -= ((amount)/100)*color.s;
    return color
}

// Assumes color is in a { h, s, l } format. Amount is a percentage for how much you increase it from it's current value
function saturate(color, amount) {
    amount = (amount === 0) ? 0 : (amount || 10);
    color.s += (amount/100)*(100-color.s);
    return color
}

// Assumes color is in a { h, s, l } format.
function greyscale(color) { return desaturate(color,100) }

// Assumes color is in a { h, s, l } format. Amount is a percentage for how much you increase it from it's current value
function lighten(color, amount) {
    amount = (amount === 0) ? 0 : (amount || 10);
    color.l += (amount/100)*(100-color.l);
    return color;
}

// Assumes color is in a { h, s, l } format. Amount is a percentage for how much you decrease it from it's current value
function darken(color, amount) {
    amount = (amount === 0) ? 0 : (amount || 10);
    color.l -= ((amount)/100)*color.l;
    return color
}

// r, g, and b are contained in [0, 255], amount is a percentage for how much you decrease it from it's current value
function brighten(r,g,b, amount) {
    amount = (amount === 0) ? 0 : (amount || 10);
    r = Math.max(0, Math.min(255, r - Math.round(255 * - (amount / 100))));
    g = Math.max(0, Math.min(255, g - Math.round(255 * - (amount / 100))));
    b = Math.max(0, Math.min(255, b - Math.round(255 * - (amount / 100))));
    return { r: r, g: g, b: b }
}
