import pytest


def pytest_sessionstart(session):
    """Hook to set the autograder module reference globally."""
    import autograder  # Import your autograder.py file
    session.config._autograder_module = autograder  # Set it in the config object


def pytest_runtest_makereport(item, call):
    if call.when == "call":
        outcome = call.excinfo is None

        # Access the question and test_scores from autograder.py using the item
        test_scores = getattr(item.module, 'test_scores', {})
        weights = getattr(item.module, 'weights', {})

        # question = item.funcargs.get('question')
        question = item.name.split("[")[-1][:-1]
        if question.isdigit():
            question = int(question)
            score = test_scores.get(question, 0)
            max_score = weights.get(question)
            # result_message = f"({score}/{max_score})"
            # print(result_message)

            # Store score in user properties for later use in pytest_report_teststatus
            item.user_properties.append(("score", f"({score}/{max_score})"))


def pytest_report_teststatus(report, config):
    """Modify test output to include score next to test result."""
    if report.when == "call":
        for prop in report.user_properties:
            if prop[0] == "score":
                score_msg = prop[1]
                if report.outcome == "passed":
                    return report.outcome, "P", f"PASSED {score_msg}"
                elif report.outcome == "failed":
                    return report.outcome, "F", f"FAILED {score_msg}"
                elif report.outcome == "skipped":
                    return report.outcome, "S", f"SKIPPED {score_msg}"


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Display final summary of the test results."""
    terminalreporter.write_sep("=", "TEST SCORE SUMMARY")

    # Access test_scores and weights from the module
    test_scores = getattr(config._autograder_module, 'test_scores', {})
    weights = getattr(config._autograder_module, 'weights', {})

    total_score = sum(test_scores.values())
    max_score = sum(weights.values())

    # Print the total score at the end of pytest run
    terminalreporter.write_line(f"Total Score: {total_score:.2f}/{max_score:.2f}")
