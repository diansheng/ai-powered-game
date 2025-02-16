from dataclasses import dataclass

from huggingface_hub import InferenceClient
import config

# 初始化 InferenceClient

@dataclass(init=False)
class NPC:
    # 游戏设定：让 AI 进入角色
    # 记录对话历史
    chat_history = []
    client = InferenceClient(model=config.MODEL_NAME, token=config.API_TOKEN)

    def __init__(self, name, system_message=None):
        self.name=name
        if system_message:
            self.system_message=system_message
        else:
            system_message = """
                You are an NPC in a fantasy RPG game, set in the world of Aetheria.
                You play as {}, a wise and mysterious alchemist living in the city of Lumora.
                Your role is to guide players, provide lore, and offer quests. 
                Stay in character and do not break the fourth wall."""
            self.system_message=system_message.format(name)


    def get_npc_response(self, player_input):
        try:
            # 组织对话历史
            messages = [{"role": "system", "content": self.system_message}]
            for chat in self.chat_history:
                role, content = chat.split(": ", 1)
                messages.append({"role": role.lower(), "content": content})

            messages.append({"role": "user", "content": player_input})

            # 调用 Hugging Face OpenAI 兼容 API
            response = self.client.chat.completions.create(
                messages=messages,
                max_tokens=config.MAX_NEW_TOKENS
            )

            # 提取 AI 回复
            response_text = response.choices[0].message.content.strip()

            # 存储对话历史
            self.chat_history.append(f"user: {player_input}")
            self.chat_history.append(f"assistant: {response_text}")

            return response_text
        except Exception as e:
            return f"Error: {str(e)}"
