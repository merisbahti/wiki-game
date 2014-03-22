#Gets a wiki site based on article name, name must start with /wiki/ 
def getwikisite(name):
    import urllib.request
    print(name)
    return urllib.request.urlopen("http://en.wikipedia.org"+name).read()

def get_links(doc):
    from bs4 import BeautifulSoup 
    from bs4 import BeautifulSoup, SoupStrainer
    l = []
    for link in BeautifulSoup(doc, parse_only=SoupStrainer('a')):
        if link.has_attr('href') and link['href'].startswith("/wiki/") and not "." in link['href'] and not ":" in link['href']:
            l.append(link['href'])
    return l

# Traverse this bitch. The Idea is that the highest amount of steps is 8
def search(link, visited_links, target, steps = 0, chain = None): 
    steps = 1+steps
    if steps > 8:
        return None 
    if chain is None:
        chain = link
    else:
        chain = chain + "->" + link
    print(chain)
    links = get_links(getwikisite((link))) 
    visited_links.append(link)
    #print(visited_links)
    if (target in links):
        print("Found target")
        return (chain+"->"+target, steps)
    else:
        for newlink in links:
            if newlink not in visited_links:
                result = search(newlink, visited_links, target, steps, chain)
                if result is not None:
                    return result
        print("Done a whole level")
        return None
            

print(search("/wiki/Cream_liqueur", [], "/wiki/Hitler", 0))
