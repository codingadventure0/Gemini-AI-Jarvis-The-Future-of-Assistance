# Jarvis Program
import speech_recognition as sr # Importing the speech recognition library for converting speech to text
import pyttsx3 # Importing the pyttsx3 library for text-to-speech conversion
import webbrowser # Importing webbrowser to open URLs in the default web browser
import os # Importing the os library to interact with the operating system (file operations, environment variables, etc.)
import time # Importing time library to manage time-related tasks (e.g., sleep, timestamps)
import requests # Importing requests library for making HTTP requests to interact with APIs or download content from the web
import wikipedia # Importing the wikipedia library to fetch articles from Wikipedia
import subprocess # Importing subprocess library to run system commands (e.g., to open applications or run scripts)
import json # Importing json to work with JSON data (parse, load, dump)
import smtplib # Importing smtplib to send emails using SMTP protocol
import psutil # Importing psutil to retrieve information on system processes and resource usage (e.g., CPU, memory)
import platform
import spacy
from datetime import datetime
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import google.generativeai as genai
import pywhatkit
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cv2
import pyautogui # for taking screenshot
from fuzzywuzzy import fuzz, process  # for opening application in pc
import random


#Its take administrative permission if needed some where
# import ctypes
# import sys
# import os

# def is_admin():
#     """Check if the script is running with administrative privileges."""
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False

# if not is_admin():
#     # Relaunch the script with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#     sys.exit()  # Exit the current instance since the new one will take over

# Global settings
nlp = spacy.load('en_core_web_sm')  # Natural Language Processing model

# Configure the Gemini API
genai.configure(api_key="YOUR API KEY") # Your Gemini API KEY HERE

