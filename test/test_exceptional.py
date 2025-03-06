import pytest
from test.TestUtils import TestUtils
from recipe_converter import (convert_flour_to_grams, convert_sugar_to_grams)

class TestRecipeConverterExceptional:
    test_obj = TestUtils()
    
    def test_negative_flour(self):
        try:
            with pytest.raises(ValueError) as exc_info:
                convert_flour_to_grams(-2.5)
            assert "must be positive" in str(exc_info.value)
            self.test_obj.yakshaAssert("test_negative_flour", True, "exceptional")
            print("test_negative_flour = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_negative_flour", False, "exceptional")
            print("test_negative_flour = Failed")
    
    def test_zero_sugar(self):
        try:
            with pytest.raises(ValueError) as exc_info:
                convert_sugar_to_grams(0)
            assert "must be positive" in str(exc_info.value)
            self.test_obj.yakshaAssert("test_zero_sugar", True, "exceptional")
            print("test_zero_sugar = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_zero_sugar", False, "exceptional")
            print("test_zero_sugar = Failed")
    
    def test_invalid_unit(self):
        try:
            with pytest.raises(ValueError) as exc_info:
                convert_volume_to_ml(1, "gallons")
            assert "Invalid unit" in str(exc_info.value)
            self.test_obj.yakshaAssert("test_invalid_unit", True, "exceptional")
            print("test_invalid_unit = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_invalid_unit", False, "exceptional")
            print("test_invalid_unit = Failed")

if __name__ == '__main__':
    pytest.main(['-v'])