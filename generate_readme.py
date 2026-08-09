import sys
from PIL import Image

def image_to_ascii(image_path, width=45):
    # ASCII characters used to build the output text, ordered from least dense to most dense
    # This is better for dark terminal backgrounds where more ink = brighter image
    ASCII_CHARS = [" ", ".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]
    
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error: {e}")
        return []

    # Resize image
    aspect_ratio = image.height / image.width
    # Adjust for character aspect ratio
    new_height = int(aspect_ratio * width * 0.5)
    image = image.resize((width, new_height))
    
    # Convert to grayscale
    image = image.convert("L")
    
    # Convert pixels to ascii
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        index = (pixel * (len(ASCII_CHARS) - 1)) // 255
        ascii_str += ASCII_CHARS[index]
    
    # Format into lines
    ascii_lines = [ascii_str[index: index + width] for index in range(0, len(ascii_str), width)]
    return ascii_lines

def create_ansi_readme():
    ESC = "\x1b"
    CYAN = f"{ESC}[36m"
    GREEN = f"{ESC}[32m"
    RED = f"{ESC}[31m"
    RESET = f"{ESC}[0m"
    BOLD = f"{ESC}[1m"
    WHITE = f"{ESC}[37m"
    YELLOW = f"{ESC}[33m"

    ascii_art = image_to_ascii("WhatsApp Image 2026-07-28 at 8.21.43 PM.jpeg", width=50)

    info = [
        f"{GREEN}Nivedh@Neural-grid{RESET} {WHITE}-------------------------------------------------{RESET}",
        f"{RED}. Subject:{RESET} {WHITE}.........................{RESET} {CYAN}Nivedh Sunil{RESET}",
        f"{RED}. Role:{RESET} {WHITE}............................{RESET} {CYAN}Backend AI Engineer & OS Dev{RESET}",
        f"{RED}. Origin:{RESET} {WHITE}..........................{RESET} {CYAN}Bengaluru, Karnataka, India{RESET}",
        f"{RED}. Status:{RESET} {WHITE}..........................{RESET} {CYAN}Building OSs for fun. Shipping AI.{RESET}",
        f"{RED}. ToolChain:{RESET} {WHITE}.......................{RESET} {CYAN}VS Code, Git, Python, C, Zig{RESET}",
        f"",
        f"{GREEN}Neural.Core:{RESET} {WHITE}.....{RESET} {CYAN}Python, JavaScript, C, Zig, TypeScript{RESET}",
        f"{GREEN}Neural.AI:{RESET} {WHITE}.......{RESET} {CYAN}Transformers, Groq, Llama, LangChain{RESET}",
        f"{GREEN}Neural.Projects:{RESET} {WHITE}.{RESET} {CYAN}N-OS, ZigNGPT, LabMate, TERRA-X{RESET}",
        f"{GREEN}Neural.Backend:{RESET} {WHITE}..{RESET} {CYAN}FastAPI, Node.js, SQL, Vector DBs{RESET}",
        f"{GREEN}Neural.Stack:{RESET} {WHITE}....{RESET} {CYAN}Agentic AI, LLMs, React Three Fiber{RESET}",
        f"",
        f"{RED}- Contact -------------------------------------------------------------{RESET}",
        f"{GREEN}Grid.Portfolio:{RESET} {WHITE}....................{RESET} {CYAN}nivedhn160.github.io{RESET}",
        f"{GREEN}Grid.LinkedIn:{RESET} {WHITE}.....................{RESET} {CYAN}linkedin.com/in/nivedh-sunil{RESET}",
        f"{GREEN}Grid.GitHub:{RESET} {WHITE}.......................{RESET} {CYAN}github.com/NivedhN160{RESET}",
        f"",
        f"{RED}- GitHub Stats --------------------------------------------------------{RESET}",
        f"{GREEN}Repos:{RESET} {WHITE}....{RESET} {CYAN}25+{{Contributed: 40+}}{RESET} {WHITE}|{RESET} {GREEN}Stars:{RESET} {WHITE}.................{RESET} {CYAN}130+{RESET}",
        f"{GREEN}Commits:{RESET} {WHITE}..{RESET} {CYAN}2000+{RESET}                 {WHITE}|{RESET} {GREEN}Followers:{RESET} {WHITE}.............{RESET} {CYAN}50+{RESET}",
        f"{GREEN}Lines of Code on GitHub:{RESET} {WHITE}.{RESET} {CYAN}350,000+ ({RESET}{GREEN}250,000++{RESET}{CYAN}, {RESET}{RED}100,000--{RESET}{CYAN}){RESET}",
    ]

    # Combine ASCII art and info side by side
    max_ascii_width = max(len(line) for line in ascii_art) + 2 if ascii_art else 50
    
    content = ["```ansi"]
    
    # Pad ascii or info so they match in height
    total_lines = max(len(ascii_art), len(info))
    
    for i in range(total_lines):
        if i < len(ascii_art):
            left = f"{CYAN}{ascii_art[i]}{RESET}"
            left_plain_len = len(ascii_art[i])
        else:
            left = " " * max_ascii_width
            left_plain_len = max_ascii_width
            
        padding = " " * (max_ascii_width - left_plain_len)
        
        if i < len(info):
            right = info[i]
        else:
            right = ""
            
        content.append(f"{left}{padding}{right}")
        
    content.append("```")
    
    markdown_content = '''# 🚀 Welcome to my Neural Grid

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=36BCF7&center=true&vCenter=true&width=800&lines=Initializing+Neural+Link...;Connection+Established.;NIVEDH+SUNIL+terminal+accessed;Building+OSs+for+fun+%7C+Shipping+AI+for+work" alt="Typing SVG" />
</div>

''' + "\n".join(content) + '''

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=NivedhN160&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117" height="150" alt="GitHub Stats" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=NivedhN160&theme=tokyonight&hide_border=true&background=0D1117" height="150" alt="GitHub Streak" />
</div>
'''
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)

if __name__ == "__main__":
    create_ansi_readme()
