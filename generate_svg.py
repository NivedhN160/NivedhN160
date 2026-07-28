import os
from PIL import Image

def image_to_ascii(image_path, width=45):
    # ASCII chars for dark background
    ASCII_CHARS = [" ", ".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return []
    
    aspect_ratio = image.height / image.width
    new_height = int(aspect_ratio * width * 0.55)
    image = image.resize((width, new_height))
    image = image.convert("L")
    pixels = image.getdata()
    
    ascii_str = ""
    for pixel in pixels:
        index = (pixel * (len(ASCII_CHARS) - 1)) // 255
        ascii_str += ASCII_CHARS[index]
        
    return [ascii_str[index: index + width] for index in range(0, len(ascii_str), width)]


def generate_svg():
    ascii_art = image_to_ascii("WhatsApp Image 2026-07-28 at 8.21.43 PM.jpeg", width=55)
    
    info_lines = [
        ("<tspan fill='#36BCF7'>Nivedh@Neural-grid</tspan> <tspan fill='#8B949E'>---------------------------------------------</tspan>", 0),
        ("<tspan fill='#FF7B72'>. Subject:</tspan> <tspan fill='#8B949E'>.........................</tspan> <tspan fill='#36BCF7'>Nivedh Sunil</tspan>", 0),
        ("<tspan fill='#FF7B72'>. Role:</tspan> <tspan fill='#8B949E'>............................</tspan> <tspan fill='#36BCF7'>Backend AI Engineer &amp; OS Dev</tspan>", 0),
        ("<tspan fill='#FF7B72'>. Origin:</tspan> <tspan fill='#8B949E'>..........................</tspan> <tspan fill='#36BCF7'>Bengaluru, Karnataka, India</tspan>", 0),
        ("<tspan fill='#FF7B72'>. Status:</tspan> <tspan fill='#8B949E'>..........................</tspan> <tspan fill='#36BCF7'>Building OSs for fun. Shipping AI.</tspan>", 0),
        ("<tspan fill='#FF7B72'>. ToolChain:</tspan> <tspan fill='#8B949E'>.......................</tspan> <tspan fill='#36BCF7'>VS Code, Git, Python, C, Zig</tspan>", 0),
        ("", 0),
        ("<tspan fill='#3FB950'>Neural.Core:</tspan> <tspan fill='#8B949E'>.....</tspan> <tspan fill='#36BCF7'>Python, JavaScript, C, Zig, TypeScript</tspan>", 0),
        ("<tspan fill='#3FB950'>Neural.AI:</tspan> <tspan fill='#8B949E'>.......</tspan> <tspan fill='#36BCF7'>Transformers, Groq, Llama, LangChain</tspan>", 0),
        ("<tspan fill='#3FB950'>Neural.Projects:</tspan> <tspan fill='#8B949E'>.</tspan> <tspan fill='#36BCF7'>N-OS, ZigNGPT, LabMate, TERRA-X</tspan>", 0),
        ("<tspan fill='#3FB950'>Neural.Backend:</tspan> <tspan fill='#8B949E'>..</tspan> <tspan fill='#36BCF7'>FastAPI, Node.js, SQL, Vector DBs</tspan>", 0),
        ("<tspan fill='#3FB950'>Neural.Stack:</tspan> <tspan fill='#8B949E'>....</tspan> <tspan fill='#36BCF7'>Agentic AI, LLMs, React Three Fiber</tspan>", 0),
        ("", 0),
        ("<tspan fill='#FF7B72'>- Contact --------------------------------------------------------</tspan>", 0),
        ("<tspan fill='#3FB950'>Grid.Portfolio:</tspan> <tspan fill='#8B949E'>....................</tspan> <tspan fill='#36BCF7'>nivedhn160.github.io</tspan>", 0),
        ("<tspan fill='#3FB950'>Grid.LinkedIn:</tspan> <tspan fill='#8B949E'>.....................</tspan> <tspan fill='#36BCF7'>linkedin.com/in/nivedh-sunil</tspan>", 0),
        ("<tspan fill='#3FB950'>Grid.GitHub:</tspan> <tspan fill='#8B949E'>.......................</tspan> <tspan fill='#36BCF7'>github.com/NivedhN160</tspan>", 0),
        ("", 0),
        ("<tspan fill='#FF7B72'>- GitHub Stats ---------------------------------------------------</tspan>", 0),
        ("<tspan fill='#3FB950'>Repos:</tspan> <tspan fill='#8B949E'>....</tspan> <tspan fill='#36BCF7'>25+{Contributed: 40+}</tspan> <tspan fill='#8B949E'>|</tspan> <tspan fill='#3FB950'>Stars:</tspan> <tspan fill='#8B949E'>.................</tspan> <tspan fill='#36BCF7'>130+</tspan>", 0),
        ("<tspan fill='#3FB950'>Commits:</tspan> <tspan fill='#8B949E'>..</tspan> <tspan fill='#36BCF7'>2000+</tspan>                 <tspan fill='#8B949E'>|</tspan> <tspan fill='#3FB950'>Followers:</tspan> <tspan fill='#8B949E'>.............</tspan> <tspan fill='#36BCF7'>50+</tspan>", 0),
        ("<tspan fill='#3FB950'>Lines of Code on GitHub:</tspan> <tspan fill='#8B949E'>.</tspan> <tspan fill='#36BCF7'>350,000+ (</tspan><tspan fill='#3FB950'>250,000++</tspan><tspan fill='#36BCF7'>, </tspan><tspan fill='#FF7B72'>100,000--</tspan><tspan fill='#36BCF7'>)</tspan>", 0),
    ]

    total_lines = max(len(ascii_art), len(info_lines))
    
    svg_header = """<svg xmlns="http://www.w3.org/2000/svg" width="950" height="500">
    <rect width="100%" height="100%" rx="10" ry="10" fill="#0D1117" />
    <text font-family="'Courier New', Courier, monospace" font-size="13" xml:space="preserve" font-weight="bold">"""
    
    svg_footer = """    </text>
</svg>"""

    svg_content = []
    
    max_ascii_len = max(len(l) for l in ascii_art) if ascii_art else 55
    y_start = 30
    line_height = 16

    for i in range(total_lines):
        y = y_start + (i * line_height)
        
        # Left side: ASCII art
        left = ascii_art[i] if i < len(ascii_art) else " " * max_ascii_len
        # Escape special XML chars in ASCII art
        left = left.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        
        # Right side: Information
        right_str = info_lines[i][0] if i < len(info_lines) else ""
        
        # We use absolute x positions for perfect alignment
        left_tspan = f'<tspan x="20" y="{y}" fill="#36BCF7">{left}</tspan>'
        right_tspan = f'<tspan x="450" y="{y}">{right_str}</tspan>' if right_str else ""
        
        svg_content.append(left_tspan + right_tspan)

    with open("dark.svg", "w", encoding="utf-8") as f:
        f.write(svg_header + "\\n" + "\\n".join(svg_content) + "\\n" + svg_footer)

if __name__ == "__main__":
    generate_svg()
