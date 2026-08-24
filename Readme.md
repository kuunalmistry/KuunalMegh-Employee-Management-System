<div align="center">

<h1>☁️ Kuunal Employee Management System</h1>

<p>
  <strong>A Cloud-Based Employee Management Application</strong>
</p>

<p>
  Built with Python Flask and deployed on Microsoft Azure
</p>

<br>

<p>
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Microsoft-Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white">
  <img src="https://img.shields.io/badge/Azure-SQL-0078D4?style=for-the-badge&logo=microsoftsqlserver&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white">
</p>

<p>
  <img src="https://img.shields.io/badge/Deployment-Successful-2EA44F?style=flat-square">
  <img src="https://img.shields.io/badge/Cloud-Azure-0078D4?style=flat-square">
  <img src="https://img.shields.io/badge/CI%2FCD-Automated-2088FF?style=flat-square">
</p>

<br>

<p>
  <a href="#-about-the-project">About</a> •
  <a href="#-features">Features</a> •
  <a href="#-technology-stack">Tech Stack</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-deployment">Deployment</a> •
  <a href="#-setup">Setup</a>
</p>

</div>

<hr>

<h2>🚀 Project Overview</h2>

<table>
<tr>
<td width="50%">

<h3>💼 Employee Management</h3>

<p>
A web-based application designed to manage employee records through a clean
and simple interface.
</p>

</td>

<td width="50%">

<h3>☁️ Cloud Deployment</h3>

<p>
The application is hosted on Microsoft Azure App Service and connected to
Azure SQL Database.
</p>

</td>
</tr>

<tr>
<td width="50%">

<h3>⚡ Automated CI/CD</h3>

<p>
GitHub Actions automatically builds and deploys the application whenever
changes are pushed to the repository.
</p>

</td>

<td width="50%">

<h3>🔐 Secure Configuration</h3>

<p>
Database credentials and application secrets are managed through Azure
Environment Variables.
</p>

</td>
</tr>
</table>

<hr>

<h2>📌 About the Project</h2>

<p>
<strong>Kuunal Employee Management System</strong> is a cloud-based web
application developed using <strong>Python</strong> and
<strong>Flask</strong>.
</p>

<p>
The system provides an interface for managing employee information while
demonstrating the complete lifecycle of a modern cloud application —
from development and database integration to automated deployment on
Microsoft Azure.
</p>

<p>
The project combines <strong>Flask</strong>, <strong>Azure SQL Database</strong>,
<strong>Azure App Service</strong>, <strong>GitHub</strong>, and
<strong>GitHub Actions</strong> into a complete cloud deployment workflow.
</p>

<hr>

<h2>🎯 Assignment Objectives</h2>

<table>
<tr>
<td>🌐</td>
<td>Develop a web-based Employee Management System using Flask.</td>
</tr>

<tr>
<td>🎨</td>
<td>Create a structured frontend using HTML and CSS.</td>
</tr>

<tr>
<td>🗄️</td>
<td>Connect the application to a SQL database.</td>
</tr>

<tr>
<td>☁️</td>
<td>Deploy the application using Microsoft Azure App Service.</td>
</tr>

<tr>
<td>🔐</td>
<td>Configure secure environment variables.</td>
</tr>

<tr>
<td>⚙️</td>
<td>Implement automated CI/CD using GitHub Actions.</td>
</tr>

<tr>
<td>🧪</td>
<td>Test and verify the deployed cloud application.</td>
</tr>
</table>

<hr>

<h2>✨ Features</h2>

<table>
<tr>
<td width="50%">

<h3>👥 Employee Records</h3>
<p>View employee information through the web dashboard.</p>

<h3>➕ Add Employees</h3>
<p>Add new employee records using a dedicated form.</p>

<h3>✏️ Edit Employees</h3>
<p>Update existing employee information whenever required.</p>

</td>

<td width="50%">

<h3>🗑️ Delete Employees</h3>
<p>Remove employee records from the database.</p>

<h3>🗄️ Database Integration</h3>
<p>Store employee information using Azure SQL Database.</p>

<h3>☁️ Cloud Hosting</h3>
<p>Access the application through Azure App Service.</p>

</td>
</tr>
</table>

<hr>

<h2>🛠️ Technology Stack</h2>

<table>
<tr>
<th>Technology</th>
<th>Role</th>
</tr>

<tr>
<td>🐍 <strong>Python 3.11</strong></td>
<td>Backend programming language</td>
</tr>

<tr>
<td>⚗️ <strong>Flask</strong></td>
<td>Web application framework</td>
</tr>

<tr>
<td>🎨 <strong>HTML / CSS</strong></td>
<td>Frontend structure and styling</td>
</tr>

<tr>
<td>🗄️ <strong>Azure SQL</strong></td>
<td>Cloud database</td>
</tr>

<tr>
<td>☁️ <strong>Azure App Service</strong></td>
<td>Application hosting</td>
</tr>

