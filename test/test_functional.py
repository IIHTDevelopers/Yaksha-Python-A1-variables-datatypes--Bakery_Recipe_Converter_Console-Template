import pytest
from test.TestUtils import TestUtils
import re
import inspect

# Try to import, but if it fails, create dummy constants and functions
try:
    from skeleton import (convert_flour_to_grams, convert_sugar_to_grams, 
                                CUP_FLOUR_TO_GRAMS, CUP_SUGAR_TO_GRAMS)
except Exception as e:
    # Define dummy constants and functions that will cause tests to fail gracefully
    CUP_FLOUR_TO_GRAMS = -1  # This will fail the constant test
    CUP_SUGAR_TO_GRAMS = -1  # This will fail the constant test
    
    def convert_flour_to_grams(cups):
        raise Exception("Function not properly implemented")
    
    def convert_sugar_to_grams(cups):
        raise Exception("Function not properly implemented")

@pytest.fixture
def test_obj():
    return TestUtils()

def test_required_variables(test_obj):
    """Test if all required variables are defined with exact naming"""
    try:
        with open('recipe_converter.py', 'r') as file:
            content = file.read()
        
        required_vars = {
            'recipe_name': r'recipe_name\s*=',
            'flour_cups': r'flour_cups\s*=',
            'sugar_cups': r'sugar_cups\s*=',
            'flour_grams': r'flour_grams\s*=',
            'sugar_grams': r'sugar_grams\s*='
        }
        
        for var_name, pattern in required_vars.items():
            if not re.search(pattern, content):
                test_obj.yakshaAssert("test_required_variables", False, "functional")
                pytest.fail(f"Required variable '{var_name}' not found or incorrectly named (check case sensitivity)")
            else:
                continue
        
        test_obj.yakshaAssert("test_required_variables", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_required_variables", False, "functional")
        print("test_required_variables = Failed")

def test_flour_constant(test_obj):
    """Test if flour constant is defined correctly"""
    try:
        if CUP_FLOUR_TO_GRAMS != 128:
            test_obj.yakshaAssert("test_flour_constant", False, "functional")
            pytest.fail(f"CUP_FLOUR_TO_GRAMS should be 128, got {CUP_FLOUR_TO_GRAMS}")
        else:
            test_obj.yakshaAssert("test_flour_constant", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_flour_constant", False, "functional")
        print("test_flour_constant = Failed")

def test_sugar_constant(test_obj):
    """Test if sugar constant is defined correctly"""
    try:
        if CUP_SUGAR_TO_GRAMS != 200:
            test_obj.yakshaAssert("test_sugar_constant", False, "functional")
            pytest.fail(f"CUP_SUGAR_TO_GRAMS should be 200, got {CUP_SUGAR_TO_GRAMS}")
        else:
            test_obj.yakshaAssert("test_sugar_constant", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_sugar_constant", False, "functional")
        print("test_sugar_constant = Failed")

def test_flour_conversion_formula(test_obj):
    """Test flour conversion formula implementation"""
    try:
        # Get function source code
        function_code = inspect.getsource(convert_flour_to_grams)
        # Remove whitespace and newlines for consistent checking
        code = function_code.replace(" ", "").replace("\n", "")
        
        # Check if formula components are present
        if "CUP_FLOUR_TO_GRAMS" not in code:
            test_obj.yakshaAssert("test_flour_conversion_formula", False, "functional")
            pytest.fail("Must use CUP_FLOUR_TO_GRAMS constant in conversion")
        
        if f"*CUP_FLOUR_TO_GRAMS" not in code and f"CUP_FLOUR_TO_GRAMS*" not in code:
            test_obj.yakshaAssert("test_flour_conversion_formula", False, "functional")
            pytest.fail("Must multiply cups with CUP_FLOUR_TO_GRAMS")
        
        if "round(" not in code:
            test_obj.yakshaAssert("test_flour_conversion_formula", False, "functional")
            pytest.fail("Must use round() function")

        # Verify one test case to ensure formula works
        result = convert_flour_to_grams(1)
        if result != 128:
            test_obj.yakshaAssert("test_flour_conversion_formula", False, "functional")
            pytest.fail("Formula implementation incorrect")
            
        test_obj.yakshaAssert("test_flour_conversion_formula", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_flour_conversion_formula", False, "functional")
        print("test_flour_conversion_formula = Failed")

def test_sugar_conversion_formula(test_obj):
    """Test sugar conversion formula implementation"""
    try:
        function_code = inspect.getsource(convert_sugar_to_grams)
        code = function_code.replace(" ", "").replace("\n", "")
        
        # Check if formula components are present or not inside the function 
        if "CUP_SUGAR_TO_GRAMS" not in code:
            test_obj.yakshaAssert("test_sugar_conversion_formula", False, "functional")
            pytest.fail("Must use CUP_SUGAR_TO_GRAMS constant in conversion")
        
        if f"*CUP_SUGAR_TO_GRAMS" not in code and f"CUP_SUGAR_TO_GRAMS*" not in code:
            test_obj.yakshaAssert("test_sugar_conversion_formula", False, "functional")
            pytest.fail("Must multiply cups with CUP_SUGAR_TO_GRAMS")
        
        if "round(" not in code:
            test_obj.yakshaAssert("test_sugar_conversion_formula", False, "functional")
            pytest.fail("Must use round() function")
        
        result = convert_sugar_to_grams(1)
        if result != 200:
            test_obj.yakshaAssert("test_sugar_conversion_formula", False, "functional")
            pytest.fail("Formula implementation incorrect")
            
        test_obj.yakshaAssert("test_sugar_conversion_formula", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_sugar_conversion_formula", False, "functional")
        print("test_sugar_conversion_formula = Failed")

if __name__ == '__main__':
    pytest.main(['-v'])