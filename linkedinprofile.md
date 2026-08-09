0 notifications total

Skip to search

Skip to main content

Keyboard shortcuts
Close jump menu
I’m looking for...
Home
My Network
Jobs
2
2 new messages notifications
Messaging
12
12 new notifications
Notifications
NIVEDH SUNIL
Me

For Business
Reactivate Premium: 50% Off
NIVEDH SUNIL
NIVEDH SUNIL
Builds operating systems for fun. Ships AI for work.
Followers
1,326
All activity

Posts

Comments

Videos

Images

Reactions

Filter by:
All
Loaded 27 Posts posts
Feed post number 1
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
1w •  

Hackathons are where you build something in 7 hours that you'll spend 7 months explaining.

Attended the Browser-Use Hackathon GTM Edition by Webcmd x GTMX Ventures today at HSR Layout.

The premise was simple. Point an AI agent at a real browser and make it do GTM work: prospecting, outreach, account research, CRM hygiene. One hard rule: the demo runs live. No slides pretending something works.

I built a "Buying-Signal Scanner", I really don't know why.

The insight is that hiring signals are buying signals. When a company posts multiple RevOps, GTM Strategy, or Sales Engineering roles, they aren't just hiring, they're instead actively feeling operational pain and evaluating new tools. Most people look at job boards to find jobs. I pointed an agent at them to find customers instead.

The architecture has three layers. webcmd adapters scrape Greenhouse via JSON and Lever via real browser automation because not every job board has a clean API and the agent shouldn't care either way. An orchestrator loop runs both across a batch of target companies. Then the extracted roles get piped to an LLM which scores each company 0-10 on their need for a GTM tool based on what's actually open.

Output is a ranked list and the terminal tells you why.

Wrote the Lever adapter from scratch because the webcmd's "record once, execute forever" seemed too good to be true and when tested, it actually held and It does work.

Still haven't won a hackathon. 
The scanner disagrees with the judges about that.

https://lnkd.in/diMZcZYu

hashtag#BrowserUse hashtag#AgenticAI hashtag#BuildInPublic hashtag#Hackathon hashtag#webcmd hashtag#GTM hashtag#Bengaluru
…more

Play
like
34
You and 33 others
5 comments

like
Like

Comment

Repost

Send
630 impressions
View analytics
Feed post number 2
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
1w •  

N-OS v1.2 is out.
I somehow made it worse in more interesting ways.
What’s new:
Virtual memory. Paging works! Page faults now get a nice Blue Screen of Death with register dumps so you can admire my mistakes in detail.
Preemptive scheduler at 100Hz. Yes, it can actually multitask now. Sometimes.
GUI got glassmorphism and proper backbuffering. Fixed the mouse cursor flickering... after only breaking it for three weeks.
Storage: Block devices, ATA driver, VFS, FAT32. I can finally pretend to have a real filesystem.
The mock browser can "download" things into the VFS. I still don’t fully understand how it works.
Still pure C. Still no real OS underneath. Just me writing code and hoping nothing catches fire.

pkg install firefox works. 
The Start Menu is still something I wrote. 
Both are brave.
Still Beta. Still broken. Now with better error messages.
ISO is there if you want to suffer with me:

https://lnkd.in/dZuHGFwC

Boot it in VirtualBox. Good luck.
hashtag#OSDev hashtag#C hashtag#BuildInPublic hashtag#LowLevel hashtag#SystemsProgramming
…more
Activate to view larger image,
View image
Activate to view larger image,
likecelebrate
32
You and 31 others
6 comments

like
Like

Comment

Repost

Send
707 impressions
View analytics
Feed post number 3
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
2w •  

Attended the "Building Enterprise Al Agents with RAG using UiPath SDK and Llamalndex" at UiPath Bengaluru this morning.

The architecture they walked through was interesting. Agents think, robots act, people approve, orchestrator governs. Clean separation. The agent reasons over policy and context, hands a decision to the Maestro workflow, which then routes it to a robot or a human depending on how confident the agent was. The human isn't in the loop by default, only when the agent isn't sure. That's the part most enterprise AI gets wrong.

The procurement agent demo made it concrete. Purchase request comes in, LlamaIndex agent parses it, does semantic search over a policy index, reasons over what it finds, outputs a structured compliance decision. No queues, no jobs, no robots spawned by the agent itself — it just returns a recommended action and the orchestrator decides what to do with it. The hard part isn't the orchestration. It's grounding the decision in the right policy passages.

Anshuman Rai walked through how to build and deploy a coded agent to their cloud. Adarsh Thomas showed the workflow side, how decisions loop, how exceptions route to humans, how the whole thing stays governed at enterprise scale.

Most of what I've built has been custom orchestration from scratch. Seeing a platform that handles the governance layer properly was useful. The instinct to build everything yourself has limits when the thing you're building needs to run inside a bank.


UiPath Community
hashtag#UiPath hashtag#LlamaIndex hashtag#AgenticAI hashtag#EnterpriseAI hashtag#BuildInPublic hashtag#Bengaluru hashtag#AgentBuilders
…more

View image

View image

View image

View image
Activate to view larger image,
likelove
78
You and 77 others
5 comments

like
Like

Comment

Repost

Send
2,342 impressions
View analytics
Feed post number 4
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
3w •  

Prompt Wars Challenge 4. Build a World Cup 2026 Operations Center. Done.

The brief was stadium operations, navigation, and crowd management. So I built a real-time command center that detects which of the 16 official World Cup 2026 stadiums you're nearest to using geolocation and the Haversine formula, then injects that context directly into the AI assistant's brain.

Ask it where the accessible entrance is. It already knows which stadium you're at. It doesn't need you to explain.

Live FIFA match scores from TheSportsDB. Live tournament news. If the primary APIs go down, fallbacks kick in automatically. Zero downtime was the goal. The World Cup doesn't pause for a 503.

The Operations Center is live though.

Try it:
https://lnkd.in/gjcapR65

Repo:
https://lnkd.in/gX_N4nkW

Google for Developers 
Google Developer Groups - India 
Hack2skill 
Google 
Google Antigravity 
Google Cloud 

hashtag#BuildWithAI hashtag#PromptWars hashtag#Hack2Skill hashtag#Google hashtag#WorldCup2026 hashtag#GenAI hashtag#BuildInPublic
…more
Activate to view larger image,
graphical user interface, application
Activate to view larger image,
likecelebrate
25
You and 24 others
4 comments

like
Like

Comment

Repost

Send
670 impressions
View analytics
Feed post number 5
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
3w •  

N-OS v1.1 is out.

v1.0 was an OS that booted and had a terminal with a minimal GUI.
v1.1 is an OS that boots and has opinions about your .exe files and has a better GUI functions.

Added a Win32 compatibility layer. When a Windows binary calls CreateWindowExA, N-OS intercepts it and handles it natively. No Windows underneath. Just C for confidence.

Same for Linux. POSIX syscalls mocked, ELF binaries load, nothing immediately catches fire.

TCP/IP stack talks to the internet now. RTL8139 driver, full 3-way handshake, fetches HTTP payloads. An OS I wrote from scratch is on the network. I'm choosing not to think about that too hard.

pkg install firefox. It shows up in the Start Menu. The Start Menu is also something I wrote.

Still Beta. Still breaks. Now breaks in more interesting ways.

ISO's up, boot it in VirtualBox and see for yourself:
github.com/NivedhN160/N-OS

hashtag#OSDev hashtag#C hashtag#BuildInPublic hashtag#LowLevel hashtag#SystemsProgramming
…more
Activate to view larger image,
View image
Activate to view larger image,
likecelebrate
37
You and 36 others
6 comments

like
Like

Comment

Repost

Send
1,284 impressions
View analytics
Feed post number 6
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
4w •  

