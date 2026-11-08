# Plan: `reunion.html` Supplemental Page

## 1. Overview & Objectives
Create a polished supplemental web page named `reunion.html` for **Our Vinyl Vows**, adhering to the visual style of `index.html` while introducing interactive collapsible sections, HTML5 audio playback, BPM data, chronological version histories (newest first) including split live/practice tracks, lyrics sections, and embedded YouTube videos.

## 2. Data Sources & Mappings
- **BPM Source**: `bpm.md` (contains 13 songs with their BPM values). Songs not in `bpm.md` will have blank BPM.
- **Audio Sources (`index.html` & directories)**:
  - **Main Album ("You, Me and Einstein")**: Core tracks.
  - **Other Tracks**: `Brainfed.m4a`, `Dancing_Like_Walken.mp3`, `Digital_Jockey.mp3`, `Secret_Santa.mp3` (Excluding `A_Little_Dabll_Do_Ya.mp3`).
  - **Live Shows & Practices (Only if split into individual songs)**:
    - EP Rough (`01_Sticks_And_Stones.m4a`, `02_Almond_Joy.m4a`, `03_Knock_Me_Out.m4a`, `04_Pandemonium.m4a`, `05_Brainfed.m4a`)
    - Trinity Gold Media (10.14.2011) - split into songs
    - Arlene Francis Center (07.27.2012) - split into songs
    - Homestead Lanes (03.24.2013) - split into songs
    - Practice (06.25.2013) - split into songs
    - **Exclusions**: Full shows/practices not split into individual tracks (e.g., `2013.09.01_JumpingTurtle_with_Pounders.mp3`) and `A_Little_Dabll_Do_Ya.mp3`.
- **Chronological Dating for Version Sorting (Newest First)**:
  - 2013.06.25 (Practice 2013)
  - 2013.03.24 (Homestead Lanes 2013)
  - 2013 (Main Album / EP Rough)
  - 2012.07.27 (Arlene Francis Center 2012)
  - 2011.10.14 (Trinity Gold Media 2011)

## 3. Song Aggregation & Details
Each unique song will aggregate all its recorded versions across albums, other tracks, EP rough, live shows, and practices (that are split into songs).
- **Sorting**:
  - Main list: Alphabetical by song name.
  - Expanded details (versions): Chronological, **newest first**.
- **Default View per Song**:
  - Song title (clickable to toggle collapsible section).
  - HTML5 `<audio>` player for the **latest version** of the song.
  - BPM value (from `bpm.md`, or blank if unknown).
- **Expanded Collapsible View**:
  - Complete list of all recorded versions of the song (sorted newest first), each with an HTML5 audio player and date/context label.
  - Lyrics section (placeholder ready for song lyrics).
  - Embedded YouTube video (if mapped via `index.html` quick links), hidden by default and revealed when expanded.

## 4. YouTube Video Mappings
Mapped from `index.html` iframe IDs and anchor tags:
- **Gone**: `https://www.youtube.com/embed/ksUXiIoYndk`
- **A New Hope**: `https://www.youtube.com/embed/_UzDPJE9WRQ`
- **Almond Roca**: `https://www.youtube.com/embed/sxcrZgxsMxY`
- **Brainfed**: `https://www.youtube.com/embed/tztVcsT1AUw` & Live `https://www.youtube.com/embed/2aOT75rwj7Y`
- **Secret Santa**: `https://www.youtube.com/embed/OmH1cobPFWY`
- **Hell of a Way to Die**: `https://www.youtube.com/embed/FTMUG1agbLI`

## 5. Technical Implementation Details
- **File**: `reunion.html`
- **Styling**: Consistent CSS with `index.html` (Helvetica/Arial font, clean padding, responsive container, audio element styling).
- **Interactivity**: HTML5 `<details>` and `<summary>` elements for collapsible sections.
