
# Cloud Resume Challenge

## Project Overview

Built and deployed a personal resume website with a serverless backend to track real-time visitor counts.

The frontend is hosted on **GitHub Pages**, and the backend is powered by **AWS Lambda**, **DynamoDB**, and **API Gateway**. Visitor count is fetched via JavaScript and displayed dynamically on the page. CI/CD is configured using **GitHub Actions** to automatically deploy changes.

## Technologies Used

- **Frontend**: GitHub Pages, HTML, CSS, JavaScript  
- **Backend**: AWS Lambda, DynamoDB, API Gateway  
- **CI/CD**: GitHub Actions  
- **Other**: IAM (permissions), CORS configuration

## Live Demo

🔗 https://san97-12.github.io/serverless-resume-website/

## Key Features

- Static resume site hosted on GitHub Pages
- Real-time visitor count using AWS serverless stack
- REST API built with API Gateway + Lambda
- Visitor data stored in DynamoDB
- Automated deployments via GitHub Actions

## Getting Started

1. Clone the repo and edit the HTML/CSS for your resume.
2. Set up an AWS Lambda function to manage a visitor counter.
3. Create a DynamoDB table to store visitor count.
4. Use API Gateway to expose your Lambda function as a REST endpoint.
5. Connect the frontend JavaScript to your API.
6. Deploy frontend via GitHub Pages.
7. Configure GitHub Actions for CI/CD (optional but recommended).

## License

MIT License