Just thought of Creating an OS by myself and didn't know the Consequences.
Built N-OS. Bootloader to kernel, all of it, from scratch in C.
Didn't want to clone one OS, so I took the best parts from all of them. Linux, Apple MacOS, Microsoft Microsoft Windows, Plan 9, BeOS, Haiku, SerenityOS, TempleOS, MenuetOS. Studied what each one got right and built my own version instead of picking a side.
It scans the PCI bus on boot and detects your GPU. Found one, it switches to an actual gradient instead of a flat screen.
It runs other people's binaries. A PE loader for Windows .exe files, an ELF loader for Linux, both written by hand, no host OS underneath doing the work for me.
Has a TCP/IP stack too. Ethernet framing, IPv4, full TCP handshake, on a network driver.
Has an App Store. pkg install firefox and it shows up in the Start Menu.
Still Beta. Still breaks. Not done.
ISO's up, boot it in VirtualBox and see for yourself.

Try it. Break it. Tell me how:
github.com/NivedhN160/N-OS

hashtag#OSDev hashtag#SystemsProgramming hashtag#C hashtag#BuildInPublic hashtag#LowLevel hashtag#OperatingSystems hashtag#Linux hashtag#Apple hashtag#macOS hashtag#Windows hashtag#Plan9 hashtag#BeOS hashtag#Haiku hashtag#SerenityOS hashtag#TempleOS hashtag#MenuetOS hashtag#Microsoft
…more

View image

View image

View image

View image
Activate to view larger image,
likecelebratelove
41
You and 40 others
8 comments
1 repost

like
Like

Comment

Repost

Send
1,258 impressions
View analytics
Feed post number 7
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
1mo • Edited •  

My obsession with two things, love towards the Windows XP design and my own ZigNGPT has not let me stop thinking about it yet

Most people would call that a phase. I called it a roadmap.

Portfolio's now a fully clickable Microsoft Microsoft Windows XP desktop instead of a scroll-down page nobody reads past the first screen. Draggable windows, a Start menu, a Projects folder you open like it's 2003. Just because a normal portfolio is forgettable and this isn't.
Portfolio: https://lnkd.in/gKkB29BC

ZigNGPT v1 was a trigram model. That means it doesn't understand anything. It used to just count which word usually follows which word, in a language with no ML libraries and no mercy. It still has the only feature that matters: a Sarcasm mode that insults you for typing "hi."

V2 is the part I actually care about. Same personality, same Zig, but the brain underneath is no longer a frequency table. It's a transformer built from raw matrix math, with backpropagation I wrote by hand. No PyTorch. No autograd library doing the hard part for me. If the gradients are wrong, there's no stack trace pointing me to the bug, just output that's subtly garbage and a lot of staring at numbers.

If you would like to get tormented with the new brain check these out:

V1 (the trigram era): https://lnkd.in/gm4hC_4F
V2 (in progress, rebuilding the brain): https://lnkd.in/g3sZJVzG

Most people learn what a transformer is by importing one. I'm learning by failing to build one correctly, repeatedly, until I don't.

hashtag#Zig hashtag#MachineLearning hashtag#BuildInPublic hashtag#DeepLearning hashtag#SoftwareEngineering
…more
Activate to view larger image,
View image
Activate to view larger image,
likecelebratesupport
23
You and 22 others

like
Like

Comment

Repost

Send
997 impressions
View analytics
Feed post number 8
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
1mo •  

Excited to share that I've landed an internship as a Backend AI Engineering Intern at FlyRank AI!

Grateful for the opportunity, and looking forward not to crash the systems.

Alen Malkoč 

hashtag#Internship hashtag#BackendEngineering hashtag#AIEngineer hashtag#FlyRank
…more
Activate to view larger image,
text
Activate to view larger image,
likecelebratelove
137
You and 136 others
21 comments

like
Like

Comment

Repost

Send
8,463 impressions
View analytics
Feed post number 9
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
1mo • Edited •  

Built Terr-AR-ium: a 3D Voxel Sandbox that gamifies your carbon footprint.
Got tired of carbon tracker apps that are just boring charts nobody opens twice. So instead, we made your eco habits directly grow (or wreck) a live, Minecraft-style island.
Swipe right on a positive action like "Cold Wash" or "Bike to Work" and the island physically expands, sprouts bloom into full voxel trees and flowers. Swipe on a negative one like "Steak Dinner" and the decay creeps in, leaves turn yellow and brown, trees shrink. Your bad habits literally show up on the landscape.
Built the 3D scene with Three.js and React Three Fiber (React Three Drei for OrbitControls, Environment, Sparkles), fully pannable and zoomable in 360°. For content, didn't want users running out of actions, so it taps Groq's llama-3.1-8b-instant to procedurally generate endless unique eco-actions with calculated CO₂ impact on demand.
It's PWA-ready too, so you can install it straight to your home screen.
Check out the repo here: https://lnkd.in/gEcC8N8s
Live Link: https://lnkd.in/gSkT6ncV

Google 
Hack2skill 
Google for Developers 
Google Developer Groups (GDG) 
Google Student Ambassadors (India) 
hashtag#React hashtag#ThreeJS hashtag#ReactThreeFiber hashtag#Groq hashtag#Llama3 hashtag#ClimateTech hashtag#WebDevelopment hashtag#PromptWars hashtag#Hack2Skill hashtag#CarbonFootprint hashtag#Hackathon hashtag#Google hashtag#Developer hashtag#PromptEngineering
…more
like
12
You and 11 others

like
Like

Comment

Repost

Send
806 impressions
View analytics
Feed post number 10
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
1mo • Edited •  

Volunteered at the 25th Florence Nightingale Award 2026, Vidhana Soudha, Bengaluru.
Handed out event kits, spoke with Christo Joseph., FRSA , AKC which was really insightful.
Nurses got recognized for the work hospitals actually run on.
One line stuck: doctors prescribe, nurses heal.
P.S also learned how to look busy while holding a stack of kits.
Garden City University 
hashtag#FlorenceNightingaleAward2026 hashtag#VolunteerExperience hashtag#StudentVolunteer
…more

View image

View image

View image

View image
+2
Activate to view larger image,
likecelebrate
53
You and 52 others
3 comments
1 repost

like
Like

Comment

Repost

Send
1,441 impressions
View analytics
Feed post number 11
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
1mo • Edited •  

Had an Insightful session with DP Sudhagar and congratulations to the whole team DILIP KUMAR. B Alfred Antony Nithish kumar Shanthgeri Ashish Mishra Harshil Vishal Tank Abhiram Bhagath K Prathyaksh Ramesh Mohith and Sathish with the discussion we had regarding the problem statements, totally a real race against a time and the output was fabulous.

hashtag#Entrepreneurship hashtag#ProblemSolving hashtag#DesignThinking hashtag#Engineering
…more
View Ashish Mishra’s  graphic link
Ashish Mishra
   • 1st
Third-Year B.Tech CSE Student | Web Developer in Progress | Exploring Modern Web Technologies and AI-Assisted Development
1mo •  
Today, I attended an insightful Entrepreneurship Skills session by DP Sudhagar Dean, School of CMS 

The session highlighted the importance of thinking beyond conventional career paths and developing a problem-solving mindset. A key takeaway for me was that opportunities exist in every problem, and impactful solutions do not necessarily have to be technology-driven—they simply need to create value and make a difference.

One of the most engaging parts of the session was a team brainstorming activity where we were given a real-world problem statement and asked to develop a solution within a short time. Our team worked on addressing pesticide and insecticide contamination in food and proposed a filtration-based irrigation solution, demonstrating how innovation can contribute to safer and healthier agricultural practices.

The session reinforced that true engineering is not just about building technology, but about solving meaningful problems that create a positive impact on society.

Grateful for the valuable insights and learning experience.

hashtag#Entrepreneurship hashtag#Innovation hashtag#ProblemSolving hashtag#Engineering hashtag#Agriculture hashtag#StartupMindset hashtag#Learning hashtag#CareerGrowth
…more

View image

View image

View image
Activate to view larger image,
likecelebrate
24
You and 23 others
2 comments
2 reposts

like
Like

Comment

Repost

Send
720 impressions
View analytics
Feed post number 12
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
2mo •  

Hi everyone! I’m seeking a new role and would appreciate your support. If you hear of any opportunities or just want to catch up, please send me a message or comment below. I’d love to reconnect. hashtag#OpenToWork

