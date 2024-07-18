import pytest


# Объявляем фикстуру с областью видимости session
@pytest.fixture(scope="session")
def setup_session():
    print("Setting up session...")
    
    session_var = "Value from session"
    
    yield session_var
    
    print("Tearing down session...")


# Фикстура с областью видимости function
@pytest.fixture(scope="function")
def setup_function():
    print("\nSetting up function...")
    
    function_var = "Value from function"
    
    yield function_var
    
    print("Tearing down function...")


# Используем фикстуру setup_session в качестве зависимости для теста
def test_example(setup_session, setup_function):
    print("\nTest example with session var:", setup_session)
    print("Test example with function var:", setup_function)
