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

## Example Project by the book
### The Tasks Project
The application we’ll look at is called Tasks. Tasks is a minimal task-tracking application with a command-line user interface. It has enough in common with many other types of applications that I hope you can easily see how the testing concepts you learn while developing tests against Tasks are applicable to your projects now and in the future.  

While Tasks has a command-line interface (CLI), the CLI interacts with the rest of the code through an application programming interface (API). The API is the interface where we’ll direct most of our testing. The API interacts with a database control layer, which interacts with a
document database—either MongoDB or TinyDB. The type of database is configured at database initialization.  

Before we focus on the API, let’s look at tasks, the command-line tool that represents the user interface for Tasks.

Here’s an example session:
```sh
 $ tasks add 'do something' --owner Brian
 $ tasks add 'do something else'
 $ tasks list
  ID owner done summary
  -- ----- ---- -------
  1 Brian False do something
  2 False do something else
 $ tasks update 2 --owner Brian
 $ tasks list
  ID owner done summary
  -- ----- ---- -------
  1 Brian False do something
  2 Brian False do something else
$ tasks update 1 --done True
 $ tasks list
  ID owner done summary
  -- ----- ---- -------
  1 Brian True do something
  2 Brian False do something else
 $ tasks delete 1
 $ tasks list
  ID owner done summary
  -- ----- ---- -------
  2 Brian False do something else
```