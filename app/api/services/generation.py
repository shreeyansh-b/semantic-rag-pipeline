from google import genai


class GenerationService:
    def __init__(self, api_key: str):
        self._client = genai.Client(api_key=api_key)

    def generate(self, query: str, context_chunks: list[str]) -> str:
        context = "\n\n".join(context_chunks)

        prompt = f"""Answer the question based on the context below.
        Context:
        {context}

        Question:  {query}
        """

        response = self._client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text


def get_generation_service(api_key: str) -> GenerationService:
    return GenerationService(api_key)
