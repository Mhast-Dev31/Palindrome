class PalindromeChecker:
    def cleaned(self, text: str) -> str:
        return text.strip().lower().replace(" ", "")

    def is_palindrome(self, text: str) -> bool:
        clean = self.cleaned(text)
        return clean == clean[::-1]


class FileProcessor:
    def __init__(self, filename: str):
        self.filename = filename

    def read_lines(self):
        with open(self.filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    yield line

    def process_file(self, checker: PalindromeChecker):
        for line in self.read_lines():
            result = checker.is_palindrome(line)
            print(result)


class Application:
    def __init__(self, default_file="test_data.txt"):
        self.default_file = default_file

    def run(self):
        checker = PalindromeChecker()
        filename = self.default_file

        try:
            processor = FileProcessor(filename) 
            processor.process_file(checker)
        except FileNotFoundError:
            filename = input(f"{self.default_file} not found. Enter filename: ")
            try:
                processor = FileProcessor(filename)
                processor.process_file(checker)
            except FileNotFoundError:
                print("Error: File not found. Exiting program.")


if __name__ == "__main__":
    app = Application()
    app.run()
