from pathlib import Path
import json, subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "solution" / "custom-video.mp4"
OUT.parent.mkdir(parents=True, exist_ok=True)
cmd = ["ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=0x18A999:s=1080x1920:r=30:d=15", "-f", "lavfi", "-i", "sine=frequency=330:sample_rate=48000:duration=15", "-vf", "drawbox=x=80:y=180:w=920:h=560:color=white@0.12:t=fill,drawbox=x=80:y=1540:w=920:h=160:color=white@0.18:t=fill", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(OUT)]
subprocess.run(cmd, check=True, capture_output=True)
probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_name,width,height,r_frame_rate", "-of", "json", str(OUT)], check=True, capture_output=True, text=True)
(ROOT / "solution" / "ffprobe.json").write_text(json.dumps(json.loads(probe.stdout), indent=2), encoding="utf-8")
print("Wrote", OUT)