About me & what I’m looking for:
💼 I’m looking for Artificial Intelligence Intern, Software Engineer, Web Developer, Back End Developer, and Research Intern roles.
🌎 I’m open to roles in 560049, 560036, Bengaluru, Greater Bengaluru Area, and Bangalore Urban.
…more

NIVEDH is open to work
Looking for On-site or Hybrid or Remote roles in Bengaluru, Greater Bengaluru Area and Bangalore Urban
View job preferences
like
17
You and 16 others

like
Like

Comment

Repost

Send
634 impressions
View analytics
Feed post number 13
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
2mo •  

Attended The Hacknight Bangalore held by Elastic and Amazon Web Services (AWS) AWS User Group Bengaluru along with OpenClaw 

Had an exciting Introduction session from Someshwaran M and Insight from Ayyanar Jeyakrishnan (AJ) 

The One takeaway from VibeCoding in this Hackathon was:
“A system survives not because it is flawless, but because people are forced to depend on it.”

hashtag#AWS hashtag#Elastic hashtag#HackNightBlr hashtag#Hackathon hashtag#Amazon hashtag#OpenClaw hashtag#AgenticAI hashtag#AgenticAIDeveloper
…more
Activate to view larger image,
View image
Activate to view larger image,
likecelebrate
40
You and 39 others

like
Like

Comment

Repost

Send
1,013 impressions
View analytics
Feed post number 14
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
2mo • Edited •  

I was originally just trying to learn Next.js and integrate open-source AI models. But somewhere between wrestling with TypeScript errors and battling Vercel settings, I realized something: Medical lab reports are deliberately designed to induce panic.

You get a PDF back from the clinic, see a metric called "Mean Corpuscular Volume" highlighted in red, and suddenly you're writing your will. 

So instead of building another generic to-do list app, I built LabMate. 

LabMate is a free, AI-powered web app that takes those terrifying medical PDFs and translates them into plain English. It extracts your lab values, tells you what they actually mean, and provides actionable, natural lifestyle and dietary suggestions if something is abnormal, without immediately convincing you that you have a rare 18th-century disease like WebMD does.

It’s completely live! You can test it out here (you can even "Add to Home Screen" to install it as an app on your phone): 
🔗 https://lnkd.in/gfXDDzXX

Disclaimer: It's an AI tool for educational purposes, not a doctor. But it will at least tell you if you just need to eat more spinach

hashtag#Nextjs hashtag#ArtificialIntelligence hashtag#WebDevelopment hashtag#HealthTech hashtag#BuildInPublic hashtag#SoftwareEngineering hashtag#Llama3
…more
Activate to view larger image,
View image
Activate to view larger image,
likecelebrate
29
You and 28 others
5 comments

like
Like

Comment

Repost

Send
1,103 impressions
View analytics
Feed post number 15
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
3mo • Edited •  

Attended the AWS Summit Technical Edition and had an insightful chance to meet many people and companies that work with Amazon Web Services (AWS) , Multiple Applications like AWS Lambda, AWS storage S3 and many more. The System architecture and the DynamoDB from Amazon and How they were used in processing content and the Use of Amazon Bedrock to Embed AI in their system and Finally hosting it through Amplify. It was a one time learning experience. Amazon Amazon Careers Amazon Associates ClickHouse Concierto Kiro 
hashtag#AWS hashtag#AmazonWebService hashtag#AWSLambda hashtag#AWSBedrock hashtag#AWSSummitBangalore
…more

View image

View image

View image

View image
+4
Activate to view larger image,
likecelebrate
40
You and 39 others
1 comment

like
Like

Comment

Repost

Send
1,305 impressions
View analytics
Feed post number 16
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
3mo • Edited •  

Attended a Meetup/Workshop on Agentic AI from ClickHouse by the Co-Founder/CTO Alexey Milovidov and had a chance to speak with many developers and Engineers who gave insights on what to do for the future and how the markets work.
…more

View image

View image

View image

View image
Activate to view larger image,
like
33
You and 32 others

like
Like

Comment

Repost

Send
660 impressions
View analytics
Feed post number 17
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
3mo •  

Attended Inauguration of OSCode Student Chapter and An informative session on Placements, internships and how to focus on a particular domain from industry experts
Mithun S 
Abhishek Kumar
…more

View image

View image
Activate to view larger image,
like
28
You and 27 others

like
Like

Comment

Repost

Send
618 impressions
View analytics
Feed post number 18
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
3mo • Edited •  

Participated in AWS "Build For India" Hackathon and we decided, why not create an ai that bridges Startups and Content Creators and help each other find perfect collaborations and named it "MAT-CHA.AI".

It's up live, but has a tiny Database, which you surely can checkout through this link:
https://lnkd.in/guig7jNA

Collaboration:
Ashish Mishra 
Abhiram Bhagath K 
N Sree Varshini
…more

View image

View image

View image

View image
Activate to view larger image,
likecelebrate
23
You and 22 others
1 repost

like
Like

Comment

Repost

Send
570 impressions
View analytics
Feed post number 19
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
3mo •  

Attended an Ideathon Competition in MS Ramaiah University of Applied Sciences. 

Made a prototype on "Ransomware Readiness Assessment Tool", instead of making it just like a questionnaire, built it as a SaaS which could level up based on each attack and prevent the attacks and ensure your system can defend any further attacks in the future.
…more

View image

View image

View image

View image
+1
Activate to view larger image,
likecelebrate
37
You and 36 others
1 comment

like
Like

Comment

Repost

Send
804 impressions
View analytics
Feed post number 20
NIVEDH’s profile photo
NIVEDH SUNIL reposted this

View Ashish Mishra’s  graphic link
Ashish Mishra
   • 1st
Third-Year B.Tech CSE Student | Web Developer in Progress | Exploring Modern Web Technologies and AI-Assisted Development
4mo •  
🚀 Excited to share that I recently participated in the *Startup Journey – Idea Innovation & Entrepreneurship* event held at Ramaiah University of Applied Sciences.

It was a 2-day ideathon experience that truly pushed our creativity and teamwork.

👥 I had the opportunity to collaborate with an amazing team:
👉 N Sree Varshini 
👉 NIVEDH SUNIL 
👉 Abhiram Bhagath 

📌 **Day 1:**
We attended a workshop on *Design Thinking*, where we learned how to understand real-world problems and approach them with structured solutions.
We were then given our problem statement — **Ransomware Readiness Assessment Tool** — and had limited time to build and prepare our idea.

📌 **Day 2:**
We explored *Business Model Canvas*, gaining insights into how ideas can be transformed into viable business models.
We also received valuable guidance from industry experts on market trends and the startup journey.

This experience was a great learning curve, giving us valuable insights into problem-solving, teamwork, and the startup ecosystem. 💡

Grateful for this opportunity and proud of what we built together!

🙌 Thanks to the organizers, mentors, and everyone involved for such an inspiring event.

hashtag#StartupJourney hashtag#Ideathon hashtag#Innovation hashtag#Entrepreneurship hashtag#DesignThinking hashtag#Teamwork hashtag#LearningExperience hashtag#CyberSecurity
…more

View image

View image

View image

View image
+2
Activate to view larger image,
likecelebrate
35
You and 34 others
2 reposts

like
Like

Comment

Repost

Send
Feed post number 21
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
5mo • Edited •  

Prompted Antigravity to create a 3D Earth frontend using React Three Fiber.
Wanted to integrate it with an AI backend, and then thought of a Simulator.
So I built TERRA-X: A real-time scenario lab where the frontend visualizes the globe, and our backend runs predictions using Groq’s Llama 3.3 to simulate future outcomes for any city.
It combines a high-performance Python/FastAPI engine with a reactive 3D interface.
P.S The Backend Server goes off frequently
You can Simulate it by yourself by clicking the link below:
https://lnkd.in/gKP-xWXA
…more
TERRA-X Scenario Lab
nivedhn160.github.io
likecelebrate
20
You and 19 others
2 comments

like
Like

