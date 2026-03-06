
class IngestionChunking:

    DEFAULT_STRATEGY = "heading"

    # HEADING_TAGS = ["#", "##", "###", "####",
    #                 "#####", "######"]  # h1, h2 h3, h4, h5, h6

    def chunk_md_file(self, content: list[str], strategy: str = DEFAULT_STRATEGY) -> list[str]:
        """Returns list of chunks which are chunked by heading (default)"""

        if not content:
            raise ValueError("Content can't be empty!")

        if strategy is not self.DEFAULT_STRATEGY:
            raise ValueError("Only heading strategy is supported!")

        in_codeblock = False

        chunks = []

        for line in content:
            stripped_line = line.strip()

            if not stripped_line:
                print("Empty line detected! Skipping...")
                continue

            if stripped_line.startswith("```"):
                in_codeblock = not in_codeblock

                # Assumption is md file either starts with a heading
                # or has an intro without heading and then later has headings
                # In later case, the content before first heading detected will be chunked separately

                # Checking for if the first character has "#"

            if stripped_line.startswith("#") and not in_codeblock:
                chunks.append(stripped_line)
                continue

            if not chunks:
                chunks.append(stripped_line)
                continue

            chunks[-1] = chunks[-1] + "\n" + stripped_line

        return chunks
