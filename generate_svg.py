import base64
from PIL import Image
import io

def get_base64_image(image_path, size=(180, 180)):
    try:
        with Image.open(image_path) as img:
            # Crop to square
            min_dim = min(img.size)
            left = (img.width - min_dim) / 2
            top = (img.height - min_dim) / 2
            img = img.crop((left, top, left + min_dim, top + min_dim))
            img = img.resize(size, Image.Resampling.LANCZOS)
            
            # Convert to base64
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
        <!-- Font styling -->
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&amp;family=Inter:wght@400;600;800&amp;display=swap');
            .terminal-bg {{ fill: #0D1117; stroke: #30363D; stroke-width: 1px; }}
            .header-bg {{ fill: #161B22; }}
            .text-title {{ font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 800; fill: #C9D1D9; }}
            .text-subtitle {{ font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 600; fill: #8B949E; }}
            .text-code {{ font-family: 'Fira Code', monospace; font-size: 14px; fill: #58A6FF; }}
            .text-prompt {{ font-family: 'Fira Code', monospace; font-size: 14px; fill: #3FB950; font-weight: 600; }}
            .text-body {{ font-family: 'Inter', sans-serif; font-size: 14px; fill: #C9D1D9; line-height: 1.5; }}
            .text-highlight {{ fill: #FF7B72; font-weight: 600; }}
            
            .badge-bg {{ fill: #238636; rx: 10px; }}
            .badge-text {{ font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 600; fill: #FFFFFF; }}
            .badge-bg-2 {{ fill: #1F6FEB; rx: 10px; }}
            
            /* Glitch effect for image */
            .profile-pic {{ clip-path: circle(50% at 50% 50%); filter: grayscale(20%) contrast(120%); }}
        </style>
        
        <clipPath id="circleView">
            <circle cx="120" cy="200" r="80" />
        </clipPath>
        
        <!-- Subtle Grid Pattern -->
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#21262D" stroke-width="0.5" />
        </pattern>
    </defs>

    <!-- Background Window -->
    <rect width="100%" height="100%" rx="12" class="terminal-bg" />
    <rect width="100%" height="100%" rx="12" fill="url(#grid)" />
    
    <!-- Terminal Header -->
    <path d="M 0 12 Q 0 0 12 0 L 838 0 Q 850 0 850 12 L 850 40 L 0 40 Z" class="header-bg" />
    <line x1="0" y1="40" x2="850" y2="40" stroke="#30363D" stroke-width="1" />
    
    <!-- Mac OS Buttons -->
    <circle cx="25" cy="20" r="6" fill="#FF5F56" />
    <circle cx="45" cy="20" r="6" fill="#FFBD2E" />
    <circle cx="65" cy="20" r="6" fill="#27C93F" />
    
    <!-- Header Text -->
    <text x="425" y="25" text-anchor="middle" class="text-subtitle" fill="#8B949E">nivedh@neural-grid: ~</text>

    <!-- Profile Image -->
    <image href="{img_b64}" x="40" y="120" width="160" height="160" class="profile-pic" />
    <text x="120" y="310" text-anchor="middle" class="text-subtitle" fill="#3FB950">● SYSTEMS ONLINE</text>
    
    <!-- Terminal Content Area -->
    <g transform="translate(240, 80)">
        
        <!-- Command 1 -->
        <text y="20"><tspan class="text-prompt">❯</tspan> <tspan class="text-code">whoami</tspan></text>
        <text y="50" class="text-title">Nivedh Sunil</text>
        <text y="75" class="text-subtitle">Backend AI Engineer &amp; OS Developer <tspan fill="#30363D">|</tspan> Bengaluru, India</text>
        
        <!-- Command 2 -->
        <text y="120"><tspan class="text-prompt">❯</tspan> <tspan class="text-code">cat philosophy.txt</tspan></text>
        <text y="145" class="text-body">I build things most people assume already exist.</text>
        <text y="165" class="text-body">Operating systems from bare metal. Transformers without ML</text>
        <text y="185" class="text-body">libraries. <tspan class="text-highlight">Builds OSs for fun. Ships AI for work.</tspan></text>
        
        <!-- Command 3 -->
        <text y="235"><tspan class="text-prompt">❯</tspan> <tspan class="text-code">ls ./current_projects</tspan></text>
        
        <!-- Project Badges -->
        <g transform="translate(0, 255)">
            <rect width="60" height="24" class="badge-bg" />
            <text x="30" y="16" text-anchor="middle" class="badge-text">N-OS</text>
            
            <rect x="70" y="0" width="80" height="24" class="badge-bg" />
            <text x="110" y="16" text-anchor="middle" class="badge-text">ZigNGPT</text>
            
            <rect x="160" y="0" width="85" height="24" class="badge-bg-2" />
            <text x="202" y="16" text-anchor="middle" class="badge-text">LabMate AI</text>
            
            <rect x="255" y="0" width="80" height="24" class="badge-bg-2" />
            <text x="295" y="16" text-anchor="middle" class="badge-text">TERRA-X</text>
        </g>

        <!-- Command 4 -->
        <text y="315"><tspan class="text-prompt">❯</tspan> <tspan class="text-code">echo $STACK</tspan></text>
        <text y="340" class="text-body" fill="#8B949E">Python • Zig • C • React Three Fiber • FastAPI • Llama/Groq</text>
    </g>
</svg>"""

    with open("dark.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_svg()
