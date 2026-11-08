"""Experimental source transformation; arithmetic acceptance pending."""

def transform(s):
    s=s.replace(' let T=b;'," let T=preparationBase ? assign(name+'.preparationT',preparationBase) : b;")
    s=s.replace("let nw=save('scalar.W',add(one,nCore));","let nw=save('scalar.W',nCore);")
    s=s.replace("pole('scalar',rho,scalar,true,mul(rho,W2));","pole('scalar',rho,scalar,false,mul(rho,W2));")
    return s
