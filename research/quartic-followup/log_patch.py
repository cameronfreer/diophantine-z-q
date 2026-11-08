"""Experimental source transformation; arithmetic acceptance pending."""

def transform(s):
    start=s.index('  let w2=fsq(',s.index('function log('));end=s.index('\n }\n let rawout=',start)
    s=s[:start]+'''  let w2=fsq(name+'.wPower2',w),w4=fsq(name+'.wPower4',w2);
      const basis=[fc(1),w,w2,rawFmul(w,w2),w4,rawFmul(w,w4),rawFmul(w2,w4),fc(0),rawFmul(w4,w4)];
      const nc=[Q(1),Q(-398,145),Q(48424,17835),Q(-16398986,14297725),Q(8855199,48612265),Q(-131072,29167359),Q(-32768,243061325),Q(0),Q(114688,105731676375)];
      const qc=[Q(1),Q(-68,29),Q(11358,5945),Q(-137172,219965),Q(14421,219965)];
      let num=fc(0),den=fc(0);
      nc.forEach((c,j)=>num=fadd(num,fscale(basis[j],c)));
      qc.forEach((c,j)=>den=fadd(den,fscale(basis[j],c)));
      const qpoly=den.map((v,j)=>assign(name+'.rationalQ.'+j,v));
      const combined=fmul(name+'.rationalDenominator',p.point.logDenominator||p.point.k,qpoly);
      const eta=fquot(name+'.scaled',fscale(num,-1),combined,'positive_rational_Q_and_original_log_denominator');
      return p.point.logScale?saveF(name,rawFmul(p.point.logScale,eta)):saveF(name,eta);
    ''' +s[end:]
    return s
