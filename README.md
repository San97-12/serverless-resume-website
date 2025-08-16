Personal Resume Website with Live Visitor Counter
This project hosts my personal resume as a fast, secure, and scalable website on AWS, with a serverless backend that tracks and displays visitor counts in real time.

Key Features
Static resume site hosted on AWS S3 with CloudFront CDN and HTTPS
Serverless visitor counter using AWS Lambda, DynamoDB, and API Gateway
Live visitor count displayed dynamically on the resume page
Optional CI/CD automation via GitHub Actions for seamless updates
Optional Infrastructure as Code for automated resource provisioning

Technologies
AWS S3, CloudFront
AWS Lambda, DynamoDB, API Gateway
HTML, CSS, JavaScript
GitHub Actions (CI/CD)

How It Works
The resume is served as a static website from an S3 bucket, distributed globally with CloudFront.
A visitor counter backend increments the view count on each visit via Lambda and DynamoDB.
The frontend fetches and displays the visitor count using JavaScript.
Code updates can be deployed automatically through GitHub Actions.

Usage
Visit the hosted website to see the resume and live visitor count.
Code changes pushed to GitHub trigger automatic frontend deployment (if configured).