Comment

Repost

Send
669 impressions
View analytics
Feed post number 22
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
5mo • Edited •  

Built a personal portfolio website using React, styled after Windows XP for questionable reasons.
Hosted it on GitHub Pages because it was the only free hosting service I knew.
Check It Out from This Link: https://lnkd.in/g_BpXgpx
hashtag#windowsXP
…more
my-portfolio
nivedhn160.github.io
likecelebrate
16
You and 15 others

like
Like

Comment

Repost

Send
502 impressions
View analytics
Feed post number 23
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
7mo •  

Created an Emotion-Aware Debugging Assistant that estimates developer frustration in real time using facial landmarks, blink rate, head posture, proximity to screen and emotion recognition.
 Built with OpenCV, MediaPipe Face Mesh and DeepFace. The system computes a normalized frustration score, logs behavioral metrics per source file, and displays visual cues when frustration crosses a threshold.
You Can Access the code from my Repository:
https://lnkd.in/gZWbWha8
…more

View image

View image

View image

View image
+3
Activate to view larger image,
likesupport
19
You and 18 others
2 comments

like
Like

Comment

Repost

Send
900 impressions
View analytics
Feed post number 24
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
7mo •  

Joined an AI Generated Short-Film Competition by Natural Disaster Management Authority.
First, we wrote down a story, made a screenplay out of it and thought "We just need to copy and paste it as a prompt and we are done!"
But no, We had to rewrite the screenplay for each scene, edit it for continuity.
Continuity was our major concern as each scene was different from others in terms of continuity.
Hence We Present To You
"THROWN AWAY"
Written & Directed By: N Sree Varshini & NIVEDH SUNIL
Edited By: NIVEDH SUNIL
Special Thanks To Ashish Mishra
Hope You Like It
…more

Play
Remaining time 
2:59
1x

Playback speed

Turn closed captions on

Unmute

Turn fullscreen on
Auto captions have been added to your video


Edit captions

likelove
22
You and 21 others
2 comments
2 reposts

like
Like

Comment

Repost

Send
804 impressions
View analytics
Feed post number 25
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
10mo • Edited •  

Successfully completed SIH internal Hackathon
Feels good attending a Hackathon for the first time with
Ashish Mishra Sitesh Moharana N Sree Varshini Tejeshwini M

View image

View image
Activate to view larger image,
likecelebrate
25
You and 24 others
2 comments
2 reposts

like
Like

Comment

Repost

Send
1,193 impressions
View analytics
Feed post number 26
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
10mo • Edited •  

Made a Smart Mobility Companion that gives bus routes and recommendations based on Bangalore running on a Token system between Llama and GPT-neo. Also Provides average fares for travelling through bus in bangalore. Few Collaborators Ashish Mishra, Sitesh Moharana and N Sree Varshini
You can try it in the below Hugging Face Link, PS don't forget to read the Readme file 😉 
https://lnkd.in/etHR-bbg
…more

NivedhN160/smart-mobility-companion · Hugging Face
huggingface.co
likecelebrate
14
2 reposts

like
Like

Comment

Repost

Send
677 impressions
View analytics
Feed post number 27
View NIVEDH SUNIL’s open to work graphic link
NIVEDH SUNIL
   • You
Builds operating systems for fun. Ships AI for work.
10mo • Edited •  

Created a Trigram-Based Markov Language model, Trained using Bhaghavat Geetha and Sherlock Holmes. It is primarily written in Zig Laguage. Has multiple modes but the highlight must be the "Sarcasm" mode. Temporarily named it ZigNGPT
…more

View image

View image

View image

View image
Activate to view larger image,
like
16

like
Like

Comment

Repost

Send
586 impressions
View analytics

People you may know
From your industry

Abdullah Fatota 🇵🇸
Abdullah Fatota 🇵🇸
Software Engineer | M.Sc. Computer Science | Bošnjak

Connect
Naveen Kumar Bangla
Naveen Kumar Bangla
Customer Support Executive at [24]7.ai

Connect
Sudheer K.
Sudheer K.
Sr.Manager, Technology Services at UiPath | Sr. Solution Architect | CSM®

Connect
Sneha Lohar
Sneha Lohar
Digital Interaction Executive at [24]7.ai

Connect
Risal Fareed Kalwar
Risal Fareed Kalwar
Front End AI Engineer & AI Machine Learning 

Connect

Show more

About
Accessibility
Help Center

Privacy & Terms
Ad Choices
Advertising

Business Services
Get the LinkedIn app
More
 LinkedIn Corporation © 2026
NIVEDH SUNIL
MessagingYou are on the messaging overlay. Press enter to open the list of conversations.
2

Compose message
You are on the messaging overlay. Press enter to open the list of conversations.
LinkedIn
LinkedIn
Close your conversation with {0} and NIVEDH SUNIL
LinkedIn Offer

Jul 28
LinkedIn Profile
LinkedIn
Today
sent the following messages at 8:00 PM
LinkedIn
LinkedIn  8:00 PM
Hi there, NIVEDH!



Get 50% off your first two months of LinkedIn Premium when you reactivate your subscription today.



50% off? Sure!

Not interested

50% off? Sure!
0 notifications

I'm looking for…



Home
My Network
Jobs
1
Messaging
12
Notifications


Me

For Business
Reactivate Premium: 50% Off


NIVEDH SUNIL

Builds operating systems for fun. Ships AI for work.


Resources

Enhance profile
Add section

Open to
Cover photo


NIVEDH SUNIL
He/Him

Builds operating systems for fun. Ships AI for work.

Bengaluru, Karnataka, India

·

Contact info


FlyRank AI


Garden City University

500+ connections


Open to
Add section

Enhance profile

Resources
Open to work

Bengaluru +4 more | On-site · Hybrid · Remote

Show details

Analytics
Private to you

427 profile views

Discover who’s viewed your profile.

533 post impressions

Check out who’s engaging with your posts.

Past 7 days

81 search appearances

See how often you appear in search results.

Show all
About
I build things most people assume already exist.
Operating systems from bare metal. Transformers without ML libraries. A medical AI that translates lab reports before you write your will. A 3D earth simulator that predicts future scenarios for any city on the planet. A debugging assistant that reads your face to know you're frustrated before you do. A carbon tracker that grows a Minecraft island when you make good decisions and kills it when you don't. A smart mobility companion that reroutes Bangalore's bus problem using AI. A ransomware tool that gets smarter after every attack it survives.
Then there are the hackathons. AWS Build For India. Google Hack2Skill. Hacknight Bangalore. MS Ramaiah Ideathon. SIH. Not attended — competed, built, and shipped inside the time limit every single time. Haven't won one yet. The judges and I have an ongoing disagreement about that.
The pattern isn't a tech stack. It's a refusal to use something I don't fully understand, and an inability to stop once I start.
Not looking for a place to start. Already started. Looking for a place where that matters.

Top skills

Artificial Intelligence (AI) • Automation • Python (Programming Language) • JavaScript • Full-Stack Development

Featured


Post

Just thought of Creating an OS by myself and didn't know the Consequences.
Built N-OS. Bootloader to kernel, all of it, from scratch in C.
Didn't want to clone one OS, so I took the best parts from all of them. Linux, Apple MacOS, Microsoft Microsoft Windows, Plan 9, BeOS, Haiku, SerenityOS, TempleOS, MenuetOS. Studied what each one got right and built my own version instead of picking a side.
It scans the PCI bus on boot and detects your GPU. Found one, it switches to an actual gradient instead of a flat screen.
It runs other people's binaries. A PE loader for Windows .exe files, an ELF loader for Linux, both written by hand, no host OS underneath doing the work for me.
Has a TCP/IP stack too. Ethernet framing, IPv4, full TCP handshake, on a network driver.
Has an App Store. pkg install firefox and it shows up in the Start Menu.
Still Beta. Still breaks. Not done.
ISO's up, boot it in VirtualBox and see for yourself.

Try it. Break it. Tell me how:
github.com/NivedhN160/N-OS

