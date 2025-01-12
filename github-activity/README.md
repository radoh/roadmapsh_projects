# GitHub User Activity Tracker

This project implements [GitHub User Activity Tracker](https://roadmap.sh/projects/github-user-activity), a Python-based application to fetch and display the activity of a GitHub user.

## Features
- Fetches GitHub activity using the GitHub API.

---

## Prerequisites

Before getting started, ensure you have the following installed on your system:

1. **Python 3.8+**
2. **pip** (Python package manager)

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone git@github.com:radoh/roadmapsh_projects.git
   cd github-activity
   ```

2. **Install Requirements**
   Install the required Python packages from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
    - Copy the `.env.example` file and rename it to `.env`:
      ```bash
      cp .env.example .env
      ```
    - Open the `.env` file and fill in the necessary constants, such as your GitHub API token.

      Example:
      ```env
      GITHUB_ACCESS_TOKEN=your_personal_github_token
      ```

4. **Run the Program**
    - To start the program, use the following command:
      ```bash
      python github-activity.py <username>
      ```

---

## Notes

- roadmap.sh project url: https://roadmap.sh/projects/github-user-activity
- Make sure your GitHub API token has the necessary permissions to fetch user activity.
- Refer to the [official documentation](https://roadmap.sh/projects/github-user-activity) for additional configuration and advanced usage details.

---

## Acknowledgments

Special thanks to [roadmap.sh](https://roadmap.sh/) for providing the project idea and resources.

