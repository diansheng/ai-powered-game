# config.py
import sys
sys.path.insert(0, './..')
from main import hf_token
# 替换为您的 Hugging Face API 令牌
API_TOKEN = hf_token
# 选择适当的模型，例如 'gpt2'
MODEL_NAME = "Qwen/Qwen2.5-72B-Instruct"

# 生成文本时的最大 token 数量
MAX_NEW_TOKENS = 1024
