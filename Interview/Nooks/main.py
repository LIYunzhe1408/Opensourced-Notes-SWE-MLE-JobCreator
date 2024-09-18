import requests
from bs4 import BeautifulSoup


def get_related_pages_from_wiki_link(url: str) -> list:
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return []
        if not url.startswith("https://en.wikipedia.org"):
            # Don't crawl non-Wikipedia pages
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        valid_children_links = []

        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/wiki/'):
                full_link = f"https://en.wikipedia.org{href}"
                title = href[6:].replace('_', ' ')

                # Skip backlinks and non-article pages
                do_not_crawl_prefixes = ['Main Page', 'Talk:', 'Wikipedia:', 'File:', 'Special:', 'Help:', 'Portal:']
                if any(title.startswith(prefix) for prefix in do_not_crawl_prefixes) or full_link == url:
                    continue
                valid_children_links.append(full_link)

        return list(set(valid_children_links))  # Remove duplicates

    except Exception as e:
        print(f"Error fetching Wikipedia page: {e}")
        return []


def find_degree_of_separation(url1: str, url2: str) -> int:
    if url1 == url2:
        return 0
    degree = 0

    related_pages = get_related_pages_from_wiki_link(url1)
    if url2 in related_pages:
        degree += 1
        return degree

    degree += 1
    relate_list = []
    for related_page in related_pages:
        temp_related_pages = get_related_pages_from_wiki_link(related_page)
        relate_list.append(temp_related_pages)
        if url2 in temp_related_pages:
            degree += 1
            return degree

    degree += 1
    for page_list in relate_list:
        for page in page_list:
            relate_links = get_related_pages_from_wiki_link(page)
            if url2 in relate_links:
                degree += 1
                return degree

    return -1


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Sales"
    related_pages = get_related_pages_from_wiki_link(url)
    print(f"Number of related links for {url}: {len(related_pages)}")

    url1 = "https://en.wikipedia.org/wiki/Random_walk"
    url2 = "https://en.wikipedia.org/wiki/Megalodon"
    separation = find_degree_of_separation(url1, url2)
    print(f"Degree of separation between {url1} and {url2}: {separation}")
