import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/celia123/Documentos/Github/chatbot_ros/ws_chatbot/install/chatbot'