#OSDev #SystemsProgramming #C #BuildInPublic #LowLevel #OperatingSystems #Linux #Apple #macOS #Windows #Plan9 #BeOS #Haiku #SerenityOS #TempleOS #MenuetOS #Microsoft


41 reactions · 8 comments41 · 8 comments

Post

Created a Trigram-Based Markov Language model, Trained using Bhaghavat Geetha and Sherlock Holmes. It is primarily written in Zig Laguage. Has multiple modes but the highlight must be the "Sarcasm" mode. Temporarily named it ZigNGPT


16 reactions16

Post

My obsession with two things, love towards the Windows XP design and my own ZigNGPT has not let me stop thinking about it yet

Most people would call that a phase. I called it a roadmap.

Portfolio's now a fully clickable Microsoft Microsoft Windows XP desktop instead of a scroll-down page nobody reads past the first screen. Draggable windows, a Start menu, a Projects folder you open like it's 2003. Just because a normal portfolio is forgettable and this isn't.
Portfolio: https://lnkd.in/gKkB29BC

ZigNGPT v1 was a trigram model. That means it doesn't understand anything. It used to just count which word usually follows which word, in a language with no ML libraries and no mercy. It still has the only feature that matters: a Sarcasm mode that insults you for typing "hi."

V2 is the part I actually care about. Same personality, same Zig, but the brain underneath is no longer a frequency table. It's a transformer built from raw matrix math, with backpropagation I wrote by hand. No PyTorch. No autograd library doing the hard part for me. If the gradients are wrong, there's no stack trace pointing me to the bug, just output that's subtly garbage and a lot of staring at numbers.

If you would like to get tormented with the new brain check these out:

V1 (the trigram era): https://lnkd.in/gm4hC_4F
V2 (in progress, rebuilding the brain): https://lnkd.in/g3sZJVzG

Most people learn what a transformer is by importing one. I'm learning by failing to build one correctly, repeatedly, until I don't.

#Zig #MachineLearning #BuildInPublic #DeepLearning #SoftwareEngineering


23 reactions23

Post

I was originally just trying to learn Next.js and integrate open-source AI models. But somewhere between wrestling with TypeScript errors and battling Vercel settings, I realized something: Medical lab reports are deliberately designed to induce panic.

You get a PDF back from the clinic, see a metric called "Mean Corpuscular Volume" highlighted in red, and suddenly you're writing your will. 

So instead of building another generic to-do list app, I built LabMate. 

LabMate is a free, AI-powered web app that takes those terrifying medical PDFs and translates them into plain English. It extracts your lab values, tells you what they actually mean, and provides actionable, natural lifestyle and dietary suggestions if something is abnormal, without immediately convincing you that you have a rare 18th-century disease like WebMD does.

It’s completely live! You can test it out here (you can even "Add to Home Screen" to install it as an app on your phone): 
🔗 https://lnkd.in/gfXDDzXX

Disclaimer: It's an AI tool for educational purposes, not a doctor. But it will at least tell you if you just need to eat more spinach

#Nextjs #ArtificialIntelligence #WebDevelopment #HealthTech #BuildInPublic #SoftwareEngineering #Llama3


29 reactions · 5 comments29 · 5 comments

Project

Emotion-Aware Code Debugging Assistant

Featured with Premium

Show all featured items
Activity
1,326 followers

Create a post

Posts

Comments

Videos

Images
View NIVEDH SUNIL’s profile, open to work
NIVEDH SUNIL

  • You

Builds operating systems for fun. Ships AI for work.

1w • 


Hackathons are where you build something in 7 hours that you'll spend 7 months explaining.

Attended the Browser-Use Hackathon GTM Edition by Webcmd x GTMX Ventures today at HSR Layout.

The premise was simple. Point an AI agent at a real browser and make it do GTM work: prospecting, outreach, account research, CRM hygiene. One hard rule: the demo runs live. No slides pretending something works.

I built a "Buying-Signal Scanner", I really don't know why.

The insight is that hiring signals are buying signals. When a company posts multiple RevOps, GTM Strategy, or Sales Engineering roles, they aren't just hiring, they're instead actively feeling operational pain and evaluating new tools. Most people look at job boards to find jobs. I pointed an agent at them to find customers instead.

The architecture has three layers. webcmd adapters scrape Greenhouse via JSON and Lever via real browser automation because not every job board has a clean API and the agent shouldn't care either way. An orchestrator loop runs both across a batch of target companies. Then the extracted roles get piped to an LLM which scores each company 0-10 on their need for a GTM tool based on what's actually open.

Output is a ranked list and the terminal tells you why.

Wrote the Lever adapter from scratch because the webcmd's "record once, execute forever" seemed too good to be true and when tested, it actually held and It does work.

Still haven't won a hackathon. 
The scanner disagrees with the judges about that.

https://lnkd.in/diMZcZYu

#BrowserUse #AgenticAI #BuildInPublic #Hackathon #webcmd #GTM #Bengaluru… more


34

5

630 impressions

View analyticsView analytics

View NIVEDH SUNIL’s profile, open to work
NIVEDH SUNIL

  • You

Builds operating systems for fun. Ships AI for work.

1w • 


N-OS v1.2 is out.
I somehow made it worse in more interesting ways.
What’s new:
Virtual memory. Paging works! Page faults now get a nice Blue Screen of Death with register dumps so you can admire my mistakes in detail.
Preemptive scheduler at 100Hz. Yes, it can actually multitask now. Sometimes.
GUI got glassmorphism and proper backbuffering. Fixed the mouse cursor flickering... after only breaking it for three weeks.
Storage: Block devices, ATA driver, VFS, FAT32. I can finally pretend to have a real filesystem.
The mock browser can "download" things into the VFS. I still don’t fully understand how it works.
Still pure C. Still no real OS underneath. Just me writing code and hoping nothing catches fire.

pkg install firefox works. 
The Start Menu is still something I wrote. 
Both are brave.
Still Beta. Still broken. Now with better error messages.
ISO is there if you want to suffer with me:

https://lnkd.in/dZuHGFwC

Boot it in VirtualBox. Good luck.
#OSDev #C #BuildInPublic #LowLevel #SystemsProgramming… more

View image

32

6

708 impressions

View analyticsView analytics

View NIVEDH SUNIL’s profile, open to work
NIVEDH SUNIL

  • You

Builds operating systems for fun. Ships AI for work.

2w • 


Attended the "Building Enterprise Al Agents with RAG using UiPath SDK and Llamalndex" at UiPath Bengaluru this morning.

The architecture they walked through was interesting. Agents think, robots act, people approve, orchestrator governs. Clean separation. The agent reasons over policy and context, hands a decision to the Maestro workflow, which then routes it to a robot or a human depending on how confident the agent was. The human isn't in the loop by default, only when the agent isn't sure. That's the part most enterprise AI gets wrong.

The procurement agent demo made it concrete. Purchase request comes in, LlamaIndex agent parses it, does semantic search over a policy index, reasons over what it finds, outputs a structured compliance decision. No queues, no jobs, no robots spawned by the agent itself — it just returns a recommended action and the orchestrator decides what to do with it. The hard part isn't the orchestration. It's grounding the decision in the right policy passages.

Anshuman Rai walked through how to build and deploy a coded agent to their cloud. Adarsh Thomas showed the workflow side, how decisions loop, how exceptions route to humans, how the whole thing stays governed at enterprise scale.

Most of what I've built has been custom orchestration from scratch. Seeing a platform that handles the governance layer properly was useful. The instinct to build everything yourself has limits when the thing you're building needs to run inside a bank.


UiPath Community
#UiPath #LlamaIndex #AgenticAI #EnterpriseAI #BuildInPublic #Bengaluru #AgentBuilders… more

View image
1/4


78

5

2,342 impressions

View analyticsView analytics

View NIVEDH SUNIL’s profile, open to work
NIVEDH SUNIL

  • You

Builds operating systems for fun. Ships AI for work.

3w • 


Prompt Wars Challenge 4. Build a World Cup 2026 Operations Center. Done.

