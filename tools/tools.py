from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str):
    """Searches for Linkedin or Twitter Profile Page."""
    print("search: ", name)
    search = TavilySearchResults()
    res = search.run(f"{name}")

    # return the first result.url
    return res[0]["url"]
