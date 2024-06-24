from llama_index.core.chat_engine.context import ContextChatEngine
from llama_index.core.llms.llm import LLM
from llama_index.core.base.llms.types import ChatMessage, MessageRole
from llama_index.core.memory.chat_summary_memory_buffer import ChatSummaryMemoryBuffer
from llama_index.core.base.base_retriever import BaseRetriever
class ObsidianEngine:
    def __init__(self, retriever: BaseRetriever, llm: LLM) -> None:
        self.memory = ChatSummaryMemoryBuffer(
            token_limit=1000,
            llm=llm
        )
        self.ce = ContextChatEngine(
            retriever=retriever,
            llm=llm,
            memory=self.memory,
            prefix_messages=[
                ChatMessage(role=MessageRole.SYSTEM, content="You are a chat assistant with access to knowledge. You must be helpful and precise.")
            ]
        )

    def run(self, query: str):
        sacr = self.ce.stream_chat(
            message=query
        )
        return sacr
