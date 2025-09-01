#!/bin/bash

echo "🚀 Setting up IV Spread Bot on VPS..."

# Navigate to project directory (adjust path as needed)
cd /path/to/your/IV_Spread

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Set up .env file
echo "⚙️  Setting up configuration..."
if [ ! -f .env ]; then
    cp env_template.txt .env
    echo "⚠️  Please edit .env file with your Alpaca API credentials!"
    echo "   nano .env"
fi

# Make scripts executable
chmod +x *.sh

echo "✅ Setup complete!"
echo "🚀 To start the bot: ./start_bot.sh"
echo "📊 To monitor: ./monitor_bot.sh"
echo "🛑 To stop: ./stop_bot.sh"
