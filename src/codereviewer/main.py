import sys
import warnings
import json

from codereviewer.crew import Codereviewer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
    


def _print_result(result) -> None:
    # CrewAI results can be str, dict-like, or custom objects
    if result is None:
        return
    if isinstance(result, (str, bytes)):
        print(result)
    else:
        # Fallback: try to print nicely
        print(str(result))


def run():
    """
    Run the crew.
    """
    codebase_path = sys.argv[1] if len(sys.argv) > 1 else "."

    inputs = {
        "codebase_path": codebase_path,
        "project_name": "RefactorCrew",
        "language_hint": "auto",
        "goals": "Review the codebase, identify issues, propose a refactor plan, and produce a patch/diff.",
        "output_format": "markdown",
    }

    try:
        result = Codereviewer().crew().kickoff(inputs=inputs)
        _print_result(result)
        return 0
    except Exception as e:
        print(f"An error occurred while running the crew: {e}", file=sys.stderr)
        return 1


def train():
    """
    Train the crew for a given number of iterations.
    Usage (typical): crewai train <n_iterations> <filename> [codebase_path]
    """
    codebase_path = sys.argv[3] if len(sys.argv) > 3 else "."

    inputs = {
        "codebase_path": codebase_path,
        "project_name": "RefactorCrew",
        "language_hint": "auto",
        "goals": "Train the crew to produce consistent code review reports and refactoring plans.",
        "output_format": "markdown",
    }

    try:
        result = Codereviewer().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs,
        )
        _print_result(result)
        return 0
    except Exception as e:
        print(f"An error occurred while training the crew: {e}", file=sys.stderr)
        return 1


def replay():
    """
    Replay the crew execution from a specific task.
    Usage (typical): crewai replay <task_id>
    """
    try:
        result = Codereviewer().crew().replay(task_id=sys.argv[1])
        _print_result(result)
        return 0
    except Exception as e:
        print(f"An error occurred while replaying the crew: {e}", file=sys.stderr)
        return 1


def test():
    """
    Test the crew execution and returns the results.
    Usage (typical): crewai test <n_iterations> <eval_llm> [codebase_path]
    """
    codebase_path = sys.argv[3] if len(sys.argv) > 3 else "."

    inputs = {
        "codebase_path": codebase_path,
        "project_name": "RefactorCrew",
        "language_hint": "auto",
        "goals": "Evaluate the crew's review quality and refactoring recommendations.",
        "output_format": "markdown",
    }

    try:
        result = Codereviewer().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs,
        )
        _print_result(result)
        return 0
    except Exception as e:
        print(f"An error occurred while testing the crew: {e}", file=sys.stderr)
        return 1


def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    if len(sys.argv) < 2:
        print("No trigger payload provided. Please provide JSON payload as argument.", file=sys.stderr)
        return 1

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        print("Invalid JSON payload provided as argument", file=sys.stderr)
        return 1

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": "",
    }

    try:
        result = Codereviewer().crew().kickoff(inputs=inputs)
        _print_result(result)
        return 0
    except Exception as e:
        print(f"An error occurred while running the crew with trigger: {e}", file=sys.stderr)
        return 1