from .llm import call_llm
from .tools import read_file, write_file, run_code
from .parser import parse_response
from .prompts import SYSTEM_PROMPT

def run_agent(task):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": task}
    ]

    for _ in range(25):
        response = call_llm(messages)
        parsed = parse_response(response)

        print("\n🤖:", parsed)

        if parsed.get("type") == "final":
            print("\n✅ DONE:", parsed.get("content"))
            break

        tool = parsed.get("tool")
        args = parsed.get("args", {})

        result = ""

        if tool == "read_file":
            result = read_file(args["path"])

        elif tool == "write_file":
            result = write_file(args["path"], args["content"])

        elif tool == "run_code":
            result = run_code(args["command"])

        messages.append({"role": "assistant", "content": response})
        messages.append({"role": "user", "content": f"Tool result:\n{result}"})
