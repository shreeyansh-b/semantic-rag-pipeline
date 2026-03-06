class IngestionLoader:

    def read_md_file(self, filepath):
        """Reads the content from markdown files and returns a list of lines"""
        # TODO: consider accepting a list of filepaths and returning a dict {filepath: content}
        # TODO: validate that the file is actually a .md file before reading
        # TODO: add support for reading from a directory (glob all *.md files)
        # NOTE: 'content' is accessible outside the `with` block because Python's
        #       with/if/for blocks do NOT create a new scope (unlike JS) — variables
        #       live in the enclosing function's scope.
        try:
            with open(filepath, 'r', encoding="utf-8") as file:
                content = file.readlines()
            # file handle is closed here, but 'content' (a plain string) persists
            return content
        except FileNotFoundError:
            return "File not found!"
        except Exception as e:
            return f"An error occurred: {e}"
