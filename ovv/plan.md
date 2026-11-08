# Summary of Changes: `reunion.html` Reunion Song Archive

## 1. Overview of Delivered Features
- **Supplemental Web Page (`reunion.html`)**: Created a polished companion page matching the aesthetic and styling of `index.html`.
- **BPM Integration**: Integrated BPM data from `bpm.md` for all applicable songs, leaving unknowns blank.
- **Main Album Identification**: Added album cover thumbnail icons (`albumcover.jpg`) next to the 9 tracks belonging to the main album *You, Me and Einstein*.
- **Default Audio Playback**: Configured default audio players in the summary headers to embed the **main album version** when an album version exists, falling back to the latest recording otherwise.
- **Chronological Version History**: Expanded collapsible sections (`<details>` / `<summary>`) showing all recorded versions (main album, other tracks, EP rough, split live shows, and practice sessions) sorted **newest first**.
- **Dual-Container Pre-Sorted Architecture**: Built two separate pre-sorted containers (`#container-alpha` for alphabetical order across all 19 songs, and `#container-track` for original track order across the 9 album tracks) to ensure lightning-fast switching without DOM element reordering or audio player resets.
- **Interactive Filtering & Toggle Undos**: Added text filter buttons ("Hide Album Songs", "Show Album Songs Only", "Show All") that support toggle-undoing (clicking an active filter twice resets to show all) and feature active state styling.
- **Dynamic Row Renumbering**: Automatically recalculates and formats sequential song numbering (`01.` through `19.`) dynamically for any active filter or sort state.
- **Audio Auto-Pause**: Automatically pauses any currently playing audio file whenever a filter or sort button is clicked.
- **Supplemental Artifacts**: Created `bpm.md`, `bpm.jpg`, and updated `plan.md`.

## 2. Next Steps (Future Updates by User)
- Add complete song lyrics to the lyrics placeholder sections.
- Add additional MP3 recordings / alternate versions before merging PR #6 (`https://github.com/mathew-fleisch/portfolio/pull/6`).
https://youtube.com/playlist?list=PLHfL8knEAezg&si=7YPecCzgIAoWFZ-B