class Jarvis:
    def __init__(self):
        """Initialize speech engine, recognizer, and NLP models."""
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.commands_list = []  # Keeps track of commands
        self.error_log = []  # Error log to track issues
        self.active_mode = False  # Starts in passive mode, only activates on "ready to work"
        self.stop_response = False  # Used to halt response mid-task
        self.init_settings()
        

    def init_settings(self):
        """Initialize settings that define the behavior of the assistant."""
        self.settings = {
            "voice_speed": 150,
            "error_tolerance": 3,  # How many retries before flagging an error
            "max_wait_time": 5,  # Max seconds to wait for user input
        }

    def speak(self, text):
        """Converts text to speech."""
        print(f"Jarvis: {text}")  # Print statement added for when Jarvis speaks
        self.engine.say(text)
        self.engine.runAndWait()
    
    def time_based_greeting(self):
        """Provide a greeting based on the current time of day."""
        hour = datetime.now().hour
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 17:
            greeting = "Good afternoon"
        elif 17 <= hour < 22:
            greeting = "Good evening"
        else:
            greeting = "Good night"
        
        self.speak(f"{greeting} Sir. I hope you're having a wonderful day.")
        # self.random_tech_thought()

    def random_tech_thought(self):
        """Speak a random thought related to technology, AI, coding, or hacking."""
        thoughts = [
            "Did you know that Python is one of the most popular languages for AI and machine learning?",
            "Coding is not just about syntax, it's about solving real-world problems.",
            "Artificial Intelligence has the potential to transform industries and daily life.",
            "Quantum computing could be the next revolution in computing technology.",
            "The rise of ethical hacking helps companies secure their systems.",
            "Machine learning models improve as they learn from more data, which is why data collection is so important.",
            "5G networks are bringing faster speeds and lower latency, enabling new possibilities in IoT and smart cities.",
            "Augmented Reality and Virtual Reality are making experiences more immersive in gaming and beyond.",
            "Data science and AI are helping solve some of the most complex challenges in healthcare.",
            "Cybersecurity is critical. As more devices connect to the internet, the attack surface increases.",
            "The Internet of Things (IoT) is revolutionizing how we interact with our environment.",
            "Cloud computing is allowing businesses to scale rapidly without large upfront investments.",
            "Open-source software fosters collaboration and innovation across the tech community.",
            "Big data analytics provides insights that drive smarter business decisions.",
            "Artificial Intelligence can help automate mundane tasks, freeing up time for creative work.",
            "Blockchain technology is changing the way we think about data integrity and transparency.",
            "Edge computing reduces latency by processing data closer to the source.",
            "Robotic process automation (RPA) is streamlining operations in various industries.",
            "Natural language processing (NLP) enables machines to understand and respond to human language.",
            "Data visualization tools are essential for making complex data understandable.",
            "The demand for data scientists is growing as organizations seek to leverage data for competitive advantage.",
            "Sustainability in tech is becoming more important, with green technologies emerging.",
            "DevOps practices enhance collaboration between development and operations teams.",
            "User experience (UX) design is crucial for creating products that users love.",
            "Cybersecurity awareness is vital for all employees, not just IT specialists.",
            "Gaming technology is advancing rapidly, with graphics and gameplay becoming more realistic.",
            "3D printing is revolutionizing manufacturing and prototyping processes.",
            "Machine learning is being applied in fraud detection systems to protect consumers.",
            "Mobile app development is an essential skill as mobile usage continues to rise.",
            "Voice recognition technology is becoming increasingly sophisticated and widely adopted.",
            "Digital marketing relies heavily on data analytics to target the right audiences.",
            "Artificial Intelligence is transforming customer service through chatbots and virtual assistants.",
            "Data privacy is more important than ever in our increasingly digital world.",
            "Wearable technology is changing how we monitor our health and fitness.",
            "Smart home devices are making our lives more convenient and efficient.",
            "Remote work technology has advanced significantly, enabling teams to collaborate from anywhere.",
            "Augmented Reality applications are enhancing retail experiences by allowing virtual try-ons.",
            "Cyber threats are constantly evolving, making continuous learning in cybersecurity essential.",
            "The future of transportation may include autonomous vehicles and smart traffic systems.",
            "E-learning platforms are democratizing education and making learning more accessible.",
            "Gamification is being used in various sectors to increase engagement and motivation.",
            "Smart cities leverage technology to improve quality of life for their residents.",
            "Data ethics is a critical consideration in the development of AI systems.",
            "The rise of digital currencies is changing how we think about money and transactions.",
            "Biometric security measures are becoming standard for protecting personal devices.",
            "Quantum algorithms could solve complex problems much faster than classical algorithms.",
            "Collaboration tools are essential for productivity in distributed teams.",
            "Cloud-native development practices are transforming how applications are built and deployed.",
            "Social media platforms are using AI to enhance user engagement and personalize content.",
            "Artificial Intelligence is being used to enhance decision-making in various industries.",
            "Data literacy is becoming a fundamental skill for professionals in every field.",
            "Supply chain management is benefiting from AI and machine learning for optimization.",
            "Tech companies are increasingly focusing on diversity and inclusion in their workforce.",
            "The rise of smart assistants like Alexa and Google Home is changing how we interact with technology.",
            "Digital twins are being used in industries to simulate and optimize processes.",
            "The proliferation of data creates both opportunities and challenges for organizations.",
            "Advancements in materials science are leading to the development of new tech products.",
            "The gig economy is reshaping how people work and earn income.",
            "Augmented analytics tools are empowering business users to gain insights without needing extensive training.",
            "As technology evolves, so does the importance of continuous learning and adaptation.",
            "Human-centered design is key to creating technologies that truly meet user needs."
        ]

        self.speak(f"Good thoughts of this time. {random.choice(thoughts)}")
        self.speak("Now i am ready to help you sir.")

    def listen(self, threshold=4000):
        """Listen for voice input but ignore quieter sounds."""
        with self.microphone as source:
            print("Listening...........")  # Print when Jarvis starts listening
            self.recognizer.adjust_for_ambient_noise(source)
            self.recognizer.energy_threshold = threshold  # Adjust sensitivity
            audio = self.recognizer.listen(source)
            try:
                query = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {query}")  # Print what the user said
                return query
            except sr.WaitTimeoutError:
                self.speak("I'm sorry, I couldn't hear you. Please try again.")
                return ""
            except sr.UnknownValueError:
                self.speak("Sorry, I did not catch that. Please repeat.")
                return ""
            except sr.RequestError:
                self.speak("Sorry, I'm having trouble connecting to the recognition service.")
                return ""
            except Exception as e:
                self.handle_errors(f"Voice recognition error: {str(e)}")
                return ""

    def handle_errors(self, error_message, severity="low"):
        """Enhanced error logging with notification for high-severity issues."""
        self.error_log.append({"message": error_message, "severity": severity, "timestamp": str(datetime.now())})
        print(f"Error Logged: {error_message}")
        if severity == "critical":
            self.speak("A critical error occurred. Please check the logs.")
        elif severity == "high":
            self.speak("A significant issue occurred. You might want to check the logs.")

    def save_logs(self):
        """Save logs to a file."""
        with open("jarvis_error_log.json", "w") as log_file:
            json.dump(self.error_log, log_file)

    # Gemini integration for enhanced responses
    def ask_gemini(self, query):
        """Use Gemini to get an answer to any question."""
        try:
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(contents=query)
            if response:
                answer = response.text.replace("*", "").replace("#", "")
                self.speak(f"{answer}")
            else:
                self.speak("I'm sorry, I couldn't find an answer to that.")
        except Exception as e:
            self.handle_errors(f"Gemini API error: {str(e)}")
    
    # Feature 1: Web Searching with Browser Optimization
    def search_web(self, query):
        """Perform a web search."""
        try:
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            self.speak(f"Here is what I found for {query}")
        except Exception as e:
            self.handle_errors(f"Web search error: {str(e)}")

    # Feature 2: Weather Information with API handling
    def get_weather(self, location):
        """Fetches weather information."""
        api_key = 'your_api_key_here'  # Replace with your actual API key
        try:
            base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            response = requests.get(base_url)
            if response.status_code == 200:
                data = response.json()
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                self.speak(f"The temperature in {location} is {temperature}°C with {description}.")
            else:
                self.speak("Sorry, I couldn't fetch the weather details right now.")
        except Exception as e:
            self.handle_errors(f"Weather API error: {str(e)}")

    # Feature 3: Opening System Applications
    def open_application(self, app_name):
        """Open applications with similar words using fuzzy matching."""
        # Enhanced dictionary of applications and their commands/paths
        app_map = {
            # Browsers
            "chrome": "start chrome",
            "edge": "start msedge",

            # Microsoft Office Suite
            "word": "start winword",
            "excel": "start excel",
            "powerpoint": "start powerpnt",
            "onenote": "start onenote",
            "outlook": "start outlook",
            "access": "start msaccess",

            # Adobe Suite
            "adobe reader": "start acrord32",
            "photoshop": r'"C:\\Program Files\\Adobe\\Adobe Photoshop 2023\\Photoshop.exe"',
            "illustrator": r'"C:\\Program Files\\Adobe\\Adobe Illustrator 2023\\Illustrator.exe"',
            "adobe premiere": r'"C:\\Program Files\\Adobe\\Adobe Premiere Pro 2023\\Adobe Premiere Pro.exe"',
            "after effects": r'"C:\\Program Files\\Adobe\\Adobe After Effects 2023\\AfterFX.exe"',

            # Development Tools
            "notepad": "notepad",
            "visual studio code": "code",
            "visual studio": r'"C:\\Program Files\\Microsoft Visual Studio\\2023\\Community\\Common7\\IDE\\devenv.exe"',
            "pycharm": r'"C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.1\\bin\\pycharm64.exe"',
            "eclipse": r'"C:\\Program Files\\Eclipse Foundation\\eclipse.exe"',
            "android studio": r'"C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"',
            "command prompt": "cmd",
            "powershell": "start powershell",
            "git bash": r'"C:\\Program Files\\Git\\git-bash.exe"',

            # File Management
            "file explorer": "explorer",
            "downloads": "explorer shell:Downloads",
            "documents": "explorer shell:Documents",
            "pictures": "explorer shell:Pictures",
            "videos": "explorer shell:Videos",
            "desktop": "explorer shell:Desktop",
            
            # System Utilities
            "task manager": "taskmgr",
            "calculator": "calc",
            "control panel": "control",
            "system information": "msinfo32",
            "device manager": "devmgmt.msc",
            "disk management": "diskmgmt.msc",
            "event viewer": "eventvwr.msc",
            "performance monitor": "perfmon.msc",
            "resource monitor": "resmon",
            "snipping tool": "snippingtool",
            "paint": "mspaint",
            "wordpad": "write",
            "notepad++": r'"C:\\Program Files\\Notepad++\\notepad++.exe"',

            # Media Players
            "windows media player": "wmplayer",
            "vlc": r'"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"',
            "groove music": "start mswindowsmusic:",
            "photos": "start ms-photos:",

            # Microsoft Store Apps
            "whatsapp": "explorer.exe shell:AppsFolder\\WhatsApp.WhatsApp_8wekyb3d8bbwe!",
            "spotify": "explorer.exe shell:AppsFolder\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0!",
            "netflix": "explorer.exe shell:AppsFolder\\4DF9E0F8.Netflix_mcm4njqhnhss8!",
            "camera": "start microsoft.windows.camera:",

            # Windows Settings
            "settings": "start ms-settings: ",
            "network settings": "start ms-settings:network ",
            "bluetooth settings": "start ms-settings:bluetooth ",
            "display settings": "start ms-settings:display ",
            "windows update": "start ms-settings:windowsupdate ",
            "personalization": "start ms-settings:personalization ",
            "privacy settings": "start ms-settings:privacy ",
            "time and language": "start ms-settings:dateandtime ",
            "region settings": "start ms-settings:regionformat ",
            "accounts settings": "start ms-settings:accounts ",
            "storage settings": "start ms-settings:storagesense ",
            "notifications settings": "start ms-settings:notifications ",
            "system settings": "start ms-settings:system ",
            "sound settings": "start ms-settings:sound ",
            "display brightness": "start ms-settings:display-brightness ",
            "ease of access settings": "start ms-settings:easeofaccess ",
            "keyboard settings": "start ms-settings:easeofaccess-keyboard ",
            "mouse settings": "start ms-settings:easeofaccess-mouse ",
            "power and sleep": "start ms-settings:powersleep ",
            "windows security": "start windowsdefender: ",

            # Social Media and Communication Tools
            "discord": r'"C:\\Users\\<YourUsername>\\AppData\\Local\\Discord\\app-1.0.9002\\Discord.exe"',
            "zoom": r'"C:\\Users\\<YourUsername>\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"',
            "telegram": r'"C:\\Users\\<YourUsername>\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"',
            "skype": "start skype:",

            # Cloud Storage
            "onedrive": "start onedrive",
            "google drive": r'"C:\\Program Files\\Google\\Drive\\googledrivesync.exe"',
            "dropbox": r'"C:\\Program Files (x86)\\Dropbox\\Client\\Dropbox.exe"',

            # Miscellaneous Applications
            "steam": r'"C:\\Program Files (x86)\\Steam\\Steam.exe"',
            "epic games": r'"C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"',
            "origin": r'"C:\\Program Files (x86)\\Origin\\Origin.exe"',
            "battle.net": r'"C:\\Program Files (x86)\\Battle.net\\Battle.net.exe"',
            "uplay": r'"C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\Uplay.exe"',
            "bluestacks": r'"C:\\Program Files\\BlueStacks\\Bluestacks.exe"',
            "paint 3d": "start ms-paint:",

            # Accessibility Tools
            "magnifier": "magnify",
            "narrator": "narrator",
            "on screen keyboard": "osk",
            "speech recognition": "start ms-speechrecognition:",
            "ease of access center": "control access.cpl",
            
            # Networking and Sharing
            "remote desktop": "mstsc",
            "network and sharing center": "control /name Microsoft.NetworkAndSharingCenter",
            "network connections": "ncpa.cpl",
            "wifi settings": "start ms-settings:network-wifi",
            "ethernet settings": "start ms-settings:network-ethernet",
            "mobile hotspot settings": "start ms-settings:network-mobilehotspot",
            
            # Security and Maintenance
            "windows defender": "start windowsdefender:",
            "firewall": "firewall.cpl",
            "bitlocker": "control /name Microsoft.BitLockerDriveEncryption",
            "update history": "start ms-settings:windowsupdate-history",
            "backup settings": "start ms-settings:backup",

            # File Compression and Extraction
            "winrar": r'"C:\\Program Files\\WinRAR\\WinRAR.exe"',
            "7zip": r'"C:\\Program Files\\7-Zip\\7zFM.exe"',
            
            # Entertainment
            "movies and tv": "start mswindowsvideo:",
            "groove music": "start mswindowsmusic:",
            "photos app": "start ms-photos:",
            "xbox game bar": "start xbox:",
            
            # Utilities
            "clock": "start ms-clock:",
            "alarm": "start ms-clock:alarm",
            "timer": "start ms-clock:timer",
            "stopwatch": "start ms-clock:stopwatch",
            "weather": "start bingweather:",
            "maps": "start bingmaps:",
            "mail": "start outlookmail:",
            "calendar": "start outlookcal:",
            "feedback hub": "start feedback-hub:",
        }

        # user_defined_apps = self.load_user_apps()  # Load additional apps
        # app_map.update(user_defined_apps)
    
        # Find the best match for the app_name
        best_match, match_score = process.extractOne(app_name, app_map.keys(), scorer=fuzz.partial_ratio)

        if match_score >= 75:  # Threshold for a "good enough" match
            self.speak(f"Opening {best_match}.")
            try:
                os.system(app_map[best_match])
            except Exception as e:
                self.handle_errors(f"Application opening error: {str(e)}")
        else:
            self.speak("I couldn't find an application with that name.")

    # Feature 4: Sending Email
    def send_email(self, to_address, subject, body):
        """Send email using SMTP."""
        from_address = "your_email@gmail.com"
        password = "your_password"
        try:
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_address, password)
            server.send_message(msg)
            server.quit()
            self.speak(f"Email sent to {to_address}.")
        except Exception as e:
            self.handle_errors(f"Email error: {str(e)}")

    # Feature 5: Wikipedia Integration
    def fetch_wikipedia(self, query):
        """Searches and returns Wikipedia summary."""
        try:
            result = wikipedia.summary(query, sentences=2)
            self.speak(f"According to Wikipedia: {result}")
        except Exception as e:
            self.handle_errors(f"Wikipedia error: {str(e)}")

    # Feature 6: System Monitoring
    def system_stats(self):
        """Get CPU, Memory and Disk usage statistics."""
        try:
            cpu_usage = psutil.cpu_percent()
            memory_info = psutil.virtual_memory()
            disk_info = psutil.disk_usage('/')
            self.speak(f"CPU usage is at {cpu_usage}%. Memory usage is at {memory_info.percent}%. Disk usage is at {disk_info.percent}%.")
        except Exception as e:
            self.handle_errors(f"System stats error: {str(e)}")

    # Feature 7: Task Scheduling and Reminders
    # def schedule_task(self, task_description, delay_seconds):
    #     """Schedule a task to be done after a specified delay."""
    #     try:
    #         self.speak(f"Scheduling task: {task_description} in {delay_seconds} seconds.")
    #         time.sleep(delay_seconds)
    #         self.speak(f"Reminder: It's time to {task_description}")
    #     except Exception as e:
    #         self.handle_errors(f"Task scheduling error: {str(e)}")
    def schedule_task(self, task_description, delay_seconds):
        """Schedule a task asynchronously."""
        def task_reminder():
            time.sleep(delay_seconds)
            self.speak(f"Reminder: It's time to {task_description}")
        
        self.speak(f"Scheduling task: {task_description} in {delay_seconds} seconds.")
        task_thread = threading.Thread(target=task_reminder)
        task_thread.start()

    # Feature 8: File Handling
    def file_search(self, filename):
        """Search for a file in the system."""
        try:
            for root, dirs, files in os.walk("/"):
                if filename in files:
                    file_path = os.path.join(root, filename)
                    self.speak(f"File found: {file_path}")
                    return file_path
            self.speak(f"File {filename} not found.")
        except Exception as e:
            self.handle_errors(f"File search error: {str(e)}")

    # Feature 9: AI-based Predictive Models (Placeholder)
    def ai_prediction(self, input_data):
        """Placeholder for AI-based predictions (e.g., weather, stock prices)."""
        # Implement ML models (e.g., using TensorFlow or scikit-learn)
        self.speak("This feature is still under development. Stay tuned!")

    # New Feature 10: Fetch Latest News
    def fetch_news(self):
        """Fetch latest news headlines."""
        api_key = 'your_news_api_key_here'  # Replace with your news API key
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
            response = requests.get(url)
            news_data = response.json()
            headlines = news_data['articles'][:5]  # Fetch top 5 headlines
            self.speak("Here are the latest news headlines:")
            for i, article in enumerate(headlines, start=1):
                self.speak(f"{i}. {article['title']}")
        except Exception as e:
            self.handle_errors(f"News fetching error: {str(e)}")

    # New Feature 11: Timer
    def set_timer(self, seconds):
        """Set a timer."""
        try:
            self.speak(f"Setting a timer for {seconds} seconds.")
            time.sleep(seconds)
            self.speak("Time's up!")
        except Exception as e:
            self.handle_errors(f"Timer error: {str(e)}")
    


    def play_music(self, genre=None):
        """Play music based on genre or specific song."""
        self.speak("Which platform would you like to use? Spotify or YouTube.")
        platform = self.listen()
        
        # Define the search query for the genre or specific music request
        search_query = f"{genre} music" if genre else "popular music"

        if platform.lower() == "youtube":
            # Open YouTube search results directly in a browser
            self.speak(f"Playing {search_query} on YouTube.")
            # webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            pywhatkit.playonyt(search_query)  # This will play the first video result
        
        elif platform.lower() == "spotify":
            # Set up Spotify authentication with Spotipy
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id="YOUR_SPOTIFY_CLIENT_ID",
                client_secret="YOUR_SPOTIFY_CLIENT_SECRET",
                redirect_uri="YOUR_REDIRECT_URI",
                scope="user-modify-playback-state"
            ))
            
            # Search for the track on Spotify
            results = sp.search(q=search_query, limit=1, type='track')
            if results['tracks']['items']:
                track_uri = results['tracks']['items'][0]['uri']
                # Start playback on Spotify
                sp.start_playback(uris=[track_uri])
                self.speak(f"Playing {search_query} on Spotify.")
            else:
                self.speak("I couldn't find that song on Spotify.")
        
        else:
            self.speak("I'm currently able to use only YouTube or Spotify.")


    def entertain_user(self, mood):
        if mood in ["lonely", "bored", "sad"]:
            self.speak("I can tell you a joke, play some music, or show an interesting video. What would you like?")
            choice = self.listen()
            if "joke" in choice:
                self.tell_joke()
            elif "music" in choice:
                self.play_music("relaxing")
            elif "video" in choice:
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        else:
            self.speak("Let me know if there’s something specific you would like.")

    
    def respond_to_feelings(self, feeling):
        """Respond to emotional states with motivational phrases."""
        if feeling in ["lonely", "sad", "down"]:
            self.speak("Remember, I'm here to chat and help you out! How about some music or a motivational quote?")
        else:
            self.speak("I'm here for anything you need.")

    
    def take_screenshot(self):
        """Takes a screenshot and saves it to the specified directory with a sequential name."""
        directory = r"C:\Users\Abhishek Kumar\Pictures\Screenshots"
        if not os.path.exists(directory):
            os.makedirs(directory)  # Create the directory if it doesn't exist
        
        # Find the next sequential filename
        files = [f for f in os.listdir(directory) if f.startswith("st") and f.endswith(".png")]
        numbers = [int(f[2:-4]) for f in files if f[2:-4].isdigit()]
        next_number = max(numbers, default=0) + 1  # Start from 1 if no existing files

        filename = f"st{next_number}.png"
        filepath = os.path.join(directory, filename)
        
        # Take and save the screenshot
        self.speak("Taking a screenshot.")
        screenshot = pyautogui.screenshot()
        screenshot.save(filepath)
        self.speak(f"Screenshot saved as '{filename}' in the Screenshots folder.")

    def shutdown_pc(self):
        """Shutdown the computer."""
        self.speak("Shutting down the computer.")
        os.system("shutdown /s /t 1")

    def restart_pc(self):
        """Restart the computer."""
        self.speak("Restarting the computer.")
        os.system("shutdown /r /t 1")
    
    def lock_pc(self):
        """Locks the PC."""
        self.speak("Locking the PC.")
        if platform.system() == "Windows":
            subprocess.call("rundll32.exe user32.dll, LockWorkStation")
        elif platform.system() == "Linux":
            subprocess.call("gnome-screensaver-command -l")
        else:
            self.speak("Lock function is not supported on this platform.")

    def toggle_wifi(self, state):
        """Turns Wi-Fi on or off on Windows using netsh command."""
        try:
            if state.lower() == "on":
                self.speak("Turning on Wi-Fi.")
                subprocess.call('netsh interface set interface "Wi-Fi" admin=ENABLED', shell=True)
            elif state.lower() == "off":
                self.speak("Turning off Wi-Fi.")
                subprocess.call('netsh interface set interface "Wi-Fi" admin=DISABLED', shell=True)
            else:
                self.speak("Invalid Wi-Fi state specified.")
        except Exception as e:
            self.handle_errors(f"Wi-Fi control error: {str(e)}")

    
            
    def toggle_bluetooth(self, state):
        """Turns Bluetooth on or off on Windows using PowerShell."""
        self.speak(f"Turning {'on' if state.lower() == 'on' else 'off'} Bluetooth.")
        try:
            if state.lower() == "on":
                subprocess.call('powershell -Command "Start-Service -Name bthserv"', shell=True)
            elif state.lower() == "off":
                subprocess.call('powershell -Command "Stop-Service -Name bthserv"', shell=True)
            else:
                self.speak("Invalid Bluetooth state specified.")
        except Exception as e:
            self.handle_errors(f"Bluetooth control error: {str(e)}")
    
    def info_developer(self):
        """Provides comprehensive information about the developer of Jarvis."""
        developer_info = (
            "My developer is Mr. Abhishek Kumar. He is an accomplished MERN stack developer with a wealth of experience in building dynamic and responsive web applications. "
            "He is highly proficient in programming languages such as C, C++, and Python, allowing him to tackle a wide range of software development challenges. "
            "In addition to his development skills, he has a keen interest in cybersecurity, enabling him to create secure and resilient applications that protect user data. "
            "Through his expertise, he designed and developed me, Jarvis, to be your personal AI assistant, capable of assisting you with various tasks, answering your queries, and providing valuable information. "
            "My primary goal is to enhance your productivity and make your life easier by seamlessly integrating with your daily activities and helping you find solutions quickly."
        )
        self.speak(developer_info)
        # Follow-up question
        self.speak("Would you like to know more about my owner?")
        
        # Listen for the user's response
        user_response = self.listen()  # Assuming you have a listen method to capture user input
        user_response = user_response.lower()  # Normalize the response for easier matching
        
        if "yes" in user_response or "sure" in user_response or "please" in user_response:
            self.speak("You can connect with him via LinkedIn, GitHub, Stack Overflow, Instagram, or Gmail.")
        else:
            self.speak("Okay, thanks for your interest!")


    def activate_jarvis(self):
        """Activate Jarvis when the wake word is detected."""
        self.speak("I am ready to work. What can I do for you?")
        self.active_mode = True

    def deactivate_jarvis(self):
        """Deactivate Jarvis when the stop command is given."""
        self.speak("Understood, stopping my response.")
        self.active_mode = False
        self.stop_response = True  # Reset for future commands

    def passive_listen(self):
        """Listen passively for activation or deactivation keywords."""
        while True:
            query = self.listen()
            if "jarvis ready to work" in query :
                self.activate_jarvis()
                break
            elif "jarvis stop responding" in query:
                self.deactivate_jarvis()
                break

    def main_listen_and_respond(self):
        """Main method to listen and respond actively when in active mode."""
        while True:
            if not self.active_mode:
                self.passive_listen()  # Keep listening passively until activated

            query = self.listen()
            if "jarvis stop responding" in query:
                self.deactivate_jarvis()
                continue

            # Process and respond to commands if in active mode
            if query and self.active_mode:
                # Insert additional command processing here
                self.process_query(query)
            
            # If response is interrupted, reset Jarvis to passive listening
            if self.stop_response:
                self.stop_response = False  # Reset the stop_response flag for future commands
                self.passive_listen()  # Return to passive listening mode

    # Add new feature for terminating applications
    def list_running_processes(self):
        """Lists all running processes with PID and names."""
        self.speak("Here are the running processes:")
        for proc in psutil.process_iter(['pid', 'name']):
            pid = proc.info['pid']
            name = proc.info['name']
            print(f"Process ID: {pid}, Process Name: {name}")
            self.speak(f"Process ID: {pid}, Process Name: {name}")
    
    def terminate_process(self, process_name=None, pid=None):
        """Terminate a process by name or PID."""
        try:
            if pid:
                # Terminate by PID
                process = psutil.Process(pid)
                process.terminate()
                self.speak(f"Process with PID {pid} has been terminated.")
            elif process_name:
                # Terminate by name
                terminated = False
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'].lower() == process_name.lower():
                        proc.terminate()
                        terminated = True
                        self.speak(f"Process {process_name} has been terminated.")
                        break
                if not terminated:
                    self.speak(f"Could not find a process named {process_name}.")
            else:
                self.speak("Please specify a process name or PID.")
        except psutil.NoSuchProcess:
            self.speak("The process does not exist or has already been terminated.")
        except Exception as e:
            self.handle_errors(f"Error terminating process: {str(e)}")

    # Centralized command processing
    def process_query(self, query):
        """Process user query and call the appropriate function."""
        
        if any(greeting in query for greeting in ["hello", "hi","hii" "hey", "what's up"]):
            self.speak("Hello! How can I assist you today?")
        elif any(greeting in query for greeting in ["good morning", "morning","good afternoon", "afternoon", "good evening", "evening", "good night","night"]):
            self.time_based_greeting()
        elif 'weather' in query:
            self.speak("Please tell me the city name.")
            city = self.listen()
            self.get_weather(city)
        elif 'search' in query:
            search_query = query.replace('search', '').strip()
            self.search_web(search_query)
        elif 'send email' in query:
            self.speak("To whom should I send the email?")
            recipient = self.listen()
            self.speak("What is the subject?")
            subject = self.listen()
            self.speak("What should the body say?")
            body = self.listen()
            self.send_email(recipient, subject, body)
        elif 'wikipedia' in query:
            topic = query.replace('wikipedia', '').strip()
            self.fetch_wikipedia(topic)
        elif 'system stats' in query:
            self.system_stats()
        elif 'set a timer' in query:
            self.speak("For how many seconds?")
            seconds = int(self.listen())
            self.set_timer(seconds)
        elif 'news' in query:
            self.fetch_news()
        elif 'jarvis' in query:
            self.ask_gemini(query.replace('jarvis', '').strip())    
        elif "play music" in query:
            genre = query.replace("play music", "").strip()
            self.play_music(genre)
        elif "entertain me" in query:
            self.entertain_user("bored")
        elif "feeling lonely" in query or "feeling sad" in query:
            self.respond_to_feelings("lonely")
        elif 'open' in query:
            app_name = query.replace('open', '').strip()
            self.open_application(app_name)
        elif "shutdown pc" in query:
            self.shutdown_pc()
        elif "restart pc" in query:
            self.restart_pc()
        elif "take screenshot" in query:
            self.take_screenshot()
        elif "lock my pc" in query:
            self.lock_pc()
        elif "on my wi-fi" in query:
            self.toggle_wifi("on")
        elif "off my wi-fi" in query:
            self.toggle_wifi("off")
        elif "on my bluetooth" in query:
            self.toggle_bluetooth("on")
        elif "off my bluetooth" in query:
            self.toggle_bluetooth("off")
        elif "terminate process" in query or "close application" in query:
            if "by name" in query:
                process_name = query.replace('terminate process by name', '').replace('close application by name', '').strip().lower()
                self.terminate_process(process_name=process_name)
            elif "by pid" in query:
                pid = int(query.replace('terminate process by pid', '').strip())
                self.terminate_process(pid=pid)
            else:
                self.speak("Would you like to terminate the process by name or PID?")
        
        elif "list running processes" in query or "show running applications" in query:
            self.list_running_processes()
        elif (
                "who is your developer" in query or 
                "tell me about your developer" in query or 
                "who created you" in query or 
                "who made you" in query or 
                "who is your owner" in query or 
                "what can you tell me about your developer" in query or 
                "give me information about your developer" in query
            ):
            self.info_developer()
        elif "how can i delete you" in query or "can you be deleted" in query:
            self.speak("Only my owner has the rights to delete me. I exist to serve you based on his commands.")
        elif "who are you" in query.lower():
            self.speak("I am Jarvis, your AI assistant, here to help you with your queries.")
        elif any(lists in query for lists in ["exit", "quit","stoped" "close","goodbye","good bye jarvis","good bye","bye"]):
            self.speak("Okay Goodbye Sir!!")
            exit()    
        else:
            self.ask_gemini(query)

# Main loop for activating Jarvis
if __name__ == '__main__':
    jarvis = Jarvis()
    # jarvis.speak("Hello, I am Jarvis. How can I assist you ??")
    jarvis.time_based_greeting()
    jarvis.random_tech_thought()
    jarvis.main_listen_and_respond()
    # while True:
    #     user_query = jarvis.listen()
    #     jarvis.process_query(user_query)