The brief was stadium operations, navigation, and crowd management. So I built a real-time command center that detects which of the 16 official World Cup 2026 stadiums you're nearest to using geolocation and the Haversine formula, then injects that context directly into the AI assistant's brain.

Ask it where the accessible entrance is. It already knows which stadium you're at. It doesn't need you to explain.

Live FIFA match scores from TheSportsDB. Live tournament news. If the primary APIs go down, fallbacks kick in automatically. Zero downtime was the goal. The World Cup doesn't pause for a 503.

The Operations Center is live though.

Try it:
https://lnkd.in/gjcapR65

Repo:
https://lnkd.in/gX_N4nkW

Google for Developers
Google Developer Groups - India
Hack2skill
Google
Google Antigravity
Google Cloud

#BuildWithAI #PromptWars #Hack2Skill #Google #WorldCup2026 #GenAI #BuildInPublic… more

View image

25

4

671 impressions

View analyticsView analytics

View NIVEDH SUNIL’s profile, open to work
NIVEDH SUNIL

  • You

Builds operating systems for fun. Ships AI for work.

3w • 


N-OS v1.1 is out.

v1.0 was an OS that booted and had a terminal with a minimal GUI.
v1.1 is an OS that boots and has opinions about your .exe files and has a better GUI functions.

Added a Win32 compatibility layer. When a Windows binary calls CreateWindowExA, N-OS intercepts it and handles it natively. No Windows underneath. Just C for confidence.

Same for Linux. POSIX syscalls mocked, ELF binaries load, nothing immediately catches fire.

TCP/IP stack talks to the internet now. RTL8139 driver, full 3-way handshake, fetches HTTP payloads. An OS I wrote from scratch is on the network. I'm choosing not to think about that too hard.

pkg install firefox. It shows up in the Start Menu. The Start Menu is also something I wrote.

Still Beta. Still breaks. Now breaks in more interesting ways.

ISO's up, boot it in VirtualBox and see for yourself:
github.com/NivedhN160/N-OS

#OSDev #C #BuildInPublic #LowLevel #SystemsProgramming… more

View image

37

6

1,285 impressions

View analyticsView analytics

View NIVEDH SUNIL’s profile, open to work
NIVEDH SUNIL

  • You

Builds operating systems for fun. Ships AI for work.

4w • 


Just thought of Creating an OS by myself and didn't know the Consequences.
Built N-OS. Bootloader to kernel, all of it, from scratch in C.
Didn't want to clone one OS, so I took the best parts from all of them. Linux, Apple MacOS, Microsoft Microsoft Windows, Plan 9, BeOS, Haiku, SerenityOS, TempleOS, MenuetOS. Studied what each one got right and built my own version instead of picking a side.
It scans the PCI bus on boot and detects your GPU. Found one, it switches to an actual gradient instead of a flat screen.
It runs other people's binaries. A PE loader for Windows .exe files, an ELF loader for Linux, both written by hand, no host OS underneath doing the work for me.
Has a TCP/IP stack too. Ethernet framing, IPv4, full TCP handshake, on a network driver.
Has an App Store. pkg install firefox and it shows up in the Start Menu.
Still Beta. Still breaks. Not done.
ISO's up, boot it in VirtualBox and see for yourself.

Try it. Break it. Tell me how:
github.com/NivedhN160/N-OS

#OSDev #SystemsProgramming #C #BuildInPublic #LowLevel #OperatingSystems #Linux #Apple #macOS #Windows #Plan9 #BeOS #Haiku #SerenityOS #TempleOS #MenuetOS #Microsoft… more

View image
1/4


41

8

1
1,258 impressions

View analyticsView analytics

View NIVEDH SUNIL’s profile, open to work
NIVEDH SUNIL

  • You

Builds operating systems for fun. Ships AI for work.

1mo • Edited • 


My obsession with two things, love towards the Windows XP design and my own ZigNGPT has not let me stop thinking about it yet

Most people would call that a phase. I called it a roadmap.

Portfolio's now a fully clickable Microsoft Microsoft Windows XP desktop instead of a scroll-down page nobody reads past the first screen. Draggable windows, a Start menu, a Projects folder you open like it's 2003. Just because a normal portfolio is forgettable and this isn't.
Portfolio: https://lnkd.in/gKkB29BC

ZigNGPT v1 was a trigram model. That means it doesn't understand anything. It used to just count which word usually follows which word, in a language with no ML libraries and no mercy. It still has the only feature that matters: a Sarcasm mode that insults you for typing "hi."

V2 is the part I actually care about. Same personality, same Zig, but the brain underneath is no longer a frequency table. It's a transformer built from raw matrix math, with backpropagation I wrote by hand. No PyTorch. No autograd library doing the hard part for me. If the gradients are wrong, there's no stack trace pointing me to the bug, just output that's subtly garbage and a lot of staring at numbers.

If you would like to get tormented with the new brain check these out:

V1 (the trigram era): https://lnkd.in/gm4hC_4F
V2 (in progress, rebuilding the brain): https://lnkd.in/g3sZJVzG

Most people learn what a transformer is by importing one. I'm learning by failing to build one correctly, repeatedly, until I don't.

#Zig #MachineLearning #BuildInPublic #DeepLearning #SoftwareEngineering… more

View image

23


997 impressions

View analyticsView analytics

View NIVEDH SUNIL’s profile, open to work
NIVEDH SUNIL

  • You

Builds operating systems for fun. Ships AI for work.

1mo • 


Excited to share that I've landed an internship as a Backend AI Engineering Intern at FlyRank AI!

Grateful for the opportunity, and looking forward not to crash the systems.

Alen Malkoč

#Internship #BackendEngineering #AIEngineer #FlyRank… more

View image

137

21

8,464 impressions

View analyticsView analytics

View NIVEDH SUNIL’s profile, open to work
NIVEDH SUNIL

  • You

Builds operating systems for fun. Ships AI for work.

1mo • Edited • 


Built Terr-AR-ium: a 3D Voxel Sandbox that gamifies your carbon footprint.
Got tired of carbon tracker apps that are just boring charts nobody opens twice. So instead, we made your eco habits directly grow (or wreck) a live, Minecraft-style island.
Swipe right on a positive action like "Cold Wash" or "Bike to Work" and the island physically expands, sprouts bloom into full voxel trees and flowers. Swipe on a negative one like "Steak Dinner" and the decay creeps in, leaves turn yellow and brown, trees shrink. Your bad habits literally show up on the landscape.
Built the 3D scene with Three.js and React Three Fiber (React Three Drei for OrbitControls, Environment, Sparkles), fully pannable and zoomable in 360°. For content, didn't want users running out of actions, so it taps Groq's llama-3.1-8b-instant to procedurally generate endless unique eco-actions with calculated CO₂ impact on demand.
It's PWA-ready too, so you can install it straight to your home screen.
Check out the repo here: https://lnkd.in/gEcC8N8s
Live Link: https://lnkd.in/gSkT6ncV

Google
Hack2skill
Google for Developers
Google Developer Groups (GDG)
Google Student Ambassadors (India)
#React #ThreeJS #ReactThreeFiber #Groq #Llama3 #ClimateTech #WebDevelopment #PromptWars #Hack2Skill #CarbonFootprint #Hackathon #Google #Developer #PromptEngineering… more


12


807 impressions

View analyticsView analytics

View NIVEDH SUNIL’s profile, open to work
NIVEDH SUNIL

  • You

Builds operating systems for fun. Ships AI for work.

1mo • Edited • 


Volunteered at the 25th Florence Nightingale Award 2026, Vidhana Soudha, Bengaluru.
Handed out event kits, spoke with Christo Joseph., FRSA , AKC which was really insightful.
Nurses got recognized for the work hospitals actually run on.
One line stuck: doctors prescribe, nurses heal.
P.S also learned how to look busy while holding a stack of kits.
Garden City University
#FlorenceNightingaleAward2026 #VolunteerExperience #StudentVolunteer… more

View image
1/6


53

3

1
1,442 impressions

View analyticsView analytics


Show all
Experience

FlyRank AI logo
Backend AI Engineer - Intern

