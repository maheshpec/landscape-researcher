from langgraph.constants import START, END
from langgraph.graph import StateGraph
from pprint import pprint

from bot_types import State

def ocr(state: State):
    pass

graph_builder = StateGraph(State)
graph_builder.add_node("ocr", ocr)

graph_builder.add_edge(START, "ocr")
graph_builder.add_edge("ocr", END)
graph = graph_builder.compile()

def main():
    state = State(file_path="plant_list.pdf")
    for state_stream in graph.stream(state, stream_mode="values"):
        if len(state_stream["messages"]) > 0:
            state_stream["messages"][-1].pretty_print()


if __name__ == "__main__":
    main()
