# PUCP Web Scraping
from pucp_scraper.parser import parse_urls_to_scrape
from pucp_scraper.scraper import scrape_item
from pucp_scraper.writer import write_to_csv


if __name__ == "__main__":
    base_url = "https://repositorio.pucp.edu.pe"
    initial_url = "communities/d727ae50-d839-4cdb-b630-2fedd11c8a89?spc.page=1&query=lengua%20de%20seña"

    urls_to_scrape = parse_urls_to_scrape(base_url, initial_url)
    print(urls_to_scrape)

    data = []
    for url in urls_to_scrape:
        try:
            title, meta_tags = scrape_item(url)
            dict_to_write = {
                "title": title,
                "description": meta_tags.get("description", ""),  # safe access
                "author": meta_tags.get("citation_author", ""),
            }
            data.append(dict_to_write)
        except Exception as e:
            print(e)

    write_to_csv(data)

    print("El web scraping ha finalizado.")
