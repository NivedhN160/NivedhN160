import base64
from PIL import Image
import io

def get_base64_image(image_path, size=(160, 160)):
    try:
        with Image.open(image_path) as img:
            min_dim = min(img.size)
            left = (img.width - min_dim) / 2
            top = (img.height - min_dim) / 2
            img = img.crop((left, top, left + min_dim, top + min_dim))
            img = img.resize(size, Image.Resampling.NEAREST)
            
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return f"data:image/png;base64,{img_str}"
    except Exception as e:
        print(f"Error loading image: {e}")
        return ""

def generate_svg():
    img_b64 = get_base64_image("WhatsApp Image 2026-07-28 at 8.21.43 PM.jpeg")
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="850" height="420">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=VT323&amp;display=swap');
            .bg {{ fill: #000000; }}
            text {{ font-family: 'VT323', 'Courier New', monospace; font-size: 20px; fill: #00FF41; }}
            .dim {{ fill: #008F11; }}
            .profile-pic {{ filter: grayscale(100%) contrast(150%) brightness(70%); }}
        </style>
        
        <!-- CRT scanline overlay -->
        <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="4" y2="0" stroke="#000000" stroke-width="2" stroke-opacity="0.5"/>
        </pattern>
    </defs>

    <rect width="100%" height="100%" class="bg" />
    
    <image href="{img_b64}" x="30" y="30" width="160" height="160" class="profile-pic" />
    <!-- Apply scanlines over the image -->
    <rect x="30" y="30" width="160" height="160" fill="url(#scanlines)" />
    
    <text x="30" y="220" class="dim">CONNECTION: OK</text>
    <text x="30" y="245">root@neural-grid</text>
    <text x="30" y="270" class="dim">UPTIME: 99.9%</text>
    
    <g transform="translate(230, 45)">
        <text y="0">root@neural-grid:~# whoami</text>
        <text y="25" class="dim">Nivedh Sunil</text>
        <text y="50" class="dim">Backend AI Engineer &amp; OS Dev</text>
        
        <text y="95">root@neural-grid:~# cat philosophy.txt</text>
        <text y="120" class="dim">I build things most people assume already exist.</text>
        <text y="145" class="dim">Operating systems from bare metal.</text>
        <text y="170" class="dim">Transformers without ML libraries.</text>
        <text y="195" class="dim">Builds OSs for fun. Ships AI for work.</text>
        
        <text y="240">root@neural-grid:~# ls -la ./projects</text>
        <text y="265" class="dim">drwxr-xr-x 2 root root 4096 N-OS</text>
        <text y="290" class="dim">drwxr-xr-x 2 root root 4096 ZigNGPT</text>
        <text y="315" class="dim">drwxr-xr-x 2 root root 4096 LabMate</text>
        <text y="340" class="dim">drwxr-xr-x 2 root root 4096 TERRA-X</text>
        
        <text y="385">root@neural-grid:~# echo $STACK</text>
        <text y="410" class="dim">[Python] [Zig] [C] [React] [FastAPI] [Llama]</text>
    </g>
</svg>"""

    with open("dark.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_svg()