FlyRank AI · Internship

Jun 2026 - Present · 2 mos

Bengaluru, Karnataka, India · Remote

Currently interning at FlyRank AI as an AI intern, focusing on Backend AI Engineering.

Freelance Front End Developer

Anish and Ashitha Engineering Private Limited · Freelance

Nov 2025 - Jan 2026 · 3 mos

Bengaluru, Karnataka, India · Hybrid

Worked on Enhancing the Company Website 

 Cascading Style Sheets (CSS) and HTML5

Education
Garden City University logo
Garden City University

Bachelor of Technology - BTech, Computer Science and Engineering

Sep 2024 – Jun 2028

 HTML, Problem Solving and +21 skills

Sri Chaitanya College of Education logo
Sri Chaitanya College of Education

Higher Secondary Education

Jun 2022 – May 2024

Show all 3 educations
Licenses & certifications (24)
Cisco logo
Introduction to Data Science

Cisco

Issued Jul 2026

Show credential
Anthropic logo
Certificate of Completion: Al Fluency Framework & Foundations

Anthropic

Issued Jul 2026

Credential ID g86xdsydsj7j

Show credential
Show all 24 licenses
Projects (14)
N-OS

Jun 2026 – Present

 A 32-bit bare-metal OS built from scratch in C, bootloader to kernel. Custom GUI, virtual file system, hand-written TCP/IP stack, and a Win32/POSIX compatibility layer that natively executes Windows PE and Linux ELF binaries.

Thumbnail for GitHub - NivedhN160/N-OS
GitHub - NivedhN160/N-OS

ZigNGPTv2.0

Jun 2026 – Present

A Higher Abbrevation to the previous version of ZigNGPT

Thumbnail for GitHub - NivedhN160/ZigNGPTv2.0
GitHub - NivedhN160/ZigNGPTv2.0

Show all
Volunteering
Student Representative

Silver Jubilee 25th Florence Nightingale Awards Karnataka 2026

Jun 2026 · 1 mo

Health

Had the Opportunity to go to Vidhana Soudha, Bengaluru to attend this event and meet the honorable Health Minister U. T. Khader

Thumbnail for Representatives
Representatives

Skills (71)
Pipelining

Hugging Face Products

Show all
Test scores (4)
4th Semester

Score: 9.125 · Apr 2026


Associated with Garden City University

3rd Semester

Score: 9.82 · Dec 2025


Associated with Garden City University

Show all
Languages (6)
English

Full professional proficiency

Hindi

Native or bilingual proficiency

Show all 6 languages
Organizations
Institute of Electrical and Electronics Engineers

Member · Dec 2024 – Jan 2026


Associated with Garden City University

Interests

Top Voices

Companies

Groups

Newsletters

Schools

Suniel Shetty 

· 3rd

Entrepreneur I Actor I Investor & Mentor I Sportsman at Heart

1,092,315 followers


Following

Sundar Pichai 

· 3rd+

CEO at Google

4,836,636 followers


Following
Show all
Profile language
English

Public profile & URL
www.linkedin.com/in/nivedhn160


Who your viewers also viewed
Private to you


Student at SURE TRUST


View

Someone at Garden City University


View

Someone at Garden City University


View

Someone at FlyRank AI


View
People you may know
From your industry


Abdullah Fatota 🇵🇸

· 3rd

Software Engineer | M.Sc. Computer Science | Bošnjak

Connect
Naveen Kumar Bangla

· 3rd

Customer Support Executive at [24]7.ai

Connect

Risal Fareed Kalwar

· 3rd

Front End AI Engineer & AI Machine Learning 

Connect

Sneha Lohar

· 3rd+

Digital Interaction Executive at [24]7.ai

Connect

Hafiz Muhammad Asim

· 3rd

Backend AI Engineer - Intern at FlyRank AI

Connect
Show all
You might like
Pages for you


JPMorganChase

Financial Services

7,531,565 followers


Pinaki & 7 other connections work here


Follow

HackCulture

Technology, Information and Internet

5,301 followers


Monika & 21 other connections follow this page


Follow
Show all

About

Accessibility

Talent Solutions

Community Guidelines

Careers

Marketing Solutions 

Privacy & Terms

Ad Choices

Advertising

Sales Solutions

Mobile

Small Business

Safety Center

LinkedIn Corporation © 2026

Questions?

Visit our Help Center.

Manage your account and privacy

Go to your Settings.

Recommendation transparency

Learn more about Recommended Content.

Select language


English (English)
NIVEDH SUNIL
MessagingYou are on the messaging overlay. Press enter to open the list of conversations.
2

Compose message
You are on the messaging overlay. Press enter to open the list of conversations.
LinkedIn
LinkedIn
Close your conversation with {0} and NIVEDH SUNIL
LinkedIn Offer

Jul 28
LinkedIn Profile
LinkedIn
Today
sent the following messages at 8:00 PM
LinkedIn
LinkedIn  8:00 PM
Hi there, NIVEDH!



Get 50% off your first two months of LinkedIn Premium when you reactivate your subscription today.



50% off? Sure!

Not interested

50% off? Sure!
0 notifications

I'm looking for…



Home
My Network
Jobs
1
Messaging
12
Notifications


Me

For Business
Reactivate Premium: 50% Off


NIVEDH SUNIL

Builds operating systems for fun. Ships AI for work.


Projects

N-OS

Jun 2026 – Present

 A 32-bit bare-metal OS built from scratch in C, bootloader to kernel. Custom GUI, virtual file system, hand-written TCP/IP stack, and a Win32/POSIX compatibility layer that natively executes Windows PE and Linux ELF binaries.

Thumbnail for GitHub - NivedhN160/N-OS
GitHub - NivedhN160/N-OS

ZigNGPTv2.0

Jun 2026 – Present

A Higher Abbrevation to the previous version of ZigNGPT

Thumbnail for GitHub - NivedhN160/ZigNGPTv2.0
GitHub - NivedhN160/ZigNGPTv2.0

NGPT

Aug 2025 – Present

NGPT-Neural GPT is a custom large language model chatbot interface that integrates Meta AI's LLaMA 2 model alongside GPT-Neo retrieval-augmented QA. It combines deep conversational abilities from LLaMA with precise, knowledge-grounded answers from GPT-Neo for versatile AI interactions.

Thumbnail for GitHub - NivedhN160/Pre-trained-Generative-model-with-DuckDuckGo-access
GitHub - NivedhN160/Pre-trained-Generative-model-with-DuckDuckGo-access

Buying-Signal Scanner — Browser-Use Hackathon GTM Edition

Jul 2026 – Jul 2026

Built at the Browser-Use Hackathon GTM Edition by webcmd x GTMX Ventures. The insight: hiring signals are buying signals. When a company posts multiple RevOps, GTM Strategy, or Sales Engineering roles, they aren't just hiring, they're feeling operational pain and evaluating new tools. Most people look at job boards to find jobs. I pointed an agent at them to find customers instead.

Thumbnail for GitHub - NivedhN160/Browser-Use-Hackathon
GitHub - NivedhN160/Browser-Use-Hackathon

Terr-AR-ium

Jun 2026 – Jun 2026

Terr-AR-ium: a 3D Voxel Sandbox that gamifies your carbon footprint.

Terr-ar-ium

Thumbnail for GitHub - NivedhN160/promptwars
GitHub - NivedhN160/promptwars

Civic Twin: Bangalore (Elastic-AWS Hacknight BLR hackathon)

May 2026 – May 2026

an agentic civic-services assistant built for a hackathon (using Elastic + AWS). It unifies BBMP, BESCOM, and BWSSB access into one chat interface, using AWS Bedrock (Llama 3.3 70B) for orchestration, an MCP tool server for actions, Elasticsearch for indexing government data, and Supabase for identity. Its standout feature is a "Family Delegation Model" letting non-resident family members manage civic issues (complaints, bills, scheme discovery) for parents in Bangalore, with auto-GPS ward detection and a persistent ID vault.

Thumbnail for GitHub - NivedhN160/Hacknight-blr-elastic-aws
GitHub - NivedhN160/Hacknight-blr-elastic-aws

