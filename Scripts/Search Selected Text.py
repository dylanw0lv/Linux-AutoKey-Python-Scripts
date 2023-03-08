import webbrowser

text = clipboard.get_selection().split()
search_list = [i + "+" if text.index(i) != (len(text) - 1) else i for i in text]
search = "".join(search_list)

webbrowser.open(f"https://www.google.com/search?q={search}")



