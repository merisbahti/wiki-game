#Gets a wiki site based on article name, name must start with /wiki/ 
def getwikisite(name):
    import urllib.request
    return urllib.request.urlopen("http://en.wikipedia.org"+name).read()

# Get all links except ones that contain a dot or colon. (Avoid non-articles)
def get_links(doc):
    from bs4 import BeautifulSoup 
    from bs4 import BeautifulSoup, SoupStrainer
    l = []
    for link in BeautifulSoup(doc, parse_only=SoupStrainer('a')):
        if link.has_attr('href') and link['href'].startswith("/wiki/") and not "." in link['href'] and not ":" in link['href']:
            l.append(link['href'])
    return l

# Recursive function
def search(start, target, steps = 0, chain = None, visited_links = []): 
    steps = 1+steps
    if steps > 8:
        return None 
    if chain is None:
        chain = start 
    else:
        chain = chain + "->" + start
    links = get_links(getwikisite((start))) 
    visited_links.append(start)
    if (target in links):
        return (chain+"->"+target, steps)
    else:
        for newlink in links:
            if newlink not in visited_links:
                result = search(newlink, target, steps, chain, visited_links)
                if result is not None:
                    return result
        return None
