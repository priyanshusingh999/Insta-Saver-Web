# Instagram Downloader

A Streamlit web application to download Instagram Reels, Stories, and Photos by providing the URL. The app uses Selenium with a headless Chrome browser to interact with [fastdl.app](https://fastdl.app) to fetch download links.

## Features

- Download Instagram Reels, Stories, and Photos
- Simple and user-friendly interface using Streamlit
- Progress bar to track download link generation
- Runs in a headless browser environment

## Installation

### Prerequisites

- Python 3.10 or higher
- Google Chrome or Chromium browser
- ChromeDriver compatible with your Chrome version (if running locally)

### Setup

1. Clone the repository or download the project files.

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the app locally:

```bash
streamlit run main.py
```

Open the displayed URL in your browser. Enter the Instagram URL you want to download, select the content type (Reel, Story, or Photo), and click the download button. The app will generate a download link for you.

## Docker

The project includes a Dockerfile to containerize the app.

### Build the Docker image

```bash
docker build -t insta-saver-web .
```

### Run the Docker container

```bash
docker run -p 8501:8501 insta-saver-web
```

The app will be accessible at `http://localhost:8501`.

## Deployment

The project includes a `render.yaml` file for deployment on Render.com or similar platforms using Docker.

## Notes

- The app uses a headless Chrome browser via Selenium, so ensure the necessary drivers and dependencies are installed.
- The Docker image installs Chromium and the required drivers automatically.

## License

This project is licensed under the MIT License.
