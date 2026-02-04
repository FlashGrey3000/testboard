# README
Just learning testing with `pytest` and ~~trying to create a *chess-like* game-engine~~ to test the edge-cases and stuff.  

I don't think I'll be building anything massive, as it is going against the idea of learning testing in itself, initially.  

Instead I'll be trying to build small algorithms / converters that can help clear the idea of testing and also help understand testing as a whole and I am not just sitting testing `assert 1 + 1 == 2`.  

> Update: 04/02/26
I have started reading the book `Python Testing with pytest` by `Brian Okken` and it has been a fun read *so far*.  

I will be trying to follow the book as well.    

## Learning Roadmap
Based on what I feel I should cover to kick things off.

### 1. Basic Tests
- Using `assert` statements effectively
- Understanding test discovery
- Naming conventions for tests

### 2. Fixtures
- Function vs module scope
- Dependency injection
- Setup and teardown behavior

### 3. Parametrization
- Using `@pytest.mark.parametrize`
- Covering edge cases systematically

### 4. Mocking
- Using `unittest.mock` and `patch`
- Mocking I/O, time, randomness
- Mocking behavior instead of implementation

### 5. Test Doubles
- Understanding fakes, mocks, and stubs
- When **not** to mock

### 6. Failure-Driven Learning
- Intentionally breaking code
- Watching tests fail
- Fixing issues with confidence