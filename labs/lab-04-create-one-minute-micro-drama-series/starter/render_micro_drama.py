from pathlib import Path
import subprocess

OUT = Path(__file__).resolve().parents[1] / "solution" / "micro-drama-pilot.mp4"
OUT.parent.mkdir(parents=True, exist_ok=True)
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=0xB85C5C:s=1080x1920:r=30:d=60",
    "-f", "lavfi", "-i", "sine=frequency=330:sample_rate=48000:duration=60",
    "-vf", "drawbox=x=80:y=180:w=920:h=560:color=white@0.12:t=fill,drawbox=x=80:y=1540:w=920:h=160:color=white@0.18:t=fill",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(OUT)
], check=True, capture_output=True)
print("Created", OUT)
