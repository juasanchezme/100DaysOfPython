# Day 2. 
## Concepts Practised
The expression `"{:.2f}".format(...)` in Python is used to format floating-point numbers to a specific format. In this case, `"{:.2f}"` means the number will be rounded to **2 decimal places**.

- `{:}`: Placeholder for the value to be formatted.
- `.2f`: Specifies the format:
- `f`: Indicates a floating-point number.
- `.2`: Rounds the number to **two decimal places**.

# Git Setup and Basic Commands

Basic Git commands to configure, initialize, and manage a Git repository.

## 1. Git Configuration

Before using Git, you need to configure your username and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
To verify your Git configuration, use:
```bash
git config --list
```
## 2.  Initializing a Repository in a Specific Folder
```bash
cd "C:/path/to/your/folder"
```
## 3. Cloning a Repository

```bash
git clone <repository_url>
```
## 4. Checking the Status of the Repository
```bash
git status
```
## 5. Adding Changes

To stage a specific file:
```bash
git add <file_name>
```
To stage all changes:
```bash
git add .
```
## 6.Committing Changes
```bash
git commit -m "Your commit message"
```
## 7. Viewing Commit History
```bash
git log
```
Simplified one-line commit history:

```bash
git log --oneline
```