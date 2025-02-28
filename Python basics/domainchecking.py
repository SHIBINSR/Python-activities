import whois

def is_registered(domain_name):
    try:
        global w
        w =whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
    
domains=["google.com",
         "github.com",
         "numota.in",
         "shibinsr17.com",
         "rahulvm.in",
         "jefree.com"]

for i in domains:
    if is_registered(i):
        print(i,"alredy registerd")
        
    else:
        print(i,"not registered")