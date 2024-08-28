import re
from flask import Flask,abort, request
from .waf_logging import waf_logger
import urllib.parse

app = Flask(__name__)

SQL_INJECTION_PATTERNS = [
    r"(\bOR\b|\bor\b)",             # Matches ' OR ' or 'or'
    r"(\bAND\b|\band\b)",           # Matches ' AND ' or 'and'
    r"(union\s+select)",            # Matches 'union select'
    r"(--|\#)",                     # Matches SQL comments and statement separators
    r"(\bXOR\b|\bxor\b)",           # Matches ' XOR ' or 'xor'
    r"(\bEXEC\b|\bexec\b)",         # Matches ' EXEC ' or 'exec'
    r"(\bINSERT\b|\binsert\b)",     # Matches ' INSERT ' or 'insert'
    r"(\bDROP\b|\bdrop\b)",         # Matches ' DROP ' or 'drop'
    r"(\bUPDATE\b|\bupdate\b)",     # Matches ' UPDATE ' or 'update'
    r"(\bDELETE\b|\bdelete\b)",     # Matches ' DELETE ' or 'delete'
    r"(\bSELECT\b|\bselect\b)",     # Matches ' SELECT ' or 'select'
    r"('.*')",                      # Matches patterns with single quotes around content
    r"(')",                         # Matches any single quote
    r"(1\s*=\s*1)",                 # Matches '1=1' patterns
]

def detect_sql_injection(data):
    for pattern in SQL_INJECTION_PATTERNS:
        if re.search(pattern, data, re.IGNORECASE):
            return True
    return False

@app.before_request
def waf():
    # print("[DEBUGGING] GOT INTO WAF MIDDLEWARE")
    
    # checking query parameters
    for key, value in request.args.items():
        decoded_value = urllib.parse.unquote(value)  
        # print(f"[DEBUGGING] Checking query param: {key} = {decoded_value}")
        if detect_sql_injection(value):
            waf_logger.info(f"SQL Injection attempt: {key} = {value}")
            abort(403)  

    # checking form data
    for key, value in request.form.items():
        # print(f"[DEBUGGING] Checking form data: {key} = {value}")
        if detect_sql_injection(value):
            waf_logger.info(f"SQL Injection attempt: {key} = {value}")
            abort(403)  

    # checking headers
    for key, value in request.headers.items():
        # print(f"[DEBUGGING] Checking header: {key} = {value}")
        if detect_sql_injection(value):
            waf_logger.info(f"SQL Injection attempt: {key} = {value}")
            abort(403)  

    # checking raw body
    if request.data:
        body = request.data.decode('utf-8')
        # print(f"[DEBUGGING] Checking raw body: {body}")
        if detect_sql_injection(body):
            waf_logger.info(f"SQL Injection attempt: {body}")
            abort(403)   

@app.route('/')
def home():
    return "Welcome to the SECURE Flask App!"

if __name__ == '__main__':
    app.run()
