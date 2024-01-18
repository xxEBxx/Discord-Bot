# Discord Bot Project Overview 🤖

## Project Context 🌐
The Discord Bot project addresses the evolving needs of a Discord server undergoing a critical transition. Faced with a substantial reduction in the number of moderators, the project aims to introduce advanced member management and an innovative moderation approach.

## Problem to Solve 🎯
The project originated from a significant reduction in moderators, presenting a challenge to the stability and quality of moderation within the dynamic Discord environment. The primary goal is to establish a system capable of detecting, understanding, and responding to undesirable behavior, particularly focusing on the detection of inappropriate words. This ambitious objective seeks to maintain a respectful environment aligned with community rules despite the reduced number of human moderators.

## Implemented Solutions 🚀
To tackle the challenges, the project incorporates proactive member management, automatically applying warnings and penalties to ensure an immediate and consistent response to undesirable behavior. A key innovation lies in the integration of a machine learning model, enabling automated detection of unwanted behavior and forming a proactive line of defense against harmful activities. The bot adapts its responses over time, anticipating and adjusting moderation based on changes in server dynamics.

## Challenges Encountered 🛠️
The development of the Discord Bot project was not without its challenges. Integrating the machine learning model demanded a deep understanding of concepts and associated libraries. Consistent management of warnings and sanctions, while maintaining bot stability, presented a complex challenge. Navigating interactions on the Discord server to ensure an optimal user experience and striking a balance between diverse functionality and moderation roles required careful planning.

## Installation Instructions 🛠️

To install and set up the Discord bot on your server, follow these steps:

1. **Clone the Repository:**
   - Clone the GitHub repository to your local machine using the following command:
     ```bash
     git clone https://github.com/xxEBxx/Discord-Bot.git
     ```

2. **Install Dependencies:**
   - Navigate to the project directory and install the required dependencies:
     ```bash
     cd Discord-Bot
     pip install -r requirements.txt
     ```

3. **Configure the Bot:**
   - Create a Discord bot on the Discord Developer Portal and obtain the bot token.
   - Set up environment variables or configuration files with the bot token and other necessary credentials.
   - Add a file named `filetoken.py` to the project root directory with the following variables:
     ```python
     token_code = "your_bot_token_here"
     guild_id = "your_guild_id_here"
     id_of_the_server_owner = "your_server_owner_id_here"
     bad_words = set()  # Add inappropriate words as a set, leave empty if nothing is initialized
     ```

4. **Run the Bot:**
   - Execute the `main.py` file to start the Discord bot:
     ```bash
     python main.py
     ```

5. **Configure Server Features:**
   - Customize the bot's features and behavior based on your server's requirements.
   - Review and modify commands in the `main.py` file to suit your preferences.

6. **Test the Bot:**
   - Join the Discord server where the bot is installed and test its various commands and features.
   - Ensure that the proactive member management and machine learning aspects are functioning as intended.

## Demo Video and Report 🎥

Explore the project's capabilities by watching the demo video and diving into the detailed report:

- **Demo Video:** Watch our 🚀 demonstration [video](https://github.com/xxEBxx/Discord-Bot/blob/main/Demo_Report/Demo%20Bot%20comp.mp4) to get an overview of the Discord Bot's features.
- **Report:** Read the detailed 📝 project [report](https://github.com/xxEBxx/Discord-Bot/blob/main/Demo_Report/REPORT.pdf) for insights into the development and functionality.
- **Presentation:** View our 🖥️ PowerPoint presentation to dive deeper into the project's architecture and key features. [ALGO.pptx](https://github.com/xxEBxx/Discord-Bot/files/13982223/ALGO.pptx)

## Contributing 🤝

If you are interested in contributing to the project, please check the [CONTRIBUTING.md](CONTRIBUTING.md) guide.

Congratulations! Your Discord bot is now installed and ready to enhance moderation and member management within your server. Adjust configurations, explore commands, and enjoy the benefits of automation and machine learning integration.
