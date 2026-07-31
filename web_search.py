from duckduckgo_search import DDGS


def search_web(query):

    try:

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=5
                )
            )

        if not results:
            return "No results found."

        answer = ""

        for i, item in enumerate(results, start=1):

            answer += (
                f"{i}. {item['title']}\n"
                f"{item['body']}\n\n"
            )

        return answer

    except Exception as e:

        return str(e)