# 🎵 Python Lyrics Player

A simple Python-based music player that displays song lyrics in the terminal with a typewriter animation and timestamp-based synchronization.

The project uses **Pygame Community Edition (pygame-ce)** for audio playback and Python for dynamic lyric rendering.

## ✨ Features

* 🎧 Play MP3 audio directly from Python.
* ⌨️ Display lyrics with a typewriter-style animation.
* ⏱️ Timestamp-based lyric synchronization.
* 🔄 Dynamically update lyrics based on the current playback position.
* 🖥️ Terminal-based interface.
* 🐍 Built with Python.

## 🛠️ Technologies Used

* Python 3.14
* Pygame CE
* Time Module
* OS Module

## 📁 Project Structure

```text
Lyrics/
│
├── main.py
├── song.mp3
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Navigate to the Project

```bash
cd Lyrics
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install pygame-ce
```

### 4. Add Your Audio File

Place your MP3 file inside the project directory and name it:

```text
song.mp3
```

### 5. Run the Application

```bash
python main.py
```

## 🎼 How It Works

The application follows a simple workflow:

1. Loads the MP3 audio file using Pygame.
2. Starts music playback.
3. Retrieves the current playback position.
4. Compares the playback time with predefined lyric timestamps.
5. Calculates how many characters should be displayed.
6. Updates the terminal to create a dynamic lyrics animation.

## 📝 Customization

You can customize the lyrics in `main.py`:

```python
lyrics = [
    "Maybe I just wanna be yours",
    "I wanna be yours",
    "I wanna be yours",
    "Wanna be yours",
    "Wanna be yours",
    "Wanna be yours....."
]
```

Adjust the timestamps according to your audio:

```python
timings = [
    [0.0, 3.0],
    [3.0, 6.0],
    [6.0, 9.0],
    [9.0, 12.0],
    [12.0, 15.0],
    [15.0, 19.8]
]
```

**Note:** These timestamps are examples. Adjust them to match the actual vocal timing of your audio.

## 🚀 Future Improvements

* [ ] More accurate vocal synchronization.
* [ ] Smooth terminal animations.
* [ ] Support for multiple songs.
* [ ] Automatic lyric timestamp detection.
* [ ] Customizable terminal themes.
* [ ] GUI-based music player.

## 👨‍💻 Author

**Shahariar Ahammad Fahim**

CSE Student | Python Developer | Frontend Developer

## 📜 License

This project is open-source and available under the MIT License.
