#!/usr/bin/env python3
import os
import av
import numpy as np
from bs4 import BeautifulSoup

def estimate_bpm(file_path, target_fps=100):
    """Estimate average BPM of an audio file using PyAV and NumPy autocorrelation."""
    try:
        if not os.path.exists(file_path):
            return None
        container = av.open(file_path)
        stream = container.streams.audio[0]
        sr = stream.sample_rate
        
        samples = []
        for frame in container.decode(stream):
            arr = frame.to_ndarray()
            mono = arr.mean(axis=0)
            samples.append(mono)
        if not samples:
            return None
        audio = np.concatenate(samples)
        
        hop_size = int(sr / target_fps)
        num_frames = len(audio) // hop_size
        if num_frames == 0:
            return None
        
        trimmed = audio[:num_frames * hop_size]
        reshaped = trimmed.reshape(num_frames, hop_size)
        envelope = np.sqrt(np.mean(reshaped**2, axis=1))
        
        envelope = np.diff(envelope, prepend=envelope[0])
        envelope = np.clip(envelope, 0, None)
        
        min_lag = int(60 * target_fps / 220)
        max_lag = int(60 * target_fps / 60)
        
        corr = np.correlate(envelope - np.mean(envelope), envelope - np.mean(envelope), mode="full")
        corr = corr[len(corr)//2:]
        
        search_range = corr[min_lag:max_lag]
        if len(search_range) == 0:
            return None
            
        best_lag = np.argmax(search_range) + min_lag
        bpm = (60.0 * target_fps) / best_lag
        
        while bpm < 90:
            bpm *= 2
        return round(bpm)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def main():
    html_path = "reunion.html"
    if not os.path.exists(html_path):
        print(f"Error: {html_path} not found.")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    print(f"{'Song Title':<30} | {'First Audio File':<60} | {'Estimated BPM':<15}")
    print("-" * 110)

    updated_count = 0
    for details in soup.find_all("details"):
        bpm_span = details.find(class_="song-bpm")
        title_span = details.find(class_="song-title")
        
        if bpm_span and not bpm_span.text.strip().replace("BPM:", "").strip():
            title = title_span.get_text().strip() if title_span else "Unknown"
            # Clean title text (remove numbers/icons if any)
            audio = details.find("audio")
            audio_src = audio["src"] if audio and audio.has_attr("src") else ""
            
            bpm = estimate_bpm(audio_src)
            bpm_str = str(bpm) if bpm else "Unknown"
            print(f"{title:<30} | {audio_src:<60} | {bpm_str:<15}")
            
            if bpm:
                bpm_span.string = f"BPM: {bpm}"
                updated_count += 1

    if updated_count > 0:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"\nSuccessfully updated {updated_count} song(s) in {html_path} with estimated BPMs.")

if __name__ == "__main__":
    main()
