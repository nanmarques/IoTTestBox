import pytest
from py.xml import html


# REPORT SETTINGS
# Change Title
def pytest_html_report_title(report):
    report.title = "REPORT TITLE"


# Change Summary
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("SUMMARY FOR THE EXECUTION")])


@pytest.fixture(scope='session')
def var_cache():
    return {}