Other contributors

View all contributors
MAT-CHA.AI (AI for Bharath Hackathon)

Jan 2026 – Mar 2026

MAT-CHA.AI is an AI-powered platform that intelligently connects startups with relevant content creators using semantic search and Large Language Models. Instead of matching based on follower count, the system analyzes content style, niche, and brand requirements to generate smart, explainable collaboration matches, helping small creators gain opportunities while enabling brands to discover authentic marketing partners efficiently. 

GitHub - NivedhN160/Jarvis-Runtime

Other contributors




Ransomware Readiness Assesment Tool (MS Ramaiah Startup Mela Ideathon)

Mar 2026 – Mar 2026

AR2DAT — Autonomous Ransomware Response & Defense Dashboard: A front-end prototype simulating an AI-driven incident-response system, featuring real-time threat monitoring, forensic log analysis, an interactive attack-simulation engine, adaptive threat-learning visualization, and automated response workflows. Built with vanilla HTML/CSS/JS and Chart.js.

GitHub - NivedhN160/ransomware-assessment-system

Other contributors




ZigNGPTv1.0

Jun 2025 – Mar 2026

A Language model written in Zig Programming Language

Thumbnail for GitHub - NivedhN160/project1
GitHub - NivedhN160/project1

Terra-X

Jan 2026 – Feb 2026

TERRA-X is a state-of-the-art laboratory interface that allows users to manipulate global variables and witness AI-projected outcomes for any coordinate on Earth. It combines real-time weather grounding with the world's fastest LLMs to provide clinical, scientifically-accurate scenarios.

Thumbnail for GitHub - NivedhN160/Terra-X
GitHub - NivedhN160/Terra-X


Who your viewers also viewed
Private to you


Student at SURE TRUST


View

Someone at Garden City University


View

Someone at Garden City University


View

Someone at FlyRank AI


View
About

Accessibility

Talent Solutions

Community Guidelines

Careers

Marketing Solutions 

Privacy & Terms

Ad Choices

Advertising

Sales Solutions

Mobile

Small Business

Safety Center

LinkedIn Corporation © 2026

Questions?

Visit our Help Center.

Manage your account and privacy

Go to your Settings.

Recommendation transparency

Learn more about Recommended Content.

Select language


English (English)
NIVEDH SUNIL
MessagingYou are on the messaging overlay. Press enter to open the list of conversations.
2

Compose message
You are on the messaging overlay. Press enter to open the list of conversations.
LinkedIn
LinkedIn
Close your conversation with {0} and NIVEDH SUNIL
LinkedIn Offer

Jul 28
LinkedIn Profile
LinkedIn
Today
sent the following messages at 8:00 PM
LinkedIn
LinkedIn  8:00 PM
Hi there, NIVEDH!



Get 50% off your first two months of LinkedIn Premium when you reactivate your subscription today.



50% off? Sure!

Not interested

50% off? Sure!
0 notifications

I'm looking for…



Home
My Network
Jobs
1
Messaging
12
Notifications


Me

For Business
Reactivate Premium: 50% Off


NIVEDH SUNIL

Builds operating systems for fun. Ships AI for work.


Licenses & certifications

Cisco logo
Introduction to Data Science

Cisco

Issued Jul 2026

Show credential
Anthropic logo
Certificate of Completion: Al Fluency Framework & Foundations

Anthropic

Issued Jul 2026

Credential ID g86xdsydsj7j

Show credential
Salesforce logo
Salesforce Agentforce - AI Builders Day! Workshop

Salesforce

Issued Jun 2026

Thumbnail for Participation Certificate
Participation Certificate

M. S. RAMAIAH UNIVERSITY OF APPLIED SCIENCES logo
"Startup Journey - Idea Innovation & Entrepreneurship" Ideathon

M. S. RAMAIAH UNIVERSITY OF APPLIED SCIENCES

Issued Mar 2026

Thumbnail for Certificate
Certificate

 participated in the Workshop / Startup Mela / Ideathon titled "Startup Journey - Idea Innovation & Entrepreneurship" held at Ramaiah University of Applied Sciences on March 24-25, 2026.

Amazon Web Services (AWS) logo
AWS: AI for Bharath Hackathon

Amazon Web Services (AWS)

Issued Jun 2026

Credential ID 2026H2S04AIFB-P02157

Show credential
Skillsoft logo
Graph Data Structures: Understanding Graphs & Knowledge Graphs

Skillsoft

Issued Apr 2026

Credential ID 179077715

Show credential
Automata and Computability

Birla Institute of Technology & Science, Pilani

Issued Mar 2026

Credential ID ZP03PDTTNU9Z

Show credential
Qualitative Research Methods

University of Amsterdam

Issued Mar 2026

Credential ID JADXVRK6R8T7

Show credential
Design Thinking for Innovators

Coursera

Issued Mar 2026

Credential ID PUHWKRVG7EM7

Show credential
Mixed Methods Research: Bridging Qualitative & Quantitative

Coursera

Issued Mar 2026

Credential ID BSCI4OLOPDWK

Show credential

Who your viewers also viewed
Private to you


Student at SURE TRUST


View

Someone at Garden City University


View

Someone at Garden City University


View

Someone at FlyRank AI


View
About

Accessibility

Talent Solutions

Community Guidelines

Careers

Marketing Solutions 

Privacy & Terms

Ad Choices

Advertising

Sales Solutions

Mobile

Small Business

Safety Center

LinkedIn Corporation © 2026

Questions?

Visit our Help Center.

Manage your account and privacy

Go to your Settings.

Recommendation transparency

Learn more about Recommended Content.

Select language


English (English)
NIVEDH SUNIL
MessagingYou are on the messaging overlay. Press enter to open the list of conversations.
2

Compose message
You are on the messaging overlay. Press enter to open the list of conversations.
LinkedIn
LinkedIn
Close your conversation with {0} and NIVEDH SUNIL
LinkedIn Offer

Jul 28
LinkedIn Profile
LinkedIn
Today
sent the following messages at 8:00 PM
LinkedIn
LinkedIn  8:00 PM
Hi there, NIVEDH!



Get 50% off your first two months of LinkedIn Premium when you reactivate your subscription today.



50% off? Sure!

Not interested

50% off? Sure!
0 notifications

I'm looking for…



Home
My Network
Jobs
1
Messaging
12
Notifications


Me

For Business
Reactivate Premium: 50% Off


NIVEDH SUNIL

Builds operating systems for fun. Ships AI for work.


Test scores

4th Semester

Score: 9.125 · Apr 2026


Associated with Garden City University

3rd Semester

Score: 9.82 · Dec 2025


Associated with Garden City University

2nd Semester

Score: 9.55 · Jul 2025


Associated with Garden City University

1st Semester

Score: 9.55 · Mar 2025


Associated with Garden City University


Who your viewers also viewed
Private to you


Student at SURE TRUST


View

Someone at Garden City University


View

Someone at Garden City University


View

Someone at FlyRank AI


View
About

Accessibility

Talent Solutions

Community Guidelines

Careers

Marketing Solutions 

Privacy & Terms

Ad Choices

Advertising

Sales Solutions

Mobile

Small Business

Safety Center

LinkedIn Corporation © 2026

Questions?

Visit our Help Center.

Manage your account and privacy

Go to your Settings.

Recommendation transparency

Learn more about Recommended Content.

Select language


English (English)
NIVEDH SUNIL
MessagingYou are on the messaging overlay. Press enter to open the list of conversations.
2

Compose message
You are on the messaging overlay. Press enter to open the list of conversations.
LinkedIn
LinkedIn
Close your conversation with {0} and NIVEDH SUNIL
LinkedIn Offer

Jul 28
LinkedIn Profile
LinkedIn
Today
sent the following messages at 8:00 PM
LinkedIn
LinkedIn  8:00 PM
Hi there, NIVEDH!



Get 50% off your first two months of LinkedIn Premium when you reactivate your subscription today.



50% off? Sure!

Not interested

50% off? Sure!
