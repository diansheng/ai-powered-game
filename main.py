import gradio as gr
from npc import NPC
from puzzles import generate_puzzle
from database import update_gold, get_gold

npc = NPC(name='Eldrin')

expected_answer = None

def chat_with_npc(player_input):
    if player_input.lower() == "开始解谜":
        global expected_answer
        puzzle, answer = generate_puzzle()
        expected_answer = answer
        return f"{puzzle}（请在聊天框输入答案）"

    return npc.get_npc_response(player_input)


def check_answer(player_input, correct_answer):
    if player_input == correct_answer:
        update_gold(10)  # 奖励金币
        expected_answer = None
        return "正确！你获得了 10 金币 🎉"
    return "错误，再试试！"

# 存储完整对话历史
chat_history = []


def chat(user_input):
    if not user_input.strip():
        return chat_history  # 如果输入为空，不做处理

    # 先检查游戏逻辑（如任务提交）
    if expected_answer is not None:
        game_response = check_answer(user_input, expected_answer)
        if game_response:
            chat_history.append(("You", user_input))
            chat_history.append(("System", game_response))  # System 代表游戏逻辑的反馈
            return chat_history

    # 如果没有任务相关的内容，则与 NPC 聊天
    npc_response = npc.get_npc_response(user_input)

    # 追加对话历史
    chat_history.append(("You", user_input))
    chat_history.append((npc.name, npc_response))  # Eldrin 是 NPC 名称

    return chat_history


if __name__ == "__main__":
    # 创建 Gradio UI
    with gr.Blocks() as demo:
        gr.Markdown("# 🏰 Welcome to Aetheria!")

        chatbox = gr.Chatbot()  # 显示完整对话历史
        user_input = gr.Textbox(placeholder="Type your message here...")

        # 绑定输入与聊天函数
        user_input.submit(chat, user_input, chatbox)

    # 启动应用
    demo.launch()

