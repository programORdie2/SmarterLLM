# SmarterLLM 🧠

This project is tries to make LLMs more intelligent by giving them access to the internet, the current date and time and making them better at math by using tools.

## Setup

To get started with this project, follow these steps:

1. Clone the repository: `git clone https://github.com/programORdie2/SmarterLLM.git`
2. CD into the directory: `cd src`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Configure the project settings: Rename `.env.sample` to `.env` and replace the placeholder with your [Groq API key](https://console.groq.com/keys).
5. Run the project: `python main.py`

## Adding tools

To add a tool, all you need to do is:

1. Write your tool code and add it to the `/src/tools` directory.
2. Make sure it just returns `None` on error.
3. Add it to the list of tools in `/src/tool_list.py`, and describe it.
4. Done!


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository: `git fork https://github.com/programORdie2/SmarterLLM`
2. Create a new branch: `git checkout -b your-branch-name`
3. Make your changes and commit them: `git commit -m "your commit message"`
4. Push your changes to your fork: `git push origin your-branch-name`
5. Open a pull request: `https://github.com/programORdie2/SmarterLLM/pulls`

That's it!

## License

This project is licensed under the AGPL3 License. See the [LICENSE](LICENSE) file for more information.