#!/bin/bash

# Quick Start Script for RAGAS Demo Setup
# This script helps you set up the demo repository quickly

set -e

echo "🚀 RAGAS GitHub Actions Demo - Quick Setup"
echo "=========================================="
echo ""

# Check if we're in the right directory
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: Please run this script from the ragas-github-actions-demo directory"
    exit 1
fi

# Step 1: Create virtual environment
echo "📦 Step 1: Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate
echo "✅ Virtual environment created"
echo ""

# Step 2: Install dependencies
echo "📥 Step 2: Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Step 3: Check for OpenAI API key
echo "🔑 Step 3: Checking for OpenAI API key..."
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  OPENAI_API_KEY not found in environment"
    echo ""
    echo "Please set your OpenAI API key:"
    echo "  export OPENAI_API_KEY='your-key-here'"
    echo ""
    echo "Or add it to your ~/.bashrc or ~/.zshrc:"
    echo "  echo 'export OPENAI_API_KEY=\"your-key-here\"' >> ~/.bashrc"
    echo ""
else
    echo "✅ OpenAI API key found"
fi
echo ""

# Step 4: Test local run
echo "🧪 Step 4: Testing local run..."
echo "Would you like to run a test now? (y/n)"
read -r response

if [ "$response" = "y" ] || [ "$response" = "Y" ]; then
    if [ -z "$OPENAI_API_KEY" ]; then
        echo "❌ Cannot run test without OPENAI_API_KEY"
    else
        echo "Running RAGAS tests..."
        python tests/ragas_test.py
    fi
else
    echo "⏭️  Skipping test run"
fi
echo ""

# Step 5: Git setup
echo "📝 Step 5: Git repository setup..."
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit: RAGAS GitHub Actions demo"
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi
echo ""

# Step 6: Next steps
echo "🎉 Setup Complete!"
echo ""
echo "Next steps:"
echo "1. Create a GitHub repository: https://github.com/new"
echo "2. Add remote: git remote add origin https://github.com/yourusername/ragas-github-actions-demo.git"
echo "3. Push code: git push -u origin main"
echo "4. Add OPENAI_API_KEY to GitHub Secrets:"
echo "   - Go to Settings → Secrets and variables → Actions"
echo "   - Click 'New repository secret'"
echo "   - Name: OPENAI_API_KEY"
echo "   - Value: your-openai-api-key"
echo "5. Create a pull request to test the workflow!"
echo ""
echo "📖 For recording the demo, see: demo/RECORDING_GUIDE.md"
echo "🎯 For strategy and tips, see: demo/FINAL_VERDICT.md"
echo ""
echo "Good luck! 🚀"
