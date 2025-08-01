import os
import re
import time
import together
from dlai_grader.grading import test_case, print_feedback
from types import FunctionType
import numpy as np
import joblib


def test_check_if_faq_or_product(learner_func):
    def g():
        function_name = learner_func.__name__
        cases = []
        t = test_case()
        if not isinstance(learner_func, FunctionType):
            t.failed = True
            t.msg = f"{learner_func} has incorrect type"
            t.want = FunctionType
            t.got = type(learner_func)
            return [t]
        cases.append(t)
        query = "What are your working hours?"
        try:
            output = learner_func(query)
        except Exception as e:
            t.failed = True
            t.msg = f"{function_name} raised an exception with the following parameters query = {query}"
            t.want = f"{function_name} must run without exceptions"
            t.got = str(e)
            return [t]
        cases.append(t)
            
        t = test_case()
        if not isinstance(output, str):
            t.failed = True
            t.msg = f"{function_name} have wrong type"
            t.want = str
            t.got = type(output)
            return [t]
        cases.append(t)
        t = test_case()
        if len(output.split()) != 1:
            t.failed = True
            t.msg = f"Output must have only one word"
            t.want = "One element"
            t.got = output      
        cases.append(t)
        return cases

    cases = g()
    print_feedback(cases)

def test_query_on_faq(learner_func):
    def g():
        function_name = learner_func.__name__
        cases = []
        t = test_case()
        if not isinstance(learner_func, FunctionType):
            t.failed = True
            t.msg = f"{learner_func} has incorrect type"
            t.want = FunctionType
            t.got = type(learner_func)
            return [t]
        query = "What are your working hours?"
        try:
            output = learner_func(query)
        except Exception as e:
            t.failed = True
            t.msg = f"{function_name} raised an exception with the following parameters query = {query}"
            t.want = f"{function_name} must run without exceptions"
            t.got = str(e)
            return [t]
            
        t = test_case()
        if not isinstance(output, dict):
            t.failed = True
            t.msg = f"{function_name} have wrong type"
            t.want = str
            t.got = type(output)
            return [t]
        cases.append(t)
        return cases

    cases = g()
    print_feedback(cases)


def test_decide_task_nature(learner_func):
    def g():
        function_name = learner_func.__name__
        cases = []
        t = test_case()
        if not isinstance(learner_func, FunctionType):
            t.failed = True
            t.msg = f"{learner_func} has incorrect type"
            t.want = FunctionType
            t.got = type(learner_func)
            return [t]
        query = "What are your working hours?"
        try:
            output = learner_func(query)
        except Exception as e:
            t.failed = True
            t.msg = f"{function_name} raised an exception with the following parameters query = {query}"
            t.want = f"{function_name} must run without exceptions"
            t.got = str(e)
            return [t]
            
        t = test_case()
        if not isinstance(output, str):
            t.failed = True
            t.msg = f"{function_name} have wrong type"
            t.want = str
            t.got = type(output)
            return [t]
        cases.append(t)
        return cases

    cases = g()
    print_feedback(cases)


def test_get_params_for_task(learner_func):
    def g():
        function_name = learner_func.__name__
        cases = []
        t = test_case()
        if not isinstance(learner_func, FunctionType):
            t.failed = True
            t.msg = f"{learner_func} has incorrect type"
            t.want = FunctionType
            t.got = type(learner_func)
            return [t]
        cases.append(t)
        task = 'technical'
        t = test_case()

        try:
            output = learner_func(task)
        except Exception as e:
            t.failed = True
            t.msg = f"{function_name} raised an exception with the following parameters task = {task}"
            t.want = f"{function_name} must run without exceptions"
            t.got = str(e)
            return [t]
        cases.append(t)
            
        t = test_case()
        if not isinstance(output, dict):
            t.failed = True
            t.msg = f"{function_name} have wrong type"
            t.want = dict
            t.got = type(output)
            return [t]
        cases.append(t)
        
        t = test_case()
        if 'top_p' not in output:
            t.failed = True
            t.msg = f"top_p missing nas a dictionary key"
            t.want = 'top_k must be in dictionary keys'
            t.got = output.keys()
            return [t]
        cases.append(t)
        
        t = test_case()
        if 'temperature' not in output:
            t.failed = True
            t.msg = f"temperature missing nas a dictionary key"
            t.want = 'temperature must be in dictionary keys'
            t.got = output.keys()
            return [t]
        cases.append(t)
        
        tasks = ['technical', 'creative', 'asd']
        for task in tasks:
            output = learner_func(task)
            t = test_case()
            if output['top_p'] >= 1:
                t.failed = True
                t.msg = "top_p cannot be greater than 1"
                t.want = "top_p < 1"
                t.got = f"top_p = {output['top_p']} for label = {task}"
            if output['temperature'] > 1.3:
                t.failed = True
                t.msg = f"temperature is too high for label = {task}"
                t.want = "temperature must be less than 1.3 and if closer to 1.3 top_p must be low"
                t.got = f"temperature = {output['temperature']} for label = {task}"
            cases.append(t)
    
        return cases


    cases = g()
    print_feedback(cases)
