
# Lyric Scraper

**Lyric Scraper** is a Python-based application that allows users to search for song lyrics by entering the artist and song title. It features both a command-line interface (CLI) and a graphical user interface (GUI) built with Tkinter. The application fetches lyrics from [AZLyrics](https://www.azlyrics.com/) and displays them in the chosen interface.

---

## Features

### Command-Line Interface (CLI)
- Simple and lightweight.
- Users input the artist and song title directly into the terminal.
- Displays the lyrics directly in the terminal.

### Graphical User Interface (GUI)
- User-friendly design with input fields for artist and song title.
- Displays the lyrics in a scrollable text box.
- **Planned Features**:
  - Album cover display for searched songs.
  - Improved design for a more modern look and feel.

---

## Installation

### Prerequisites
- Python 3.x
- Required libraries: `requests`, `beautifulsoup4`, `tkinter` (Tkinter is included in the Python standard library on most systems).

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/oneilchan/simple-lyric-scraper.git
   cd lyric-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Command-Line Interface
Run the CLI script:
```bash
python cli.py
```
1. Enter the artist name and song title when prompted.
2. The lyrics will be displayed in the terminal.

### Graphical User Interface
Run the GUI script:
```bash
python gui.py
```
1. Enter the artist name and song title in the respective input fields.
2. Click the **"Search Lyrics"** button.
3. The lyrics will appear in the text box.

---

## Planned Improvements
- **Scraper**: Handle edge cases for artist and song titles (e.g., special characters or incorrect formats).
- **CLI**: Modularize the code for better readability and maintainability.
- **GUI**:
  - Display album cover alongside lyrics.
  - Redesign for improved aesthetics and usability.

---


## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- Lyrics data sourced from [AZLyrics](https://www.azlyrics.com/).
