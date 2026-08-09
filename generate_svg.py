import base64
from PIL import Image
import io

def get_base64_image(image_path, size=(180, 180)):
    try:
        with Image.open(image_path) as img:
            min_dim = min(img.size)
            left = (img.width - min_dim) / 2
            top = (img.height - min_dim) / 2
            img = img.crop((left, top, left + min_dim, top + min_dim))
            # Use LANCZOS for a cleaner, high-quality resize
            img = img.resize(size, Image.Resampling.LANCZOS)
            
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return f"data:image/png;base64,{img_str}"
    except Exception as e:
        print(f"Error loading image: {e}")
        return ""

def generate_svg():
    img_b64 = get_base64_image("WhatsApp Image 2026-07-28 at 8.21.43 PM.jpeg")
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="490">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=VT323&amp;display=swap');
            .bg {{ fill: #050505; stroke: #00FF41; stroke-width: 2px; }}
            text {{ font-family: ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace; font-size: 15px; fill: #00FF41; }}
            .dim {{ fill: #008F11; }}
            .highlight {{ fill: #00FF41; font-weight: bold; }}
            .profile-pic {{ filter: grayscale(100%) contrast(130%) brightness(80%); }}
        </style>
        
        <!-- Subtle CRT scanline overlay -->
        <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="4" y2="0" stroke="#000000" stroke-width="2" stroke-opacity="0.6"/>
        </pattern>
    </defs>

    <!-- Outer Terminal Border -->
    <rect x="1" y="1" width="898" height="488" class="bg" />
    
    <!-- Profile Section -->
    <g transform="translate(40, 40)">
        <image href="{img_b64}" x="0" y="0" width="180" height="180" class="profile-pic" />
        <!-- Apply scanlines over the image only -->
        <rect x="0" y="0" width="180" height="180" fill="url(#scanlines)" />
        
        <text x="0" y="215" class="dim">CONNECTION: <tspan class="highlight">SECURE</tspan></text>
        <text x="0" y="235">root@neural-grid</text>
        <text x="0" y="255" class="dim">UPTIME: <tspan class="highlight">99.9%</tspan></text>
        
        <text x="0" y="295" class="dim">repos: 56 | stars: 35 | followers: 13</text>
    </g>
    
    <!-- Console Output Section - tightly packed for real terminal look -->
    <g transform="translate(260, 45)">
        <text y="0">root@neural-grid:~# whoami</text>
        <text y="20" class="dim">Nivedh Sunil</text>
        <text y="40" class="dim">Backend AI Engineer &amp; OS Dev</text>
        
        <text y="80">root@neural-grid:~# cat philosophy.txt</text>
        <text y="100" class="dim">I build things people assume already exist.</text>
        <text y="120" class="dim">OS from bare metal. Transformers without ML frameworks.</text>
        <text y="140" class="highlight">OS for fun. AI for work.</text>
        
        <text y="180">root@neural-grid:~# ls -la ./projects</text>
        <text y="200" class="dim">drwxr-xr-x 2 root root 4096 <tspan class="highlight">N-OS/</tspan>          # bare-metal OS</text>
        <text y="220" class="dim">drwxr-xr-x 2 root root 4096 <tspan class="highlight">ZigNGPTv2.0/</tspan>   # transformer from scratch in Zig</text>
        <text y="240" class="dim">drwxr-xr-x 2 root root 4096 <tspan class="highlight">Nexus/</tspan>         # personal AI ops platform</text>
        <text y="260" class="dim">drwxr-xr-x 2 root root 4096 <tspan class="highlight">N.E.O.S/</tspan>       # agent shell</text>
        
        <text y="300">root@neural-grid:~# systemctl status nexus</text>
        <text y="320" class="dim">● nexus.service — active (docker compose) | free-first | local LLM default</text>
        
        <text y="360">root@neural-grid:~# echo $STACK</text>
        <text y="380" class="dim">[Python] [Zig] [C] [FastAPI]</text>
    </g>
</svg>"""

    with open("dark.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_svg()
