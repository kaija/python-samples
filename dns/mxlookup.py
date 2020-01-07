import dns.resolver

def lookup(domain):
    try:
        MX = dns.resolver.query(domain, 'MX')
        return True
    except:
        return False