<tr>
<td>🐙 <strong>GitHub</strong></td>
<td>Source code management</td>
</tr>

<tr>
<td>⚙️ <strong>GitHub Actions</strong></td>
<td>CI/CD automation</td>
</tr>
</table>

<hr>

<h2>🏗️ Architecture</h2>

<div align="center">

<pre>
                         👤 USER
                           │
                           │ HTTPS
                           ▼
                ┌───────────────────────┐
                │   ☁️ AZURE APP        │
                │       SERVICE         │
                │                       │
                │   🐍 Python + Flask   │
                └───────────┬───────────┘
                            │
                            │ SQL Connection
                            ▼
                ┌───────────────────────┐
                │   🗄️ AZURE SQL        │
                │      DATABASE         │
                │                       │
                │   Employee Records    │
                └───────────────────────┘


        👨‍💻 Developer
             │
             │ git push
             ▼
      ┌───────────────┐
      │    GitHub     │
      │  Repository   │
      └───────┬───────┘
              │
              ▼
      ┌───────────────┐
      │ GitHub Actions│
      │               │
      │  Build        │
      │    ↓          │
      │  Deploy       │
      └───────┬───────┘
              │
              ▼
      ☁️ Azure App Service
</pre>

</div>

<hr>

<h2>📂 Repository Structure</h2>

<pre>
Kuunal-Employee-Management-System/
│
├── 📁 .github/
│   └── 📁 workflows/
│       └── ⚙️ main_kuunalmegh-employee-app-2026.yml
│
├── 📁 templates/
│   ├── 🌐 add_employee.html
│   ├── 🌐 base.html
│   ├── 🌐 edit_employee.html
│   └── 🌐 index.html
│
├── 📄 .gitignore
├── 📄 Readme.md
├── 🐍 app.py
└── 📦 requirements.txt
</pre>

<hr>

<h2>🖥️ Application Pages</h2>

<table>
<tr>
<th>Page</th>
<th>Purpose</th>
</tr>

<tr>
<td>🏠 <code>index.html</code></td>
<td>Main employee dashboard and employee listing.</td>
</tr>

<tr>
<td>➕ <code>add_employee.html</code></td>
<td>Add a new employee to the system.</td>
</tr>

<tr>
<td>✏️ <code>edit_employee.html</code></td>
<td>Edit information of an existing employee.</td>
</tr>

<tr>
<td>🧩 <code>base.html</code></td>
<td>Common layout used across application pages.</td>
</tr>
</table>

<hr>

<h2>🗄️ Database Configuration</h2>

<p>
The application uses <strong>Azure SQL Database</strong> for storing employee
records.
</p>

<h3>Required Environment Variables</h3>

<table>
<tr>
<th>Variable</th>
<th>Purpose</th>
</tr>

<tr>
<td><code>DB_SERVER</code></td>
<td>Azure SQL Server address</td>
</tr>

<tr>
<td><code>DB_NAME</code></td>
<td>Database name</td>
</tr>

<tr>
<td><code>DB_USERNAME</code></td>
<td>Database username</td>
</tr>

<tr>
<td><code>DB_PASSWORD</code></td>
<td>Database password</td>
</tr>

<tr>
<td><code>SECRET_KEY</code></td>
<td>Flask application secret key</td>
</tr>
</table>

<hr>

<h2>🔐 Security</h2>

<p>
Sensitive information is <strong>not hard-coded</strong> into the application.
Database credentials and secret keys are stored using Azure App Service
<strong>Environment Variables</strong>.
</p>

<pre>
DB_SERVER=your-server
DB_NAME=your-database
DB_USERNAME=your-username
DB_PASSWORD=your-password
SECRET_KEY=your-secret-key
</pre>

<p>
<strong>⚠️ Important:</strong> Never commit passwords, API keys, database
credentials, or other sensitive information to a public repository.
</p>

<hr>

<h2>☁️ Azure Deployment</h2>

<table>
<tr>
<th>Configuration</th>
<th>Value</th>
</tr>

<tr>
<td>Application</td>
<td><code>kuunalmegh-employee-app-2026</code></td>
</tr>

<tr>
<td>Publish</td>
<td>Code</td>
</tr>

<tr>
<td>Operating System</td>
<td>Linux</td>
</tr>

<tr>
<td>Runtime</td>
<td>Python 3.11</td>
</tr>

<tr>
<td>Region</td>
<td>Central India</td>
</tr>

<tr>
<td>App Service Plan</td>
<td>Basic B1</td>
</tr>

<tr>
<td>Database</td>
<td>Azure SQL Database</td>
</tr>
</table>

<hr>

<h2>⚙️ CI/CD Pipeline</h2>

<p>
The project uses <strong>GitHub Actions</strong> to automate the deployment
process.
</p>

<div align="center">

