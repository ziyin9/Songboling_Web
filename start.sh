#!/bin/bash
# 松柏嶺網站快速啟動腳本

echo "🍵 啟動松柏嶺網站..."
echo ""

# 啟動虛擬環境
echo "📦 啟動虛擬環境..."
source venv/bin/activate

# 運行網站
echo "🚀 啟動 Flask 服務器..."
echo "📍 網站將在 http://127.0.0.1:5001 運行"
echo ""
echo "⌨️  按 Ctrl+C 停止服務器"
echo ""

python3 app.py
