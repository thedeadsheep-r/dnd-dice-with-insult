#!/bin/bash

# ==========================================
# CONFIGURATION
# You can change these variables as needed!
# ==========================================

# Replace this with your actual GitHub repository URL
REPO_URL="https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git"

# The name of your primary branch (usually 'main')
BRANCH_NAME="main"

# ==========================================

if [ "$REPO_URL" = "https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git" ]; then
    echo "⚠️ ERROR: Please open this script and change REPO_URL to your actual GitHub link first!"
    exit 1
fi

echo "🚀 Initializing new Git repository..."
git init

echo "📦 Staging all files..."
git add .

echo "💾 Committing files..."
git commit -m "Initial commit"

echo "🌿 Setting branch to '$BRANCH_NAME'..."
git branch -M "$BRANCH_NAME"

echo "🔗 Linking to GitHub repository..."
git remote add origin "$REPO_URL"

echo "⬆️ Pushing code to GitHub..."
git push -u origin "$BRANCH_NAME"

echo "✅ Done! Your project is now on GitHub."