<pre>
       👨‍💻 Developer
             │
             │ Push Code
             ▼
      ┌───────────────┐
      │    GitHub     │
      └───────┬───────┘
              │
              ▼
      ┌───────────────┐
      │ GitHub Actions│
      └───────┬───────┘
              │
        ┌─────┴─────┐
        ▼           ▼
     🔨 BUILD     🚀 DEPLOY
        │           │
        └─────┬─────┘
              ▼
      ☁️ Azure App Service
              │
              ▼
        🌐 LIVE APP
</pre>

</div>

<h3>Workflow File</h3>

<pre>
.github/workflows/main_kuunalmegh-employee-app-2026.yml
</pre>

<hr>

<h2>📊 Deployment Status</h2>

<div align="center">

<table>
<tr>
<th>Component</th>
<th>Status</th>
</tr>

<tr>
<td>🐙 GitHub Repository</td>
<td>🟢 Configured</td>
</tr>

<tr>
<td>⚙️ GitHub Actions</td>
<td>🟢 Configured</td>
</tr>

<tr>
<td>🔨 Build Job</td>
<td>🟢 Successful</td>
</tr>

<tr>
<td>🚀 Deploy Job</td>
<td>🟢 Successful</td>
</tr>

<tr>
<td>☁️ Azure App Service</td>
<td>🟢 Running</td>
</tr>

<tr>
<td>🗄️ Azure SQL Database</td>
<td>🟢 Configured</td>
</tr>

<tr>
<td>🌐 Live Application</td>
<td>🟢 Working</td>
</tr>

</table>

</div>

<hr>

<h2>🧪 Testing & Verification</h2>

<p>
After deployment, the application was tested through the public Azure Web App
endpoint.
</p>

<table>
<tr>
<th>Test</th>
<th>Result</th>
</tr>

<tr>
<td>Application startup</td>
<td>✅ Passed</td>
</tr>

<tr>
<td>Employee dashboard</td>
<td>✅ Passed</td>
</tr>

<tr>
<td>Add employee</td>
<td>✅ Passed</td>
</tr>

<tr>
<td>Edit employee</td>
<td>✅ Passed</td>
</tr>

<tr>
<td>Delete employee</td>
<td>✅ Passed</td>
</tr>

<tr>
<td>Database connectivity</td>
<td>✅ Passed</td>
</tr>

<tr>
<td>Environment variables</td>
<td>✅ Configured</td>
</tr>

<tr>
<td>GitHub Actions Build</td>
<td>✅ Successful</td>
</tr>

<tr>
<td>GitHub Actions Deploy</td>
<td>✅ Successful</td>
</tr>
</table>

<hr>

<h2>💻 Run Locally</h2>

<h3>1️⃣ Clone the Repository</h3>

<pre>
git clone https://github.com/kuunalmistry/Kuunal-Employee-Management-System.git
</pre>

<h3>2️⃣ Open the Project</h3>

<pre>
cd Kuunal-Employee-Management-System
</pre>

<h3>3️⃣ Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>4️⃣ Configure Environment Variables</h3>

<pre>
DB_SERVER=your-server
DB_NAME=your-database
DB_USERNAME=your-username
DB_PASSWORD=your-password
SECRET_KEY=your-secret-key
</pre>

<h3>5️⃣ Run the Application</h3>

<pre>
python app.py
</pre>

<p>
The Flask development server will start locally and provide a URL through
which the application can be accessed.
</p>

<hr>

<h2>📦 Dependencies</h2>

<p>
Project dependencies are maintained inside:
</p>

<pre>
requirements.txt
</pre>

<p>
Install all dependencies with:
</p>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>🎓 Learning Outcomes</h2>

<table>
<tr>
<td>🐍</td>
<td>Python Flask web application development</td>
</tr>

<tr>
<td>🌐</td>
<td>HTML template-based frontend development</td>
</tr>

<tr>
<td>🗄️</td>
<td>SQL database integration</td>
</tr>

<tr>
<td>☁️</td>
<td>Microsoft Azure cloud deployment</td>
</tr>

<tr>
<td>⚙️</td>
<td>GitHub Actions CI/CD automation</td>
</tr>

<tr>
<td>🔐</td>
<td>Secure environment variable management</td>
</tr>

<tr>
<td>🚀</td>
<td>Automated application deployment</td>
</tr>

<tr>
<td>🧪</td>
<td>Cloud application testing and troubleshooting</td>
</tr>
</table>

<hr>

<h2>🏁 Conclusion</h2>

<p>
The <strong>Kuunal Employee Management System</strong> successfully
demonstrates how a Python Flask application can be developed, connected to a
cloud database, deployed on Microsoft Azure, and integrated with an automated
CI/CD pipeline.
</p>

<p>
The project combines application development, database management,
cloud computing, source control, and DevOps practices into one complete
deployment workflow.
</p>

<div align="center">

<hr>

<h2>☁️ Built & Deployed on Microsoft Azure</h2>

<p>
<strong>Developed by Kuunal Mistry</strong>
</p>

<p>
B.Tech — AI/ML & Computer Science
</p>

<br>

<p>
<em>Develop • Integrate • Automate • Deploy</em>
</p>

</div>
