"""Experimental source transformation; arithmetic acceptance pending."""

def transform(s):
    s=s.replace('const h=half[n].x,j=half[n].y,x=fsq(n+\'.chart.x\',h);',"const h=half[n].x,j=half[n].y;\n if(n!=='H' && reciprocalCharts.has(n)){points[n]={scaledV:h,scaledI:j};continue;}\n const x=fsq(n+'.chart.x',h);")
    start=s.index('function subtractReciprocal(');end=s.index('function subtractSharedJoint(',start)
    s=s[:start]+'''function subtractReciprocal(name,Qp,Rp){
     const V=Qp.scaledV,I=Qp.scaledI,a=Rp.h,b=Rp.j,c=Rp.x;
     const Qv=[fresh(name+'.scaledQ.0','base'),fresh(name+'.scaledQ.1','base')],
     Kv=[fresh(name+'.scaledK.0','base'),fresh(name+'.scaledK.1','base')],
     W=[fresh(name+'.jointW.0','base'),fresh(name+'.jointW.1','base')];
     const equations=[
      fsub(rawFmul(V,Qv),rawFmul(c,W)),
      fsub(fadd(fadd(rawFmul(V,V),rawFmul(Qv,Qv)),fadd(rawFmul(D,rawFmul(W,W)),fscale(rawFmul(b,W),2))),fc(1)),
      fsub(rawFmul(a,I),fadd(fadd(rawFmul(b,V),rawFmul(c,Qv)),rawFmul(D,rawFmul(V,W)))),
      fadd(rawFmul(a,Kv),fadd(fadd(rawFmul(b,Qv),rawFmul(c,V)),rawFmul(D,rawFmul(Qv,W))))
     ];
     equations.forEach((e,k)=>e.forEach((x,j)=>residual(name+'.biquad.'+k+'.'+j,x)));
     Qp.f=fquot(name+'.primaryF',rawFmul(V,V),c,'nonzero_root_square_abscissa');
     const YV=fquot(name+'.alternateFSquare',fsub(c,rawFmul(Kv,Kv)),rawFmul(D,c),'nonzero_root_square_abscissa_and_D');
     return {fSquared:YV,logDenominator:Kv,logScale:Qv};
    }
    ''' + s[end:]
    s=s.replace('function parameters(name,p){return{','function parameters(name,p){if(p.fSquared)return {point:p,fSquared:p.fSquared,z:null};return{')
    s=s.replace("let w=fmul(name+'.w',D,fsq(name+'.fSquare',p.f));", "let w=fmul(name+'.w',D,p.fSquared||fsq(name+'.fSquare',p.f));")
    s=s.replace("rawFmul(primaryRatio,PU[i].point.g),PU[i].point.l", "rawFmul(primaryRatio,PU[i].point.scaledV),PU[i].point.scaledI")
    s=s.replace("const tests=[...PU.map((p,i)=>({value:p.point.g,order:i===0?45:i===1?12:1})),...PV.map(p=>({value:fconj(p.f),order:1}))];", "const tests=[...PU.map((p,i)=>({squared:p.f,order:i===0?45:i===1?12:1})),...PV.map(p=>p.fSquared?({squared:fconj(p.fSquared),order:1}):({value:fconj(p.f),order:1}))];")
    s=s.replace("tests.forEach((t,j)=>saveF('test'+j,t.value));", "tests.forEach((t,j)=>saveF((t.squared?'squaredTest':'test')+j,t.squared||t.value));")
    s=s.replace(".map((t,j)=>fsq('testSquare.'+m+'.'+j,t.value));", ".map((t,j)=>t.squared||fsq('testSquare.'+m+'.'+j,t.value));")
    return s
