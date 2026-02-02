# AI_generated_python_news_monitor
# AI Generated Python News Monitor
A Python-based tool that automatically checks for news updates on python.org by deepseek and logs any changes. Deployed to PythonAnywhere for daily scheduled execution with zero manual operation.

## Features
1. News Extraction: Fetch latest news titles and publish times from Python.org by deepseek
2. Auto Comparison: Compare with the previous result to detect updates
3. Change Logging: Log new items with timestamps to Changelog.txt
4. Scheduled Execution: Runs daily via PythonAnywhere

## Project Structure
1. main_program.py: Main script (scraping + comparison + logging)
2. news_last.txt: Stores last fetched result (auto-generated)
3. Changelog.txt: Logs newly published news with timestamps (auto-generated)
>These .txt files are created automatically on first run.

## Tech Stack
Module         | Tool/Method
---------------|------------
Web Request    |"requests"
HTML Parsing   |deepseek api
File Handling  |"open"，"readlines"，"write"
Cloud Hosting  |PythonAnywhere（free tier）

## Sample Output

```text
News updates available.
[2025-03-14 17:27] Python 3.14.0 alpha 6 is out
```

## Changelog Sample
```text
[2025-03-14 17:27] Python 3.14.0 alpha 6 is out
[2025-03-12 15:32] PSF Distinguished Service Award Granted to Thomas Wouters
[2025-03-11 15:53] PSF Distinguished Service Award Granted to Van Lindberg
[2025-03-06 13:40] PSF Distinguished Service Award Granted to Ewa Jodlowska
[2025-03-04 11:40] Announcing Python Software Foundation Fellow Members for Q4 2024! 🎉
```

## Deployment Platform
1. Hosted on PythonAnywhere
2. Scheduled daily task with automatic execution
3. Supports manual logs, output viewing, and historical inspection

## Highlights
1. Extracts the HTML source code from Python's official website and submits it to the DeepSeek API for analysis to retrieve news content and timestamps
2. Smart comparison: Only logs newly detected updates
3. Modular structure: Easy to integrate notification systems like email or Telegram
4. Designed for long-term use with persistent logs

## Future Plans
1. Monitor multiple pages and websites simultaneously
2. Switch log format to CSV/JSON for better analysis
3. Integrate email/WeChat/Telegram notification system
4. Package as .exe or build GUI for non-technical users

## Author
Developed by Cheng-Lazypd as a project on automation, deployment, and AI data monitoring. Open to collaboration, feedback, and further development.
