# code_analyzer.py
import os, ast, json

def analyze_code():
    summary = {"files_scanned": 0, "functions": 0, "classes": 0, "lines_changed": 0}
    for root, _, files in os.walk("."):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(root, f)
                summary["files_scanned"] += 1
                with open(path, "r", encoding="utf-8") as file:
                    try:
                        tree = ast.parse(file.read())
                        summary["functions"] += len([n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)])
                        summary["classes"] += len([n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)])
                    except:
                        pass
    with open("summary.json", "w") as out:
        json.dump(summary, out, indent=4)

if __name__ == "__main__":
    analyze_code()
