import pytest
from test.TestUtils import TestUtils
from recipe_converter import (convert_flour_to_grams, convert_sugar_to_grams)

class TestRecipeConverterBoundary:
    test_obj = TestUtils()
    
    def test_minimum_flour(self):
        try:
            result = convert_flour_to_grams(0.1)
            expected = 13  # 0.1 cups * 128 g/cup
            assert result == expected, f"Expected {expected}, but got {result}"
            self.test_obj.yakshaAssert("test_minimum_flour", True, "boundary")
            print("test_minimum_flour = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_minimum_flour", False, "boundary")
            print("test_minimum_flour = Failed")
    
    def test_large_flour(self):
        try:
            result = convert_flour_to_grams(10)
            expected = 1280  # 10 cups * 128 g/cup
            assert result == expected, f"Expected {expected}, but got {result}"
            self.test_obj.yakshaAssert("test_large_flour", True, "boundary")
            print("test_large_flour = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_large_flour", False, "boundary")
            print("test_large_flour = Failed")

if __name__ == '__main__':
    pytest.main(['-v'])