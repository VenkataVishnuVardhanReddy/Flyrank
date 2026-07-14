# Prompt Ladder: Pytest Unit Testing for Vision Filters

This document outlines the systematic prompt engineering process to build a robust prompt for generating `pytest` unit tests for bilateral image filters.

---

## 1. Baseline Prompt (Weak)
> *"Write python tests for a bilateral filter."*

### Representative Output Excerpt:
```python
import unittest
# Assuming you have a bilateral filter class
class TestBilateralFilter(unittest.TestCase):
    def test_filter(self):
        # some test logic
        self.assertTrue(True)
```
*Plus a 200-word explanation of what a bilateral filter is and why it preserves edges.*

### Notes:
- **What changed in prompt**: Genuinely weak baseline.
- **What improved in output**: Generates a skeletal testing file.
- **What still failed**: It uses the older `unittest` library, has no mock image data, and contains unsolicited mathematical explanations.
- **What to try next**: Specify the testing framework and exact target function signature.

---

## 2. Version 1: Clearer Goal & Framework
> *"Write unit tests using the pytest framework for a bilateral filter function with the signature: `def bilateral_filter(image: np.ndarray, d: int, sigma_color: float, sigma_space: float) -> np.ndarray`"*

### Representative Output Excerpt:
```python
import pytest
import numpy as np

def test_bilateral_filter_shape():
    img = np.random.rand(10, 10)
    out = bilateral_filter(img, 5, 0.1, 0.1)
    assert out.shape == img.shape
```

### Notes:
- **What changed in prompt**: Added a specific framework (`pytest`) and the exact function signature.
- **What improved in output**: The code strictly matches our signature, uses `pytest` assertions, and avoids explanations of filter math.
- **What still failed**: Test inputs are defined inline using simple random matrices; there is no reusable structured mock data (fixtures).
- **What to try next**: Add reusable `pytest` fixtures for realistic testing scenarios.

---

## 3. Version 2: Adding Real Context (Fixtures)
> *"Write unit tests using the pytest framework for a bilateral filter function with the signature: `def bilateral_filter(image: np.ndarray, d: int, sigma_color: float, sigma_space: float) -> np.ndarray`. Define reusable pytest fixtures for a clean gray image, a noisy gray image, and a color image (H x W x C) using NumPy."*

### Representative Output Excerpt:
```python
import pytest
import numpy as np

@pytest.fixture
def clean_gray():
    return np.ones((50, 50), dtype=np.float32) * 0.5

@pytest.fixture
def noisy_gray():
    return np.random.normal(0.5, 0.1, (50, 50)).astype(np.float32)
```

### Notes:
- **What changed in prompt**: Added context requirements for input generation using fixtures.
- **What improved in output**: The tests are modular, separated from data preparation, and test against realistic sizes.
- **What still failed**: The assertions are shallow. They only test array shapes and types, not the actual functional behaviors of noise smoothing and edge preservation.
- **What to try next**: Define functional verification requirements.

---

## 4. Version 3: Verification Requirements
> *"Write unit tests using the pytest framework for a bilateral filter function with the signature: `def bilateral_filter(image: np.ndarray, d: int, sigma_color: float, sigma_space: float) -> np.ndarray`. Define reusable pytest fixtures for a clean gray image, a noisy gray image, and a color image (H x W x C) using NumPy. Include tests that verify functional behavior: (1) flat regions should be smoothed (variance decreases), and (2) high-contrast edges should preserve their gradients."*

### Representative Output Excerpt:
```python
def test_edge_preservation(clean_gray):
    # Generates a custom gradient tracking loop to calculate Sobel differences
    # across multiple window sizes...
    for i in range(1, 49):
        # Index error: list index out of range
```

### Notes:
- **What changed in prompt**: Added functional verification criteria (flat region smoothing & edge preservation).
- **What improved in output**: Asserts actual signal processing capabilities rather than just verifying return types.
- **What still failed**: **[This didn't help / made it worse]** The AI wrote a highly complex, buggy Sobel gradient tracking loop that fails with index errors when executing. It tried to do too much math inside the test code.
- **What to try next**: Impose coding constraints to limit assertion complexity and avoid custom loops.

---

## 5. Version 4: Stating Constraints
> *"Write unit tests using the pytest framework for a bilateral filter function with the signature: `def bilateral_filter(image: np.ndarray, d: int, sigma_color: float, sigma_space: float) -> np.ndarray`. Define reusable pytest fixtures for a clean gray image, a noisy gray image, and a color image (H x W x C) using NumPy. Include tests that verify functional behavior: (1) flat regions should be smoothed (variance decreases), and (2) high-contrast edges should preserve their gradients. Constraint: Use standard NumPy array slicing and basic stats (like np.var or np.diff) for verification; do not write custom gradient calculation loops or complex math operations."*

### Representative Output Excerpt:
```python
def test_functional_smoothing(noisy_gray):
    filtered = bilateral_filter(noisy_gray, 5, 0.1, 0.1)
    assert np.var(filtered) < np.var(noisy_gray)
```

### Notes:
- **What changed in prompt**: Added constraints restricting the code style to standard NumPy functions.
- **What improved in output**: The code became clean, concise, readable, and executes without errors out-of-the-box.
- **What still failed**: Mismatched channels and extreme input parameter validation (negative values) are not verified.
- **What to try next**: Introduce edge cases and input parameter bounds to quality criteria.

---

## 6. Version 5: Quality Criteria & Edge Cases (Final)
> *"Write unit tests using the pytest framework for a bilateral filter function with the signature: `def bilateral_filter(image: np.ndarray, d: int, sigma_color: float, sigma_space: float) -> np.ndarray`. Define reusable pytest fixtures for a clean gray image, a noisy gray image, and a color image (H x W x C) using NumPy. Include tests that verify functional behavior: (1) flat regions should be smoothed (variance decreases), and (2) high-contrast edges should preserve their gradients. Constraint: Use standard NumPy array slicing and basic stats (like np.var or np.diff) for verification; do not write custom gradient calculation loops or complex math operations. Quality Criteria: Include test cases for edge cases: empty image (size 0), mismatched channels (4 channels instead of 3), and invalid parameter handling (negative sigma values should raise a ValueError)."*

### Representative Output Excerpt:
```python
def test_invalid_parameters():
    img = np.ones((10, 10))
    with pytest.raises(ValueError):
        bilateral_filter(img, 5, -0.1, 0.1)
```

### Notes:
- **What changed in prompt**: Added edge cases and error handling validation to quality criteria.
- **What improved in output**: The output covers full system constraints, including robust exception checking.
- **What still failed**: None. The generated code is robust, functional, and complete.

---

## 7. Reusable Prompt Template

```text
Target: Generate unit tests for custom vision/image processing filter functions in Python.

Instructions:
1. Use the pytest framework.
2. Target function signature: [PASTE SIGNATURE HERE, e.g., def filter_func(image: np.ndarray, param: float) -> np.ndarray]
3. Define reusable pytest fixtures for realistic test inputs (e.g., clean, noisy, color/grayscale) using NumPy.
4. Include functional verification tests checking: [LIST FUNCTIONAL REQUIREMENTS, e.g., noise reduction, edge preservation]
5. Constraints: Use only standard NumPy operations (np.var, np.diff, slicing) for assertions. Do not write custom mathematical loops or complex calculations inside test assertions.
6. Quality Criteria: Assert boundaries and edge cases, including empty inputs, invalid parameter dimensions, and exception handling (e.g., ValueError verification using pytest.raises).
```
